# rpa-models
This repository ONLY contains the datasets and scripts used to train the models in RPA Tomorrow. Currently
only two models are under development:
- deep (using seq2seq)
- simple (smaller model built from scratch)

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
To train the deep or simple model with the default configurations run
```
  python deep/seq2seq.py #or
  python simple/train_model.py
```

# NOTE!
For the pre-trained models and their releases, see [model-releases](https://github.com/rpa-tomorrow/model-releases)
