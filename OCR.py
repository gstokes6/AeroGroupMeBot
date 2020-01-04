import subprocess
import os
import sys
import wget

def main(Picture):
    PictureFile = wget(Picture['url'],'OCRtemp.png')
    command = ['tesseract', PictureFile, 'ocrTemp']
    proc = subprocess.Popen(command, stderr=subprocess.PIPE)
    f = open('ocrTemp')
    string = f.read()
    f.close()
    print(string)
    return string
