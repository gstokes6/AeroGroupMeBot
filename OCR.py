import subprocess
import os
import sys
import wget
import pytesseract
from PIL import Image

def main(Picture):
    PictureFile = wget.download(Picture['url'],'OCRtemp.png')
    image = Image.open('OCRtemp.png')
    Output =  pytesseract.image_to_string('OCRtemp.png', timeout=2)
    print(Output)
    return Output
