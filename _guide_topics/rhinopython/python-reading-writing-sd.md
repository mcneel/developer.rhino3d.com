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
We'll use a couple of simple scripts from the Python Samples folder as examples - we'll dissect these to see how they work.

## Reading a file

Here is the import-points.py script

```python
# Import points from a text file
import rhinoscriptsyntax as rs

def ImportPoints():
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


##########################################################################
# Check to see if this file is being executed as the "main" python
# script instead of being used as a module by some other python script
# This allows us to use the module which ever way we want.
if( __name__ == "__main__" ):
    ImportPoints()
```

#### Reading a file in detail

`def ImportPoints()`

We've put the action inside a function in this script, the  section. This allows the code to be re-used and simplifies error checking. 

`filter = "Text file (*.txt)|*.txt|All Files (*.*)|*.*||"`  
`filename = rs.OpenFileName("Open Point File", filter)`

The first part uses the rs function *OpenFileName()* to allow the user to specify a file to open, and sets a variable 'filename' to hold this information with a filter variable to specify text files extensions.

`if not filename: return`

If for some reason the user does not specify a file, say with a Cancel, then the *if* ensures that the rest of the code inside this particular function will not be run, since there is nothing that can be done without a file name.  This is a nice way to handling unexpected actions by the user.  Without this line the next lines in the script would result in error messages without a valid filename. Since there is only the one function in this script, a *return* means the script will stop.

`file = open(filename, "r")`

Next a varible is set to the open file for reading (see python documentation for other ways to read files (https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files)

`contents = file.readlines()`

The *file.readlines()* function will read each line of the file into a list variable. This list is held in memory as a list where item is a string of each line.

`file.close()`

The file is then closed. It is best to leave files open only while they are actually needed.

At this point in the script, a new function is defined, called `__point_from_string(text)`. Inside this new local function, each line in *contents* is converted into three numbers and returns those as the xy,z coordinates of a point.

`contents = [__point_from_string(line) for line in contents]`

The list of lines from the orignal text file is fed into this function, line by line to create a list of points, by calling the `__point_from_string(text)` function.

`rs.AddPoints(contents)`

Lastly, the points in the list are added to the Rhino document as point objects. 

Note all if this code will not actually run unless the function is called - this is done from the very last line of the script:

```python
if( __name__ == "__main__" ):
    ImportPoints()
```


## Writing a file

Writing a file is similiar to reading, but the order in which things are done is different. This time we'll look at the ExportPoints.py sample file.

```python
import rhinoscriptsyntax as rs

#Get the points to export
objectIds = rs.GetObjects("Select Points",1+2, True, True)
if( objectIds==None ): return

#Get the filename to create
filter = "Text File (*.txt)|*.txt|All Files (*.*)|*.*||"
filename = rs.SaveFileName("Save point coordinates as", filter)
if( filename==None ): return


with open(filename, "w") as file:
     # treat the objects differently depending on whether they are points or point clouds
	for id in objectIds:
	    #process point clouds
	    if( rs.IsPointCloud(id) ):
		points = rs.PointCloudPoints(id)
		for pt in points:
		    file.write(str(pt)+"\n")
	    elif( rs.IsPoint(id) ):
		point = rs.PointCoordinates(id)
		file.write(str(point) + "\n")

```
There are a couple of things to notice, compared to the previous example. We need some points to export, so we'll let the user select some point objects and point clouds. There is a filter applied to the selection, the `1+2`. 1 filters for point objects and 2 filters for point clouds - we can add the filters together to make combinations such as we have here - 1+2 or, we could have written just 3, that would work as well, it is just harder to parse when reviewing or modifying the code:


`objectIds = rs.GetObjects("Select Points", 1+2, True, True)`

As before we check to make sure that the user has in fact selcted the things we're looking for.

`if( objectIds==None ): return`


Next we'll get a file name as in the first example:
```python
#Get the filename to create
filter = "Text File (*.txt)|*.txt|All Files (*.*)|*.*||"
filename = rs.SaveFileName("Save point coordinates as", filter)
if( filename==None ): return
```


When writing to a file it must first be *opened*.  While it is open, the information can be written to the file.  After wrting all the information, the file must be closed. In the first example we explicitly opened, read and then closed the file. This time we've used the `with` statement to open the file - 'with' is convenient becuse it takes care of closing the file and cleaning up when the script leaves the indented 'with' section.

```python
with open(filename, "w") as file:
     # treat the objects differently depending on whether they are points or point clouds
	for id in objectIds:
	    #process point clouds
	    if( rs.IsPointCloud(id) ):
		points = rs.PointCloudPoints(id)
		for pt in points:
		    file.write(str(pt)+"\n")
		#process point objects
	    elif( rs.IsPoint(id) ):
		point = rs.PointCoordinates(id)
		file.write(str(point) + "\n")
````
Keep in mind that 'points' in the script are not the same as 'point objects' in the Rhino file. As you can see in the above, the script looks at the selected objects and extracts the x,y,z points to write to the file.

For more information on reading and writing from Python, see the [Python Methods in File Objects documentation](https://docs.python.org/2/tutorial/inputoutput.html#methods-of-file-objects)
