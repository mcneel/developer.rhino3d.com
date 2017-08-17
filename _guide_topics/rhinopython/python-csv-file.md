---
title: How to read and write a CSV files
description: Use Python to read and write comma delimited files.
authors: ['Scott Davidson']
author_contacts: ['scottd']
sdk: ['RhinoPython']
languages: ['Python']
platforms: ['Mac', 'Windows']
categories: ['Intermediate']
origin:
order: 75
keywords: ['script', 'Rhino', 'python']
layout: toc-guide-page
---
CSV (comma separated values ) files are commonly used to store and retrieve many different types of data. The CSV format is one of the most flexible and easiest format to read.

As an example, a CSV file might be used to store point locations in their X, Y, Z coordinate values:

```none
0.58,-3.7,0
0.58,-3.1,0
-0.23,0.91,0
-5,8.2,0
-3,9.2,0
2.1,8.8,0
2.5,5.5,0
6.2,1.6,0
6,1,0
```

Or a CSV might contain building data, for instance room and usage information in a database type format.  Note that this CSV has a header titles on the first row: 

```none
RoomID,Floor,Use,Square Footage,Capacity,Price
100,1,Retail,6598,55,6500
101,1,Retail,1900,25,3000
102,1,Retail,1850,25,3000
103,1,Restroom,250,0,0
104,1,Maintenance,150,0,0
200,2,Studio,875,2,850
201,2,Studio,734,2,850
202,2,Studio,624,2,850
203,2,Studio,624,2,850
```

