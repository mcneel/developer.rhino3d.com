---
layout: bootstrap
---

# FilletSurfaces

Create constant radius rolling ball fillets between two surfaces. Note,
        this function does not trim the original surfaces of the fillets
        

### Parameters:

surface0, surface1 = identifiers of first and second surface
- ***radius*** = a positive fillet radius
- ***uvparam0[opt]*** = a u,v surface parameter of surface0 near where the fillet
  is expected to hit the surface
- ***uvparam1[opt]*** = same as uvparam0, but for surface1
        

### Returns:


ids of surfaces created on success
None on error
        
