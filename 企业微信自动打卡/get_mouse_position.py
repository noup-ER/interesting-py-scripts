import time
from PIL import ImageGrab
import pyautogui


img = ImageGrab.grab()
screen_x = pyautogui.size().width
screen_y = pyautogui.size().height
real_x = img.size[0]
real_y = img.size[1]
rate_x = screen_x / real_x
rate_y = screen_y / real_y
time.sleep(2)
x = pyautogui.position()[0]
y = pyautogui.position()[1]
print(x/rate_x,y/rate_y)