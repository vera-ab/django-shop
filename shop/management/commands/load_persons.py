from django.core.management.base import BaseCommand
import os
from shop.models import Person


class Command(BaseCommand):
    help = 'load person'

    def add_arguments(self, parser):
        parser.add_argument('-f', '--file', type=str, help='Define a file with data')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file']
        if not os.path.isfile(file_path):
            print("File path {} does not exist.".format(file_path))
        with open(file_path) as file:
            for line in file.readlines():
                data = line.split('\t')
                if data[2] == '\\N':
                    data[2] = None
                else:
                    data[2]+='-12-31'
                if data[3] == '\\N':
                    data[3] = None
                else:
                    data[3] += '-12-31'

                person = Person(data[0], data[1], data[2], data[3])
                person.save()