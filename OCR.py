import subprocess
import os
import sys
import wget
import pytesseract
from PIL import Image

def main(Picture):
    TempfilePath = 'OCRtemp.jpg'
    PictureFile = wget.download(Picture['url'],TempfilePath)
    
    image = Image.open(TempfilePath)
    #Output =  pytesseract.image_to_string(TempfilePath, timeout=2)
    Output =  pytesseract.image_to_string(image, timeout=2)
    print(Output)
    return Output
