+++
authors = ["steve"]
categories = ["Intermediate", "Advanced"]
description = "This guide gives an overview of using RhinoCommon to drive file format IO with code"
keywords = [ ".NET", "RhinoCommon", "Plugin", "Python", "Grasshopper", "Rhino3D" ]
languages = [ "C#", "Python" ]
sdk = [ "RhinoCommon", "RhinoPython", "Grasshopper"]
title = "Code-Driven File IO"
type = "guides"
weight = 4

[admin]
TODO = ""
origin = ""
picky_sisters = ""
state = "Complete"

[included_in]
platforms = [ "Windows", "Mac" ]
since = 8

[page_options]
byline = true
toc = true
toc_type = "single"
block_webcrawlers = false
+++

Prior to Rhino 8, code-driven exporting was done by using the active document and scripting the export command. This was both inefficient and painful to write.

Rhino 8 introduces the abililty to read and write files of any format that Rhino supports entirely through code. This includes support for options that need to be applied to properly read or write different files.

## How does it work?

Import and export plug-ins are provided an optional dictionary at read and write time. When the dictionary is present, instead of asking for user input, the importers and exporters pay attention to keys and values in the dictionary to make decisions on options for I/O. RhinoCommon provides classes for these options that can be converted into a dictionary that the import and export plug-ins can interpret. Look in the `Rhino.FileIO` namespace for format specific option classes.

## Example: Write an AutoCAD dwg from Rhino

This example shows how to write the active `RhinoDoc` to an AutoCAD dwg with options:

<div class="codetab">
  <button class="tablinks" onclick="openCodeTab(event, 'cs')" id="defaultOpen">C#</button>
  <button class="tablinks" onclick="openCodeTab(event, 'py')">Python</button>
</div>

<div class="tab-content">
<div class="codetab-content" id="cs">

```cs
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

</div>

<div class="codetab-content" id="py">

```py
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

</div>
</div>

## Headless Document Support

Headless `RhinoDoc` instances can be used to further streamline the process. Headless documents are `RhinoDoc` instances that never affect the Rhino user interface. Their use can improve performance as none of the geometry in the document needs to be displayed in Rhino. You can either create a headless document from scratch and add geometry to it or import from a file using options.

## Example: Read a SketchUp file into Rhino

This example shows how to read a SketchUp skp file and example the geometry using a headless RhinoDoc:

<div class="codetab">
  <button class="tablinks1" onclick="openCodeTab(event, 'cs1')" id="defaultOpen1">C#</button>
  <button class="tablinks1" onclick="openCodeTab(event, 'py1')">Python</button>
</div>

<div class="tab-content">
<div class="codetab-content1" id="cs1">

```cs
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

</div>

<div class="codetab-content1" id="py1">

```py
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

</div>
</div>

## Using Grasshopper with Code Driven File.io

When using Grasshopper to read or write files, there are some differences then the above examples.  The main difference is Grasshopper is it own document.  When reading in a file, objects are then processed thru Grasshopper independantly.  And when writing out a file format, then a headless doc needs to be created in the same component that writes the file.  See the examples below:

Reading in a file format can be done in new Rhino 8 components using the Import File component:

{{< image url="import_file_gh.png" alt="import_file_gh.png" class="image_center">}}

[{{< awesome "fas fa-download">}} ](ExportTo3MFV3.gh) [Download Example Grasshopper Definition for Exporting a File](ExportTo3MFV3.gh)

Here the file is imported and the objects can then be processed.

To write out any of the File formats from Rhino, create headless Doc and then add objects to it.  The example below writes a 3MF file using a Python 3 component. Set the script component `objects` input to `List Access` and `GeometryBase` Input Hint:

```py
import System
import Rhino

doc = Rhino.RhinoDoc.CreateHeadless(None)

if not objects is None:
    for o in objects:
        doc.Objects.Add(o)

options = Rhino.FileIO.File3mfWriteOptions()
options.Title = title
options.Designer = Rhino.RhinoApp.LicenseUserName
options.Metadata["Test"] = "Star"
options.MoveOutputToPositiveXYZOctant = True;

if not path is None:
    path = System.Environment.ExpandEnvironmentVariables(path)
    success = doc.Export(path, options.ToDictionary())
    print(success)
doc.Dispose();
```


## Other Use Cases

- Batch processing: a directory of files could be read into headless documents and exported to another format.
- Grasshopper: Using headless documents in Grasshopper with all Rhino file formats supports allows for processing geometry from different files without forcing the main Rhino active doc to change.