import answers
import random
import time
from pyautogui import position, write, click
from PIL.ImageGrab import grab

def check_answer(answer):
    global guess, outcome

    
    for i in range(5):
        if outcome[i] == ' ' and guess[i] in answer and guess.count(outcome[i])==1:
            return False
            
        if outcome[i] == 'y' and (guess[i] not in answer or guess[i] == answer[i]):
            return False
        
        if outcome[i] == 'g' and guess[i] != answer[i]:
            return False
        
    return True

def is_color_close(color,target):
    for i in range(4):
        if abs(color[i] - target[i]) > 10:
            return False
    return True
    

# Define colours
BLANK = (231, 232, 238, 255)
GREY = (101, 106, 128, 255)
YELLOW = (233, 178, 43, 255)
GREEN = (102, 169, 89, 255)


# Define grid position
x0 = 1020
y0 = 480
dx = 200
dy = 200

# use the follwing to figure out positions, then DOUBLE these values:
# print(position()) 

while True:
    possible_answers = answers.answers

    for i in range(6):
        # time.sleep(1)

        print(possible_answers)
        # Randomly guess from the potential answers
        guess = random.choice(possible_answers)
        write(guess+'\n')

        # Check the outcome of the guess
        outcome = ''
        pixels = grab().load() # take a screengrab and load pixels
        for x in range(5):
            pixel_color = pixels[ x0 + x*dx, y0 + i*dy ]
            if is_color_close(pixel_color, GREY):
                outcome += ' '
            elif is_color_close(pixel_color, YELLOW):
                outcome += 'y'
            elif is_color_close(pixel_color, GREEN):
                outcome += 'g'
            else:
                print(f'Couldn\'t pick up letter {x}')

        if outcome == 'ggggg' or outcome=='': #second part is a temporary way to fix the code breakinghilly
            print('Got it!')
            break

        # outcome = input(guess+' ')
        # enter the outcome: 
        # ' ' = gray, wrong letter
        # 'y' = yellow, correct letter wrong spot
        # 'g' = green, correct letter correct spot
        # eg enter 'yg y ' 

        possible_answers = list(filter(check_answer,possible_answers))
        # print(possible_answers)
    else:
        print('Failed :((')
        break

    time.sleep(1)
    click((720,720))
