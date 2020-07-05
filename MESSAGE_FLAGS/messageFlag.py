##imports go here

##Define class
class messageFlag:
    def __init__(self,message):
        self.isTrue = False
        self.checkTrue(message)

    def checkTrue(self,message):
        print("You've found the base class somehow")
        self.isTrue = False

    def response(self):
        if self.isTrue:
            print("You've found the base class somehow")
            ##do thing
            
        
    



