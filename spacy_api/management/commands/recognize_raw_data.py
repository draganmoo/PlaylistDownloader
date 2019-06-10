from django.core.management.base import BaseCommand

from spacy_api.utils.utils import save_dataframe_to_csv, retrieve_raw_data
from spacy_api.utils.recognizer import recognize_dataframe

from os.path import join



class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('playlist_id', type=str)

    def handle(self, *args, **options):
        model_path = join('spacy_api', join('spacy_models', 'model'))
        output_path = join('spacy_api', join('spacy_models', join('training_sets', 'recognized.csv')))

        dataframe = retrieve_raw_data(options['playlist_id'])
        print('Raw data retrieved !')

        recognized_data = recognize_dataframe(model_path, dataframe)
        print('Raw data recognized !')
        save_dataframe_to_csv(output_path, recognized_data)
