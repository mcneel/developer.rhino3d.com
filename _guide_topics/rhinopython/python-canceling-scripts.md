---
title: Canceling a Python script in Rhino
description: This guide demonstrates how to cancel a Python script in Rhino.
authors: ['scott_davidson']
author_contacts: ['scottd']
sdk: ['RhinoPython']
languages: ['Python']
platforms: ['Windows', 'Mac']
categories: ['Python Windows']
origin:
order: 5
keywords: ['python', 'commands']
layout: toc-guide-page
TODO:
---

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

---

## Related Topics

- [What is Python and RhinoScript?]({{ site.baseurl }}/guides/rhinopython/what-are-python-rhinoscript)
- [Your First Python Script in Rhino (Windows)]({{ site.baseurl }}/guides/rhinopython/your-first-python-script-in-rhino-windows)
- [Running Scripts]({{ site.baseurl }}/guides/rhinopython/python-running-scripts)
- [Canceling Scripts]({{ site.baseurl }}/guides/rhinopython/python-canceling-scripts)
- [Editing Scripts]({{ site.baseurl }}/guides/rhinopython/python-editing-scripts)
- [Scripting Options]({{ site.baseurl }}/guides/rhinopython/python-scripting-options)
