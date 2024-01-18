from pandas import read_csv
from random import randint, shuffle, choice

CSV_FILE = 'data/french_words.csv'

class Flashcard:
    # initialize the class
    def __init__(self):
        self.df = read_csv(CSV_FILE)
        self.data = self.df.to_dict(orient='records')
        self.random_word = choice(self.data)

    def get_random_word(self):
        self.random_word = choice(self.data)

