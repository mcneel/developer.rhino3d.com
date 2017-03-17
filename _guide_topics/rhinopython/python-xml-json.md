---
title: How to use JSON with Python
description: How to format in JSON or XML.
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

[JSON (JavaScript Object Notation)](http://www.json.org/) is an easy to read, flexible text based format that can be used to store and communicate information to other products. It is mainly based on key:value pairs and is web and .NET friendly.  There are many libraries and products that support JSON.

One of the reasons JSON might be used is to collect data from the Rhino model to be used in other places.  Use JSON to store information for a door schedule, or a parts list.  A report can be created on the name, size and location of all the bitmaps in a model.  A JSON file can have the endpoints of all the lines in a model representing column or beam connection points. JSON files are used in several other places and products.  JSON is also easy to display on dynamic webpages.

Here is an example of a JSON structure describing a medical office, taken from a set of polylines off a Rhino floorplan. As you will see in the example, the medical space includes 5 rooms and parking, with square footage and pricing for each dedicated space.

```json
{ "office": {
    "medical": [
      { "room-number": 100,
        "use": "reception",
        "sq-ft": 50,
        "price": 75
      },
      { "room-number": 101,
        "use": "waiting",
        "sq-ft": 250,
        "price": 75
      },
      { "room-number": 102,
        "use": "examination",
        "sq-ft": 125,
        "price": 150
      },
      { "room-number": 103,
        "use": "examination",
        "sq-ft": 125,
        "price": 150
      },
      { "room-number": 104,
        "use": "office",
        "sq-ft": 150,
        "price": 100
      }
    ],
    "parking": {
      "location": "premium",
      "style": "covered",
      "price": 750
    }
}
```
It is this dictionary setup that works best for Json.

For more information on creating and manipulating this type of information in Python see the [Dictionary as a Database Guide]({{ site.baseurl}}/guides/rhinopython/python-dictionary-database/)

## JSON in Python

JSON can store Lists, bools, numbers, tuples and dictionaries. But to be saved into a file, all these structures must be reduced to strings. It is the string version that can be read or written to a file. Python has a JSON module that will help converting the datastructures to JSON strings. Use the `import` function to import the JSON module.

```python
import json
```
The JSON module is mainly used to convert the python dictionary above into a JSON string that can be written into a file.

```python
json_string = json.dumps(datastore)
```

The JSON module can also take a JSON string and convert it back to a dictionary structure:

```python
datastore = json.loads(json_string)
```

While the JSON module will convert strings to Python datatypes, normally the JSON functions are used to read and write directly from JSON files.

## Writing a JSON file

Not only can the `json.dumps()` function convert a Python datastructure to a JSON string, but it can also dump a JSON string directly into a file.  Here is an example of writing a structure above to a JSON file:

```python
#Get the file name for the new file to write
filter = "JSON File (*.json)|*.json|All Files (*.*)|*.*||"
filename = rs.SaveFileName("Save JSON file as", filter)

# If the file name exists, write a JSON string into the file.
if filename:
    # Writing JSON data
    with open(filename, 'w') as f:
        json.dump(datastore, f)
```

Remember only a JSON formatted string can be written to the file. For more information about using Rhino.Python to read and write files see the [How to read and write a simple file]({{ site.baseurl}}/guides/rhinopython/python-reading-writing/)

## Reading JSON

Reading in a JSON file uses the `json.load()` function.

```python
import rhinoscriptsyntax as rs
import json

#prompt the user for a file to import
filter = "JSON file (*.json)|*.json|All Files (*.*)|*.*||"
filename = rs.OpenFileName("Open JSON File", filter)

#Read JSON data into the datastore variable
if filename:
    with open(filename, 'r') as f:
        datastore = json.load(f)

#Use the new datastore datastructure
print datastore["office"]["parking"]["style"]
```

The result of the code above will result in the same data structure at the top of this guide.

For more information about using Rhino.Python to read and write files see the [How to read and write a simple file]({{ site.baseurl}}/guides/rhinopython/python-reading-writing/)

For more details on accessing the information in the dictionary datastructure see,  [Dictionary as a Database Guide]({{ site.baseurl}}/guides/rhinopython/python-dictionary-database/)
