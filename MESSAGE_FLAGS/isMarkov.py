from MESSAGE_FLAGS import messageFlag
import markovify

##for seeing if Gavin is invoked
from MESSAGE_FLAGS import isMentioned
import LOAD_ENV_VARS
import groupMe


class isMarkov(messageFlag.messageFlag):
    def __init__(self,message):
        super().__init__(message)
        self.sender_id = message['sender_id']
        
    def checkTrue(self,message):
        ##Logic to find if flag is set
        self.message = message
        ##first see if invoked
        #invokedFlag = isMentioned.isMentioned(message,'73358488')#Gavin
        invokedFlag = isMentioned.isAcademicInvoked(message)#Academic
        isInvoked = invokedFlag.isTrue

        ##see if keyword is in message
        Msg = message['text'].lower()
        Msg = Msg.replace('@academic','').replace('[[academic]]','')
        isKeyPhrase = ( "markov" in Msg )

        if (isKeyPhrase and isInvoked):
            self.willLike = True
            self.isTrue = True
        
    def response(self):
        groupMe.reply(self.Markov())

    def Markov(self):
        path = 'json_models/' + self.sender_id + '.json'
        with open(path,'r',encoding="utf-8") as f:
            model_json = f.read()  
        reconstituted_model = markovify.Text.from_json(model_json)

        response = ''
        for i in range(5):
            try:
                response = response + reconstituted_model.make_sentence() + '\n\n'
            except:
                print("got a none, whoops")
        return response
