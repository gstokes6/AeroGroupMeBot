from MESSAGE_FLAGS import messageFlag

##Helper flag for other flags
class isMentioned(messageFlag.messageFlag):
    ##default "checkTrue" to satisfy polymorphism and find name of sender
    def __init__(self,message,userIdToCheck=None):
        self.mentionAttachments = []
        super().__init__(message)
        self.checkTrue(message,userIdToCheck)
        

    def checkTrue(self,message,userIdToCheck=None):
        userIds = []
        for attachment in message['attachments']:
            if attachment['type'] == 'mentions':
                self.mentionAttachments.append(attachment)
                userIds.append(attachment['user_ids'])
        if userIdToCheck in userIds:
            self.isTrue = True

        
    def response(self):
        1+1 #lol

        
