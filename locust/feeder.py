import os
import csv
import random

class Feeder():
    def __init__(self, file_path):
        if(os.path.isabs(file_path)):
           absfile_path = file_path
        else:
            # a relative path was provided.
           base_path = os.path.dirname(os.path.realpath(__file__))
           absfile_path = os.path.join(base_path, file_path)
        self.feed_items = self.load_csv(absfile_path)

    def load_csv(self, file_path):
        with open(file_path) as csvfile:
            reader = csv.DictReader(csvfile)
            rows_dict = list(reader)
            return rows_dict
    def get_list(self):
        return self.feed_items
    def next(self):
        #FIXME Add support for other fetch strategies e.g Sequential
        return random.choice(self.feed_items)
    def is_empty(self):
        if self.feed_items:
             return False
        return True
