+++
aliases = ["/5/guides/rhinoscript/primer-101/3-script-anatomy/", "/6/guides/rhinoscript/primer-101/3-script-anatomy/", "/7/guides/rhinoscript/primer-101/3-script-anatomy/", "/wip/guides/rhinoscript/primer-101/3-script-anatomy/"]
authors = [ "david" ]
categories = [ "RhinoScript 101" ]
category_page = "guides/rhinoscript/primer-101/"
keywords = [ "rhinoscript", "vbscript", "commands" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "3 Script Anatomy"
type = "guides"
weight = 14
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++

## 3.1 Programming in Rhino

Rhinoceros offers various ways of programmatic access. We've already met macros and scripts, but the plot thickens. Please invest a few moments of your life into looking at the diagram below, which you will never be asked to reproduce:

{{< image url="/images/primer-script-anatomy.svg" alt="/images/primer-script-anatomy.svg" class="image_center" width="75%" >}}

The above is a complete breakdown of all developer tools that Rhino has to offer. I'll give you a brief introduction as to what this diagram actually represents and although that is not vital information for our primary goal here ("learning how to script" in case you were wondering), you might as well familiarize yourself with it so you have something to talk about on a first date.

At the very core of Rhino are the code libraries. These are essentially collections of procedures and objects which are used to make life easier for the programs that link to them. The most famous one is the openNURBS library which was developed by Robert McNeel & Associates but is competely open source and has been ported by 3rd party programmers to other operating systems such as Unix and Linux. OpenNURBS provides all the required file writing and reading methods as well the basic geometry library. Practically all the 3D applications that support the 3dm file format use the openNURBS library. These code libraries have no knowledge of Rhino at all, they are 'upstream' so to speak.

Rhino itself (the red blob) is tightly wrapped around these core libraries, it both implements and extends them. Apart from this obvious behaviour, Rhino also adds the possibility of plugins. Whereas most companies provide plugin support for 3rd party developers, McNeel has taken a rather exotic approach which elimates several big problems. The technical term for this approach is "eating your own dogfood" and it essentially boils down to McNeel programmers using the same tools as 3rd party programmers. Rather than adding code to Rhino itself, McNeel programmers prefer writing a plugin instead. For one, if they screw up the collateral damage is usually fairly minor. It also means that the SDK (Software Development Kit, that which is used to build plugins) is rigorously tested internally and there is no need to maintain and support a separate product. Unfortunately the result of this policy has made plugins so powerful that it is very easy for ill-informed programmers to crash Rhino. This is slightly less true for those developers that use the dotNET SDK to write plugins and it doesn't apply at all to us, scripters. A common proverb in the software industry states that you can easily shoot yourself in the foot with programming, but you can take your whole leg off with C++. Scripters rarely have to deal with anymore more severe than a paper-cut.

The orange pimples on Rhino's smooth surface are plugins. These days plugins can be written in C++ and all languages that support the DotNET framework (VB.NET, CSharp, Delphi, J#, IronPython etc. etc.). One of these plugins is the RhinoScript plugin and it implements and extends the basic Microsoft Visual Basic Scripting
language at the front end, while tapping into all the core Rhino resources at the back end. Scripts thus gain access to Rhino, the core libraries and even other plugins through the RhinoScript plugin.

Right, enough fore-play, time to get back to hard core programming.

## 3.2 The Bones

Once you run a certain script, either through the in-build editor or as an external file, the VBScript interpreter will thumb through your script and superficially parse the syntax. It will not actually execute any of the code at this point, before it starts doing that it first want to get a feel for the script. The interpreter is capable of finding certain syntax errors during this prepass. If you see a dialog box like this:

{{< image url="/images/CompilerErrorDialog.png" alt="/images/CompilerErrorDialog.png" class="image_center" width="50%" >}}

before anything has actually taken place, it means the compiler ran into a problem with the syntax and decided it wasn't worth trying to run the script. If the script crashes while it is running, the Source of the error message will not be the Microsoft VBScript Compiler. However, even scripts without syntax errors might not function as expected. In order for a script to run successfully, it must adhere to a few rules. Apart from syntax errors -which must be avoided- every script must implement a certain structure which tells the interpreter what's what:

{{< image url="/images/primer-ScriptStructure.png" alt="/images/primer-ScriptStructure.png" class="image_center" width="50%" >}}

Note that the example script on page 11 did not adhere to these rules. It ran just the same, but it was a bad example in this respect.

The Option Explicit area is named after the Option Explicit statement which it contains. The Option Explicit statement is optional, but I highly recommend adding it to every single script you ever write. If you are running a script in Option Explicit mode, you have to define all your variables before you can use them (see paragraph 2.3.5). If you omit Option Explicit, your variables will be declared for you by the compiler. Although this may sound as a good thing at first, it is much harder to find problems which are caused by typos in variable names. Option Explicit will save you from yourself.

In addition to the Option Explicit statement, the Option Explicit area may also contains a set of comments. Comments are blocks of text in the script which are ignored by the compiler and the interpreter. You can use comments to add explanations or information to a file, or to temporarily disable certain lines of code. It is considered good practise to always include information about the current script at the top of the file such as author, version and date. Comments are always preceded by an apostrophe. Global variables are also optional. Typically you do not need global variables and you're usually better off without them.

The area of the script which is outside the function declarations is referred to as 'script level'. All script level code will be executed by the interpreter whenever it feels like it so you're usually better off by putting all the code into functions and having them execute at your command.

## 3.3 The Guts

Every script requires at least one function (or subroutine) which contains the main code of the script. It doesn't have to be a big function, and it can place calls to any number of other functions but it is special because it delineates the extents of the script. The script starts running as soon as this function is called and it stops when the function completes. Without a main function, there is nothing to run.

Functions are not run automatically by the interpreter. They have to be called specifically from other bits of code. The only way to start the cascade of functions calling functions, is to place a call to the main subroutine somewhere outside all function declarations. You could put it anywhere, including at the very bottom of the script file, but I prefer to keep it near the top, just after the Option Explicit statement and just before the main subroutine begins. Without a main function call your script will be parsed and compiled, but it will not be executed. Do not get confused by terms such as 'function', 'subroutine', 'procedure' or 'method', at this time they all pretty much mean the same thing.

A script file may contain any number of additional functions/subroutines/procedures. But since I haven't told you yet what they are (apart from the fact that they are very similar), we'll skip this bit. For now.
Don't get too comfortable.

```
Option Explicit						         < Option Explicit statement
`Script written by David Rutten on 28-08-2006  < Default comments

Public intCount						         < A Global variable

Call Main()						             < Main function call
Sub Main()						             < Main function declaration
	Dim strInfo						         < Main function start
	strInfo = "This is just a test"	  
	Rhino.Print strInfo				
	Rhino.Print "I repeat: " \& strInfo  
End Sub							             < Main function end
```


## 3.4 The Skin

{{< image url="/images/buttonscript.jpg" alt="/images/buttonscript.jpg" class="float_right" width="325" >}}

After a script has been written and tested, you might want to put it in a place which has easy
access such as a Rhino toolbar button. If you want to run scripts from within buttons, there's two things you can do:

1. Link the script
2. Implement the script

If you link the script you'll only have to hardcode the *_LoadScript* command to point to the script file on the hard disk. If you want to implement the script, you'll have to wrap it up into a *_RunScript* command. Imagine the script on the previous page has been saved on the hard disk as an **.rvb file*. The following button editor screenshot shows how to use the two options:




## Next Steps

That was a basic overview of Python running in Rhino.  Now learn to use [operators and functions](/guides/rhinoscript/primer-101/4-operators-and-functions/) to get something done.
