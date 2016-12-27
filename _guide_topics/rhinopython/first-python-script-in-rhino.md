---
title: Your first Script in Rhino
description: This guide demonstrates how to create Python scripts in Rhino.
authors: ['Scott Davidson']
author_contacts: ['scott']
apis: ['RhinoPython']
languages: ['Python']
platforms: ['Windows', 'Mac']
categories: ['Getting Started']
origin:
order: 1
keywords: ['python', 'commands']
layout: toc-guide-page
---

## Your first Script

This tutorial shows you how to display a message box in Rhino that says "Hello World". It covers the most basic concepts for editing,  loading and running scripts.

#### The Complete Script

```python
MsgBox "Hello World"
```
Test the Script

•Start Rhino


•At the command prompt, type EditScript and press Enter.


•The Edit Script dialog box appears.


•In the script Code window, type


MsgBox "Hello World"

•Click the "Run the script" button.


•The Edit Script dialog box disappears, and the message below appears:




The HelloWorld Subroutine

If you were writing a more complex script, and wanted to display "Hello World" at strategic points throughout the script, you could write this code every time you wanted the message to appear.

But if you changed your mind and wanted it to say "Howdy World" instead, you'd have to search for all the places "Hello World" was used, and replace them.

An easier way to solve this problem is to write a Subroutine (Sub for short).  At several places throughout your script, you call the Sub.  The Sub handles displaying the message, so you only have to change the message in one place.

Here's what the subroutine looks like:

Sub HelloWorld()

MsgBox "Hello World"

End Sub

To call this subroutine, simply type:

HelloWorld

Testing HelloWorld

•At the command prompt, type EditScript and press Enter.


•The Edit Script dialog box appears.


•In the script Code window, type


Sub HelloWorld()

MsgBox "Hello World"

End Sub

•Click the Run button.


Nothing happened? That's because the RhinoScript defined the Subroutine but did not actually call it.

•To call the subroutine, either add this line of code and click Run.


Sub HelloWorld()

MsgBox "Hello World"

End Sub

HelloWorld

Saving HelloWorld

When you do more than write a couple lines of script, it becomes necessary to save the script to a file so that you can run the script without typing it every time.

To save your script:

•In the Edit Script dialog box, Click the Save button.


•Save the file as "Hello World.rvb".


Running HelloWorld.rvb

•At the Command prompt, type LoadScript and press Enter.


•In the Load Scrip Filet dialog box, click Add...


•Select "Hello World.rvb" and click Open.


•In the Select Script File list, select "Hello World.rvb".


•Click Load.


Your script will run, and display the familiar "Hello World" dialog box.

---