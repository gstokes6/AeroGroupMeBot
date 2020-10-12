from MESSAGE_FLAGS import messageFlag

##for seeing if academic is invoked
from MESSAGE_FLAGS import isAcademicInvoked
import LOAD_ENV_VARS
import groupMe

class isAutomation(messageFlag.messageFlag):
    def __init__(self,message):
        super().__init__(message)
        
    def checkTrue(self,message):
        ##Logic to find if flag is set
        
        ##first see if invoked
        invokedFlag = isAcademicInvoked.isAcademicInvoked(message)
        isInvoked = invokedFlag.isTrue
        
        Msg = message['text'].lower()
        isKeyPhrase = ( "automation" in Msg )

        if (isKeyPhrase and isInvoked):
            self.isTrue = True
        
    def response(self):
        groupMe.reply("The truth is that automation is slowly becoming the norm in workplaces across America, that's why I believe in the idea of a universal basic income. #YangGang")
