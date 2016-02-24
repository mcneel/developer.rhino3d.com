---
title: Adjusting Clipping Planes from Conduits
description: This brief guide discusses adjusting clipping planes from display conduits using C/C++.
author: dale@mcneel.com
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Advanced']
origin: http://wiki.mcneel.com/developer/sdksamples/conduitboundingbox
order: 1
keywords: ['rhino', 'display', 'conduit']
layout: toc-guide-page
---

# Adjusting Clipping Planes from Conduits

{{ page.description }}

## Overview

You may reason that it is necessary to change Rhino's Z-Buffer range because when you draw using the `CRhinoDisplayConduit` class, as objects that are far from Rhino's objects are being clipped.  However, the Z-Buffer range has nothing to do with whether or not objects get culled, or clipped, from the viewing frustum.  This behavior has to do with Rhino's near and far clipping planes.  Rhino's clipping planes are adjusted dynamically in order to maximize the precision within the Z-Buffer.  Additionally, Rhino does this by placing the near plane as close to the closest visible object in the frustum, and the far plane as far as the furthest visible object in the frustum.

If you are adding or drawing objects that Rhino does not know about - that are not in the drawing database - then they will not be included in those calculations.  Thus, you must also implement the `SC_CALCBOUNDINGBOX` channel inside your conduit and add to the overall scene bounding box.  This will make Rhino adjust its clipping planes to include your objects.  For example...

## Example

```cpp
class CTestDisplayConduit : public CRhinoDisplayConduit
{
public:
  CTestDisplayConduit();

  bool ExecConduit(
    CRhinoDisplayPipeline& dp,
    UINT nChannel,
    bool& bTerminate
    );

  // TODO: add other methods and members here
};

CTestDisplayConduit::CTestDisplayConduit()
: CRhinoDisplayConduit(CSupportChannels::SC_PREDRAWOBJECTS|CSupportChannels::SC_CALCBOUNDINGBOX)
{
  // TODO: initialize members here
}

bool CTestDisplayConduit::ExecConduit(
    CRhinoDisplayPipeline& dp,
    UINT nChannel,
    bool& bTerminate
    )
{
  switch( nChannel )
  {
    case CSupportChannels::SC_CALCBOUNDINGBOX:
    {
      m_pChannelAttrs->m_BoundingBox.Union( /*YOUR_OBJECTS_BOUNDING_BOXES*/ );
      break;
    }
    case CSupportChannels::SC_PREDRAWOBJECTS:
    {
      // TODO: add drawing code here
      break;
    }
  }
  return true;
}
```
