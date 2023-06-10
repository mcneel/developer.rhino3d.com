+++
authors = []
categories = []
description = "This guide gives an overview of using RhinoCommon to drive file format IO"
keywords = [ ".NET", "RhinoCommon", "Plugin" ]
languages = [ "C#" ]
sdk = [ "RhinoCommon" ]
title = "Code-Driven File IO"
type = "guides"
weight = 4

[admin]
TODO = "Author this page"
origin = ""
picky_sisters = ""
state = "In Progress"

[included_in]
platforms = [ "Windows", "Mac" ]
since = 8

[page_options]
byline = true
toc = true
toc_type = "single"
block_webcrawlers = true
+++

Prior to Rhino 8, code driven exporting was done by using the active document and scripting the export command. This was both painful to write and inefficient.

Rhino 8 introduces the abililty to read and write files of any format that Rhino supports entirely through code. This includes support for options that need to be applied to properly read or write different files.

## How does it work?
Import and export plug-ins are provided an optional dictionary at read and write time. When the dictionary is present, the importers and exporters should pay attention to keys and values in the dictionary to make decisions on options for I/O instead of asking for user input. RhinoCommon provides classes for these options that can be converted into a dictionary that the import and export plug-ins can interpret. Look in the Rhino.FileIO namespace for format specific option classes.

## Example - Write active RhinoDoc to an AutoCAD dwg file with options
``` C#
// C# Sample
var doc = Rhino.RhinoDoc.ActiveDoc;
if (doc != null)
{
    // create/set options for exporting to DWG file
    var options = new Rhino.FileIO.FileDwgWriteOptions();
    options.UseLWPolylines = true;
    options.Version = Rhino.FileIO.FileDwgWriteOptions.AutocadVersion.Acad2000;
    // convert options into a dictionary
    var optionsDictionary = options.ToDictionary();

    var path = System.Environment.GetFolderPath(System.Environment.SpecialFolder.Desktop);
    path = System.IO.Path.Combine(path, "sample.dwg");

    // export to a file with our options dictionary
    bool success = doc.Export(path, optionsDictionary);
    if (success)
        System.Console.WriteLine("Successfully exported sample.dwg");
    else
        System.Console.WriteLine("Error while trying to export sample.dwg");
}
```

``` Py
# Python Sample
import scriptcontext
import Rhino
import os

if scriptcontext.doc is not None:
    options = Rhino.FileIO.FileDwgWriteOptions()
    options.UseLWPolylines = True
    options.Version = Rhino.FileIO.FileDwgWriteOptions.AutocadVersion.Acad2000
    options_dictionary = options.ToDictionary()

    path = os.path.expanduser("~/Desktop/sample_py.dwg")
    success = scriptcontext.doc.Export(path, options_dictionary)
    if success:
        print("Successfully exported sample.dwg")
    else:
        print("Error while trying to export sample.dwg")
```

## Headless Document Support
Headless RhinoDoc instances can be used to further streamline the process. Headless documents are RhinoDoc instances that never affect the Rhino user interface. Their use can improve performance as none of the geometry in the document needs to be displayed in Rhino. You can either create a headless document from scratch and add geometry to it or import from a file using options

## Example - Read SketchUp file and examine the geometry using a headless RhinoDoc

``` C#
// C# Sample
// Create a headless doc and import SketchUp file into it
var doc = Rhino.RhinoDoc.CreateHeadless(null);
var options = new Rhino.FileIO.FileSkpReadOptions();
options.ImportCurves = false;
options.EmbedTexturesInModel = false;

var path = System.Environment.GetFolderPath(System.Environment.SpecialFolder.Desktop);
path = System.IO.Path.Combine(path, "test.skp");
doc.Import(path, options.ToDictionary());

// Analyze what was read into the doc
System.Console.WriteLine($"{doc.Objects.Count} objects");
foreach(var obj in doc.Objects)
{
    var bbox = obj.Geometry.GetBoundingBox(true);
    System.Console.WriteLine($"Center is {bbox.Center}");
}

// done with the doc, free up the memory it is using
doc.Dispose();
```

``` Py
# Python sample
import Rhino
import os

doc = Rhino.RhinoDoc.CreateHeadless(None)
options = Rhino.FileIO.FileSkpReadOptions()
options.ImportCurves = False
options.EmbedTexturesInModel = False

path = os.path.expanduser("~/Desktop/test.skp")
doc.Import(path, options.ToDictionary())

print(f"{doc.Objects.Count} objects")
for obj in doc.Objects:
    bbox = obj.Geometry.GetBoundingBox(True)
    print(f"Center is {bbox.Center}")

doc.Dispose()
```

## Other Use Cases
- Batch processing - a directory of files could be read into headless documents and exported to another format
- Grasshopper - Using headless documents in Grasshopper with all Rhino file formats supports allows for processing geometry from different files without forcing the main Rhino active doc to change