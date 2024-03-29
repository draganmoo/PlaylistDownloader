import spacy, pandas as pd

from spacy_api.utils.utils import read_dataframe_from_csv, LABELS



def recognize_dataframe(model, dataframe):
    recognized = []
    nlp = spacy.load(model)
    for index, row in dataframe.iterrows():
        recognized.append(recognize_entities_from_dic(nlp, row))

    return pd.DataFrame(recognized, columns=LABELS)


def recognize_entities_from_dic(nlp, dic):
    doc = nlp(dic['RAW'])
    for entity in doc.ents:
        dic[entity.label_] = entity.text

    return dic



def load_nlp(model_path):
    return spacy.load(model_path)

def recognize_entities_from_raw(nlp, raw):
    doc = nlp(raw)
    return {entity.label_: entity.text for entity in doc.ents}
