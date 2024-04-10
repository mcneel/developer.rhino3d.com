+++
aliases = [""]
authors = [ "rajaa" ]
categories = [ "Csharp Essentials" ]
category_page = "guides/grasshopper/csharp-essentials/"
keywords = [ "csharp", "commands" ]
languages = [ "C#" ]
sdk = [ "RhinoCommon" ]
title = "Chapter Three: RhinoCommon Geometry"
type = "guides"
weight = 15
override_last_modified = "2018-12-05T14:59:06Z"
draft = false

[admin]
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 7
until = ""

[page_options]
block_webcrawlers = false
byline = true
toc = true
toc_type = "single"

+++

## 3.1 Programming in Rhino

Rhinoceros offers various ways of programmatic access. We've already met macros and scripts, but the plot thickens. Please invest a few moments of your life into looking at the diagram below, which you will never be asked to reproduce:

{{< image url="/images/rhino-technology-overview-01.png" alt="The Rhino Stack" class="image_center" width="75%" >}}

The above is a complete breakdown of all developer tools that Rhino has to offer. I'll give you a brief introduction as to what this diagram actually represents and although that is not vital information for our primary goal here ("learning how to script" in case you were wondering), you might as well familiarize yourself with it so you have something to talk about on a first date.

At the very core of Rhino are the code libraries. These are essentially collections of procedures and objects which are used to make life easier for the programs that link to them. The most famous one is the openNURBS library which was developed by Robert McNeel & Associates but is completely open source and has been ported by 3rd party programmers to other operating systems such as Unix and Linux. OpenNURBS provides all the required file writing and reading methods as well the basic geometry library. Practically all the 3D applications that support the 3dm file format use the openNURBS library. These code libraries have no knowledge of Rhino at all, they are 'upstream' so to speak.

Rhino itself (the red blob) is tightly wrapped around these core libraries, it both implements and extends them. Apart from this obvious behavior, Rhino also adds the possibility of plugins. Whereas most companies provide plugin support for 3rd party developers, McNeel has taken a rather exotic approach which eliminates several big problems. The technical term for this approach is "eating your own dogfood" and it essentially boils down to McNeel programmers using the same tools as 3rd party programmers. Rather than adding code to Rhino itself, McNeel programmers prefer writing a plugin instead. For one, if they screw up the collateral damage is usually fairly minor. It also means that the SDK (Software Development Kit, that which is used to build plugins) is rigorously tested internally and there is no need to maintain and support a separate product. Unfortunately the result of this policy has made plugins so powerful that it is very easy for ill-informed programmers to crash Rhino. This is slightly less true for those developers that use the dotNET SDK to write plugins and it doesn't apply at all to us, scripters. A common proverb in the software industry states that you can easily shoot yourself in the foot with programming, but you can take your whole leg off with C++. Scripters rarely have to deal with anything more severe than a paper-cut.

The orange pimples on Rhino's smooth surface are plugins. These days plugins can be written in C++ and all languages that support the DotNET framework (VB.NET, CSharp, Delphi, J#, IronPython etc. etc.). One of these plugins is the Python plugin and it implements and extends the basic IronPython Language.
language as well as Python at the front end, while tapping into all the core Rhino resources at the back end. Scripts thus gain access to Rhino, the core libraries and even other plugins through the RhinoScriptSyntax plugin.

Right, enough fore-play, time to get back to hard core programming.

## 3.2 The bones

