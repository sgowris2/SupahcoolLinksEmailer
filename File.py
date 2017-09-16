__author__ = 'sudeep'

import csv
from Participant import get_participants


class File:
    def __init__(self, filename):
        self.filename = filename
        self.raw_list = get_list_from_file(self.filename)
        self.participants = get_participants(self.raw_list)


def get_list_from_file(filename):
    f = open(filename, 'rb')
    csv_reader = csv.reader(f)
    return list(csv_reader)