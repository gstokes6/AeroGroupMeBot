##imports
import re

##Functions
def FirstPass(msg):
    msg = msg.lower()
    msg = msg.replace('@academic','')
    msg = msg.replace('[[academic]]','')
    msg = msg.replace('[','')
    msg = msg.replace(']','')
    msglist = msg.split(' ')
    for item in msglist:
        if item == '':
            msglist.remove('')
    return msglist

def DumbRe(Patern,String):
    Result = False
    if re.search(Patern,String):
        if re.search(Patern,String).group(0) == String:
            Result = True
    return Result

def RegPass(msgList):
    TypeList = []
    for item in msgList:
        if DumbRe('[a-z]{4}',item):
            TypeList.append('ClassFirstFragment')
        elif DumbRe('[0-9]{4}',item):
            TypeList.append('ClassSecondFragmentNoSection')
        elif DumbRe('[0-9]{4}-[0-9]{1,3}',item):
            TypeList.append('ClassSecondFragmentWithSection')
        elif DumbRe('[a-z]{4}[0-9]{4}',item):
            TypeList.append('ClassNoSection')
        elif DumbRe('[a-z]{4}[0-9]{4}-[0-9]{1,3}',item):
            TypeList.append('ClassWithSection')
        elif DumbRe('update',item):
            TypeList.append('Update')
        elif DumbRe('Test',item):
            TypeList.append('Calendar')
        else:
            TypeList.append('Nonsense')
    
    return TypeList

def Condense(MsgList,TypeList):
    RemoveCount = 0
    for i in range(len(MsgList)-1):
        i = i - RemoveCount
        if ((TypeList[i]+TypeList[i+1]) == 'ClassFirstFragmentClassSecondFragmentNoSection'):
            TypeList[i] = 'ClassNoSection'
            TypeList.remove(TypeList[i+1])
            MsgList[i] = MsgList[i] + MsgList[i+1]
            MsgList.remove(MsgList[i+1])
            RemoveCount = RemoveCount+1
        elif ((TypeList[i]+TypeList[i+1]) == 'ClassFirstFragmentClassSecondFragmentWithSection'):
            TypeList[i] = 'ClassWithSection'
            TypeList.remove(TypeList[i+1])
            MsgList[i] = MsgList[i] + MsgList[i+1]
            MsgList.remove(MsgList[i+1])
            RemoveCount = RemoveCount+1
##    while ('Nonsense' in TypeList):
##        index = TypeList.index('Nonsense')
##        MsgList.remove(MsgList[index])
##        TypeList.remove('Nonsense')
    for i in range(len(TypeList)):
        if TypeList[i] in ['Nonsense','ClassFirstFragment','ClassSecondFragmentWithSection','ClassSecondFragmentNoSection']:
            MsgList = MsgList[0:i]
            TypeList = TypeList[0:i]
            break
    return MsgList,TypeList

def AddZeros(MsgList,TypeList):
    for i in range(len(MsgList)):
        if TypeList[i]=='ClassWithSection':
            Temp = MsgList[i]
            TempList = Temp.split('-')
            while len(TempList[1]) < 3:
                TempList[1] = '0'+TempList[1]
            MsgList[i] = TempList[0]+'-'+TempList[1]
    return MsgList

def GetCommandType(Msg,TypeResult,Attachment):
    if Attachment != []:
        if Attachment[0]['type'] == 'image':
            return "ImageUpload",Attachment[0]
        elif Attachment[0]['type'] == 'file':
            return "FileUpload",Attachment[0]
    else:
        if ("are you with me" in Msg)or ("is everbody with me" in Msg):
            return "Hartfield",None
        elif TypeResult == []:
            return "Nonsense",None
        elif TypeResult[0] == 'Update':
            return "Update",None
        else:
            return "Nonsense",None

def AttachSan(Attach):
    NewAttach = []
    for attach in Attach:
        if attach['type'] != 'mentions':
            NewAttach.append(attach)
    #Attach[:] = [attach for attach in Attach if attach['type'] == 'mentions']
    return NewAttach

def Main(Msg,Attach):
    Attach = AttachSan(Attach)
    print(Attach)
    if ((Msg.replace(' ','') == "@academic") or (Msg.replace(' ','') == "[[academic]]")) and (Attach==[]):
        return [],[],'PostLink'
    FirstPassResult = FirstPass(Msg)
    RegPassResult = RegPass(FirstPassResult)
    CondenseResult,TypeResult = Condense(FirstPassResult,RegPassResult)
    CondenseResult = AddZeros(CondenseResult,TypeResult)
    CommandType = GetCommandType(Msg,TypeResult,Attach)
    return CondenseResult,TypeResult,CommandType

##Test
if __name__ == "__main__":
    Test1 = "@Academic AERO 4140-1 Other unrelated things"
    Test1Msg = {'attachments': [{'type': 'image', 'url': 'https://i.groupme.com/663x593.jpeg.2b7b5e940cdd4c53bc580de5c93098bb'}, {'loci': [[0, 9]], 'type': 'mentions', 'user_ids': ['73362029']}], 'avatar_url': 'https://i.groupme.com/800x800.jpeg.079750da115c4d3baae220c371654878', 'created_at': 1566495571, 'group_id': '52068192', 'id': '156649557132492476', 'name': 'Gavin Stokes', 'sender_id': '73358488', 'sender_type': 'user', 'source_guid': 'ac67b98e9d4317b924772ccd64c2504b', 'system': False, 'text': '@Academic ', 'user_id': '73358488'}
    Test1Attach = Test1Msg['attachments']
    Test2 = "@academic update"
    Test2Attach = []

    ReturnMsg1,ReturnType1,CommandType1 = Main(Test1,Test1Attach)
    ReturnMsg2,ReturnType2,CommandType2 = Main(Test2,Test2Attach)
    
    print(ReturnMsg1)
    print(ReturnType1)
    print(CommandType1)
    print(ReturnMsg2)
    print(ReturnType2)
    print(CommandType2)



