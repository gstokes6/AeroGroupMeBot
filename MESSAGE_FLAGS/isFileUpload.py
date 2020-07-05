from MESSAGE_FLAGS import messageFlag
import LOAD_ENV_VARS

import requests

##for seeing if academic is invoked
from MESSAGE_FLAGS import isAcademicInvoked

class isFileUpload(messageFlag.messageFlag):
    ##default "checkTrue" to satisfy polymorphism and find name of sender
    def __init__(self,message):
        super().__init__(message)
        self.fileData = None
        self.fileType = None
        self.fileName = None
        

    def checkTrue(self,message):
        if not ( len(message['attachments']) > 0):
            return
        
        attachment = message['attachments'][0]
        if attachment['type'] != 'file':
            return
        
        group_id = message['group_id']
        file_id = attachment['file_id']
        gm_access_token = LOAD_ENV_VARS.ENV_VARS['gm_access_token']
        TempURL = "https://file.groupme.com/v1/%s/files/%s?token=%s"%(group_id,file_id,gm_access_token)
        self.fileData = requests.get(TempURL)
        FileType = self.fileData.headers['content-type'].split('/')[1]
        print(r.headers['content-type'])
        if FileType == 'vnd.openxmlformats-officedocument.presentationml.presentation':
            FileType = 'pptx'
        elif FileType == 'vnd.ms-powerpoint':
            FileType = 'ppt'
        elif FileType == 'vnd.openxmlformats-officedocument.wordprocessingml.document':
            FileType = 'docx'
        elif FileType == 'msword':
            FileType = 'doc'
        elif FileType == 'vnd.openxmlformats-officedocument.spreadsheetml.sheet':
            FileType = 'xlsx'
        elif FileType == 'vnd.ms-excel':
            FileType = 'xls'
            
        self.fileType = FileType
        self.fileName = str(message['created_at']) + '.' + FileType
        self.isTrue = True

        
    def response(self):
##        self.fileType = FileType
##        self.fileName = str(message['created_at']) + '.' + FileType
##        TempFile = open(FileName, 'wb').write(r.content)
##
##        if len(message['text'].upper().split()) > 1:
##            FolderName = message['text'].upper().split()[1]
##        else:
##            FolderName = None
##        GD.SortFile(drive,FileName,message['created_at'],Root,FolderName)
##        LikeMessage(message)
        print("This is a flag for if WheelSpin")
        
