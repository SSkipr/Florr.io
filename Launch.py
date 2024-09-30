import easyocr
import cv2
import os
import pyautogui
import time


Initialize = input("SSkipr's Florr.io Anti AFK | ")
ToS = input("yap | ")



reader = easyocr.Reader(['en'])


pics_directory = os.path.join(os.path.dirname(__file__), 'FlorrAntiAFKBin')
os.makedirs(pics_directory, exist_ok=True)

screenshot_path = os.path.join(pics_directory, 'FlorrAntiAFKPicture.png')
image = pyautogui.screenshot()
image.save(screenshot_path)

image_cv = cv2.imread(screenshot_path)

result = reader.readtext(image_cv)

found = False
for (bbox, text, prob) in result:
    if "I'm here" in text:
        found = True
        print(f'Found _object_ at location: {bbox}')

        x_min = int(bbox[0][0])
        y_min = int(bbox[0][1])
        x_max = int(bbox[2][0])
        y_max = int(bbox[2][1])
        center_x = (x_min + x_max) // 2
        center_y = (y_min + y_max) // 2
        
        pyautogui.click(center_x, center_y)
        print(f'Clicked at: ({center_x}, {center_y})')
        time.sleep(1)

if found:
    print('_object_ was found in the screenshot.')
else:
    print('_object_was not found in the screenshot.')
