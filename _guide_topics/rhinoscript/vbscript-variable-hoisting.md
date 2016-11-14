---
title: VBScript Variable Hoisting
description: This guides discusses variable scoping and hoisting in VBScript.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Fundamentals']
origin: http://wiki.mcneel.com/developer/scriptsamples/hoisting
order: 3
keywords: ['script', 'Rhino', 'vbscript']
layout: toc-guide-page
---

 
## Problem

Consider the following VBScript code, which does not work:

```vbnet
Option Explicit
s = "Hello"
```

Now, consider the following working code:

```vbnet
Option Explicit
s = "Hello"
Dim s
```

Why can a variable be used before declaring it in VBScript?

## Solution

Consider this code:

```vbnet
Dim s
s = Foo(123)

Function Foo(x)
  Foo = x + 345
End Function
```

Here the function is being used before it is declared.  Similarly, variables can be used before they are declared. The behaviour is by design.  Variable declarations and functions are logically "hoisted" to the top of their scope in VBScript.

Also, declaring a variable twice in the same script block is illegal, but redefinition in another block is legal.  Procedures may be redeclared at will except if the procedure is in a class, in which case redeclaration is illegal.

The following is legal in VBScript:

```vbnet
s = Foo(123)
If Blah Then
  Function Foo(x)
    Foo = x + 345
  End Function
End If
```

## Details

This is not recommended, but it *is* legal:

```vbnet
Dim i
For i = 1 To 2
  Rhino.Print c
Next
Const c = 10
```

And this works too:

```vbnet
For i = 1 To 2
  Rhino.Print c
  Dim i
Next
Const c = 10
```

But, this fails with a "name redefined" error:

```vbnet
For i = 1 To 2
  Rhino.Print c
  Const c = 10
  Dim i
Next
```

In conclusion, in VBScript:

- Variable declarations are logically hoisted to the top of the scope.
- Constants are evaluated at code compilation time; the constants' values are injected into the code.
