import os
import gDrive
def init(debug = False):
    
    if debug:
        global ENV_VARS
        ENV_VARS = {
            'debug':debug
            }
        return
    print("why")
    ##Groupme related enviromental variables
    bot_id = os.getenv('GROUPME_BOT_ID')
    group_id = os.getenv('GROUPME_GROUP_ID')
    gm_access_token = os.getenv('GROUPME_ACCESS_TOKEN')
    ##Google Drive related enviromental variables
    root = os.getenv('ROOT')
    gd_access_token = os.getenv('GD_ACCESS_TOKEN')
    gd_client_secret = os.getenv('GD_CLIENT_SECRET')
    gd_client_id = os.getenv('GD_CLIENT_ID')
    gd_refresh_token = os.getenv('GD_REFRESH_TOKEN')
    gd_token_expiry = os.getenv('GD_TOKEN_EXPIRY')

    #global ENV_VARS
    ENV_VARS = {
                'bot_id':bot_id,
                'group_id':group_id,
                'gm_access_token':gm_access_token,

                'root':root,
                'gd_access_token':gd_access_token,
                'gd_client_secret':gd_client_secret,
                'gd_client_id':gd_client_id,
                'gd_refresh_token':gd_refresh_token,
                'gd_token_expiry':gd_token_expiry,

                'debug':debug
                }
    
    global gDriveInstance
    gDriveInstance = gDrive.gDrive()
