---
layout: bootstrap
---

# ExplodeCurves

Explodes, or un-joins, one curves. Polycurves will be exploded into curve
        segments. Polylines will be exploded into line segments. ExplodeCurves will
        return the curves in topological order. 
        

### Parameters:

- ***curve_ids*** = the curve object(s) to explode.
- ***delete_input[opt]*** = Delete input objects after exploding.
        

### Returns:


List identifying the newly created curve objects
        