Once you run a script through the in-build editor (remember you can access the editor by typing "Scripteditor" in Rhino's command line) the Python interpreter will thumb through your script and superficially parse the syntax. It will not actually execute any of the code at this point, before it starts doing that it first wants to get a feel for the script. The interpreter is capable of finding certain syntax errors during this prepass. If you see a dialog box like this:

{{< image url="/images/syntaxerror.jpg" alt="/images/syntaxerror.jpg" class="image_center" width="75%" >}}

before anything has actually taken place, it means the compiler ran into a problem with the syntax and decided it wasn't worth trying to run the script. If the script crashes while it is running, the Source of the error message will not be the Python Compiler. However, even scripts without syntax errors might not function as expected. In order for a script to run successfully, it must adhere to a few rules. Apart from syntax errors -which must be avoided- every script must implement a certain structure which tells the interpreter what's what:

{{< image url="/images/primer-script-structure.svg" alt="/images/primer-script-structure.svg" class="image_center" width="75%" >}}

<!--TODO: The font in the SVG above is not rendeirng correctly.  What Font to use -->

Note that the example script on page 11 did not adhere to these rules. It ran just the same, but it was a bad example in this respect.

The Import Statement allows the user to import different modules that are either built into Python when its downloaded, or from external developments.  Importing modules allows a user to access methods outside of the current file and reference objects, functions or other information.  There are various types of Import Statements: *import X, from X import, from X import a, b, c, X = __import__(‘X’)*, each with advantages and disadvantages.  For simplicity we can stick with import X for the time being.  This technique imports module X and allows us to use any methods within that module.

Comments (blocks of text in the script which are ignored by the compiler and the interpreter), can be used to add explanations or information to a file, or to temporarily disable certain lines of code. It is considered good practice to always include information about the current script at the top of the file such as author, version and date. Comment lines are indicated with a # sign.

Global variables are variables that can be accessed anywhere in your code (outside of functions, within functions and within classes).  Variable scope refers to the limitation or accessibility of a variable across different portions of code.  Global variables obviously can be accessed globally, while other variables may be limited to certain areas of your code.  For example, any variable that is created within a class or a function (we will cover classes and functions later) is limited to within that function.  This means they cannot be used outside of that function or class (unless they are specifically passed as input/output).  For now, we don't need to worry about different types of scope and let's assume that our variables are globally accessible unless otherwise noted.

Functions are blocks of code that compact certain functionality into a small package.  Functions can have variables, take input, provide output and do a number of other important tasks.  We will go into further detail about functions in the coming chapters.  Classes are similar in that they provide an opportunity for creating module code to package/compress segments of your code, while also providing other powerful tools.  Functions and classes must be created before they can be used (this is rather obvious). For that reason, the *Functions & Classes section* comes before the *Function Calls and Class Instances section*.  This just means that before we can actually *Call* (use) a Function, we need to first create the function.

## 3.3 The guts

The following example shows the essential structure that was just described, including: the Import Statement (always needed!), Global Variables, a Function and a Call to the Function.  The importance of syntax should also be stated - Please take note of the capitalization and indentation within this example.  Python is both case sensitive and indent sensitive.  If you spell a variable name once with a capital letter and another time with a lowercase letter, it will not recognize it as the same variable! The indent is used to indicate if certain lines should be included within a Function, Class, Loop or Conditional statement.  In this example, the line "print (text)" is indented to be contained within the function "simpleFunction" because it should only be executed once that function is called (Don't worry yet about how and why functions work, we will explain them soon).   Indentation and Case Sensitivity should be highly emphasized since they are a couple of the most common mistakes that you will run into!

{{< download-script "rhinopython/rhinopython101/3_3_AnatomyExample.py" "3_3_AnatomyExample.py">}}

```python
#! python3                                 # Language Type

import rhinoscriptsyntax as rs             # Import Statements
import scriptcontext as sc
import math

import System
import System.Collections.Generic
import Rhino
import rhinoscriptsyntax as rs                        
#Script written by Ehsan Iran-Nijad        # Default comments

strInfo = "This is just a test"            # Global Variable

def simpleFunction(text):                  # Function Declaration
    print(text)                            # Code to Execute Within the Function
                                               # (Note the Indentation)
simpleFunction(strInfo)                    # Calling the Function (After it's created)
```

One of the key features of RhinoScriptSyntax that makes it easy to write powerful scripts is the large library of Rhino specific functions.  This set of functions is known as the rhinoscriptsyntax package. To import the rhinoscriptsyntax package you must include the `import rhinoscriptsyntax` statement, `as rs` indicates that we will be using the name "rs" whenever we refer to this package. In the Editor, go to Help>Python Help for a list of all the rhinoscriptsyntax methods. Documentation can also be found at [http://www.rhino3d.com/5/ironpython/index.html](http://www.rhino3d.com/5/ironpython/index.html)

Note: McNeel has made all of the classes in the .NET Framework available to Python, including the classes available in RhinoCommon. This allows you to do some pretty amazing things inside of a python script. Many of the features that once could only be done in a .NET plug-in can now be done in a python script!
(Don't stress about this until you become a master of the basics...for now, just know its available!)

## 3.4 The skin

{{< image url="/images/buttonscript.jpg" alt="/images/buttonscript.jpg" class="float_right" width="325" >}}

After a script has been written and tested, you might want to put it in a place which has easy
access such as a Rhino toolbar button. If you want to run scripts from within buttons, there are two things you can do:

1. Link the script
2. Implement the script

If you want to implement the script, you'll have to wrap it up into a *_RunPythonScript* command. Imagine the script on the previous page has been saved on the hard disk as an \*.py file. The following button editor screenshot shows how to use the two options:    

## 3.5 The Editor

A Code Editor is an essential tool for any programmer.  Luckily, the script-editor within Rhino is built-in. It includes a Debugger for testing and working line-by-line through any script!  It is extremely good practice to use the debugger when writing any code longer than just a few lines.  The expression "bug in your code," means that something has gone wrong in your code - i.e your code fails, cannot continue to run or has given the wrong output. *(Of interesting note -  the first computer bug is said to have been found in 1947, when Harvard University's Mark II Aiken Relay Calculator machine was experiencing problems. An investigation showed that there was a moth trapped in the machine. The operators removed the moth and taped it into the log book. The entry reads: "First actual case of bug being found." And thus, the world of debugging was born!)* With any malfunctioning code, the programmers job is to quickly and easily identify the bug, however, this can be sometimes extremely difficult, especially if the code has many loops, conditional statements, functions, classes and spans hundreds or thousands of lines.  

To find out more about using the editor and its integrated debugger, see the [Script Editing Guide](/guides/scripting/scripting-command/)
## Next Steps

That was a basic overview of Python running in Rhino.  Now learn to use [operators and functions](/guides/rhinopython/primer-101/4-operators-and-functions/) to get something done.
