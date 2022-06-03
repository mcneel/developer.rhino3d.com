+++
authors = [ "dale" ]
categories = [ "Fundamentals" ]
description = "This guide presents an overview of Python syntax."
keywords = [ "script", "Rhino", "python" ]
languages = [ "Python" ]
sdk = [ "RhinoPython" ]
title = "Python Basic Syntax"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Mac", "Windows" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++


## Overview

Many scripting and programming languages, such as JScript, C#, and C++, make no attempt to match the code that is run with the actual physical lines typed into the text editor.  This is because they not recognize the end of a line of code until it sees the termination character (in these cases, the semicolon).  Thus, the actual physical lines of type taken up by the code are irrelevant.

Unlike other languages, Python does not use an end of line character. Most of the time a simple <kbd>Enter</kbd> will do. Yet, Python is very particular about indentation, spaces and lines in certain cases.  This document is to help understand Python formatting.

It is important to understand how Python interprets:

2. End of Statement
1. Names and Capitalization
2. Comments
3. Block Structures
4. Tabs and Spaces

For the official very detailed documentation on Python Syntax, see the [Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

## End of Statements

To end a statement in Python, you do not have to type in a semicolon or other special character; you simply press <kbd>Enter</kbd>.  For example, this code will generate a syntax error:

```python
message
=
'Hello World!'
```

This will not:

```python
message = 'Hello World!'
```

In general, the lack of a required statement termination character simplifies script writing in Python.  There is, however, one complication: To enhance readability, it is recommended that you limit the length of any single line of code to 79 characters.  What happens, then, if you have a line of code that contains 100 characters?

Although it might seem like the obvious solution, you cannot split a statement into multiple lines simply by entering a carriage return. For example, the following code snippet returns a run-time error in Python because a statement was split by using <kbd>Enter</kbd>.

```python
  message= 'This message will generate an error because
  it was split by using the enter button on your
  keyboard'
```


You cannot split a statement into multiple lines in Python by pressing <kbd>Enter</kbd>. Instead, use the backslash (`\`) to indicate that a statement is continued on the next line.  In the revised version of the script, a blank space and an underscore indicate that the statement that was started on line 1 is continued on line 2.  To make it more apparent that line 2 is a continuation of line 1, line 2 is also indented four spaces.  (This was done for the sake of readability, but you do not have to indent continued lines. )

```python
message\
=\
'This \
back slash \
acts \
like \
enter'
print\
message
```

```python
message\
=\
'''triple
quotes
will
span
multiple lines
without
errors'''
print\
message
```

Line continuation is automatic when the split comes while a statement is inside parenthesis ( ( ), brackets ( [ ) or braces ( { ).  This is convenient, but can also lead to errors if there is no closing Parenthesis, bracket or brace.  Python would interpret the rest of the script as one statement in that case.

Python uses single quotes (') double quotes (") and triple quotes (""") to denote literal strings.  Only the triple quoted strings (""") also will automatically continue across the end of line statement.

Sometimes, more than one statement may be put on a single line.  In Python a semicolon (;) can be used to separate multiple statements on the same line.  For instance three statements can be written:

```python
y = 3; x = 5; print(x+y)
```

To the Python interpreter, this would be the same set of statements:

```python
y = 3
x = 5
print(x+y)
```
