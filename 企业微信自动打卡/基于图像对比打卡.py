#! /usr/local/bin/python3.9

import os
import time
import pyautogui
from readScreen import updateScreen,get_pos_base2img

def click(path):
    updateScreen()
    pos = get_pos_base2img("./screen.png", path)
    if pos:
        pyautogui.click(pos[0] / 2, pos[1] / 2)
    time.sleep(10)


os.system("open -a 企业微信")
time.sleep(10)
click("./企业微信截图/企业微信图标.png")
click("./企业微信截图/工作台.png")
click("./企业微信截图/问卷星.png")
click("./企业微信截图/每日健康.png")
click("./企业微信截图/确认.png")
click("./企业微信截图/获取位置.png")
time.sleep(10)
click("./企业微信截图/确认.png")
pyautogui.scroll(-3000)
time.sleep(2)
click("./企业微信截图/提交.png")