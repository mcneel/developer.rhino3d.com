---
layout: bootstrap
---

# Command

Runs a Rhino command script. All Rhino commands can be used in command
        scripts. The command can be a built-in Rhino command or one provided by a
        3rd party plug-in.
        

### Parameters:

- ***commandString*** = a Rhino command including any arguments
- ***echo[opt]*** = the command echo mode
        

### Returns:


  True or False indicating success or failure
        
Write command scripts just as you would type the command sequence at the
command line. A space or a new line acts like pressing <Enter> at the
command line. For more information, see "Scripting" in Rhino help.
    
Note, this function is designed to run one command and one command only.
Do not combine multiple Rhino commands into a single call to this method.
  WRONG:
    rs.Command("_Line _SelLast _Invert")
  CORRECT:
    rs.Command("_Line")
    rs.Command("_SelLast")
    rs.Command("_Invert")
    
Also, the exclamation point and space character ( ! ) combination used by
button macros and batch-driven scripts to cancel the previous command is
not valid.
  WRONG:
    rs.Command("! _Line _Pause _Pause")
  CORRECT:
    rs.Command("_Line _Pause _Pause")
After the command script has run, you can obtain the identifiers of most
recently created or changed object by calling LastCreatedObjects.
        
