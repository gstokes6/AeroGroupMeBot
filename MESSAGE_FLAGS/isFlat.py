from MESSAGE_FLAGS import messageFlag
import groupMe

class isFlat(messageFlag.messageFlag):
    def __init__(self,message):
        super().__init__(message)
        
    def checkTrue(self,message):
        ##Logic to find if flag is set
        Msg = message['text'].lower()
        if ("flat" in Msg) and ("earth" in Msg):
            self.isTrue = True

    def response(self):
        groupMe.reply_with_image('Checkmate atheists', 'flatMoon.png')
        
