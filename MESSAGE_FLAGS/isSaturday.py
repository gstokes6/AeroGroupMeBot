from MESSAGE_FLAGS import messageFlag
import groupMe

class isSaturday(messageFlag.messageFlag):
    def __init__(self,message):
        super().__init__(message)
        self.retort = ""
        
    def checkTrue(self,message):
        ##Logic to find if flag is set
        splitText = message['text'].lower().split('saturdays',1)
        if ('saturdays' in message['text']) and ("SAT" in message['scheduleList']) and ("dads" in splitText[1]):
            self.satCheck = True
            self.isTrue = True
        
        elif ('saturdays' in message['text']) and ("dads" in splitText[1]):
            self.satCheck = False
            self.isTrue = True
                
        else:
            self.satCheck = False
            
    def response(self):
        if self.satCheck:
            groupMe.reply_with_image('And Dad\'s car!', 'and_dads_car.png')
        else:
            groupMe.reply('You fool, it\'s not Saturday!')
        

