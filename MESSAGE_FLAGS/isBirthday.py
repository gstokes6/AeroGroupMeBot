from MESSAGE_FLAGS import messageFlag
import groupMe

import datetime

class isBirthday(messageFlag.messageFlag):
    def __init__(self, message):
        super().__init__(message)
        self.retort = ""
        
    def checkTrue(self, message):
        ##Logic to find if flag is set
        currentDate = datetime.datetime.today()
        self.month = str(currentDate.month)
        self.day = str(currentDate.day)
        self.hour = str(currentDate.hour)
        self.minute = str(currentDate.minute)
        if ('special' in message['text'].lower()) and ('day' in message['text'].lower()):
            self.name = 'Gavin Stokes'
            self.isTrue = True
            # if (currentDate.day == 12) and (currentDate.month == 10):

                # self.chrisCheck = True
            
    def response(self):
        groupMe.reply('happy birthday to the absolute lad @'+self.name+' on this beautiful day of '+self.month+'/'+self.day+' at the magnificent time of '+self.hour+':'+self.minute)