# IMPORTS
import os
import json
import requests
import wget
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from flask import Flask, request
import GoogleDrive as GD

mycreds = GD.MakeCreds(os.getenv('GD_ACCESS_TOKEN'),os.getenv('GD_CLIENT_SECRET'),os.getenv('GD_CLIENT_ID'),os.getenv('GD_REFRESH_TOKEN'),os.getenv('GD_TOKEN_EXPIRY'))
client_secrets = GD.MakeClient(os.getenv('GD_CLIENT_SECRET'),os.getenv('GD_CLIENT_ID'))
drive = GD.GetDrive()
GD.Setup(drive)

app = Flask(__name__)
bot_id = os.getenv('GROUPME_BOT_ID')
group_id = os.getenv('GROUPME_GROUP_ID')
gm_access_token = os.getenv('GROUPME_ACCESS_TOKEN')
print(bot_id)
url = 'https://api.groupme.com/v3/bots/post'

# Called whenever the app's callback URL receives a POST request
# That'll happen every time a message is sent in the group
@app.route('/', methods=['POST'])
def webhook():
    # 'message' is an object that represents a single GroupMe message.
    message = request.get_json()
    print(message)
    # TODO: Your bot's logic here
    if (not sender_is_bot(message)) and (len(message['attachments'])!= 0) and (message['text']):
        print('Found Message')
        FoundMention = 0
        for attachment in message['attachments']:
            #Check for Mention of @academic here
            if attachment['type'] == 'mentions':
                if '73362029' in attachment['user_ids']:
                    FoundMention = 1
        if (FoundMention != 0) and (len(message['attachments']) > 1):
            for attachment in message['attachments']:
                if (attachment['type'] == 'image'):
                    TempURL = attachment['url']
                    FileName = str(message['created_at']) + '.' + TempURL.split('.')[-2]
                    tempfile = wget.download(TempURL,FileName)
                    if len(message['text'].upper().split()) > 1:
                        FolderName = message['text'].upper().split()[1]
                    else:
                        FolderName = None
                    GD.SortFile(drive,tempfile,message['created_at'],FolderName)
                    requests.post("https://api.groupme.com/v3/messages/%s/%s/like?token=%s"%(group_id,message['id'],gm_access_token))
##                ##No support for files yet
##                if (attachment['type'] == 'file'):
##                    TempURL = "https://file.groupme.com/v1/%s/files/%s"%(group_id,attachment['file_id'])
##                    print(TempURL)
##                    FileName = str(message['created_at']) + '.' + TempURL.split('.')[-2]
##                    tempfile = wget.download(TempURL,FileName)
##                    if len(message['text'].upper().split()) > 1:
##                        FolderName = message['text'].upper().split()[1]
##                    else:
##                        FolderName = None
##                    GD.SortFile(drive,tempfile,message['created_at'],FolderName)
        elif not ('' == message['text'].lower().replace('@academic ','')):
            #Implement Text Saving
            print("Text saving case found")
        else:
            SharingLink = GD.FindOrCreateFolderLink(drive,['Python Bot'])['alternateLink']
            print(SharingLink)
            reply(SharingLink,bot_id)
    GD.UpdateEnvVars()
    return "ok", 200

################################################################################

# Send a message in the groupchat
def reply(msg,bot_id):
    url = 'https://api.groupme.com/v3/bots/post'
    data = {
                    'text'                  : msg,
                    'bot_id'                : bot_id

    }
    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read().decode()


# Checks whether the message sender is a bot
def sender_is_bot(message):
    return message['sender_type'] == "bot"

