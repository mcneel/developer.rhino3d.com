+++
aliases = ["/en/5/guides/cpp/changing-display-precision/", "/en/6/guides/cpp/changing-display-precision/", "/en/7/guides/cpp/changing-display-precision/", "/wip/guides/cpp/changing-display-precision/"]
authors = [ "dale" ]
categories = [ "Advanced" ]
description = "This brief guide demonstrates how to change the unit's display precision of the current document using C/C++."
keywords = [ "rhino", "display", "precision" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Changing Display Precision"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/displayprecision"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++

 
## Problem

Rhino has a document display precision - the "display precision" option found in the *Units* page in the *Options* dialog.  Imagine you want to modify this using C/C++ from your plugin.

## Solution

A document's display precision, the number of decimal places used for the distance display, is maintained on an `ON_3dmUnitsAndTolerances` object, which in turn is stored on a `CRhinoDocProperties` object which is a member of the current `CRhinoDoc` object.  To modify this variable, you will need to:

1. Make a copy of the document's `ON_3dmUnitsAndTolerances` object.
1. Modify the object's `m_distance_display_precision` member variable.
1. Replace the current `ON_3dmUnitsAndTolerances` with the newly modified one.

## Sample

The following sample code demonstrates how to change the unit's display precision of the current document using the Rhino C/C++ SDK...

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  // Make a copy of the current model units and tolerances
  ON_3dmUnitsAndTolerances units = context.m_doc.Properties().ModelUnitsAndTolerances();

  // Prompt the user to enter a new display precision value
  CRhinoGetInteger gi;
  gi.SetCommandPrompt( L"New display precision" );
  gi.SetDefaultInteger( units.m_distance_display_precision );
  gi.SetLowerLimit( 0 );
  gi.SetUpperLimit( 6 );
  gi.GetInteger();
  if( gi.CommandResult() == CRhinoCommand::success )
  {
    // The the user's input
    int distance_display_precision = gi.Number();
    if( distance_display_precision != units.m_distance_display_precision )
    {
      units.m_distance_display_precision = distance_display_precision;
      // Replace the current setting with our updated value
      context.m_doc.Properties().SetModelUnitsAndTolerances( units, false );
    }
  }

  return CRhinoCommand::success;
}
```
