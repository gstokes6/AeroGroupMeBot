from MESSAGE_FLAGS import messageFlag

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
        groupMe.reply("This is where I would put my hartfield code, IF I HAD ONE")
        
