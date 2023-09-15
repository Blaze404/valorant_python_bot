from PIL import ImageGrab, Image
import time
import os
import pytesseract
path_to_save = r'C:\Users\Asus\OneDrive\Desktop\afk bot'
image_path = os.path.join(path_to_save, 'sc.png')


BUY_PHASE_COODINATES = (750,160,1100,250)

VANDAL_COORDINATES = (780, 585, 944, 723)

def process_image(iamge_name, lang_code):
    image = Image.open(iamge_name)
    return pytesseract.image_to_string(image, lang=lang_code)

def take_screenshot():
    # fullscreen
    image = ImageGrab.grab(bbox=BUY_PHASE_COODINATES)
    image.save(image_path)


def is_buy_phase():
    take_screenshot()
    string = process_image(image_path, 'eng')
    string = string.lower()
    if "buy" in string or "phase" in string:
        return True
    return False


# time.sleep(2)
# take_screenshot()
# string = process_image(image_path, 'eng')
# print(string)