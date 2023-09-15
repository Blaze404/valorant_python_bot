import screenshot
import pyautogui as pag
import random
import time
import pynput.keyboard as kb # import Key, Controller
import pynput.mouse as ms # import Button, Controller
import numpy as np

keyboard = kb.Controller()
mouse = ms.Controller()


VANDAL_COORDINATES = [820, 610]

bought_this_round = False
bought = time.time()

time.sleep(2)
movement = "random"
while True:
    ## check if but phase
    if bought_this_round:
        current = time.time()
        diff = int(current - bought)
        if diff >= 50:
            bought_this_round = False

    try:
        is_buy_phase = screenshot.is_buy_phase()
    except:
        is_buy_phase = False
    if is_buy_phase and not bought_this_round:
        bought = time.time()
        bought_this_round = True
        ## click b
        keyboard.press("b")
        time.sleep(0.5)
        keyboard.release("b")

    # pag.moveTo(VANDAL_COORDINATES[0], VANDAL_COORDINATES[1], duration = 0.5)
        mouse.position = (VANDAL_COORDINATES[0], VANDAL_COORDINATES[1])
        mouse.click(ms.Button.left, 1)
        


        sequence = ["w", "w", "d", "d", "1", "g", kb.Key.esc, "s", "s", "a", "a", "z"]
        for s in sequence:
            keyboard.press(s)
            time.sleep(0.5)
            keyboard.release(s)

    if movement == 'random':
        keys = ["w", "a", "s", "d", "r", "w", "a", "s", "d"]
        key = np.random.choice(keys)
        # for key in keys:
        keyboard.press(key)
        time.sleep(0.5)
        keyboard.release(key)
        
        if key=="r":
            time.sleep(0.5)
            
        keyboard.press(key)
        time.sleep(0.5)
        keyboard.release(key)
        time.sleep(0.5)   
        mouse.click(ms.Button.left, 1)
    
    if movement == 'circular':
        keys = ["w", "a", "s", "d", "r"]
        for key in keys:
        # for key in keys:
            keyboard.press(key)
            time.sleep(0.5)
            keyboard.release(key)
            #time.sleep(0.5)
            keyboard.press(key)
            time.sleep(0.5)
            keyboard.release(key)
            time.sleep(0.5)   
        mouse.move(5, -5)
        mouse.click(ms.Button.left, 1)

