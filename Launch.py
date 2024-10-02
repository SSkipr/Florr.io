import easyocr
import cv2
import os
import pyautogui
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Initialization
Initialize = input("SSkipr's Florr.io Anti AFK | ")
ToS = input("BY CLICKING ENTER/RETURN, YOU ACKNOWLEDGE THAT YOU UNDERSTAND THE RISKS INVOLVED AND AGREE THAT I AM NOT RESPONSIBLE FOR ANY CONSEQUENCES THAT MAY ARISE FROM ITS USE. USE THIS TOOL AT YOUR OWN DISCRETION | ")

# Verification // this was intended for the .exe, but its not working rn
url = "https://tlc-development.netlify.app/"
html = urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")
for script in soup(["script", "style"]):
    script.extract()
text = soup.get_text()
lines = (line.strip() for line in text.splitlines())
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
AppVersion = '\n'.join(chunk for chunk in chunks if chunk)

if AppVersion == "Shutdown":
    print("SSkipr has closed this gateway")
else:
    print("SSkipr's Florr.io Anti AFK | Version: " + AppVersion)

time.sleep(2)

"""
  __  __       _       
 |  \/  |     (_)      
 | \  / | __ _ _ _ __  
 | |\/| |/ _` | | '_ \ 
 | |  | | (_| | | | | |
 |_|  |_|\__,_|_|_| |_|                   

"""

# Initialize EasyOCR Reader
reader = easyocr.Reader(['en'])

pics_directory = os.path.join(os.path.dirname(__file__), 'FlorrAntiAFKBin')
os.makedirs(pics_directory, exist_ok=True)

while True:
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
        print('_object_ was not found in the screenshot.')

    time.sleep(5)
