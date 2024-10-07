+++
aliases = ["/en/5/samples/cpp/add-arrowheads-to-curves/", "/en/6/samples/cpp/add-arrowheads-to-curves/", "/en/7/samples/cpp/add-arrowheads-to-curves/", "/en/wip/samples/cpp/add-arrowheads-to-curves/"]
authors = [ "dale" ]
categories = [ "Adding Objects" ]
description = "Demonstrates how arrowheads can be added to any curve object my modifying attributes."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Add Arrowheads to Curves"
type = "samples/cpp"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/objectdecoration"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0
+++

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  // Define a line
  ON_Line line;
  line.from = ON_3dPoint(0, 0, 0);
  line.to = ON_3dPoint(10, 0, 0);

  // Make a copy of Rhino's default object attributes
  ON_3dmObjectAttributes attribs;
  context.m_doc.GetDefaultObjectAttributes( attribs );

  // Modify the object decoration style
  //attribs.m_object_decoration = ON::no_object_decoration;
  //attribs.m_object_decoration = ON::start_arrowhead;
  //attribs.m_object_decoration = ON::end_arrowhead;
  attribs.m_object_decoration = ON::both_arrowhead;

  // Create a new curve object with our attributes
  context.m_doc.AddCurveObject( line, &attribs );
  context.m_doc.Redraw();

  return CRhinoCommand::success;
}
```
