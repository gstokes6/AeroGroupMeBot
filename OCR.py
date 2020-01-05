import subprocess
import os
import sys
import wget

def main(Picture):
    PictureFile = wget.download(Picture['url'],'OCRtemp.png')
    command = ['tesseract', PictureFile, 'ocrTemp']
    proc = subprocess.Popen(command, stderr=subprocess.PIPE)
    f = open('ocrTemp')
    string = f.read()
    f.close()
    print('OCR String:')
    print(string)
    return string
