from django.core.management.base import BaseCommand
import os
from shop.models import Movie


class Command(BaseCommand):
    help = 'load movies'

    def add_arguments(self, parser):
        parser.add_argument('-f', '--file', type=str, help='Define a file with data')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file']
        if not os.path.isfile(file_path):
            print("File path {} does not exist.".format(file_path))
        with open(file_path) as file:
            for line in file.readlines():
                data = line.split('\t')
                if data[5] == '\\N':
                    data[5] = None
                else:
                    data[5] += '-12-31'
                data[8] = data[8].strip('\n')
                data[8] = data[8].split(',')

                movie = Movie(data[0], data[1], data[3], data[4], data[5], data[8])
                movie.save()

