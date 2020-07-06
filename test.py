import datetime

import LOAD_ENV_VARS


        
testClass1 = {
    'className':'TEST-1000',
    'startTime':'12:00',
    'endTime':'13:00',
    'classDays':'0123456'
    }
testClass2 = {
    'className':'TEST-1000',
    'startTime':"12:00",
    'endTime':"13:00",
    'classDays':'0123456'#0 is monday, 1 is tuesday, etc
    }

testClassList = [testClass1,testClass2]

def loadSchedule(self):
    SpreadsheetFile = GD.FindOrCreateFolder( ['Classes.xlsx'] )
    Spreadsheet = self.drive.CreateFile( { 'id':SpreadsheetFile['id'] } )
    Spreadsheet.GetContentFile('Classes.xlsx')
    wb = openpyxl.load_workbook(Path)
    Datasheet = wb['Classes']
    Row = 2
    self.ClassList = []
    while DataSheet.cell(row = Row, column = 1).value:
        classDays = DataSheet.cell(row = Row, column = 2).value
        struct = {
            'className':(DataSheet.cell(row = Row, column = 1).value),
            'startTime':(DataSheet.cell(row = Row, column = 3).value),
            'endTime':(DataSheet.cell(row = Row, column = 4).value),
            'classDays':classDays.replace('Su','0').replace('M','1').replace('Tu','2').replace('W','3').replace('Th','4').replace('F','5').replace('Sa','6')
            }
        self.classList.append(struct)
        Row = Row + 1
    
def checkClasses(self,message):
    for Class in self.scheduleList:
        startTime = datetime.time(int(Class['startTime'].split(':')[0]), int(Class['startTime'].split(':')[1]) )
        endTime = datetime.time(int(Class['endTime'].split(':')[0]), int(Class['endTime'].split(':')[1]) )
        inClassTime = ( (startTime<now) and (now<endTime) )
        onClassDay = ( str(datetime.date.today().weekday()) in Class['classDays'] )
        if inClassTime and inClassDay:
            print('in ' + Class['className'])
