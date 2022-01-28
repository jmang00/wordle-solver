from time import sleep
from pyautogui import position, write, click
from PIL.ImageGrab import grab

import solver


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
# use print(position()) to figure out positions, then DOUBLE these values
x0 = 1020
y0 = 480
dx = 200
dy = 200
outcome = None


while True:
    sleep(1)
    click((720,640))

    for guess_no in range(6):
        sleep(1)

        # Randomly guess from the potential answers
        guess = solver.get_guess()
        write(guess+'\n')

        # Check the outcome of the guess
        outcome = ''
        pixels = grab().load() # take a screengrab and load pixels
        for i in range(5):
            pixel_color = pixels[ x0 + i*dx, y0 + guess_no*dy ]
            if is_color_close(pixel_color, GREY):
                outcome += ' '
            elif is_color_close(pixel_color, YELLOW):
                outcome += 'y'
            elif is_color_close(pixel_color, GREEN):
                outcome += 'g'
            else:
                print(f'Couldn\'t pick up colour of letter {x}')
        
        if len(outcome) < 5:
            print('Something went wrong')
            again = False
            break

        if outcome == 'ggggg' or outcome=='':
            print('Got it!')
            again = True
            break

        solver.set_outcome(guess,outcome)

        # if manually inputting outcome:
        # outcome = input(guess+' ')
        # enter the outcome: 
        # ' ' = gray, wrong letter
        # 'y' = yellow, correct letter wrong spot
        # 'g' = green, correct letter correct spot
        # eg enter 'yg y ' 

    else:
        print('Failed :((')
        break
    
    if not again:
        break
