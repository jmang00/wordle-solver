from data.answers import answers
from copy import copy
from random import choice


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
    
    def get_guess(self):
        return choice(self.possible_answers)
    
    def set_outcome(self,guess,outcome):
        # For each word in possible_answers, if is_answer_still_possible returns False then it is removed from the list
        self.possible_answers = list( filter( lambda x: is_answer_still_possible(x,guess,outcome), self.possible_answers ) )





