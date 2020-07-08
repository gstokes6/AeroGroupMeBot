from MESSAGE_FLAGS import messageFlag
import groupMe

## import datetime

class isSaturday(messageFlag.messageFlag):
    def __init__(self,message):
        super().__init__(message)
        self.retort = ""
        
    def checkTrue(self,message):
        ##Logic to find if flag is set
        splitText = message['text'].lower().split('saturdays',1)
        ## weekDay = datetime.datetime.today().weekday()
        if ('saturdays' in message['text'].lower()) and ("dads" in splitText[1]):
            self.isTrue = True
            ## if weekDay == 2:    ## Saturday
            if ("SAT" in message['scheduleList'):
                self.satCheck = True
            else:
                self.satCheck = False
                
        else:
            self.isTrue = False
            self.satCheck = False
            
    def response(self):
        if self.satCheck:
            groupMe.reply_with_image('And Dad\'s car!', 'and_dads_car.png')
        else:
            groupMe.reply('You fool, it\'s not Saturday!')
        

