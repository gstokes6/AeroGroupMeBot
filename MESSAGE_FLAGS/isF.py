from MESSAGE_FLAGS import messageFlag
import groupMe

class isF(messageFlag.messageFlag):
    def __init__(self,message):
        super().__init__(message)
        
    def checkTrue(self,message):
        ##Logic to find if flag is set
        splitF = message['text'].lower().split(' ')
        Msg = message['text'].lower()
        if("f" in splitF):
            split2 = message['text'].lower().split('f', 1)
            if ("chat" in split2[1]) or ("get" in split2[0]):
                self.isTrue = True
    def response(self):
        groupMe.reply('F')
        
