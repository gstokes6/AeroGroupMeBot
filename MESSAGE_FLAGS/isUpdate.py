from MESSAGE_FLAGS import messageFlag

##for seeing if academic is invoked
from MESSAGE_FLAGS import isAcademicInvoked
import LOAD_ENV_VARS
import groupMe

class isUpdate(messageFlag.messageFlag):
    def __init__(self,message):
        super().__init__(message)
        
    def checkTrue(self,message):
        ##Logic to find if flag is set
        
        ##first see if invoked
        invokedFlag = isAcademicInvoked.isAcademicInvoked(message)
        isInvoked = invokedFlag.isTrue
        
        ##see if keyword is in message
        Msg = message['text'].lower()
        Msg = Msg.replace('@academic','').replace('[[academic]]','')
        isKeyPhrase = ( "update" in Msg )

        if (isKeyPhrase and isInvoked):
            self.willLike = True
            self.isTrue = True
        
    def response(self):
        updateFile = LOAD_ENV_VARS.gDrive.FindOrCreateFolder(drive,['Bot Guts','Update.txt'])
        updateTextFile = drive.CreateFile({'id':updateFile['id']})
        updateText = updateTextFile.GetContentString()
        groupMe.reply(updateText)
        
