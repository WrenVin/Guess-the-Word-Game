#Hangman
  
from random import choice
from string import ascii_letters

class Hangman:
    def __init__(self):
        self.words = {"beach":'Somewhere near an ocean', 'jerky':'A dried piece of meat', 'space': 'The last frontier', 'clouds':'in the sky', 'house':'A building you spend alot of time in', 'trial':'Something you go though for commiting a crime', 'Earth':'Big, Blue, and green', 'money':'Somthing everyone wants more of', 'train':'the invention that laid the "Tracks" for the future', 
        'about':'close to or almost', 'knowledge':'something the really smart people have', 'people':'You, your aunt, your baby brother, you mean ELA teacher, etc.', 'steal':'somthing that criminals do', 'goodness':'somthing that we need more of', 'child':'young human', 'hands':'you have two on your arms', 'place':'word for somewhere you are', 'weeks':'there are 56 of these in a year', 'government':'somthing that controls our country', 
        'company':'another word for a large buisness', 'math':'somthing we learn at school'}
        for self.word in self.words.keys():
            self.final_word = self.word
            #print(self.final_word)
            break
        self.b = self.words.get('{}'.format(self.final_word))
        self.char_num = 0
        self.word = self.final_word[self.char_num]
        
    def main(self):
        self.lost = True
        self.amount_found_word = ''
        print("Welcome to Hangman Digital! Make sure to only enter lowercase letters. \nYou only have 30 tries. Make sure to only enter ONE letter at a time.")
        hint = input('Would you like a hint?(y/n):')
        if hint == 'y':
            print(self.b)
        for i in range(30):
            self.input_ = input(">>>{}".format(self.amount_found_word))
            try:
                if self.input_ == self.word:
                    self.char_num += 1
                    self.word = self.final_word[self.char_num]
                    self.amount_found_word += self.input_
                    self.input_ += self.word
                if self.input_ == self.final_word:
                    raise IndexError
            except IndexError:
                self.lost = False
                break
        if self.lost:
            print('You Lost...')
        else:
            print('You Won!!! Final Word:{}'.format(self.final_word))
 
while True:
    hangman = Hangman()
    hangman.main()
    restart = input('Again?(y/n):')
    if restart != 'y':
        break
  























