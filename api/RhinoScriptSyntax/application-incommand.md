---
layout: bootstrap
---

# InCommand

Determines if Rhino is currently running a command. Because Rhino allows
        for transparent commands (commands run from inside of other commands), this
        method returns the total number of active commands.
        

### Parameters:

ignore_runners [opt] = If true, script running commands, such as
    LoadScript, RunScript, and ReadCommandFile will not counted.
        

### Returns:


the number of active commands
        
