from PIL import Image
import numpy as np
import colorsys
import time

def TupleMulti(t1,t2):
    t3 = []
    for i in range(0,len(t1)):
        t3.append(t1[i]*t2[i])
    return( round(t3[0]), round(t3[1]), round(t3[2]))

def colorize(im,weight):
    """
    Colorize PIL image `original` with the given
    'red weight', 0-1; returns another PIL image.
    """
    normX,normY = im.size
    out = Image.new('RGB',(normX,normY))
    t2 = (1+weight*2,1-weight,1-weight)
    for X in range(0,normX):
        for Y in range(0,normY):
            out.putpixel((X,Y),TupleMulti(im.getpixel((X,Y)),t2))
    return out

def zoom(im,zoom):
    normX,normY = im.size
    scale = 1.0/zoom
    box = (round(normX/2) - round(normX*scale/2),round(normY/2) - round(normY*scale/2),round(normX/2) + round(normX*scale/2),round(normY/2) + round(normY*scale/2))
    out = im.crop(box)
    out = out.resize((normX,normY))
    return out

def GetHart(i):
    im = Image.open("centered-hartfield-roy.jpg")
    ZoomIntensity = 1+.15*i
    RedIntensity = .004*i*i
    print(ZoomIntensity,RedIntensity)
    z = zoom(im,ZoomIntensity)
    out = colorize(z,RedIntensity)
    out.save('ModifiedHart.jpg')


if __name__ == "__main__":
    i = 0
    out = GetHart(i)
    out.show()





