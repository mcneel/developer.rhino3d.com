---
layout: bootstrap
---

# FairCurve

Fairs a curve. Fair works best on degree 3 (cubic) curves. Fair attempts
        to remove large curvature variations while limiting the geometry changes to
        be no more than the specified tolerance. Sometimes several applications of
        this method are necessary to remove nasty curvature problems.
        

### Parameters:

- ***curve_id*** = curve to fair
- ***tolerance[opt]*** = fairing tolerance
        

### Returns:


True or False indicating success or failure
        
