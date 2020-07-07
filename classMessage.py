import importlib
from MESSAGE_FLAGS import *
import groupMe
import LOAD_ENV_VARS

class message:
    def __init__(self,messageClass):
        ##add new flag names here, must have class definition python file in MESSAGE_FLAGS folder.
        self.MESSAGE_FLAG_LIST = ["isAcademicInvoked","is69","isF","isHartfield","isWheelSpin","isSender",
                                  "isFileUpload","isUpdate","isLinkRequest",'isRandomLike','isMentioned',
                                  'isMock','isSaturday','isMailen']

        ##Initialize the flag list and GroupMe message holder containers
        self.messageFlagsList = []
        ##add schedule to message
        messageClass['scheduleList'] = LOAD_ENV_VARS.gDriveInstance.checkClasses(messageClass)
        print(messageClass['scheduleList'])
        self.message = messageClass

        self.getMessageFlagsList()

    def getMessageFlagsList(self):
         messageFlagsList = []
         for flagName in self.MESSAGE_FLAG_LIST:
            ##Create class representing the folder module we are defining the flag object in
            messageFlagFolderModule = __import__("MESSAGE_FLAGS."+flagName)
            ##narrow down to the actual module
            messageFlagFile = getattr(messageFlagFolderModule,flagName)
            ##narrow down to the class atribute for the flag class
            messageFlagClass = getattr(messageFlagFile,flagName)
            ##Create the flag class finally
            messageFlag = messageFlagClass(self.message)
            ##Save to list
            messageFlagsList.append(messageFlag)
         ##push the updated list back to message class
         self.messageFlagsList = messageFlagsList

    def response(self):
        ##are we liking first?
        willLike = False
        for flag in self.messageFlagsList:
            willLike = (willLike or flag.willLike)
        if willLike:
            groupMe.likeMessage(self.message)

        ##now do reply
        for flag in self.messageFlagsList:
            if flag.isTrue:
                flag.response()


    def printDiagnostics(self):
        DiagnosticList = []
        for messageFlag in self.messageFlagsList:
            DiagnosticList.append({type(messageFlag).__name__:messageFlag.isTrue})
        print(DiagnosticList)

if __name__ == "__main__":
    LOAD_ENV_VARS.init()
    testMsg = "@Academic are you with me AERO 4140-1 Other unrelated things 69"
    testMessageInput = {'attachments': [{'type': 'image', 'url': 'https://i.groupme.com/663x593.jpeg.2b7b5e940cdd4c53bc580de5c93098bb'}, {'loci': [[0, 9]], 'type': 'mentions', 'user_ids': ['73362029']}], 'avatar_url': 'https://i.groupme.com/800x800.jpeg.079750da115c4d3baae220c371654878', 'created_at': 1566495571, 'group_id': '52068192', 'id': '156649557132492476', 'name': 'Gavin Stokes', 'sender_id': '73358488', 'sender_type': 'user', 'source_guid': 'ac67b98e9d4317b924772ccd64c2504b', 'system': False, 'text': testMsg, 'user_id': '73358488'}
    testMessage = message(testMessageInput)
    testMessage.printDiagnostics()
    testMessage.response()
    
