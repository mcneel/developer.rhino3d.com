import rhinoscriptsyntax as rs

def createcurvaturegraph():
    curve_ids = rs.GetObjects("Curves for curvature graph", 4, False, True, True)
    if not curve_ids: return

    samples = 10
    scale = 1.0

    preview = []
    while True:
        rs.EnableRedraw(False)
        for p in preview: rs.DeleteObjects(p)
        preview = []
        for id in curve_ids:
            cg = addcurvaturegraph(id, samples, scale)
            preview.append(cg)
        rs.EnableRedraw(True)

        result = rs.GetString("Curvature settings", "Accept", ("Samples", "Scale", "Accept"))
        if not result:
            for p in preview: rs.DeleteObjects(p)
            break
        result = result.upper()
        if result=="ACCEPT": break
        elif result=="SAMPLES":
            numsamples = rs.GetInteger("Number of samples per knot-span", samples, 3, 100)
            if numsamples: samples = numsamples
        elif result=="SCALE":
            sc = rs.GetReal("Scale of the graph", scale, 0.01, 1000.0)
            if sc: scale = sc


def addcurvaturegraph( idCrv, spansamples, scale):
    allGeometry = []
    knots = rs.CurveKnots(idCrv)
    p=5
    for i in range(len(knots)-1):
        tmpGeometry = addcurvaturegraphsection(idCrv, knots[i], knots[i+1], spansamples, scale)
        if tmpGeometry: allGeometry.append(tmpGeometry)
    rs.AddObjectsToGroup(allGeometry, rs.AddGroup())
    return allGeometry


def addcurvaturegraphsection(idCrv, t0, t1, samples, scale):
    if (t1-t0)<=0.0: return
    N = -1
    tstep = (t1-t0)/samples
    t = t0
    points = []
    objects = []
    while t<=(t1+(0.5*tstep)):
        if t>=t1:t = t1-1e-10
        N += 1
        cData = rs.CurveCurvature(idCrv, t)
        if not cData:
            points.append( rs.EvaluateCurve(idCrv, t) )
        else:
            c = rs.VectorScale(cData[4], scale)
            a = cData[0]
            b = rs.VectorSubtract(a, c)
            objects.append(rs.AddLine(a,b))
            points.append(b)
        t += tstep

    objects.append(rs.AddInterpCurve(points))
    return objects


if __name__=="__main__":
    createcurvaturegraph()
