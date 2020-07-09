from MESSAGE_FLAGS import messageFlag
import groupMe

class isF(messageFlag.messageFlag):
    def __init__(self,message):
        super().__init__(message)
        
    def checkTrue(self,message):
        ##Logic to find if flag is set
        splitF = message['text'].lower().split('f',1)
        Msg = message['text'].lower()
        if(("f" in Msg) and ("get" in splitF[0])) or (("f" in Msg) and ("chat" in splitF[1])):
            self.isTrue = True
    def response(self):
        groupMe.reply('F')
        
