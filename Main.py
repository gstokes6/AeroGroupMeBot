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
    # TODO: Your bot's logic here
    if (not sender_is_bot(message)) and (len(message['attachments'])!= 0) and (message['text']):
        if ('[[academic]]' in message['text'].lower().split()[0]):
            print('Found Message')
            FoundMention = 0
            for attachment in message['attachments']
                #Check for Mention of @academic here
                if True:
                    FoundMention = 1
            if FoundMention != 0:
                for attachment in message['attachments']:
                    print(attachment)
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
    GD.UpdateEnvVars()
    return "ok", 200

################################################################################

# Send a message in the groupchat
def reply(msg):
    print(bot_id)
    data = {
                    'text'                  : msg,
                    'bot_id'                : bot_id

    }
    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read().decode()


    #response = requests.post("https://api.groupme.com/v3/bots/post", data = struc)
    #print(response,response.status_code,response.reason)

# Send a message with an image attached in the groupchat
def reply_with_image(msg, imgURL):
    url = 'https://api.groupme.com/v3/bots/post'
    urlOnGroupMeService = upload_image_to_groupme(imgURL)
    data = {
                    'bot_id'                : bot_id,
                    'text'                  : msg,
                    'picture_url'           : urlOnGroupMeService
    }
    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read().decode()
        
# Uploads image to GroupMe's services and returns the new URL
def upload_image_to_groupme(imgURL):
    imgRequest = requests.get(imgURL, stream=True)
    filename = 'temp.png'
    postImage = None
    if imgRequest.status_code == 200:
        # Save Image
        with open(filename, 'wb') as image:
                        for chunk in imgRequest:
                                        image.write(chunk)
        # Send Image
        headers = {'content-type': 'application/json'}
        url = 'https://image.groupme.com/pictures'
        files = {'file': open(filename, 'rb')}
        payload = {'access_token': 'eo7JS8SGD49rKodcvUHPyFRnSWH1IVeZyOqUMrxU'}
        r = requests.post(url, files=files, params=payload)
        imageurl = r.json()['payload']['url']
        os.remove(filename)
        return imageurl

# Checks whether the message sender is a bot
def sender_is_bot(message):
    return message['sender_type'] == "bot"

