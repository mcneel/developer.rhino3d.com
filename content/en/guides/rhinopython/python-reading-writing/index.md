+++
authors = [ "scottd" ]
categories = [ "Intermediate" ]
description = "Use Python to read and write files."
keywords = [ "script", "Rhino", "python" ]
languages = [ "Python" ]
sdk = [ "RhinoPython" ]
title = "How to read and write a simple file"
type = "guides"
weight = 3
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Mac", "Windows" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++
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

We've put the action inside a function in this script, the

```python
def ImportPoints()
```

section. This allows the code to be re-used and simplifies error checking.
The first part uses the rs function

```python
rs.OpenFileName()
```

to allow the user to specify a file to open, and sets a variable 'filename' to hold this information:

```python
filename = rs.OpenFileName("Open Point File", filter)
```

with a filter for text files.

If for some reason the user does not specify a file, say with a Cancel, then the line

```python
if not filename: return
```

ensures that the rest of the code inside this particular function will not be run, since there is nothing that can be done without a file name, and executing the next lines in the script will result in error messages without it. Since there is only the one function in this script, a cancel means the script will stop.

Next a variable is set to the open file for reading:

```python
file = open(filename, "r")
```

and a variable is set to the contents of the file  which is then held in memory as a list with one item per line:

```python
contents = file.readlines()
```

The file is then closed:

```
python file.close()
```

See python documentation for other ways to read files (<https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files>).

At this point in the script, a new function is added, called *__point_from_string(text)* ,  inside the main function, that parses text in the expected format and converts the text into three numbers and returns those as the xy,z coordinates of a point.

The list of lines from the orignal text file is fed into this function, line by line to create a list of points, by calling that function:

```python
contents = [__point_from_string(line) for line in contents]
```

Lastly, the points in the list are added to the Rhino document as point objects:

```python
rs.AddPoints(contents)
```

Note all if this code will not actually run unless the function is called - this is done from the very last line of the script:

```python
if( __name__ == "__main__" ):
    ImportPoints()
```


## Writing a file

Writing a file is similar to reading, but the order in which things are done is different. This time we'll look at the ExportPoints.py sample file.

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


There are a couple of things to notice, compared to the previous example. We need some points to export, so we'll let the user select some point objects and point clouds. There is a filter applied to the selection, the _1+2_. 1 filters for point objects and 2 filters for point clouds - we can add the filters together to make combinations such as we have here - 1+2 or, we could have written just 3, that would work as well, it is just harder to parse when reviewing or modifying the code:


```python
objectIds = rs.GetObjects("Select Points", 1+2, True, True)
```

As before we check to make sure that the user has in fact selected the things we're looking for.

```python
if( objectIds==None ): return
```

Next we'll get a file name as in the first example:

```python
#Get the filename to create
filter = "Text File (*.txt)|*.txt|All Files (*.*)|*.*||"
filename = rs.SaveFileName("Save point coordinates as", filter)
if( filename==None ): return
```


When writing to a file it must first be *opened*.  While it is open, the information can be written to the file.  After writing all the information, the file must be closed. In the first example we explicitly opened, read and then closed the file. This time we've used the *with* statement to open the file - *with* is convenient because it takes care of closing the file and cleaning up when the script leaves the indented *with* section.

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
​```

Keep in mind that 'points' in the script are not the same as 'point objects' in the Rhino file. Points are a list of x,y,z coordinates and point objects are objects in the Rhino file that have, among other properties like display color or layer, a location - the point coordinates.  As you can see in the above, the script iterates a list of IDs -those of the selected point objects or point clouds, and extracts the x,y,z coordinates to write to the file. The exported points are only the x,y,z coordinates of the point objects.

For more information on reading and writing from Python, see the [Python Methods in File Objects documentation](https://docs.python.org/2/tutorial/inputoutput.html#methods-of-file-objects)

