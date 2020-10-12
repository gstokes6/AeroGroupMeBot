from MESSAGE_FLAGS import messageFlag
import groupMe

import datetime
from datetime import timedelta

class isBirthday(messageFlag.messageFlag):
    def __init__(self, message):
        super().__init__(message)
        self.retort = ""
        
    def checkTrue(self, message):
        ##Logic to find if flag is set
        currentDate = datetime.datetime.today() - timedelta(hours=5)
        self.month = str(currentDate.month)
        self.day = str(currentDate.day)
        self.hour = str(currentDate.hour)
        self.minute = str(currentDate.minute)
        if ('special' in message['text'].lower()) and ('day' in message['text'].lower()) and (currentDate.month == 10) and (currentDate.day == 12):
            self.name = 'Gavin Stokes'
            self.isTrue = True
            # if (currentDate.day == 12) and (currentDate.month == 10):

                # self.chrisCheck = True
            
    def response(self):
        groupMe.reply('happy birthday to the absolute lad @'+self.name)