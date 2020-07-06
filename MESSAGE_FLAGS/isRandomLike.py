from MESSAGE_FLAGS import messageFlag
import groupMe
import random

class isRandomLike(messageFlag.messageFlag):
    def __init__(self,message):
        super().__init__(message)
        
    def checkTrue(self,message):
        ##Logic to find if flag is set
        if random.random() < .33:
            self.isTrue = True
            self.willLike = True
            
    def response(self):
        1+1 #lol
        
