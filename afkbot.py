import pyautogui as pag
import random
import time
import pynput.keyboard as kb # import Key, Controller
import pynput.mouse as ms # import Button, Controller
import numpy as np

keyboard = kb.Controller()
mouse = ms.Controller()

movement = 'random'

while True:
    x = random.randint(600, 700)
    y = random.randint(200, 300)
    
    # pag.moveTo(x,y, 0.5)
    
    time.sleep(2)
    
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
    
    
    
    #contents = ["]", "2"]
    #for content in contents:
    #    keyboard.press(content)
    #    time.sleep(0.5)
    #    keyboard.release(content)
