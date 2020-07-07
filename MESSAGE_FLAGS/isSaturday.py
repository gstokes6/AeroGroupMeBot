from MESSAGE_FLAGS import messageFlag
import groupMe

class isSaturday(messageFlag.messageFlag):
    def __init__(self,message):
        super().__init__(message)
        self. retort = ""
        
    def checkTrue(self,message):
        ##Logic to find if flag is set
        if "SAT" in message['scheduleList']:
            self.satCheck = True
            splitText = message['text'].lower().split('saturdays',1)
            if len(splitText)>1:
                if("dads" in splitText[1]):
                    self.retort = 'And Dad\'s car!'
        else:
            self.satCheck = False
            self.retort = 'You fool, it\'s not Saturday!'
            
        self.isTrue = True
            
    def response(self):
        if self.satCheck:
            groupMe.reply_with_image(self.retort, 'and_dads_car.png')
        else:
            groupMe.reply(self.retort)
        

