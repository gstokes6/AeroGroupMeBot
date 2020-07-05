from urllib.parse import urlencode
from urllib.request import Request, urlopen
import requests

import LOAD_ENV_VARS

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
    group_id = LOAD_ENV_VARS.ENV_VARS['group_id']
    gm_access_token = LOAD_ENV_VARS.ENV_VARS['gm_access_token']    
    requests.post("https://api.groupme.com/v3/messages/%s/%s/like?token=%s"%(group_id,message['id'],gm_access_token))
