---
title: How to read and write a simple file 
description: Use Python to read and write files.
authors: ['Scott Davidson']
author_contacts: ['scottd']
apis: ['RhinoPython']
languages: ['Python']
platforms: ['Mac', 'Windows']
categories: ['intermediate']
origin:
order: 75
keywords: ['script', 'Rhino', 'python']
layout: toc-guide-page
---

## Reading a file

Here is an example script that reads a text files of points:

```python
import rhinoscriptsyntax as rs

#prompt the user for a file to import
filter = "Text file (*.txt)|*.txt|All Files (*.*)|*.*||"
filename = rs.OpenFileName("Open Point File", filter)
if not filename: return
    
#read each line from the file
file = open(filename, "r")
contents = file.readlines()
file.close()

# local helper function    
def __point_from_string(text):
    items = text.strip("()\n").split(",")
    x = float(items[0])
    y = float(items[1])
    z = float(items[2])
    return x, y, z

contents = [__point_from_string(line) for line in contents]
rs.AddPoints(contents)
```

The first section prompts for a filename using the OpenFileName() method to prompt the user to select an existing file.  The file name is set to the `filename` variable.

```python
#prompt the user for a file to import
filter = "Text file (*.txt)|*.txt|All Files (*.*)|*.*||"
filename = rs.OpenFileName("Open Point File", filter)
if not filename: return
```

The `if not' statment will exit the script if no file is selected.

The next part of this script is pure Python.  The file is opened into a variable *file*.  Then t file is read line by line into a list of strings in the contents variable.

```python
#read each line from the file
file = open(filename, "r")
contents = file.readlines()
file.close()
```
Reading a file line by line is one way to read a file.  For other methods see the [Python Methods in File Objects documentation](https://docs.python.org/2/tutorial/inputoutput.html#methods-of-file-objects)

The rest of the routine takes each line one by one breaks the line into into points.

## Writing a file

Writing a file is similiar to reading, but the order in which things are done is different.

```python
import rhinoscriptsyntax as rs

#Get the points to export
objectIds = rs.GetObjects("Select Points",rs.filter.point | rs.filter.pointcloud,True,True)
if( objectIds==None ): return

#Get the filename to create
filter = "Text File (*.txt)|*.txt|All Files (*.*)|*.*||"
filename = rs.SaveFileName("Save point coordinates as", filter)
if( filename==None ): return
    
file = open(filename, "w")
for id in objectIds:
    #process point clouds
    if( rs.IsPointCloud(id) ):
        points = rs.PointCloudPoints(id)
        for pt in points:
            file.writeline(str(pt))
    elif( rs.IsPoint(id) ):
        point = rs.PointCoordinates(id)
        file.writeline(str(point))
file.close()
```

It is in this part of the scrip that the name of the file to save is established:

```python
#Get the filename to create
filter = "Text File (*.txt)|*.txt|All Files (*.*)|*.*||"
filename = rs.SaveFileName("Save point coordinates as", filter)
if( filename==None ): return
```
The `if` statement checks that the filename has been set, if not, then it ends the script. 

When writing to a file it must first be *opened*.  While it is open, the information can be written to the file.  After wrting all the information, the file must be closed.

```python
file = open(filename, "w") # open the file for write.
for id in objectIds:
    #process point clouds
    if( rs.IsPointCloud(id) ):
        points = rs.PointCloudPoints(id)
        for pt in points:
            file.writeline(str(pt)) #write a line to the file
    elif( rs.IsPoint(id) ):
        point = rs.PointCoordinates(id)
        file.writeline(str(point)) # write a line to the file.
file.close()
````

There are many types of writes that can be done.  The `writeline` method is perhaps the easiest to understand. For other methods see the [Python Methods in File Objects documentation](https://docs.python.org/2/tutorial/inputoutput.html#methods-of-file-objects)
