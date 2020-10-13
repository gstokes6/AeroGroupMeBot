# IMPORTS
import os
import json

import wget
import urllib
import shutil


import LOAD_ENV_VARS
LOAD_ENV_VARS.init(True)#init with debug

import classMessage
tommyID = '22852771'
academicID = '73362029'
tommyMention = {'loci': [[35, 13]], 'type': 'mentions', 'user_ids': ['22852771']}
academicMention = {'loci': [[0, 9]], 'type': 'mentions', 'user_ids': ['73362029']}

message = {
        'text':'@Acadmeic markov can i get an f text 69 lol',
        'sender_id':tommyID,
        'scheduleList':[],
        'attachments':[academicMention]
    }
print(message)
messageClass = classMessage.message(message)
messageClass.printDiagnostics()
messageClass.response()


