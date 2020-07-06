from MESSAGE_FLAGS import messageFlag
  
from PIL import Image
import colorsys

##for seeing if academic is invoked
from MESSAGE_FLAGS import isAcademicInvoked
import groupMe

class isHartfield(messageFlag.messageFlag):
    def __init__(self,message):
        super().__init__(message)
        
    def checkTrue(self,message):
        ##Logic to find if flag is set
        
        ##first see if invoked
        invokedFlag = isAcademicInvoked.isAcademicInvoked(message)
        isInvoked = invokedFlag.isTrue
        
        ##see if keyword is in message
        Msg = message['text'].lower()
        isKeyPhrase = ( ("are you with me" in Msg) or ("everybody with me" in Msg) )

        if (isKeyPhrase and isInvoked):
            self.isTrue = True
        
    def response(self):
        self.GetHart(10)
        groupMe.reply_with_image("This is where I would put my hartfield code, IF I HAD ONE","ModifiedHart.jpg")


##Supporting Functions        
    def TupleMulti(self,t1,t2):
        t3 = []
        for i in range(0,len(t1)):
            t3.append(t1[i]*t2[i])
        return( round(t3[0]), round(t3[1]), round(t3[2]))

    def colorize(self,im,weight):
        """
        Colorize PIL image `original` with the given
        'red weight', 0-1; returns another PIL image.
        """
        normX,normY = im.size
        out = Image.new('RGB',(normX,normY))
        t2 = (1+weight*2,1-weight,1-weight)
        for X in range(0,normX):
            for Y in range(0,normY):
                out.putpixel((X,Y),self.TupleMulti(im.getpixel((X,Y)),t2))
        return out

    def zoom(self,im,zoom):
        normX,normY = im.size
        scale = 1.0/zoom
        box = (round(normX/2) - round(normX*scale/2),round(normY/2) - round(normY*scale/2),round(normX/2) + round(normX*scale/2),round(normY/2) + round(normY*scale/2))
        out = im.crop(box)
        out = out.resize((normX,normY))
        return out

    def GetHart(self,i):
        im = Image.open("centered-hartfield-roy.jpg")
        ZoomIntensity = 1+.15*i
        RedIntensity = .004*i*i
        z = self.zoom(im,ZoomIntensity)
        out = self.colorize(z,RedIntensity)
        out.save('ModifiedHart.jpg')
