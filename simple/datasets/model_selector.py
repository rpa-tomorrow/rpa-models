import spacy
import en_core_web_md
from os import listdir
from os.path import isfile, join
from spacy.matcher import Matcher

def modelSelectorTest(input):
    nlp = spacy.load("en_core_web_md")
    matcher = Matcher(nlp.vocab)

    # path =  "../simple/datasets/models"
    # models = [f for f in listdir(path) if isfile(join(path, f))]
    # print("models = " + ' '.join(map(str, models)))

    # for model in models: 
    #     patterns.append([{"LOWER": model.split('.')[0]}])

    patterns = [[{"LOWER": "remind"}], [{"LOWER": "availability"}], [{"LOWER": "send"}]]

    for pattern in patterns:
        matcher.add("modelResult", None, pattern)

    doc = nlp(input)
    matches = matcher(doc)

    for match_id, start, end in matches:
        string_id = nlp.vocab.strings[match_id]  # Get string representation
        span = doc[start:end]  # The matched span
        print(match_id, string_id, start, end, span.text)

    # return (match_id, string_id, start, end, span.text) 


    # nlp = spacy.load("en_core_web_md")
    # matcher = Matcher(nlp.vocab)
    # # Add match ID "HelloWorld" with no callback and one pattern
    # pattern = [{"LOWER": "hello"}, {"IS_PUNCT": True}, {"LOWER": "world"}]
    # matcher.add("HelloWorld", None, pattern)

    # doc = nlp("sug min kuk")
    # matches = matcher(doc)
    # for match_id, start, end in matches:
    #     string_id = nlp.vocab.strings[match_id]  # Get string representation
    #     span = doc[start:end]  # The matched span
    #     print(match_id, string_id, start, end, span.text)