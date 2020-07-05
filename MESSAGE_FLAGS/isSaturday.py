from MESSAGE_FLAGS import messageFlag
import groupMe

class isSaturday(messageFlag.messageFlag):
    def __init__(self,message):
        super().__init__(message)
        
    def checkTrue(self,message):
        ##Logic to find if flag is set
        Msg = message['text'].lower()
        if("Saturdays are made for dads" in Msg):
            self.isTrue = True
    def response(self):
        groupMe.reply('And Dad\'s car!')
        
