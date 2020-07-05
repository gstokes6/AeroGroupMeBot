# IMPORTS
import os
import json

import wget
import urllib
import shutil
import datetime
import random

from urllib.parse import urlencode
from urllib.request import Request, urlopen
from flask import Flask, request

##import GoogleDrive as GD
##import Sanitization as san
##import DateToolBox as dtb
##import Memes

import classMessage
import LOAD_ENV_VARS
LOAD_ENV_VARS.init()

print('Update 4 code')

app = Flask(__name__)
url = 'https://api.groupme.com/v3/bots/post'

##mycreds = GD.MakeCreds(os.getenv('GD_ACCESS_TOKEN'),os.getenv('GD_CLIENT_SECRET'),os.getenv('GD_CLIENT_ID'),os.getenv('GD_REFRESH_TOKEN'),os.getenv('GD_TOKEN_EXPIRY'))
##client_secrets = GD.MakeClient(os.getenv('GD_CLIENT_SECRET'),os.getenv('GD_CLIENT_ID'))
##drive = GD.GetDrive()
##GD.Setup(drive,Root)

# Called whenever the app's callback URL receives a POST request
# That'll happen every time a message is sent in the group
@app.route('/', methods=['POST'])
def webhook():
    # 'message' is an object that represents a single GroupMe message.
    message = request.get_json()
    print(message)
    print('Current Class:')
    ##print(dtb.IsInClass(drive,Root,message['created_at']))

##    Attach = message['attachments']
##    Gavin = False
##    for attachment in Attach:
##        if attachment['type'] == 'mentions':
##            #if '73362029' in attachment['user_ids']:
##            if '73358488' in attachment['user_ids']:
##                loci = attachment['loci']
##                Gavin = True
##    if Gavin and (False):
##        name = message['name']
##        nameID = message['sender_id']
##        newtext = Mock(message['text'].replace('@Gavin Stokes 2','@'+name))
##        #newtext = Mock(message['text'].replace('@Academic','@'+name))
##        replyMention(newtext,nameID,[loci[0],len(nameID)],bot_id)
##        
##    
##    


    if (not sender_is_bot(message)):
        if random.random() < .33:
            LikeMessage(message)
        messageClass = classMessage.message(message)
        messageClass.printDiagnostics()
        text = messageClass.response()
##        if not ( text == "" ):
##            reply(text)



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
##            
##        elif (CommandType == 'Update'):
##            UpdateID = GD.FindOrCreateFolder(drive,[Root,'Bot Guts','Update.txt'])
##            UpdateTextFile = drive.CreateFile({'id':UpdateID})
##            UpdateText = UpdateTextFile.GetContentString()
##            reply(UpdateText, bot_id)
##            LikeMessage(message)
##
##        elif (CommandType == 'Hartfield') and (dtb.IsInClass(drive,Root,message['created_at']) in ['AERO4510','AERO5530']):
##            CounterID = GD.FindOrCreateFolder(drive,[Root,'Bot Guts','HartCounter.txt'])
##            Counter = drive.CreateFile({'id':CounterID})
##            
##            date_time_obj = datetime.datetime.strptime(Counter['modifiedDate'], '%Y-%m-%dT%H:%M:%S.%fZ')            
##            print(date_time_obj)
##            print(datetime.datetime.fromtimestamp(message['created_at']).date())
##            if (date_time_obj.date() != datetime.datetime.fromtimestamp(message['created_at']).date()):
##                Iteration = 0
##            else:
##                Iteration = int(Counter.GetContentString())
##            Memes.GetHart(Iteration)
##            HartPath = 'ModifiedHart.jpg'
##            reply_with_image("Time for a 5 min lecture. Today's count: " + str(Iteration+1), HartPath)
##            Counter.SetContentString(str(Iteration+1))
##            Counter.Upload()
##
##            TotalCounterID = GD.FindOrCreateFolder(drive,[Root,'Bot Guts','TotalHartCounter.txt'])
##            TotalCounter = drive.CreateFile({'id':TotalCounterID})
##            TotalIteration = int(TotalCounter.GetContentString())
##            TotalCounter.SetContentString(str(TotalIteration+1))
##            TotalCounter.Upload()
##
##            LikeMessage(message)
##
##        elif (CommandType == 'Vibrations') and (dtb.IsInClass(drive,Root,message['created_at']) == 'AERO4630'):
##            reply(Memes.Vibrations(),bot_id)
##            
##        elif (CommandType == 'Hartfield') and (dtb.IsInClass(drive,Root,message['created_at']) == 'AERO4620'):
##            CounterID = GD.FindOrCreateFolder(drive,[Root,'Bot Guts','MailenCounter.txt'])
##            Counter = drive.CreateFile({'id':CounterID})
##            
##            date_time_obj = datetime.datetime.strptime(Counter['modifiedDate'], '%Y-%m-%dT%H:%M:%S.%fZ')            
##            print(date_time_obj)
##            print(datetime.datetime.fromtimestamp(message['created_at']).date())
##            if (date_time_obj.date() != datetime.datetime.fromtimestamp(message['created_at']).date()):
##                Iteration = 0
##            else:
##                Iteration = int(Counter.GetContentString())
##            Memes.GetMailen(Iteration)
##            HartPath = 'ModifiedMailen.jpg'
##            reply_with_image("I need more coffee. Today's count: " + str(Iteration+1), HartPath)
##            Counter.SetContentString(str(Iteration+1))
##            Counter.Upload()
##
##            TotalCounterID = GD.FindOrCreateFolder(drive,[Root,'Bot Guts','TotalMailenCounter.txt'])
##            TotalCounter = drive.CreateFile({'id':TotalCounterID})
##            TotalIteration = int(TotalCounter.GetContentString())
##            TotalCounter.SetContentString(str(TotalIteration+1))
##            TotalCounter.Upload()
##
##            LikeMessage(message)
##            
##        elif (CommandType == 'F'):
##            reply('F', bot_id)
##            
##        elif (CommandType == 'PostLink'):
##            SharingLink = GD.FindOrCreateFolderLink(drive,[Root])['alternateLink']
##            reply(SharingLink,bot_id)
##            LikeMessage(message)
##        if (Nice):
##            reply('Nice.',bot_id)
##    GD.UpdateEnvVars()
    return "ok", 200

