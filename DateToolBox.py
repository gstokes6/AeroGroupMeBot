import time
import openpyxl
import GoogleDrive as GD

def GetSpreadsheet(Path):
    wb = openpyxl.load_workbook(Path)
    Datasheet = wb['Classes']
    return Datasheet,wb

def GetSpreadsheetContents(DataSheet):
    Classes = []
    MeetingDays = []
    TimeStart = []
    TimeEnd = []
    Row = 2
    while DataSheet.cell(row = Row, column = 1).value:
        Classes.append(DataSheet.cell(row = Row, column = 1).value)
        MeetingDays.append(DataSheet.cell(row = Row, column = 2).value)
        TimeStart.append(DataSheet.cell(row = Row, column = 3).value)
        TimeEnd.append(DataSheet.cell(row = Row, column = 4).value)
        Row = Row + 1
    return Classes,MeetingDays,TimeStart,TimeEnd

def AddClassFolders(drive,Classes):
    for Class in Classes:
        GD.FindOrCreateFolder(drive,['Python Bot','Uploads',Class])



if __name__ == "__main__":
    drive = GD.GetDrive()
    path = 'test.xlsx'
    
    PythonBotID = GD.FindOrCreateFolder(drive,['Python Bot'])
    file_list = drive.ListFile({'q': "'%s' in parents and trashed=false"%(PythonBotID)}).GetList()
    file_list[0].GetContentFile(path)
    
    DataSheet,wb = GetSpreadsheet(path)
    Classes,MeetingDays,TimeStart,TimeEnd = GetSpreadsheetContents(DataSheet)
    AddClassFolders(drive,Classes)
