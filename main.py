import random
import sys
import time
import tkinter
from functools import partial

import keyboard
import pyautogui
from PIL import ImageGrab

menu = tkinter.Tk()
menu.geometry('400x600')

body = tkinter.Entry(menu, border=4, font=('Bahnschrift', 20))
body.pack(side='left', padx=20, pady=60)
body.place(x=20, y=200, height=50, width=200)

label = tkinter.Label(menu, border=4, text='Fishing Rod Abort Timer (CPU time)', font=('Bahnschrift Bold', 10))
label.place(x=20, y=150)
label1 = tkinter.Label(menu, border=4, text='(Default: 40)', font=('Bahnschrift', 10))
label1.place(x=20, y=170)

load = tkinter.Button(menu, border=4, text='Enter', font=('Bahnschrift', 20), bg='black', fg='white')
load.pack(side='right', padx=60, pady=60)
load.place(x=240, y=200, height=50, width=140)

title = tkinter.Label(menu, border=4, text='Pixelmon AutoFisher', font=('Bahnschrift Bold', 35), justify='left')
title.pack(side='right', padx=60, pady=60)
title.place(x=20, y=0)

title2 = tkinter.Label(menu, border=4, text='2022 Edition', font=('Bahnschrift Bold', 16), justify='left')
title2.pack(side='right', padx=60, pady=60)
title2.place(x=135, y=60)

title1 = tkinter.Label(menu, border=4, text='hi guys', font=('Bahnschrift', 8), justify='left')
title1.pack(side='right', padx=60, pady=60)
title1.place(x=20, y=60)

red = tkinter.Button(menu, border=20, text='FISH', font=('Bahnschrift Bold', 38), bg='red')
# red.pack(side='right', padx=60, pady=60)
red.place(x=50, y=350, height=200, width=300)


def maxTimerWrite(event):
    maxTimeropen = open('maxTimer.txt', 'w')
    if len(body.get()) == 2:
        try:
            bodyNum = int(body.get())
            maxTimeropen.write(str(bodyNum))
            maxTimeropen.close()
        except:
            pass


def cheating(event):
    ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

    fishCount = 0

    commands = ['help 3', 'help', 'review', 'lastlegend', 'help 2', 'hunt', 'buy', 'help 4', 'clan help']

    time.sleep(5)

    pyautogui.click(button='right')

    def runFisher():
        # Looks for and clicks on run button
        runFisher = list(pyautogui.locateOnScreen('run.png'))
        runFisher[0] -= 1920
        pyautogui.moveTo(runFisher)
        pyautogui.click()

        # Pauses for the battle message to disappear
        time.sleep(6)

    timer1 = 0
    maxTimeropen = open('maxTimer.txt', 'r')
    maxTimer = int(maxTimeropen.read())
    while True:
        if keyboard.is_pressed('-'):
            sys.exit()
        timer = 0
        # Looks for fished message in the console
        if pyautogui.locateOnScreen('fished.png', confidence=0.9) is None:
            print('No fishes :( ' + str(timer1))
            timer1 += 1
            if timer1 == maxTimer:
                pyautogui.press('3')
                pyautogui.press('2')
                pyautogui.keyDown('a')
                time.sleep(0.2)
                pyautogui.keyUp('a')
                for i in range(2):
                    pyautogui.press('/')
                    pyautogui.write(random.choice(commands))
                    pyautogui.press('enter')
                    time.sleep(1)
                pyautogui.click(button='right')
                timer1 = 0

        else:
            print('Fishy!!!!!!!!!!!')
            fishCount += 1
            # Catches fish
            pyautogui.click(button='right')

            # Decides whether you fished an item or pokemon
            time.sleep(0.5)

            if pyautogui.locateOnScreen('stopMessage.png', confidence=0.8) is not None:
                # When an item is fished, continue to throw out the rod again
                pass
            # When an item is not fished, script will run from pokemon
            else:
                # Waits for battle menu
                while pyautogui.locateOnScreen('run.png', confidence=0.8) is None and timer <= 10:
                    time.sleep(1)
                    timer += 1
                    pyautogui.click(button='right')
                if timer > 10:
                    pyautogui.press('/')
                    pyautogui.write('endbattle')
                    pyautogui.press('enter')

                else:
                    runFisher()

            # Reset the console with an error message
            for i in range(2):
                pyautogui.press('/')
                pyautogui.write(random.choice(commands))
                pyautogui.press('enter')
                time.sleep(1)

            time.sleep(1)
            # Walks out a bit
            pyautogui.keyDown('w')
            time.sleep(3)
            pyautogui.keyUp('w')
            pyautogui.keyDown('a')
            time.sleep(0.5)
            pyautogui.keyUp('a')

            timer1 = 0

            # Send out a new rod
            pyautogui.click(button='right')


# Bind keypress event to handle_keypress()
load.bind("<Button-1>", maxTimerWrite)
red.bind("<Button-1>", cheating)

menu.mainloop()
