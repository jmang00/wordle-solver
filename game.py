from random import choice
from data.answers import answers
from termcolor import colored

from smartsolver import Solver

def get_outcome(guess, answer):
    outcome = [' ']*5
    used = []

    # greens
    for i in range(5):
        if guess[i] == answer[i]:
            outcome[i] = 'g'
            used.append(i)
            continue
        
        for j in range(5):
            if guess[i] == answer[j] and i!=j and j not in used:
                outcome[i] = 'y'
                used.append(j)
                break

    return outcome

def game(answer=choice(answers),prnt=True):
    solver = Solver()

    for guess_no in range(6):
        # Get the guess from the solver
        guess = solver.get_guess()
        
        # Figure out the outcome
        outcome = get_outcome(guess,answer)

        # Give the outcome to the solver
        solver.set_outcome(guess,outcome)

        if prnt:
            # Print the guess & it's outcome
            text = ''
            for i in range(5):
                if outcome[i] == ' ':
                    background = 'on_white'
                elif outcome[i] == 'y':
                    background = 'on_yellow'
                else:
                    background = 'on_green'

                text += colored('\u200A' + guess[i]+ '\u200A', 'grey', background, attrs=['bold'])
            print(text)

        # Check if the game has been won
        if guess == answer:
            if prnt:
                print(f'Won in {guess_no + 1} guesses :)\n')
            return guess_no + 1
    else:
        if prnt:
            print('Lost :(\n')
        return False

game()


# Test accuracy
won = 0
total = 0
for i,answer in enumerate(answers[:100]):
    result = game(answer,prnt=False)
    print(i,result)
    if result:
        won += 1
        total += result

print(f'Won {won} out of {len(answers)} ({round(won/len(answers)*100,2)}%), with {total} total guesses ({round(total/len(answers),2)} avg)')

    

