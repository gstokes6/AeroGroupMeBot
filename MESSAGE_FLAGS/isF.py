from MESSAGE_FLAGS import messageFlag
import groupMe

class isF(messageFlag.messageFlag):
    def __init__(self,message):
        super().__init__(message)
        
    def checkTrue(self,message):
        ##Logic to find if flag is set
        splitF = message['text'].lower().split(' ')
        Msg = message['text'].lower()
        if(("f" in splitF): ## and ("get" in splitF)) or (("f" in splitF) and ("chat" in splitF)):
            self.isTrue = True
    def response(self):
        groupMe.reply('F')
        
