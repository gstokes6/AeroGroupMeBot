from MESSAGE_FLAGS import messageFlag

class isAcademicInvoked(messageFlag.messageFlag):
    def __init__(self,message):
        super().__init__(message)
        
    def checkTrue(self,message):
        ##Logic to find if flag is set
        if ("@academic" in message['text'].lower()) or ("[[academic]]" in message['text'].lower()):
            self.isTrue = True

    def response(self):
        print("This is a flag for if Academic invoked")
        
