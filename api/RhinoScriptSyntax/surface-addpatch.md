---
layout: bootstrap
---

# AddPatch

Fits a surface through curve, point, point cloud, and mesh objects.
        

### Parameters:

- ***object_ids*** = a list of object identifiers that indicate the objects to use for the patch fitting. 
    Acceptable object types include curves, points, point clouds, and meshes.
- ***uv_spans_tuple_OR_surface_object_id*** =  the U and V direction span counts for the automatically generated surface OR 
    The identifier of the starting surface.  It is best if you create a starting surface that is similar in shape 
    to the surface you are trying to create.
- ***tolerance[opt]*** = The tolerance used by input analysis functions. If omitted, Rhino's document absolute tolerance is used.
- ***trim[opt]*** = Try to find an outside curve and trims the surface to it.  The default value is True.
- ***point_spacing[opt]*** = The basic distance between points sampled from input curves.  The default value is 0.1.
- ***flexibility[opt]*** = Determines the behavior of the surface in areas where its not otherwise controlled by the input.
    Lower numbers make the surface behave more like a stiff material, higher, more like a flexible material.  
    That is, each span is made to more closely match the spans adjacent to it if there is no input geometry 
    mapping to that area of the surface when the flexibility value is low.  The scale is logarithmic.  
    For example, numbers around 0.001 or 0.1 make the patch pretty stiff and numbers around 10 or 100 
    make the surface flexible.  The default value is 1.0.
- ***surface_pull[opt]*** = Similar to stiffness, but applies to the starting surface. The bigger the pull, the closer 
    the resulting surface shape will be to the starting surface.  The default value is 1.0.
- ***fix_edges[opt]*** = Clamps the edges of the starting surface in place. This option is useful if you are using a 
    curve or points for deforming an existing surface, and you do not want the edges of the starting surface 
    to move.  The default if False.
        

### Returns:


Identifier of the new surface object if successful.
None on error.
        
