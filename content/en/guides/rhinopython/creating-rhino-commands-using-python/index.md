+++
authors = [ "pascal", "will" ]
categories = [ "Python in Rhino" ]
description = "This guide demonstrates how to create Rhino commands from Python scripts."
keywords = [ "python", "commands" ]
languages = [ "Python" ]
sdk = [ "RhinoPython" ]
title = "Creating Rhino Commands Using Python"
type = "guides"
weight = 380

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/python/commands"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++


## Overview

It is possible, if a little convoluted, to create "real" Rhino commands from Python scripts.  Below is outlined the procedure on Rhino for Windows, with a couple of comments about where the files need to go for this all to work with Rhino for Mac.  The initial template for the commands, along with a new GUID and the appropriate folders are created automatically by the Python script editor on Windows.  So far it is possible but not obvious or automatic to create all this on Rhino for Mac.  It is possible to install the folders and scripts for an existing Python command on the Mac and have it all work.

First, we will cover [Rhino for Windows](#windows), then turn our attention to [Rhino for Mac](#mac).

## Windows

1. Start in the *Rhino Python editor* using the `EditPythonScript` command.
1. Click on the *New* icon, and choose *Command* in the ensuing dialog.

   ![New Command](/images/creating-rhino-commands-using-python-01.png)

1. Enter the command name and the plugin name that you would like to have the command used in - the plugin can be a new one or an existing one.  You can add multiple commands to a plugin.  In this example, we used `MyNewCommand` in *MyNewPlugIn*.  A new script file is generated with the framework for the new command...

   ![New Script](/images/creating-rhino-commands-using-python-02.png)

1. The code that the command calls is in the `def RunCommand( is_interactive ):` function.
1. Add your script code here - the template provides some dummy code and a couple of comments, all to be called from this part of the script.  The whole script can be in this one function or you can add other functions as you normally would, as needed.  Make sure to modify the initial `import` statements to suit the script you are writing - the automatic template `import`s are there for the example script provided.
1. Add this line at the bottom of the script `RunCommand(True)`.  This allows you to test the script from the editor, debug etc.  Just remember to comment that line before you distribute the script or try to use it as a command.  It is also possible to write a more "normal" script, test, etc. as needed in the usual way, then just copy and paste into this formatted command script template.
1. Note that, with Rhino for Windows, the script is automatically saved in a special location:

   ![Special Script Location](/images/creating-rhino-commands-using-python-03.png)

   In order for this to run as a command in Rhino, the script location needs to be exactly right so that Rhino knows where to look.  On Windows, the path for a command script looks like this: `%APPDATA%\McNeel\Rhinoceros\5.0\Plug-ins\PythonPlugIns\MyNewPlugIn {146e099d-760d-4a6c-8662-96119f3fd62f}` ...and it must keep that crazy name with the GUID in curly brackets, and the path that the editor set up when you created the command initially.

   ![Special Script Path](/images/creating-rhino-commands-using-python-04.png)

1. _Optional_: To distribute the script as a plugin, simply share the entire folder. You can zip it up, if you like, and other users can easily extract the `MyNewPlugIn {146e099d-760d-4a6c-8662-96119f3fd62f}` folder and place it in `%APPDATA%\McNeel\Rhinoceros\5.0\Plug-ins\PythonPlugIns\` on their own computers.

   Rhino should be closed when "installing" new plugins, otherwise it will need to be restarted before it recognizes any new commands.

   Another option for distributing Python plugins is to [create an RHI installer](#creating-an-rhi-installer).

### Creating an RHI Installer

This allows users to just double-click (or drag-and-drop) your plugin and, "hey presto", it's installed. It also gracefully handles upgrading to newer versions of your plugin.

In the **`dev` sub-folder** that is created in the plugin folder, create a *py* file named `__plugin__.py` that has only these lines:

```py
id="{146e099d-760d-4a6c-8662-96119f3fd62f}"
version="1.0.0.1"
title="MyNewCommand"
```

In the above `__plugin__.py`, the lines mean the following:

- Line 1 has the UUID from the plugin, found in the folder name.
- Line 2 has the version - it would be up to you to keep that current.
- Line 3 has the command name.

With this file in place, you can zip the *contents of the `dev` sub-folder* and rename it to `MyNewPlugIn.rhi`.

<div class="bs-callout bs-callout-danger">

<strong>Note</strong>: It's important that the <code>__plugin__.py</code> file and any <code>cmd.py</code> files are in the root of the RHI package. The Rhino Installer Engine will unpack the contents of the RHI into a sub-folder named according to the version found in <code>__plugin__.py</code>, replacing the <code>dev</code> sub-folder used during development.

</div>

Double-clicking this _rhi_ file on another system (with Rhino closed) should install all the files in the correct location for that user.  Rhino should then see the command as a regular command.

<div class="bs-callout bs-callout-danger">

<strong>Note</strong>: Sometimes, using this system, Rhino requires that Python be loaded before it can see the new command for the first time in a session - running <code>EditPythonScript</code>, or any other python script should allow the command to work.

</div>

## Mac

Setting this up on macOS is a bit more labor intensive, but once you see how it works, it should be fairly straightforward. (It is helpful to read the [Windows](#windows) section above to get the general idea).  

There are four things you need to pay attention to on macOS:

1. The py script file
1. The plugin name
1. The command name
1. The plugin GUID

On macOS, the location of the plugin folders must be in:

*/Users/~/Library/Application Support/McNeel/Rhinoceros/6.0/Plug-ins/PythonPlugIns/*

If the *PythonPlugIns* folder does not yet exist, you'll have to create it.

Within that folder there needs to be a folder for each command plugin such as

*PythonPlugIns/MyNewPlugIn {146e099d-760d-4a6c-8662-96119f3fd62f}*

and within the individual plugin's folder there is yet another folder called *dev* - that is where the Python script itself should be saved.  The script name must have a special format as well - again, not automatic on Rhino for Mac, so you'll need to be careful to get it right.  The file name must be in the format:

*CommandName_cmd.py*

There can be multiple command files in the folder - one for each command in the plugin.

The long messy number thing in braces is the GUID - that GUID, and in fact the folder itself, is automatically generated on Rhino for Windows when you tell the editor you want to create a command - but on macOS you need to create the GUID and the folder and *dev* sub-folder yourself.  [Generate a GUID](https://www.guidgenerator.com/online-guid-generator.aspx) and then use it in the folder name as indicated above: *PlugInName{GUID}*

The Python script itself has to be set up and named correctly as well - this is done from a template on Rhino for Windows, but you will need to do it by hand, so to speak, on macOS.  The *py* file should be set up like this:

```py
#import statements as needed:
import rhinoscriptsyntax as rs
import scriptcontext as sc
import Rhino
#this line with the name of the command:
__commandname__ = "MyNewCommand"
def RunCommand( is_interactive ):
     #Your code in here
     obj = rs.GetObject()
     if obj:
         print "Got an object"
     #etc...
```

This command script must be saved to:

`~/Library/Application Support/McNeel/Rhinoceros/6.0/Plug-ins/PythonPlugIns/PlugInName{GUID}/dev`

<div class="bs-callout bs-callout-danger">

<strong>Note</strong>: The command name must match the script filename, so in this example the file name would be: <code>MyNewCommand_cmd.py</code>

</div>
