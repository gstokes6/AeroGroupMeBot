from MESSAGE_FLAGS import messageFlag

##for seeing if Gavin is invoked
from MESSAGE_FLAGS import isMentioned
import LOAD_ENV_VARS
import groupMe


class isMock(messageFlag.messageFlag):
    def __init__(self,message):
        super().__init__(message)
        
    def checkTrue(self,message):
        ##Logic to find if flag is set
        self.message = message
        ##first see if invoked
        invokedFlag = isMentioned.isMentioned(message,'73358488')#Gavin
        #invokedFlag = isMentioned.isMentioned(message,'73362029')#Academic
        self.isTrue = invokedFlag.isTrue
        
    def response(self):
        name = self.message['name']
        nameID = self.message['sender_id']
        loci = self.message['attachments'][0]['loci']
        print(loci)
        newtext = self.Mock(self.message['text'].replace('@Gavin Stokes 2','@'+name))
        #newtext = Mock(message['text'].replace('@Academic','@'+name))
        groupMe.replyMention(newtext,nameID,[loci[0],len(nameID)])

    def Mock(self,string):
        newString = ''
        num = 0
        for letter in string:
            
            if (num % 2) == 0:
                newString = newString + string[num].lower()
            else:
                newString = newString + string[num].upper()
            num = num+1
        return newString
