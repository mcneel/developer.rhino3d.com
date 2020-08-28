---
title: Adding Command Line Options
description: This guide discusses how to add a different type of command line options to a custom command.
authors: ['dale_fugier']
sdk: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Fundamentals']
origin: http://wiki.mcneel.com/developer/sdksamples/commandlineoptions
order: 1
keywords: ['rhino']
layout: toc-guide-page
---

 
## Overview

The Rhino C/C++ SDK has a number of CRhinoGet derived classes that you can use to interactively get information from the user.  Some of these classes include:

- `CRhinoGetObject`: SDK user interface tool used to get objects.
- `CRhinoGetPoint`:  SDK user interface tool used to get points.
- `CRhinoGetString`: SDK user interface tool used to get strings.
- `CRhinoGetNumber`: SDK user interface tool used to get floating point values.
- `CRhinoGetInteger`: SDK user interface tool used to get integer values.
- `CRhinoGetAngle`: SDK user interface tool used to get angles.
- `CRhinoGetDistance`: SDK user interface tool used to get distances.
- `CRhinoGetOption`: SDK user interface tool used to get command line options.

Each `CRhinoGet` derived classes can, in addition to its primary function, prompt the user for additional options.  These options display on the command following the developer specified prompt, and appear as clickable hyperlinks.

## Sample

The following example code demonstrates how to add command line options to some user interaction.  In this example, we use the `CRhinoGetOption` class, which is only capable of displaying command line options.  But, we could have used any of the above `CRhinoGet` derived classes.

```cpp
CRhinoCommand::result CCommandTest::RunCommand(const CRhinoCommandContext& context)
{
  int nVal = 2;
  double dVal = 30.0;
  bool bVal = false;
  int list_index = 3;

  CRhinoCommandOptionValue list_items[5];
  list_items[0] = RHCMDOPTVALUE(L"Item0");
  list_items[1] = RHCMDOPTVALUE(L"Item1");
  list_items[2] = RHCMDOPTVALUE(L"Item2");
  list_items[3] = RHCMDOPTVALUE(L"Item3");
  list_items[4] = RHCMDOPTVALUE(L"Item4");

  CRhinoGetOption go;
  go.SetCommandPrompt(L"Command options");
  go.AcceptNothing();

  for (;;)
  {
    go.ClearCommandOptions();

    int nval_option_index = go.AddCommandOptionInteger(
      RHCMDOPTNAME(L"Integer"), &nVal, L"integer value", 1, 99
    );
    int dval_option_index = go.AddCommandOptionNumber(
      RHCMDOPTNAME(L"Double"), &dVal, L"double value", FALSE, 0.1, 99.9
    );
    int bval_option_index = go.AddCommandOptionToggle(
      RHCMDOPTNAME(L"Boolean"), RHCMDOPTVALUE(L"False"), RHCMDOPTVALUE(L"True"), bVal, &bVal
    );
    int list_option_index = go.AddCommandOptionList(
      RHCMDOPTNAME(L"List"), 5, list_items, list_index
    );
    int test_option_index = go.AddCommandOption(
      RHCMDOPTNAME(L"Test")
    );

    CRhinoGet::result res = go.GetOption();

    if (res == CRhinoGet::nothing)
      break;

    if (res == CRhinoGet::cancel)
      return CRhinoCommand::cancel;

    if (res != CRhinoGet::option)
      return CRhinoCommand::failure;

    const CRhinoCommandOption* option = go.Option();
    if (nullptr == option)
      return CRhinoCommand::failure;

    int option_index = option->m_option_index;

    if (option_index == nval_option_index)
      continue; // nothing to do

    if (option_index == dval_option_index)
      continue; // nothing to do

    if (option_index == bval_option_index)
      continue; // nothing to do

    if (option_index == list_option_index)
    {
      list_index = option->m_list_option_current;
      continue;
    }

    if (option_index == test_option_index)
    {
      // TODO...
    }
  }

  // TODO...

  return CRhinoCommand::success;
}
```
