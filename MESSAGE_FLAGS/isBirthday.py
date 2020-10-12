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
        if ( ('special' in message['text'].lower()) and ('day' in message['text'].lower()) and (currentDate.day == 12) and (currentDate.month == 10):
            name = "Gavin Stokes"
            self.isTrue = True
            
    def response(self):
        groupMe.reply('happy birthday to the absolute lad @'+name)