from MESSAGE_FLAGS import messageFlag
import groupMe

class isSaturday(messageFlag.messageFlag):
    def __init__(self,message):
        super().__init__(message)

    def checkTrue(self,message):
        ##Logic to find if flag is set
        splitText = message['text'].lower().split('saturdays',1)
        if len(splitText)>1:
            if("dads" in splitText[1]):
                if "SAT" in message['scheduleList']:
                    self.retort = 'And Dad\'s car!'
                    self.satCheck = True
                else:
                    self.retort = 'You fool, it\'s not Saturday!'
                    self.satCheck = False
                    
                self.isTrue = True
            
    def response(self):
        if self.satCheck:
            groupMe.reply_with_image(self.retort, 'and_dads_car.png')
        else:
            groupMe.reply(self.retort)
        

