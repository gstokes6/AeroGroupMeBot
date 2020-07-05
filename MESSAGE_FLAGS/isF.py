from MESSAGE_FLAGS import messageFlag
import groupMe

class isF(messageFlag.messageFlag):
    def __init__(self,message):
        super().__init__(message)
        
    def checkTrue(self,message):
        ##Logic to find if flag is set
        Msg = message['text'].lower()
        if("f in the chat" in Msg) or ("get an f" in Msg) or ("get a f" in Msg):
            self.isTrue = True
    def response(self):
        groupMe.reply('F')
        
