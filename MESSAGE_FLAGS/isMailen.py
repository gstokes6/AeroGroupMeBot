from MESSAGE_FLAGS import messageFlag
  
from PIL import Image
import colorsys
import datetime

##for seeing if academic is invoked
from MESSAGE_FLAGS import isAcademicInvoked
import LOAD_ENV_VARS
import groupMe

class isMailen(messageFlag.messageFlag):
    def __init__(self,message):
        super().__init__(message)
        self.message = message
        
    def checkTrue(self,message):
        ##Logic to find if flag is set
        
        ##first see if invoked
        invokedFlag = isAcademicInvoked.isAcademicInvoked(message)
        isInvoked = invokedFlag.isTrue
        
        ##see if keyword is in message
        Msg = message['text'].lower()
        isKeyPhrase = ( ("i need more coffee" in Msg) )

#        if (isKeyPhrase and isInvoked):
        if (isKeyPhrase):
            self.isTrue = True
        
    def response(self):
        CounterFile = LOAD_ENV_VARS.gDriveInstance.FindOrCreateFolder(['Bot Guts','MailenCounter.txt'])
        Counter = LOAD_ENV_VARS.gDriveInstance.drive.CreateFile({'id':CounterFile['id']})
        
        date_time_obj = datetime.datetime.strptime(Counter['modifiedDate'], '%Y-%m-%dT%H:%M:%S.%fZ')            
        if (date_time_obj.date() != datetime.datetime.fromtimestamp(self.message['created_at']).date()):
            Iteration = 0
        else:
            Iteration = int(Counter.GetContentString())
        self.GetHart(Iteration)
        groupMe.reply_with_image("Ole Relatable Russell. Today's count: " + str(Iteration+1),"ModifiedMailen.jpg")
        Counter.SetContentString(str(Iteration+1))
        Counter.Upload()

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
        t2 = (1-weight,1+weight*2,1-weight)
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

    def GetMailen(self,i):
        im = Image.open("centered-mailen.jpg")
        ZoomIntensity = 1+.15*i
        GreenIntensity = .004*i*i
        z = self.zoom(im,ZoomIntensity)
        out = self.colorize(z,GreenIntensity)
        out.save('ModifiedMailen.jpg')
