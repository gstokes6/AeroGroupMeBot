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
        
        ##first see if invoked
        invokedFlag = isMentioned.isMentioned(message,'73358488')
        isInvoked = invokedFlag.isTrue
        if (isInvoked):
            self.isTrue = True
        
    def response(self):
        name = message['name']
        nameID = message['sender_id']
        newtext = Mock(message['text'].replace('@Gavin Stokes 2','@'+name))
        #newtext = Mock(message['text'].replace('@Academic','@'+name))
        replyMention(newtext,nameID,[loci[0],len(nameID)],bot_id)
