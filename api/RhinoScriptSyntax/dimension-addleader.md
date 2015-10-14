---
layout: bootstrap
---

# AddLeader

Adds a leader to the document. Leader objects are planar.
        The 3D points passed to this function should be co-planar
        Paramters:
          points = list of (at least 2) 3D points
          view_or_plane[opt] = If a view is specified, points will be constrained
            to the view's construction plane. If a view is not specified, points
            will be constrained to a plane fit through the list of points
          text[opt] = leader's text string
        Returns:
          identifier of the new leader on success
          None on error
        


