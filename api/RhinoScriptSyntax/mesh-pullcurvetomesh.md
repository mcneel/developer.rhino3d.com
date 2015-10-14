---
layout: bootstrap
---

# PullCurveToMesh

Pulls a curve to a mesh. The function makes a polyline approximation of
        the input curve and gets the closest point on the mesh for each point on
        the polyline. Then it "connects the points" to create a polyline on the mesh
        Paramters:
          mesh_id = identifier of mesh that pulls
          curve_id = identifier of curve to pull
        Returns:
          Guid of new curve on success
          None on error
        


