from pandas import read_csv, DataFrame
from random import randint, shuffle, choice

CSV_FILE = 'data/french_words.csv'
TO_LEARN = 'data/to_learn.csv'
LEARNT = 'data/learnt.csv'
class Flashcard:
    # initialize the class
    def __init__(self):
        try:
            self.to_learn = read_csv(TO_LEARN)
        except FileNotFoundError:
            # if the file doesn't exist, create it as a copy of CSV_FILE
            with open(TO_LEARN, 'w') as file:
                read_csv(CSV_FILE).to_csv(file, index=False)
            # close the file
            file.close()
        try:
            self.learnt = read_csv(LEARNT)
        except FileNotFoundError:
            # if the file doesn't exist create a file with the headers French, English
            with open(LEARNT, 'w') as file:
                file.write('French,English\n')
            # close the file
            file.close()

        self.df = read_csv(TO_LEARN)
        self.data = self.df.to_dict(orient='records')
        self.card = choice(self.data)
        
    def get_next_card(self):
        file = read_csv(TO_LEARN)
        df = file.to_dict(orient='records') 
        self.card = choice(df)

    def add_to_learnt(self):
        # add the card to the learnt file
        with open(LEARNT, 'a') as file:
            file.write(f"{self.card['French']},{self.card['English']}\n")
        # close the file
        file.close()
        self.remove_from_to_learn()
    
    def remove_from_to_learn(self):
        file = read_csv(TO_LEARN)
        df = file.to_dict(orient='records')
        df.remove(self.card)
        # convert the list of dictionaries to a dataframe object
        df = DataFrame(df)
        # drop the row that matches the card
        df = df.drop(df[df['French'] == self.card['French']].index)
        # overwrite the TO_LEARN csv file with the updated dataframe
        df.to_csv(TO_LEARN, index=False)

        




  

    
    

