import subprocess
import os
import sys
import wget
import pytesseract

def main(Picture):
    PictureFile = wget.download(Picture['url'],'OCRtemp.png')
    Output =  pytesseract.image_to_string('OCRtemp.png', timeout=2)
    print(Output)
    return Output
