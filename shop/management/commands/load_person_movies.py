import os.path
import json
from django.core.management.base import BaseCommand
from shop.models import PersonMovie


class Command(BaseCommand):
    help = 'load person and title movie'

    def add_arguments(self, parser):
        parser.add_argument('-f', '--file', type=str, help='Define a file with data')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file']
        if not os.path.isfile(file_path):
            print("File path {} does not exist.".format(file_path))
        with open(file_path) as file:
            for line in file.readlines():
                data = line.split('\t')

                data[5] = data[5].strip('\n')
                data[5] = data[5].split(',')

                person_movie = PersonMovie(None, data[0], data[2], data[1], data[3], data[4], data[5])
                person_movie.save()