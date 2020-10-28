#!/usr/bin/env python
# coding: utf-8
from __future__ import unicode_literals, print_function

import plac
import random
import spacy
import glob, importlib, os, pathlib, sys
from pathlib import Path
from spacy.util import minibatch, compounding, decaying

def test_model(nlp, texts):
    docs = nlp.pipe(texts)
    for doc in docs:
        print(doc.text)
        print([(t.text, t.dep_, t.head.text) for t in doc if t.dep_ != "-"])

def get_batches(train_data, model_type):
    max_batch_sizes = {"tagger": 32, "parser": 16, "ner": 16, "textcat": 64}
    max_batch_size = max_batch_sizes[model_type]
    if len(train_data) < 1000:
        max_batch_size /= 2
    if len(train_data) < 500:
        max_batch_size /= 2
    batch_size = compounding(1, max_batch_size, 1.001)
    batches = minibatch(train_data, size=batch_size)
    return batches

def get_datasets(name):
    module_base= "datasets."
    train_base = name + "." + "training_data"
    test_base = name + "." + "test_data"

    train_mod = __import__(module_base + train_base)
    test_mod = __import__(module_base + test_base)

    if name == "email":
        return (train_mod.email.training_data.TRAIN_DATA, test_mod.email.test_data.TEST_DATA)
    elif name == "reminder":
        return (train_mod.reminder.training_data.TRAIN_DATA, test_mod.reminder.test_data.TEST_DATA)
    elif name == "calendar":
        return (train_mod.calendar.training_data.TRAIN_DATA, test_mod.calendar.test_data.TEST_DATA) 
    else:
        raise Exception("Could not find dataset directory with the name ", name)

@plac.annotations(
    dataset=("Name of the directory for the dataset to use", "option", "d", str),
    model=("Model name. Defaults to blank 'en' model.", "option", "m", str),
    output_dir=("Optional output directory", "option", "o", Path),
    n_iter=("Number of training iterations", "option", "n", int),
)
def train_model(dataset, model=None, output_dir=None, n_iter=15):
    train_data, test_data = get_datasets(dataset)
    """Load the model, set up the pipeline and train the parser."""
    if model is not None:
        nlp = spacy.load(model)  # load existing spaCy model
        print("Loaded model '%s'" % model)
    else:
        nlp = spacy.blank("en")  # create blank Language class
        print("Created blank 'en' model")

    # We'll use the built-in dependency parser class, but we want to create a
    # fresh instance – just in case.
    if "parser" in nlp.pipe_names:
        nlp.remove_pipe("parser")
    parser = nlp.create_pipe("parser")
    nlp.add_pipe(parser, first=True)

    for text, annotations in train_data:
        for dep in annotations.get("deps", []):
            parser.add_label(dep)

    pipe_exceptions = ["parser", "trf_wordpiecer", "trf_tok2vec"]
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]
    with nlp.disable_pipes(*other_pipes):  # only train parser
        dropout = decaying(0.6, 0.2, 1e-4)
        optimizer = nlp.begin_training()
        for itn in range(n_iter):
            random.shuffle(train_data)
            losses = {}
            # batch up the examples using spaCy's minibatch
            #batches = get_batches(train_data, "parser")
            batches = minibatch(train_data, size=compounding(4.0, 32.0, 1.001))
            for batch in batches:
                texts, annotations = zip(*batch)
                nlp.update(
                    texts, 
                    annotations, 
                    #drop=next(dropout), 
                    sgd=optimizer, 
                    losses=losses)
            print("Losses", losses)

    # test the trained model
    test_model(nlp, test_data)

    # save model to output directory
    if output_dir is not None:
        output_dir = Path(output_dir)
        if not output_dir.exists():
            output_dir.mkdir()

        with nlp.use_params(optimizer.averages):
            nlp.to_disk(output_dir)
        print("Saved model to", output_dir)

        # test the saved model
        print("Loading from", output_dir)
        nlp2 = spacy.load(output_dir)
        test_model(nlp2, test_data)

if __name__ == "__main__":
    plac.call(train_model)
