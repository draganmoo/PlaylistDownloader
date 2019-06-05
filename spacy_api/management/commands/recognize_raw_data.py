from django.core.management.base import BaseCommand

from spacy_api.utils.utils import read_dataframe_from_csv, save_dataframe_to_csv
from spacy_api.utils.recognizer import recognize_raw_from_csv

from os.path import join



class Command(BaseCommand):
    def handle(self, *args, **options):
        model_path = join('spacy_api', join('spacy_models', 'model'))
        input_path = join('spacy_api', join('spacy_models', join('training_sets', 'raw.csv')))
        output_path = join('spacy_api', join('spacy_models', join('training_sets', 'partial_training_set.csv')))

        recognized_data = recognize_raw_from_csv(model_path, input_path)
        save_dataframe_to_csv(output_path, recognized_data)
