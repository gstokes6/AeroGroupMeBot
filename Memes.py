from PIL import Image
import numpy as np
import colorsys
import time
import random

def Vibrations():
    Names = ['Brandon Alkire', 'Thomas Benda', 'Jon Blaine', 'Laken Boone', 'Jacob Bosarge', 'Ryan Bowman', 'Dakota Burkhalter', 'Adam Burkley', 'Ike Callaway', 'Brandon Carlile', 'Madison Carrens', 'James Carver', 'Jared Chappell', 'Anthony Comer', 'Thomas Cox', 'Weston Craig', 'Jared Culberson', 'Yurou Dai', 'James Dimmette', 'Matthew Gallagher', 'Levi Gosdin', 'Zachary Griffin', 'Andrew Guazzerotti', 'Brayden Guevarra', 'Anderson Hamilton', 'Liam Hamilton', 'Christopher Heilmann', 'Ezekiel Hietala', 'Xingran Huang', 'Coleson Jeffries', 'Samuel Jones', 'Devantia Jordan', 'Timothy Jordan', 'Harrison Kerr', 'Martin Kloser', 'Joseph Kolar', 'Paul Last', 'Benjamin Lattner', 'Austen Lebeau', 'Craige Legrand', 'Joshua Losch', 'Matthew Lutz', 'Tristan Macke', 'Jordan Martindale', 'William McAtee', 'Brenden McGath', 'Katherine Milbrandt', 'Anna Miller', 'Andre Montenegro', 'Keaton Morris', 'Rebecca Morris', 'Robert Mulholland', 'Tanner Nardone', 'Dakota Newsome', 'Michael Onken', 'Megan Parker', 'Grady Pastor', 'Ethan Peterson', 'Maverick Pierce', 'Kyle Ramirez', 'Boyu Ran', 'Henry Reagan', 'Seth Rhodes', 'Cassandra Richmond', 'William Robinson', 'Ethan Russell', 'Matthew Seay', 'Zixi Shi', 'Gavin Smith', 'Harrison Smith', 'Gavin Stokes', 'Harrison Taylor', 'Hunter Terry', 'Garrett Vickery', 'Zachary Wadzinski', 'Jacob Wallace', 'Taylor Watson', 'Samuel Wheeler', 'Benjamin Williams', 'Jason Williamson', 'Bradley Windom', 'Dylan Young']
    randnum = random.randrange(len(Names))
    Person = Names[randnum]
    ans = 'The random number is '+str(randnum+1)+', so fuck '+Person+' in particular.'
    ##print(ans) 
    return ans

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
def colorizeGreen(im,weight):
    """
    Colorize PIL image `original` with the given
    'red weight', 0-1; returns another PIL image.
    """
    normX,normY = im.size
    out = Image.new('RGB',(normX,normY))
    t2 = (1-weight,1+weight*2,1-weight)
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

def GetMailen(i):
    im = Image.open("centered-mailen.jpg")
    ZoomIntensity = 1+.15*i
    RedIntensity = .004*i*i
    print(ZoomIntensity,RedIntensity)
    z = zoom(im,ZoomIntensity)
    out = colorizeGreen(z,RedIntensity)
    out.save('ModifiedMailen.jpg')

if __name__ == "__main__":
    i = 0
    out = GetHart(i)
    out.show()





