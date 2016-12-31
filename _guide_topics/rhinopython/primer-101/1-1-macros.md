---
title: 1.1 Macros
description:
authors: ['Scott Davidson']
author_contacts: ['scott']
apis: ['RhinoPython']
languages: ['Python']
platforms: ['Windows', 'Mac']
categories: ['Python Windows']
origin:
order: 1
keywords: ['python', 'commands']
layout: toc-guide-page
---

Rhinoceros is based on a command-line interface. This means you can control it by using only the keyboard. You type in the commands and the program will execute them. Ever since the advent of the mouse, a user interface which is purely command-line based is considered to be primitive, and rightly so. Instead of typing:

```
Line 0,0,0 10,0,0
```
you can also click on the Line button and then twice in the viewport to define the starting and ending points of a line-curve. Because of this second (graphical) interface some people have done away with the 
command-line entirely. Emotions run high on the subject; some users are command-line fanatics, others use only toolbars and menus. Programmers have no emotions in this respect, they are all wedded to the command-line. It’s no use programming the mouse to go to a certain coordinate and then simulate a mouse click, that is just plain silly. Programmers pump text into Rhino and they expect to get text in return.

The lowest form of programming in Rhino is using macros. I do not wish to offend those of you who write macros for a living, but it cannot be denied that it is a very primitive way to automate processes. I shall only briefly pause at the subject of macros, partly so we know which is which and partly because we might at some point simulate macros using RhinoScript.

A macro is a prerecorded list of orders for Rhino to execute. The _Line command at the top of this page is an example of a very simple macro. If your job is to open Rhino files, add a line from 0,0,0 to 10,0,0 to each one and save the file again, you would probably get very tired very quickly from typing "_Line w0,0,0 w10,0,0" six times a minute. Enter macros. Macros allow you to automate tasks you would normally do by hand but not by brain. Macros cannot be made smart, nor do they react to the things they help create. They’re a bit like traffic wardens in that respect. An example of a more sophisticated macro would be:


```
_SelNone
_Polygon _NumSides=6 w0,0,0 w10,0,0
_SelLast
\-_Properties _Object _Name RailPolygon _Enter _Enter
_SelNone
_Polygon _NumSides=6 w10,0,0 w12,0,0
_SelLast
_Rotate3D w0,0,0 w10,0,0 90
\-_Properties _Object _Name ProfilePolygon _Enter _Enter
_SelNone
\-_Sweep1 _SelName RailPolygon _SelName ProfilePolygon _Enter _Enter _Closed=Yes Enter
```

<table>
<tr>
<td>
The above code will create the same hexagonal torus over and over again. It might be useful, but it's not flexible. You can type the above text into the command-line by hand, or you can put it into a button. You can even copy-paste the text directly into Rhino.

Incidentally, the underscores before all the command names are due to Rhino localization. Using underscores will force Rhino to use English command names instead of -say- Italian or Japanese or whatever the custom setting is. You should always force English command names since that is the only guarantee that your code will work on all copies of Rhino worldwide.
</td>
<td width="30%"><img src="{{ site.baseurl }}/images/hexagonaltorus.svg" width="100%" height="300" float="right"></td>
</tr>
</table>

The hyphen in front of the _Properties and _Sweep1 command is used to suppress dialog boxes. If you take the hyphens out you will no longer be able to change the way a command works through the command -line.

There’s no limit to how complex a macro can become, you can keep adding commands without restrictions, but you’ll never be able to get around the limitations that lie at the heart of macros.

---

#### Related Topics

- [What is Python and RhinoScript?]({{ site.baseurl }}/guides/rhinopython/what-are-python-rhinoscript)
- [Loading Scripts]({{ site.baseurl }}/guides/rhinopython/python-loading-scripts)
- [Running Scripts]({{ site.baseurl }}/guides/rhinopython/python-running-scripts)
- [Canceling Scripts]({{ site.baseurl }}/guides/rhinopython/python-canceling-scripts)
- [Editing Scripts]({{ site.baseurl }}/guides/rhinopython/python-editing-scripts)
- [Scripting Options]({{ site.baseurl }}/guides/rhinopython/python-scripting-options)
- [Reinitializing Python]({{ site.baseurl }}/guides/rhinopython/python-scripting-reinitialize)
