---
layout: toc-guide-page
title: VBScript Conditionals
author: dale@mcneel.com
categories: ['Basics']
platforms: ['Windows']
apis: ['RhinoScript']
languages: ['VBScript']
keywords: ['script', 'Rhino', 'vbscript']
TODO: 0
origin: http://wiki.mcneel.com/developer/vbsconditional
order: 1
---

# VBScript Conditionals

This guide is an survey of VBScript conditional statements.

## Overview

You can control the flow of your script with conditional statements and looping statements.  Using conditional statements, you can write VBScript code that makes decisions and repeats actions.  The following conditional statements are available in VBScript:

- `If`...`Then`...`Else` statement
- `Select Case` statement

## If Then Else

The `If`...`Then`...`Else` statement is used to evaluate whether a condition is True or False and, depending on the result, to specify one or more statements to run.  Usually the condition is an expression that uses a comparison operator to compare one value or variable with another.  For information about comparison operators, see the [VBScript Operators]({{ site.baseurl }}/guides/rhinoscript/vbscript_operators) guide.  `If`...`Then`...`Else` statements can be nested to as many levels as you need.

### If True

To run only one statement when a condition is True, use the single-line syntax for the `If`...`Then`...`Else` statement.  The following example shows the single-line syntax.  Notice that this example omits the `Else` keyword...

```vbnet
Sub FixDate()
  Dim myDate
  myDate = #11/17/2008#
  If myDate < Now Then myDate = Now
End Sub
```

To run more than one line of code, you must use the multiple-line (or block) syntax.  This syntax includes the `End If` statement, as shown in the following example:

```vbnet
Sub AlertUser(value)
  If value = 0 Then
    MyLayerColor = vbRed
    MyObjectColor = vbBlue
  End If
End Sub
```

### Some True Some False

You can use an `If`...`Then`...`Else` statement to define two blocks of executable statements: one block to run if the condition is True, the other block to run if the condition is False...

```vbnet
Sub AlertUser(value)
  If value = 0 Then
    MyLayerColor = vbRed
    MyObjectColor = vbBlue
  Else
    MyLayerColor = vbGreen
    MyObjectColor = vbBlack
  End If
End Sub
```

### Several Alternatives

A variation on the `If`...`Then`...`Else` statement allows you to choose from several alternatives.  Adding `ElseIf` clauses expands the functionality of the `If`...`Then`...`Else` statement so you can control program flow based on different possibilities.  For example:

```vbnet
Sub ReportValue(value)
  If value = 0 Then
    MsgBox value
  ElseIf value = 1 Then
    MsgBox value
  ElseIf value = 2 then
    Msgbox value
  Else
    Msgbox "Value out of range!"
  End If
End Sub
```

You can add as many `ElseIf` clauses as you need to provide alternative choices.  Extensive use of the `ElseIf` clauses often becomes cumbersome.  A better way to choose between several alternatives is the `Select Case` statement.

## Select Case

The `Select Case` structure provides an alternative to `If`...`Then`...`Else` for selectively executing one block of statements from among multiple blocks of statements.  A `Select Case` statement provides capability similar to the `If`...`Then`...`Else` statement, but it makes code more efficient and readable.

A `Select Case` structure works with a single test expression that is evaluated once, at the top of the structure. The result of the expression is then compared with the values for each `Case` in the structure.  If there is a match, the block of statements associated with that `Case` is executed, as in the following example...

```vbnet
Select Case MyVar
  Case "red"     MyColor = vbRed
  Case "green"   MyColor = vbGreen
  Case "blue"    MyColor = vbBlue
  Case Else      MsgBox "Pick another color."
End Select
```

Notice that the `Select Case` structure evaluates an expression once at the top of the structure.  In contrast, the `If`...`Then`...`Else` structure can evaluate a different expression for each `ElseIf` statement.  You can replace an `If`...`Then`...`Else` structure with a `Select Case` structure only if each `ElseIf` statement evaluates the same expression.

---

## Related Topics

- [What are VBScript and RhinoScript?]({{ site.baseurl }}/guides/rhinoscript/what_are_vbscript_rhinoscript)
- [VBScript Operators]({{ site.baseurl }}/guides/rhinoscript/vbscript_operators)
