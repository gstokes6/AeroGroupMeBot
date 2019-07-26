import os
import groupy as GM
from groupy import Client

Token = os.getenv('GROUPME_BOT_ID')
client = Client.from_token(Token)

for group in client.groups.list_all():
    print(gorup.name)
