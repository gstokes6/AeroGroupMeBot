import subprocess
import os
import sys
import wget

def main(Picture):
    PictureFile = wget.download(Picture['url'],'OCRtemp.png')
    Outputfile =  'ocrTemp'
    command = ['tesseract', PictureFile, Outputfile]
    proc = subprocess.Popen(command, stderr=subprocess.PIPE)
    proc.wait()
    f = open(Outputfile)
    string = f.read()
    f.close()
    print('OCR String:')
    print(string)
    return string
