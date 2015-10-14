---
layout: bootstrap
---

# ObjectsByType

Returns identifiers of all objects based on the objects' geometry type.
        

### Parameters:

- ***geometry_type*** = The type(s) of geometry objects (points, curves, surfaces,
       meshes, etc.) that can be selected. Object types can be
       added together to filter several different kinds of geometry.
        Value        Description
         0           All objects
         1           Point
         2           Point cloud
         4           Curve
         8           Surface or single-face brep
         16          Polysurface or multiple-face
         32          Mesh
         256         Light
         512         Annotation
         4096        Instance or block reference
         8192        Text dot object
         16384       Grip object
         32768       Detail
         65536       Hatch
         131072      Morph control
         134217728   Cage
         268435456   Phantom
         536870912   Clipping plane
- ***select[opt]*** = Select the objects
- ***state[opt]*** = Object state. See help
        

### Returns:


A list of Guids identifying the objects.
        
