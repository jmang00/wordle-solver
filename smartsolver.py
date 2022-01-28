from pprint import pprint
from data.answers import answers
from data.all_words import all_words
from copy import copy
from random import choice
from pprint import pprint

def is_answer_still_possible(possible_answer, guess, outcome):
    for i in range(5):
        if outcome[i] == 'g' and guess[i] != possible_answer[i]:
            return False

        if outcome[i] == 'y' and (guess[i] not in possible_answer or guess[i] == possible_answer[i]):
            return False

        if outcome[i] == ' ' and guess[i] in possible_answer:
            if guess[i] == possible_answer[i]:
                return False
                
            for j in range(5):
                if guess[i] == guess[j]: # for each instance in the possible answer
                    if outcome[j] != ' ': # if there's a colour, that means the answer is still possible so break the loop
                        break
            else:
                # given the the letter is in the word, but all of the instances are grey, you can safely remove the word
                return False
    
    return True

class Solver:
    def __init__(self):
        self.possible_answers = copy(answers)
        self.yellows = [[],[],[],[],[]]
        self.greens = ['','','','','']
        
    
    def get_guess(self):
        if len(self.possible_answers) <= 2:
            return self.possible_answers[0]

        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        frequencies = [{letter:0 for letter in alphabet} for i in range(5)]

        for possible_answer in self.possible_answers:
            for i in range(5):
                frequencies[i][possible_answer[i]] += 1
        
        scores = {}
        for word in all_words:
            yellows = 0
            greens = 0

            for i in range(5): # i is the position of the letter in the guess
                
                # greens
                if self.greens[i] == '': # if it's already confirmed as a certain letter, you can't get a new green there
                    greens += frequencies[i][word[i]]

                # yellows
                for j in range(5):
                    # j is the position of the letter in the answer
                    if i == j:
                        # don't add to the yellow score if the letter is in the right position
                        break
                    if word[i] == word[j] and i > j:
                        # for double letters in the guess, where the current letter is the second one, don't score again
                        break
                    if word[i] == self.greens[j]:
                        # don't count yellows for letters that are known to be in the word
                        break
                    if word[i] in self.yellows[i]:
                        # don't count yellows if you already know that letter is yellow
                        break

                    # if word[i] in self.greens: and word[i]
                    yellows += frequencies[i][word[i]]
            
            
            score = greens + yellows

            scores[word] = score
        
        scores = sorted( scores.items(), key=lambda x: x[1], reverse=True )

        # print(scores[:10])
        # pprint(frequencies)
        # print(self.possible_answers)
        # print(self.greens)

        return scores[0][0]
    
    def set_outcome(self,guess,outcome):
        # For each word in possible_answers, if is_answer_still_possible returns False then it is removed from the list
        self.possible_answers = list( filter( lambda x: is_answer_still_possible(x,guess,outcome), self.possible_answers ) )

        for i in range(5):
            if outcome[i] == 'y':
                self.yellows[i].append(guess[i])
            if outcome[i] == 'g':
                self.greens[i] = guess[i]




