# rpa-models
This repository ONLY contains the datasets and scripts used to train the models in RPA Tomorrow. Currently
only two categories of models are under development:
- deep (using seq2seq)
- simple (smaller models trained from scratch)
  - simple-email
  - simple-calendar
  - simple-reminder

# Requirements
* Python 3.8.5
* Anaconda

# Setup
Load the Conda environment.
```
 conda activate rpa-models
```
You will need pre-trained Spacy models for the Deep model.
```
 python -m spacy download en_core_web_lg
```

# Training models
To train the deep model with the default configurations run
```
  python deep/seq2seq.py #or
```
To train the simple model, run the following with the dataset you want to train the model only
```
  python simple/train_model.py -d <DATASET_NAME> -o <OUTPUT_DIR>
```
The `DATASET_NAME` is the name of the directory you want to work on inside `simple/datasets` e.g. "reminder".
If you don't specify the output directory the model will not be stored.

# NOTE!
For the pre-trained models and their releases, see [model-releases](https://github.com/rpa-tomorrow/model-releases)
