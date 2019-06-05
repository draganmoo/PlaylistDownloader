from django.core.management.base import BaseCommand

from spacy_api.utils.trainer import csv_to_training_format, train_model

from os.path import join



class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('training_set_csv_file', type=str, nargs='?',
            default=join('spacy_api', join('spacy_models', join('training_sets', 'training_set.csv'))))

    def handle(self, *args, **options):
        model_dir = join('spacy_api', join('spacy_models', 'model'))

        training_data = csv_to_training_format(options['training_set_csv_file'])
        train_model(training_data=training_data, model=model_dir, output_dir=model_dir)
