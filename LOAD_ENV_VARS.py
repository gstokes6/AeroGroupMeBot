import os
def init():
    Root = os.getenv('ROOT')
    bot_id = os.getenv('GROUPME_BOT_ID')
    group_id = os.getenv('GROUPME_GROUP_ID')
    gm_access_token = os.getenv('GROUPME_ACCESS_TOKEN')

    global ENV_VARS
    ENV_VARS = {'Root':Root,
                'bot_id':bot_id,
                'group_id':group_id,
                'gm_access_token':gm_access_token
                }
