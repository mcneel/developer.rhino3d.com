import rhinoscriptsyntax as rs

def equidistanceoffset():
    srf_id = rs.GetObject("Pick surface to offset", 8, True, True)
    if not srf_id: return

    offset = rs.GetReal("Offset distance", 1.0, 0.0)
    if not offset: return

    udomain = rs.SurfaceDomain(srf_id, 0)
    ustep = (udomain[1]-udomain[0])/200
    rs.EnableRedraw(False)

    offsetvertices = []
    u = udomain[0]
    while u<=(udomain[1]+0.5*ustep):
        isocurves = rs.ExtractIsoCurve(srf_id, (u,0), 1)
        if isocurves:
            t = BSearchCurve(isocurves[0], offset, 0.001)
            if t is not None:
                offsetvertices.append(rs.EvaluateCurve(isocurves[0], t))
            rs.DeleteObjects(isocurves)
        u+=ustep
        
    if offsetvertices: rs.AddInterpCrvOnSrf(srf_id, offsetvertices)
    rs.EnableRedraw(True)


def BSearchCurve(idCrv, Length, Tolerance):
    Lcrv = rs.CurveLength(idCrv)
    if Lcrv<Length: return

    tmin = rs.CurveDomain(idCrv)[0]
    tmax = rs.CurveDomain(idCrv)[1]
    t0 = tmin
    t1 = tmax
    while True:
        t = 0.5*(t1+t0)
        Ltmp = rs.CurveLength(idCrv, 0, [tmin, t])
        if abs(Ltmp-Length)<Tolerance: return t

        if Ltmp<Length: t0=t
        else: t1 = t


if __name__=="__main__":
    equidistanceoffset()
