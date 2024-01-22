import rhinoscriptsyntax as rs
import datetime
#This script will rename an object using the current system time

def renameobject():
    object_id = rs.GetObject("Select an object to rename", select=True)
    if object_id:
        newname = "Date tag: " + str(datetime.datetime.now())
        rs.ObjectName(object_id, newname)


if __name__=="__main__":
    renameobject()