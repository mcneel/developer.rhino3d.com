---
title: Debugging GH-Python components Visual Studio 
description: This guide will walk yoU through to debugging python scripts in Grasshopper using Visual Studio.
authors: ['giulio_piacentino', 'david_leon']
sdk: ['RhinoPython']
languages: ['Python']
platforms: ['Windows', 'Grasshopper']
categories: ['GhPython']
origin:
order: 3
keywords: ['python', 'commands', 'grasshopper']
layout: toc-guide-page
---

## Requirements


<ul>
  <li>Rhino WIP</li>
  <li>Visual Studio with Python Tools for Visual Studio (PTVSD)</li>
</ul>  


## Visual Studio Setup


1. Open **Visual Studio**, and create a new Iron Python Project called GHPythonDebug. 

2. Go to Debug > Options > Python > Debugging and tick Use Legacy Debugger

3. Inside *GHPythonDebug.py* type this:


	```python
	import sys

	#this is the path where the Visual Studio Python modules are locate. Change to your own: 
	loc = r'C:\Program Files (x86)\Microsoft Visual Studio\2017\Professional\Common7\IDE\Extensions\Microsoft\python\Core'

	if loc not in sys.path:
		sys.path.append(loc)

	import ptvsd

	if not ptvsd.is_attached():
		#set up secret, address and port for ptvsd
		ptvsd.enable_attach(secret = 'dev', address = ('localhost', 2019))
		ptvsd.wait_for_attach()
	```



4. Find the location of your VS ptvsd Python module:

	For Visual Studio 2019 and Visual Studio 2017, the Python workload is installed in *%ProgramFiles(x86)%\Microsoft Visual Studio\<VS_version>\<VS_edition>Common7\IDE\Extensions\Microsoft\Python* where ** <VS_version> ** is 2019 or 2017 and ** <VS_edition> ** is Community, Professional, or Enterprise.

	(For earlier version, please head to the [Microsoft site](https://docs.microsoft.com/en-us/visualstudio/python/installing-python-support-in-visual-studio?view=vs-2019#install-locations) on where to find the path). 

	Make sure that you can access that folder. You should be able to find *ptvsd* folder in that location. After you've found the correct location, replace it to the `loc` variable in the script.

## Rhino WIP Setup

{:start="5"}
5. Start **Rhino WIP** (7), and type `_EditPythonScript` to open the editor. In *Tools > Options > Script Engine*, tick the Frames and Tracing checkboxes


6. Open **Grasshopper**. Create a new GHPython component, and choose *Show Code* and *Input is path* from the component options

7. Input the path of *GHPythonDebug.py* as a text into the `Code` Input of the component. Optionally, make the path pass through a `FilePath` param, right click it, and choose ‘Synchronise’. If *test.py* is saved in the same folder as the Grasshopper file, then you only need to input the file name. 


## Debugging

{:start="8"}
8. Back in In **Visual Studio**, find in the top menu *Debug > Attach to process...* 

9. In connection Type, choose Python Remote (ptvsd)

10. In the dialog just below the type (ptvsd) -- it’s called “Connection target” in VS2019 -- write : `tcp://dev@localhost:2019/` and click *Find*. This corresponds to the secret, address and port that you defined in the code. (If clicking *Find* doesn’t work, type the address and type Enter).   

11. Choose ‘Rhino’ in the Process view below, and “Attach”. 


Now you should be able to run your script in GhPython. Breakpoints are hit, you can view and even modify locals (in the Debug->Windows->>Locals window in Visual Studio, available when debugging).


