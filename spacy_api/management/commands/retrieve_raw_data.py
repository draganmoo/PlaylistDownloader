from django.core.management.base import BaseCommand

from spacy_api.utils.utils import retrieve_raw_data, save_data_to_csv

import os



class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('playlist_id', type=str)

    def handle(self, *args, **options):
        raw_data = retrieve_raw_data(options['playlist_id'])
        path = os.path.join('spacy_api', os.path.join('spacy_models', os.path.join('training_sets', 'raw.csv')))
        save_data_to_csv(path, raw_data)