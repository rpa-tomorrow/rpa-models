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

    models = ["remind", "availabillity", "send"]
    patterns = []

    for model in models: 
        patterns.append([{"LOWER": model}])
        # patterns.append([{"LOWER": model.split('.')[0]}])

    # patterns = [[{"LOWER": "remind"}], [{"LOWER": "availabillity"}], [{"LOWER": "send"}]]

    for pattern in patterns:
        matcher.add("modelResult", None, pattern)

    doc = nlp(input)
    matches = matcher(doc)

    try:
        for match_id, start, end in matches:
            string_id = nlp.vocab.strings[match_id]  # Get string representation
            span = doc[start:end]  # The matched span
            print(match_id, string_id, start, end, span.text)

        return (match_id, string_id, start, end, span.text)

    except:
        return (0, "", 0, 0, "unsupported")

# # code used for calling the model selector, might be used later
# # model selector for substorm project
# for val in TEST_DATA:
#     res = modelSelectorTest(val)
#     print("res = " + res[4])
#     if res[4] != "unsupported": 
#         print("model has been selected = ", res[4])