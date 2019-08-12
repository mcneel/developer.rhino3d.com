---
title: Add Arrowheads to Curves
description: Demonstrates how arrowheads can be added to any curve object my modifying attributes.
authors: ['dale_fugier']
sdk: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Adding Objects']
origin: http://wiki.mcneel.com/developer/sdksamples/objectdecoration
order: 1
keywords: ['rhino']
layout: code-sample-cpp
---

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
