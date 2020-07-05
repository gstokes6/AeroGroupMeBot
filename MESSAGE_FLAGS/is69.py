from MESSAGE_FLAGS import messageFlag
import groupMe

class is69(messageFlag.messageFlag):
    def __init__(self,message):
        super().__init__(message)
        
    def checkTrue(self,message):
        ##Logic to find if flag is set
        splitText = message['text'].split('6',1)
        if len(splitText)>1:
            if ("9" in splitText[1]):
                self.isTrue = True

    def response(self):
        groupMe.reply("Nice.")
        
