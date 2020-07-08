# IMPORTS
import os
import json

import wget
import urllib
import shutil

##import Sanitization as san
##import DateToolBox as dtb
##import Memes

from flask import Flask, request

import LOAD_ENV_VARS
LOAD_ENV_VARS.init()

import classMessage

print('Update 4 code')
app = Flask(__name__)

# Called whenever the app's callback URL receives a POST request
# That'll happen every time a message is sent in the group
@app.route('/', methods=['POST'])
def webhook():
    
    # 'message' is an object that represents a single GroupMe message.
    message = request.get_json()
    print(message)
    if (not ( message['sender_type'] == "bot" )):
        messageClass = classMessage.message(message)
        messageClass.printDiagnostics()
        messageClass.response()
    return "ok", 200

################################################################################

##LEGACY CODE

##        if CommandType == 'ImageUpload':
##            TempURL = attachment['url']
##            FileName = str(message['created_at']) + '.' + TempURL.split('.')[-2]
##            tempfile = wget.download(TempURL,FileName)
##            if len(message['text'].upper().split()) > 1:
##                FolderName = message['text'].upper().split()[1]
##            else:
##                FolderName = None
##            GD.SortFile(drive,tempfile,message['created_at'],Root,FolderName)
##            LikeMessage(message)
##            
##
##        elif (CommandType == 'FileUpload'):
##            TempURL = "https://file.groupme.com/v1/%s/files/%s?token=%s"%(group_id,attachment['file_id'],gm_access_token)
##            r = requests.get(TempURL)
##            FileType = r.headers['content-type'].split('/')[1]
##            print(r.headers['content-type'])
##            if FileType == 'vnd.openxmlformats-officedocument.presentationml.presentation':
##                FileType = 'pptx'
##            elif FileType == 'vnd.ms-powerpoint':
##                FileType = 'ppt'
##            elif FileType == 'vnd.openxmlformats-officedocument.wordprocessingml.document':
##                FileType = 'docx'
##            elif FileType == 'msword':
##                FileType = 'doc'
##            elif FileType == 'vnd.openxmlformats-officedocument.spreadsheetml.sheet':
##                FileType = 'xlsx'
##            elif FileType == 'vnd.ms-excel':
##                FileType = 'xls'
##            FileName = str(message['created_at']) + '.' + FileType
##            TempFile = open(FileName, 'wb').write(r.content)
##
##            if len(message['text'].upper().split()) > 1:
##                FolderName = message['text'].upper().split()[1]
##            else:
##                FolderName = None
##            GD.SortFile(drive,FileName,message['created_at'],Root,FolderName)
##            LikeMessage(message)



