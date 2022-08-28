#! /usr/local/bin/python3.9

from PIL import ImageGrab
from easyocr import easyocr
import aircv as ac

def updateScreen():
    img = ImageGrab.grab()
    img.save("screen.png")

def readScreen():
    updateScreen()
    reader = easyocr.Reader(["ch_sim", "en"])
    return reader.readtext("screen.png")

def get_pos_base2img(src_path,obj_path):
    src = ac.imread(src_path)
    objsrc = ac.imread(obj_path)
    pos = ac.find_template(src,objsrc,threshold=0.9)
    if pos:
        return pos["result"]
    return pos