from MESSAGE_FLAGS import messageFlag

##for seeing if academic is invoked
from MESSAGE_FLAGS import isAcademicInvoked


class isLinkRequest(messageFlag.messageFlag):
    def __init__(self,message):
        super().__init__(message)
        
    def checkTrue(self,message):
        ##Logic to find if flag is set
        
        ##first see if invoked
        invokedFlag = isAcademicInvoked.isAcademicInvoked(message)
        isInvoked = invokedFlag.isTrue
        
        ##see if keyword is in message
        Msg = message['text'].lower()
        Msg = Msg.replace('@academic','').replace('[[academic]]','')
        isKeyPhrase = ( "" == Msg )

        if (isKeyPhrase and isInvoked):
            self.willLike = True
            self.isTrue = True
        
    def response(self):
        updateText = "Placeholder link for link flag until GD is re-implemented"
        groupMe.reply(updateText)
    
