+++
aliases = ["/en/5/guides/rhinopython/python-canceling-scripts/", "/en/6/guides/rhinopython/python-canceling-scripts/", "/en/7/guides/rhinopython/python-canceling-scripts/", "/wip/guides/rhinopython/python-canceling-scripts/"]
authors = [ "scottd" ]
categories = [ "Python Windows" ]
description = "This guide demonstrates how to cancel a Python script in Rhino."
keywords = [ "python", "commands" ]
languages = [ "Python" ]
sdk = [ "RhinoPython" ]
title = "Canceling a Python script in Rhino"
type = "guides"
weight = 10
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

In Rhino 6, when a script is running and it is not waiting for user input, it can be cancelled by pressing the ESC.  In Rhino.Python this is done by adding a `scriptcontext.escape_test` test.

The following script is not be cancelled by pressing the ESC key.

```python
def TightLoopEscapeTest():
  for i in range(10000):

TightLoopEscapeTest()
```
By `scriptcontext.escape_test` function the loop can now be canceled:

```python
import scriptcontext

def TimeConsumingTask():    
    for i in range(10000):
        # Was escape key pressed?
        if (scriptcontext.escape_test(False)):
            print "TimeConsumingTask cancelled."
            break
        print i

TimeConsumingTask()
```

It might be necessary to press the `ESC` key a couple times to catch the `scriptcontext.escape_test` test in the correct state.

## Related Topics

- [What is Python and RhinoScript?](/guides/rhinopython/what-is-rhinopython)
- [Your First Python Script in Rhino (Windows)](/guides/rhinopython/your-first-python-script-in-rhino-windows)
- [Running Scripts](/guides/rhinopython/python-running-scripts)
- [Canceling Scripts](/guides/rhinopython/python-canceling-scripts)
- [Editing Scripts](/guides/rhinopython/python-editing-scripts)
- [Scripting Options](/guides/rhinopython/python-scripting-options)
