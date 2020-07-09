from MESSAGE_FLAGS import messageFlag
import groupMe

class isButter(messageFlag.messageFlag):
    def __init__(self,message):
        super().__init__(message)
        
    def checkTrue(self,message):
        ##Logic to find if flag is set
        Msg = message['text'].lower()
        if("you pass butter" in Msg) or ("pass the butter" in Msg):
            self.isTrue = True
    def response(self):
        groupMe.reply('oh my god.')
        
