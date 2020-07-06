from MESSAGE_FLAGS import messageFlag
import groupMe

class isSaturday(messageFlag.messageFlag):
    def __init__(self,message):
        super().__init__(message)
        
    def checkTrue(self,message):
        ##Logic to find if flag is set
        Msg = message['text'].lower()
        if("saturdays are made for dads" in Msg):
            if (dtb.IsInClass(drive,Root,message['created_at']) == 'SAT'):
                retort = 'And Dad\'s car!'
            else:
                retort = 'You fool, it\'s not Saturday!'
            
            self.isTrue = True
            
    def response(self):
        groupMe.reply(retort)
        
