from MESSAGE_FLAGS import messageFlag
##for seeing if academic is invoked
from MESSAGE_FLAGS import isAcademicInvoked

##Helper flag for other flags
class isSender(messageFlag.messageFlag):
    ##default "checkTrue" to satisfy polymorphism and find name of sender
    def __init__(self,message,usernameToCheck=None):
        self.userDict = {'73358488':'Gavin Stokes 2'}
        self.username = ""
        super().__init__(message)
        self.checkTrue(message,usernameToCheck)
        

    def checkTrue(self,message,usernameToCheck=None):
        NameID = message['sender_id']
        self.username = self.userDict.get(NameID, "")
        
        if usernameToCheck is not None:
            if (self.username == usernameToCheck):
                self.isTrue = True

        
    def response(self):
        1+1 #lol

        
