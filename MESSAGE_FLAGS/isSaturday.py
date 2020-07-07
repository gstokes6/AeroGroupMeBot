from MESSAGE_FLAGS import messageFlag
import groupMe

class isSaturday(messageFlag.messageFlag):
    def __init__(self,message):
        super().__init__(message)
        self.retort = ""
        
    def checkTrue(self,message):
        ##Logic to find if flag is set
        if ('saturdays' in message['text']) and ("SAT" in message['scheduleList']):
            self.satCheck = True
            splitText = message['text'].lower().split('saturdays',1)
            if (len(splitText)>1) and ("dads" in splitText[1]):
                self.retort = 'And Dad\'s car!'
        elif ('saturdays' in message['text']) and ("SAT" not in message['scheduleList']):
            self.satCheck = False
            splitText = message['text'].lower().split('saturdays',1)
            if (len(splitText)>1) and ("dads" in splitText[1]):
                self.retort = 'You fool, it\'s not Saturday!'
            
        self.isTrue = False
            
    def response(self):
        if self.satCheck:
            groupMe.reply_with_image(self.retort, 'and_dads_car.png')
        else:
            groupMe.reply(self.retort)
        