The [csv module](https://docs.python.org/2/library/csv.html) in Python can be used to quickly parse CSV files into different data structures. In this sample the point coordinate file we will read into a list in which the X, Y and Z coordinates can be referenced by the index position in a *list*.  The building data will be read in to a *dictionary* object so that the various values can be referenced by the header titles as named pieces of information. 

## Reading into a list

Here is an example script to read a CSV file into a list.  Each row will become its own list and then can be referenced by the index position: 

```python
import csv
import rhinoscriptsyntax as rs

def CSVlist():
    #prompt the user for a file to import
    filter = "CSV file (*.csv)|*.csv|*.txt|All Files (*.*)|*.*||"
    filename = rs.OpenFileName("Open Point File", filter)
    if not filename: return

    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            x = float(row[0])
            y = float(row[1])
            z = float(row[2])
            print x, y, z
            rs.AddPoint(x,y,z)

##########################################################################
# Check to see if this file is being executed as the "main" python
# script instead of being used as a module by some other python script
# This allows us to use the module which ever way we want.
if( __name__ == "__main__" ):
    CSVlist()
```
{: .line-numbers}

As usual the script starts with imports.  This time the csv module is used.

```python
import csv
```
Lines 2 thru 8 are standard lines from the Rhino.Python [How to read and write a simple file]({{ site.baseurl }}/guides/rhinopython/python-reading-writing) guide.

At line 10 the file is opened for reading.

```python
with open(filename) as csvfile:
```

Then the key line in the script, that reads each row into a list of values into the variable `reader`:

```python
        reader = csv.reader(csvfile)
```

The `csv.reader` method does all the parsing of each line into a list.  Then each value on each line into a list:

```none
['0.58', '-3.7', '0']
['0.58', '-3.1', '0']
['-0.23', '0.91', '0']
['-5', '8.2', '0']
['-3', '9.2', '0']
['2.1', '8.8', '0']
['2.5', '5.5', '0']
['6.2', '1.6', '0']
['6', '1', '0']
```

Manipulsting each line of the list becomes easy:

```python
        for row in reader:
            x = float(row[0])
            y = float(row[1])
            z = float(row[2])
            print x, y, z
            rs.AddPoint(x,y,z)
```

In this case the values are split into 3 variables (x, y, z) and then printed to the console and additionally used to add a new point object to Rhino.

Reading a CSV file into list is great for data that has the same number of values in each line and the postion of the values are the same.  But sometimes it is easier to read csv values into a dictionary where the values have names.

## Reading into a dictionary

The next sample script is very similiar to above.

```python
import csv
import rhinoscriptsyntax as rs


def CSVbuilding():
    #prompt the user for a file to import
    filter = "CSV file (*.csv)|*.csv|*.txt|All Files (*.*)|*.*||"
    filename = rs.OpenFileName("Open Point File", filter)
    if not filename: return

    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['Use'], row['Square Footage'])
#            print(row)

##########################################################################
# Check to see if this file is being executed as the "main" python
# script instead of being used as a module by some other python script
# This allows us to use the module which ever way we want.
if( __name__ == "__main__" ):
    CSVbuilding()
```
{: .line-numbers}

But this script uses the dictionary reader in the csv module on line 12::

```
        reader = csv.DictReader(csvfile)
```
The [dictionary object]({{ site.baseurl }}/guides/rhinopython/python-dictionaries) contains *key:value* pairs where the name (key) of the values can be used to search through the data.  The complete dictionary object looks like this:

```none
{'Floor':'1', 'Use':'Retail', 'Square Footage':'6598', 'Price':'6500', 'RoomID':'100', 'Capacity':'55'}
{'Floor':'1', 'Use':'Retail', 'Square Footage':'1900', 'Price':'3000', 'RoomID':'101', 'Capacity':'25'}
{'Floor':'1', 'Use':'Retail', 'Square Footage':'1850', 'Price':'3000', 'RoomID':'102', 'Capacity':'25'}
{'Floor':'1', 'Use':'Restroom', 'Square Footage':'250', 'Price':'0', 'RoomID':'103', 'Capacity':'0'}
{'Floor':'1', 'Use':'Maintenance', 'Square Footage':'150', 'Price':'0', 'RoomID':'104', 'Capacity':'0'}
{'Floor':'2', 'Use':'Studio', 'Square Footage':'875', 'Price':'850', 'RoomID':'200', 'Capacity':'2'}
{'Floor':'2', 'Use':'Studio', 'Square Footage':'734', 'Price':'850', 'RoomID':'201', 'Capacity':'2'}
{'Floor':'2', 'Use':'Studio', 'Square Footage':'624', 'Price':'850', 'RoomID':'202', 'Capacity':'2'}
{'Floor':'2', 'Use':'Studio', 'Square Footage':'624', 'Price':'850', 'RoomID':'203', 'Capacity':'2'}
{'Floor':'2', 'Use':'Double', 'Square Footage':'850', 'Price':'1245', 'RoomID':'204', 'Capacity':'4'}
{'Floor':'2', 'Use':'Double', 'Square Footage':'850', 'Price':'1245', 'RoomID':'205', 'Capacity':'4'}
{'Floor':'2', 'Use':'Double', 'Square Footage':'850', 'Price':'1245', 'RoomID':'206', 'Capacity':'4'}
{'Floor':'2', 'Use':'Double', 'Square Footage':'850', 'Price':'1245', 'RoomID':'207', 'Capacity':'4'}
{'Floor':'2', 'Use':'Common', 'Square Footage':'731', 'Price':'0', 'RoomID':'208', 'Capacity':'0'}
{'Floor':'2', 'Use':'Quad', 'Square Footage':'1100', 'Price':'1650', 'RoomID':'209', 'Capacity':'8'}
{'Floor':'2', 'Use':'Quad', 'Square Footage':'1005', 'Price':'1650', 'RoomID':'210', 'Capacity':'8'}
{'Floor':'2', 'Use':'Quad', 'Square Footage':'1205', 'Price':'1650', 'RoomID':'211', 'Capacity':'8'}
```

Now since each value is proceded by a key, values may be found by searching for the key names.  For instance in this case the script prints the `Use` and `Square Footage` from each line:

```
        for row in reader:
            print(row['Use'], row['Square Footage'])
```

There are many ways to use dictionary data.  Just to add to this example, here is code to add up all the square footage from the `Retail` space in the building:

```python
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        total = 0
        for row in reader:
            if row['Use'] == 'Retail':
                total += float(row['Square Footage'])
        print "Retail space = {} sq. ft".format(total)
```

Here the loop loops for each row that contains 'Retail'  and then will add the square footage for each into the `total` variable.  In the end it prints the total in the console.

By using the `csv.DictReader()` method, the simple CSV data can become a more sophisticated dictionary of information.  This is a very powerful tool.

## Writing CSV files

Writing a file is similar to reading, but the order in which things are done is different. This time we'll look at the ExportPoints.py sample file.

```python
import csv
import rhinoscriptsyntax as rs

def CSVwrite():
    #Get the filename to create
    filter = "CSV File (*.csv)|*.csv|*.txt|All Files (*.*)|*.*||"
    filename = rs.SaveFileName("Save point coordinates as", filter)
    if( filename==None ): return

    points = rs.GetPoints(draw_lines=False, message1="Pick points to save to CSV:")
    if( points==None): return


    with open(filename, "wb") as csvfile:
        csvwriter = csv.writer(csvfile,  delimiter=',')
        for point in points:
            csvwriter.writerow([point[0], point[1], point[2]])
        print "Points written sucessfully to file"

##########################################################################
# Check to see if this file is being executed as the "main" python
# script instead of being used as a module by some other python script
# This allows us to use the module which ever way we want.
if( __name__ == "__main__" ):
    CSVwrite()

```
{: .line-numbers}

Lines 1 thru 8 are standard lines from the Rhino.Python [How to read and write a simple file]({{ site.baseurl }}/guides/rhinopython/python-reading-writing) guide.

There are a couple of things to notice, compared to the previous example. We need some points to export, 
so we'll let the user select some point objects.  Then check that some points were picked:


```python
    points = rs.GetPoints(draw_lines=False, message1="Pick points to save to CSV:")
    if( points==None): return
```

Lines 14 thru 18 opens the file for write. Then the script runs through all the points in the list using the `.writerow` method.
The write row method takes a list of values and adds the list as a line in the CSV file. 

```python
    with open(filename, "wb") as csvfile:
        csvwriter = csv.writer(csvfile,  delimiter=',')
        for point in points:
            csvwriter.writerow([point[0], point[1], point[2]])
        print "Points written sucessfully to file"
```

The `.writerow` method is great for writing out various values that in the simplest CSV form. 

## Writing out a dictionary object

Like the read methods, there is also a way to write out a dictionary object to a CSV file. 
This is a great way to format any dictionary data into a spreadsheet or table format.

```python
import csv
import rhinoscriptsyntax as rs

def CSVwrite():
    #Get the filename to create
    filter = "CSV File (*.csv)|*.csv|*.txt|All Files (*.*)|*.*||"
    filename = rs.SaveFileName("Save point coordinates as", filter)
    if( filename==None ): return

    dict = [
    {'Floor':'1', 'Use':'Retail', 'Square Footage':'6598', 'RoomID':'100'},
    {'Floor':'1', 'Use':'Retail', 'Square Footage':'1900', 'RoomID':'101'},
    {'Floor':'1', 'Use':'Retail', 'Square Footage':'1850', 'RoomID':'102'},
    {'Floor':'1', 'Use':'Restroom', 'Square Footage':'250', 'RoomID':'103'},
    {'Floor':'1', 'Use':'Maintenance', 'Square Footage':'150', 'RoomID':'104'}
    ]


    with open(filename, "wb") as csvfile:
        fieldnames = ('Floor', 'Use', 'Square Footage', 'Price', 'RoomID', 'Capacity')
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in dict:
            writer.writerow(row)

##########################################################################
# Check to see if this file is being executed as the "main" python
# script instead of being used as a module by some other python script
# This allows us to use the module which ever way we want.
if( __name__ == "__main__" ):
    CSVwrite()

```
{: .line-numbers}

In lines 10-16 we set a list of dictionaries.  The header names corespond with the key names in the dictionary.
The `.DictWriter` class can write a header in the CSV and will use the values in the keys to write the CSV.

The resulting CSV file will be formatted as follows:

```none
Floor,Use,Square Footage,RoomID
1,Retail,6598,100
1,Retail,1900,101
1,Retail,1850,102
1,Restroom,250,103
1,Maintenance,150,104
```

For more information on CSV maniputlation, see the [Python.org csv module](https://docs.python.org/2/library/csv.html).

---

## Related Topics

- [Python.org csv module](https://docs.python.org/2/library/csv.html)
- [How to read and write a simple file]({{ site.baseurl }}/guides/rhinopython/python-reading-writing) guide.
- [How to use JSON with Python]({{ site.baseurl }}/guides/rhinopython/python-xml-json)