+++
authors = [ "dale" ]
categories = [ "Advanced" ]
description = "This guide discusses a problem when trying to calculate the length of a NURBS curve using C/C++."
keywords = [ "rhino", "NURBS", "curve", "length" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Calculating the Lengths of NURBS Curves"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/nurbscurvelength"
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

You may run into problems determining the length of an `ON_NurbsCurve` created by calling `ON_Curve::GetNurbForm`.  The following block of code only gets the length of the `ON_Curve` object, not the ON_NurbsCurve object.

```cpp
CRhinoCommand::result CCommandFooBar::RunCommand( const CRhinoCommandContext& context )
{
  CRhinoGetObject go;
  go.SetCommandPrompt( L"Select curve" );
  go.SetGeometryFilter( CRhinoGetObject::curve_object );
  go.GetObjects( 1, 1 );
  if( go.CommandResult() != success )
    return go.CommandResult();

  const ON_Curve* curve = go.Object(0).Curve();
  if( 0 == curve )
    return failure;

  double curve_length = 0.0;
  if( curve->GetLength(&curve_length) )
    RhinoApp().Print( L"ON_Curve::GetLength() = %g\n", curve_length );

  ON_NurbsCurve nurbs_curve;
  if( curve->GetNurbForm(nurbs_curve) )
  {
    double nurbs_curve_length = 0.0;
    if( nurbs_curve.GetLength(&nurbs_curve_length) )
      RhinoApp().Print( L"ON_NurbsCurve::GetLength() = %g\n", nurbs_curve_length );
  }

  return success;
}
```

What is going wrong?

## Solution

There is nothing wrong with the code above.  Rather, this exposes a flaw in Microsoft Visual C++ and the way it deals with stack variables with modified *vtables*.  The problem might sound complicated, but the solution is rather easy.  Just make a simple function that you can pass your `ON_NurbsCurve` object to that will calculate the curve length for you.  For example, the function below should work for most developers:

```cpp
BOOL ON_NurbsCurve_GetLength(
        const ON_NurbsCurve& curve,
        double* length,
        double fractional_tolerance = 1.0e-8,
        const ON_Interval* sub_domain = NULL
        )
{
  return curve.GetLength( length, fractional_tolerance, sub_domain );
}
```

Then, your code would look like this:

```cpp
CRhinoCommand::result CCommandFooBar::RunCommand( const CRhinoCommandContext& context )
{
  CRhinoGetObject go;
  go.SetCommandPrompt( L"Select curve" );
  go.SetGeometryFilter( CRhinoGetObject::curve_object );
  go.GetObjects( 1, 1 );
  if( go.CommandResult() != success )
    return go.CommandResult();

  const ON_Curve* curve = go.Object(0).Curve();
  if( 0 == curve )
    return failure;

  double curve_length = 0.0;
  if( curve->GetLength(&curve_length) )
    RhinoApp().Print( L"ON_Curve::GetLength() = %g\n", curve_length );

  ON_NurbsCurve nurbs_curve;
  if( curve->GetNurbForm(nurbs_curve) )
  {
    double nurbs_curve_length = 0.0;
    if( ON_NurbsCurve_GetLength(nurbs_curve, &nurbs_curve_length) )
      RhinoApp().Print( L"ON_NurbsCurve::GetLength() = %g\n", nurbs_curve_length );
  }

  return success;
}
```
