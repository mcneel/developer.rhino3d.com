---
title: VBScript Code Conventions
description: This guide provides an overview of VBScript coding conventions.
author: dale@mcneel.com
apis: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Fundamentals']
origin: http://wiki.mcneel.com/developer/vbsconventions
order: 100
keywords: ['script', 'Rhino', 'vbscript']
layout: toc-guide-page
---

# VBScript Code Conventions

{{ page.description }}

## Overview

Coding conventions are suggestions designed to help you write VBScript and RhinoScript code.  Coding conventions can include the following:

- Naming conventions for objects, variables, and procedures
- Commenting conventions
- Text formatting and indenting guidelines

The main reason for using a consistent set of coding conventions is to standardize the structure and coding style of a script or set of scripts so that you and others can easily read and understand the code.  Using good coding conventions results in clear, precise, and readable source code that is consistent with other language conventions and is intuitive.

## Constant Naming

Earlier versions of VBScript had no mechanism for creating user-defined constants.  Constants, if used, were implemented as variables and distinguished from other variables using all uppercase characters.  Multiple words were separated using the underscore `_` character.  For example:

```vbnet
USER_LIST_MAX
NEW_LINE
```

While this is still an acceptable way to identify your constants, you may want to use an alternative naming scheme now that you can create true constants using the `Const` statement.  This convention uses a mixed-case format in which constant names have a "con" prefix.  For example:

```vbnet
conYourOwnConstant
```

## Variable Naming

To enhance readability and consistency, use the following prefixes with descriptive names for variables in your VBScript code:

| Subtype | | | |  Prefix | | | | Example |
|:--------|:-:|:-:|:-:|:--------|:-:|:-:|:-:|:--------|
| Array   | | | | arr   | | | | `arrLayers`   |
| Boolean   | | | | bln   | | | | `blnFound`   |
| Byte   | | | | byt   | | | | `bytRasterData`   |
| Date (Time)   | | | | dtm   | | | | `dtmStart`   |
| Double   | | | | dbl   | | | | `dblTolerance`   |
| Error   | | | | err   | | | | `errOrderNum`   |
| Integer   | | | | int   | | | | `intQuantity`   |
| Long   | | | | lng   | | | | `lngDistance`   |
| Object   | | | | obj   | | | | `objCurrent`   |
| Single   | | | | sng   | | | | `sngAverage`   |
| String   | | | | str   | | | | `strFirstName`   |
|=====
|
{: rules="groups"}

## Variable Scope

Variables should always be defined with the smallest scope possible.  VBScript variables can have the following scope:

| Scope | | | |  Where Variable Is Declared | | | | Visibility |
|:--------|:-:|:-:|:-:|:--------|:-:|:-:|:-:|:--------|
| Procedure-level   | | | | Event, Function, or Sub procedure.   | | | | Visible in the procedure in which it is declared.   |
| Script-level   | | | | Outside any procedure.   | | | | Visible in every procedure in the script.   |
|=====
|
{: rules="groups"}

### Variable Scope Prefixes

As script size grows, so does the value of being able to quickly differentiate the scope of variables.  A one-letter scope prefix preceding the type prefix provides this, without unduly increasing the size of variable names.

| Scope | | | |  Prefix | | | | Example |
|:--------|:-:|:-:|:-:|:--------|:-:|:-:|:-:|:--------|
| Procedure-level   | | | | None   | | | | `dblVelocity`   |
| Script-level   | | | | s   | | | | `sblnCalcInProgress`   |
|=====
|
{: rules="groups"}

## Descriptive Names

The body of a variable or procedure name should use mixed case and should be as descriptive as necessary.  Also, procedure names should begin with a verb, such as `InitNameArray` or `ValidateLayer`.

For frequently used or long terms, standard abbreviations are recommended to help keep name length reasonable.  In general, variable names greater than 32 characters can be difficult to read.  When using abbreviations, make sure they are consistent throughout the entire script.  For example, randomly switching between `Cnt` and `Count` within a script or set of scripts may lead to confusion.

## Code Commenting

All procedures should begin with a brief comment describing what they do.  This description should not describe the implementation details (how it does it) because these often change over time, resulting in unnecessary comment maintenance work, or worse, erroneous comments.  The code itself and any necessary inline comments describe the implementation.

Arguments passed to a procedure should be described when their purpose is not obvious and when the procedure expects the arguments to be in a specific range.  Return values for functions and variables that are changed by a procedure, especially through reference arguments, should also be described at the beginning of each procedure.

Procedure header comments should include the following section headings:

| Heading | | | |  Comment Contents |
|:--------|:-:|:-:|:-:|:--------|
| Purpose   | | | | What the procedure does (not how).   |
| Assumptions   | | | | List of any external variable, control, or other element whose state affects this procedure.   |
| Effects   | | | | List of the procedure's effect on each external variable, control, or other element.   |
| Inputs   | | | | Explanation of each argument that is not obvious. Each argument should be on a separate line with inline comments.   |
| Return Values   | | | | Explanation of the value returned.   |
|=====
|
{: rules="groups"}

Remember the following points:

- Every important variable declaration should include an inline comment describing the use of the variable being declared.
- Variables, controls, and procedures should be named clearly to ensure that inline comments are only needed for complex implementation details.
- At the beginning of your script, you should include an overview that describes the script, enumerating objects, procedures, algorithms, dialog boxes, and other system dependencies.  Sometimes a piece of pseudocode describing the algorithm can be helpful.

## Code Formatting

Screen space should be conserved as much as possible, while still allowing code formatting to reflect logic structure and nesting.  Here are a few suggestions:

- Indent standard nested blocks two spaces.
- Indent the overview comments of a procedure one space.
- Indent the highest level statements that follow the overview comments two spaces, with each nested block indented an additional two spaces.

## In Sum

The following code adheres to VBScript coding conventions:

```vbnet
'****************************************************
' Purpose: Locates the first occurrence of a specified
'          layer in the LayerList array.
' Inputs:  arrLayerList: the list of layers to be searched.
'          strTargetLayer: the name of the layer to search for.
' Returns: The index of the first occurrence of the
'          strTargetLayer in the strLayerList array.
'          If the target layer is not found, return -1.
'****************************************************

Option Explicit

Function FindLayer(arrLayerList, strTargetLayer)
  Dim i          ' Loop counter.
  Dim blnFound   ' Target found flag
  FindLayer = -1 ' Default return value
  i = 0          ' Initialize loop counter
  Do While i <= UBound(arrLayerList) And Not blnFound
    If arrLayerList(i) = strTargetLayer Then
      blnFound = True ' Set flag to True
      FindLayer = i   ' Set return value to loop count
    End If
    i = i + 1         ' Increment loop counter
  Loop
End Function
```

---

## Related Topics

- [What are VBScript and RhinoScript?]({{ site.baseurl }}/guides/rhinoscript/what_are_vbscript_rhinoscript)
