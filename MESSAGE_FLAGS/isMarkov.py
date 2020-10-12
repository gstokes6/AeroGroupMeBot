from MESSAGE_FLAGS import messageFlag
import markovify

##for seeing if Gavin is invoked
from MESSAGE_FLAGS import isMentioned
import LOAD_ENV_VARS
import groupMe


class isMarkov(messageFlag.messageFlag):
    def __init__(self,message):
        super().__init__(message)
        
    def checkTrue(self,message):
        ##Logic to find if flag is set
        self.message = message
        ##first see if invoked
        #invokedFlag = isMentioned.isMentioned(message,'73358488')#Gavin
        invokedFlag = isMentioned.isMentioned(message,'73362029')#Academic
        isInvoked = invokedFlag.isTrue

        ##see if keyword is in message
        Msg = message['text'].lower()
        Msg = Msg.replace('@academic','').replace('[[academic]]','')
        isKeyPhrase = ( "markov" in Msg )

        if (isKeyPhrase and isInvoked):
            self.willLike = True
            self.isTrue = True
        
    def response(self):
        groupMe.reply(self.Markov(message['sender_id']))

    def Markov(sender_id):
        path = 'json_models/' + sender_id + '.json'
        with open(path,'r',encoding="utf-8") as f:
            text = f.read()  
        reconstituted_model = markovify.Text.from_json(model_json)

        response = ''
        for i in range(5):
            response = response + reconstituted_model.make_sentence() + '\n'
        return response
