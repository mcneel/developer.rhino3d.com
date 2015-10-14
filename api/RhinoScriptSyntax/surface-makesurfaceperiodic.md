---
layout: bootstrap
---

# MakeSurfacePeriodic

Makes an existing surface a periodic NURBS surface
        Paramters:
          surface_id = the surface's identifier
          direction = The direction to make periodic, either 0=U or 1=V
          delete_input[opt] = delete the input surface
        Returns:
          if delete_input is False, identifier of the new surface
          if delete_input is True, identifer of the modifier surface
          None on error
        


