---
layout: toc-guide-page
title: VBScript Statements
author: dale@mcneel.com
categories: ['VBScript Basics']
platforms: ['Windows']
apis: ['RhinoScript']
languages: ['RhinoScript']
keywords: ['script', 'Rhino', 'vbscript']
order: 1
---

# VBScript Statements
{: .toc-title }

Many scripting and programming languages, such as JScript, C#, and C++, make no attempt to match the code that is run with the actual physical lines typed into the text editor. This is because they not recognize the end of a line of code until it sees the termination character (in these cases, the semicolon). Thus, the actual physical lines of type taken up by the code are irrelevant.

By contrast, VBScript uses the carriage return instead of a special line termination character. To end a statement in VBScript, you do not have to type in a semicolon or other special character; you simply press ENTER. For example, this code will generate a syntax error:

	Set
	objFSO
	=
	CreateObject("Scripting.FileSystemObject")

This will not:

	Set objFSO = CreateObject("Scripting.FileSystemObject")

In general, the lack of a required statement termination character simplifies script writing in VBScript. There is, however, one complication: To enhance readability, it is recommended that you limit the length of any single line of code to 80 characters. What happens, then, if you have a line of code that contains 100 characters?

Although it might seem like the obvious solution, you cannot split a statement into multiple lines simply by entering a carriage return. For example, the following code snippet returns a run-time error in VBScript because a statement was split by using ENTER.

	strMessageToDisplay = strUserFirstName & " " & strUserMiddleInitial & " " & strUserLastName
	Rhino.Print strMessageToDisplay

You cannot split a statement into multiple lines in VBScript by pressing ENTER because VBScript sees a carriage return as marking the end of a statement. In the preceding example, VBScript interprets the first line as the first statement in the script. Next it interprets the second line as the second statement in the script, and the error occurs because strUserLastName is not a valid VBScript statement.

Instead, use the underscore (_) to indicate that a statement is continued on the next line. In the revised version of the script, a blank space and an underscore indicate that the statement that was started on line 1 is continued on line 2. To make it more apparent that line 2 is a continuation of line 1, line 2 is also indented four spaces. (This was done for the sake of readability, but you do not have to indent continued lines.)

	strMessageToDisplay = strUserFirstName & " " & strUserMiddleInitial & " " _ & strUserLastName
	Rhino.Print strMessageToDisplay

	Line continuation is more complex when you try to split a statement inside a set of quotation marks. For example, suppose you split this statement using a blank space and an underscore:

	strMessage = "If you ask me anything I don't know, _ I'm not going to answer."
	Rhino.Print strMessage

If you run this script, you will encounter a run-time error because the line continuation character has been placed inside a set of quotation marks (and is therefore considered part of the string). To split this statement:

Close the first line with quotation marks, and then insert the blank space and the underscore.
Use an ampersand at the beginning of the second line. This indicates that line two is a continuation of the interrupted string in line 1.
Add quotation marks before continuing the statement.
These quotation marks indicate that this line should be included as part of the quoted string started on the previous line. Without the quotation marks, the script engine would interpret the continued line as a VBScript statement. Because this is not a valid VBScript statement, an error would occur.

The revised statement looks like this:

	strMessage = "If you ask me anything I don't know, " _ & " I'm not going to answer."
	Rhino.Print strMessage

When splitting statements in this fashion, be careful to insert spaces in the proper location.
