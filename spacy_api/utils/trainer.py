from pathlib import Path
import random, csv, spacy, pandas as pd

from spacy.util import minibatch, compounding

from spacy_api.utils.utils import read_dataframe_from_csv, compare_dataframes



def train_model(training_data, model=None, output_dir=None, n_iter=100):
    """Load the model, set up the pipeline and train the entity recognizer."""
    if model is not None:
        nlp = spacy.load(model) # load existing spaCy model
        print('Loaded model {}'.format(model))
    else:
        nlp = spacy.blank('en')  # create blank Language class
        print('Created blank \'en\' model')

    # create the built-in pipeline components and add them to the pipeline
    # nlp.create_pipe works for built-ins that are registered with spaCy
    if 'ner' not in nlp.pipe_names:
        ner = nlp.create_pipe('ner')
        nlp.add_pipe(ner, last=True)
    # otherwise, get it so we can add labels
    else:
        ner = nlp.get_pipe('ner')

    # add labels
    for _, annotations in training_data:
        for ent in annotations.get('entities'):
            ner.add_label(ent[2])

    # get names of other pipes to disable them during training
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    with nlp.disable_pipes(*other_pipes):  # only train NER
        # reset and initialize the weights randomly – but only if we're
        # training a new model
        if model is None:
            nlp.begin_training()
        for itn in range(n_iter):
            random.shuffle(training_data)
            losses = {}
            # batch up the examples using spaCy's minibatch
            batches = minibatch(training_data, size=compounding(4.0, 32.0, 1.001))
            for batch in batches:
                texts, annotations = zip(*batch)
                nlp.update(
                    texts,  # batch of texts
                    annotations,  # batch of annotations
                    drop=0.5,  # dropout - make it harder to memorise data
                    losses=losses,
                )
            print('Losses', losses)

    # save model to output directory
    if output_dir is not None:
        output_dir = Path(output_dir)
        if not output_dir.exists():
            output_dir.mkdir()
        nlp.to_disk(output_dir)
        print("Saved model to", output_dir)



def csv_to_training_format(file):
    dataframe = read_dataframe_from_csv(file)
    training_data = []
    for index, row in dataframe.iterrows():
        training_data.append(_dic_to_training_format(row))
    return training_data

def _dic_to_training_format(dic):
    raw_text = dic['RAW']
    entities = []
    for key, value in dic.items():
        if key != 'RAW' and not pd.isna(value):
            start_pos = raw_text.find(value)
            tuple = (start_pos, start_pos+len(value), key)
            entities.append(tuple)

    return (raw_text, {'entities': entities})
