import rhinoscriptsyntax as rs

def WhoFramedTheSurface():
    surface_id = rs.GetObject("Surface to frame", 8, True, True)
    if not surface_id: return

    count = rs.GetInteger("Number of iterations per direction", 20, 2)
    if not count: return

    udomain = rs.SurfaceDomain(surface_id, 0)
    vdomain = rs.SurfaceDomain(surface_id, 1)
    ustep = (udomain[1] - udomain[0]) / count
    vstep = (vdomain[1] - vdomain[0]) / count

    rs.EnableRedraw(False)
    u = udomain[0]
    while u<=udomain[1]:
        v = vdomain[0]
        while v<=vdomain[1]:
            pt = rs.EvaluateSurface(surface_id, u, v)
            if rs.Distance(pt, rs.BrepClosestPoint(surface_id, pt)[0])<0.1:
                srf_frame = rs.SurfaceFrame(surface_id, [u, v])
                rs.AddPlaneSurface(srf_frame, 1.0, 1.0)
            v+=vstep
        u+=ustep
    rs.EnableRedraw(True)


if __name__=="__main__":
    WhoFramedTheSurface()