################################################################################

# Send a message in the groupchat
def reply(msg):
    url = 'https://api.groupme.com/v3/bots/post'
    data = {
                    'text'                  : msg,
                    'bot_id'                : LOAD_ENV_VARS.ENV_VARS['bot_id']

    } 
    #PostRequest = "https://api.groupme.com/v3/bots/post?bot_id=%s&text=%s&token=%s"%(bot_id,msg,gm_access_token)
    #requests.post(PostRequest)
    
    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read().decode()
    print('Posted!')

def replyMention(msg,ID,loci):
    url = 'https://api.groupme.com/v3/bots/post'
    data = {
                    'text'                  : msg,
                    'bot_id'                : LOAD_ENV_VARS.ENV_VARS['bot_id'],
                    'attachments':[{'loci':[loci],'type':'mentions','user_ids':[str(ID)]}]

    } 
    #PostRequest = "https://api.groupme.com/v3/bots/post?bot_id=%s&text=%s&token=%s"%(bot_id,msg,gm_access_token)
    #requests.post(PostRequest)
    
    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read().decode()
    print('Posted!')
    
def reply_with_image(msg, imgPath):
	url = 'https://api.groupme.com/v3/bots/post'
	urlOnGroupMeService = upload_image_to_groupme(imgPath)
	data = {
		'bot_id'		: LOAD_ENV_VARS.ENV_VARS['bot_id'],
		'text'			: msg,
		'picture_url'		: urlOnGroupMeService
	}
	request = Request(url, urlencode(data).encode())
	json = urlopen(request).read().decode()


def upload_image_to_groupme(imgPath):
    # Send Image
    headers = {'content-type': 'application/json'}
    url = 'https://image.groupme.com/pictures'
    files = {'file': open(imgPath, 'rb')}
    payload = {'access_token': gm_access_token}
    r = requests.post(url, files=files, params=payload)
    imageurl = r.json()['payload']['url']
    os.remove(imgPath)
    return imageurl


def LikeMessage(message):
    requests.post("https://api.groupme.com/v3/messages/%s/%s/like?token=%s"%(group_id,message['id'],LOAD_ENV_VARS.ENV_VARS['gm_access_token']))

# Checks whether the message sender is a bot
def sender_is_bot(message):
    return message['sender_type'] == "bot"

def Mock(string):
    newString = ''
    num = 0
    for letter in string:
        
        if (num % 2) == 0:
            newString = newString + string[num].lower()
        else:
            newString = newString + string[num].upper()
        num = num+1
    return newString




