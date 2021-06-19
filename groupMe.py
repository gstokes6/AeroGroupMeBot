from urllib.parse import urlencode
from urllib.request import Request, urlopen
import requests

import requests
import os

import LOAD_ENV_VARS

def reply(msg):
    #If debug, just return after printing message
    if LOAD_ENV_VARS.ENV_VARS['debug']:
        print(msg)
        return
    
    url = 'https://api.groupme.com/v3/bots/post'
    bot_id = LOAD_ENV_VARS.ENV_VARS['bot_id']
    data = {
                    'text'                  : msg,
                    'bot_id'                : bot_id

    } 
    if bot_id:
        r = requests.post(url, json=data)
        print('Posted!')
    else:
        print('bot_id not found, bypassing')

def replyMention(msg,ID,loci):
    #If debug, just return after printing message
    if LOAD_ENV_VARS.ENV_VARS['debug']:
        print(msg,ID,loci)
        return
    url = 'https://api.groupme.com/v3/bots/post'
    bot_id = LOAD_ENV_VARS.ENV_VARS['bot_id']
    data = {
                    'text'                  : msg,
                    'bot_id'                : bot_id,
                    'attachments':[{'loci':[loci],'type':'mentions','user_ids':[str(ID)]}]

    } 
    #PostRequest = "https://api.groupme.com/v3/bots/post?bot_id=%s&text=%s&token=%s"%(bot_id,msg,gm_access_token)
    #requests.post(PostRequest)
    if bot_id:
        r = requests.post(url, json=data)
        print('Posted!')
    else:
        print('bot_id not found, bypassing')
    
def reply_with_image(msg, imgPath):
    #If debug, just return after printing message
    if LOAD_ENV_VARS.ENV_VARS['debug']:
        print(msg,imgPath)
        return
    bot_id = LOAD_ENV_VARS.ENV_VARS['bot_id']
    if bot_id:
        url = 'https://api.groupme.com/v3/bots/post'
        urlOnGroupMeService = upload_image_to_groupme(imgPath)
        data = {
            'bot_id'        	: bot_id,
	    'text'      	: msg,
	    'picture_url'       : urlOnGroupMeService
	}
        r = requests.post(url, json=data)
        print('Posted!')
    else:
        print('bot_id not found, bypassing')


def upload_image_to_groupme(imgPath):
    #If debug, just return after printing message
    if LOAD_ENV_VARS.ENV_VARS['debug']:
        print(imgPath)
        return
    # Send Image
    headers = {'content-type': 'application/json'}
    url = 'https://image.groupme.com/pictures'
    gm_access_token = LOAD_ENV_VARS.ENV_VARS['gm_access_token']
    files = {'file': open(imgPath, 'rb')}
    payload = {'access_token': gm_access_token}
    r = requests.post(url, files=files, params=payload)
    imageurl = r.json()['payload']['url']
    #os.remove(imgPath)
    return imageurl


def likeMessage(message):
    #If debug, just return after printing message
    if LOAD_ENV_VARS.ENV_VARS['debug']:
        print("Message is liked!")
        return
    group_id = LOAD_ENV_VARS.ENV_VARS['group_id']
    gm_access_token = LOAD_ENV_VARS.ENV_VARS['gm_access_token']
    message_id = message['id']
    if group_id:
        requests.post("https://api.groupme.com/v3/messages/%s/%s/like?token=%s"%(group_id,message_id,gm_access_token))
        print("Liked!")
    else:
        print('bot_id not found, bypassing')
