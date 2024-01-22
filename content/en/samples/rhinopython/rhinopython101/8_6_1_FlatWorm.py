import rhinoscriptsyntax as rs


def FlatWorm():
    curve_object = rs.GetObject("Pick a backbone curve", 4, True, False)
    if not curve_object: return

    samples = rs.GetInteger("Number of cross sections", 100, 5)
    if not samples: return

    bend_radius = rs.GetReal("Bend plane radius", 0.5, 0.001)
    if not bend_radius: return

    perp_radius = rs.GetReal("Ribbon plane radius", 2.0, 0.001)
    if not perp_radius: return

    crvdomain = rs.CurveDomain(curve_object)

    crosssections = []
    t_step = (crvdomain[1]-crvdomain[0])/samples
    t = crvdomain[0]
    while t<=crvdomain[1]:
        crvcurvature = rs.CurveCurvature(curve_object, t)
        crosssectionplane = None
        if not crvcurvature:
            crvPoint = rs.EvaluateCurve(curve_object, t)
            crvTangent = rs.CurveTangent(curve_object, t)
            crvPerp = (0,0,1)
            crvNormal = rs.VectorCrossProduct(crvTangent, crvPerp)
            crosssectionplane = rs.PlaneFromFrame(crvPoint, crvPerp, crvNormal)
        else:
            crvPoint = crvcurvature[0]
            crvTangent = crvcurvature[1]
            crvPerp = rs.VectorUnitize(crvcurvature[4])
            crvNormal = rs.VectorCrossProduct(crvTangent, crvPerp)
            crosssectionplane = rs.PlaneFromFrame(crvPoint, crvPerp, crvNormal)

        if crosssectionplane:
            csec = rs.AddEllipse(crosssectionplane, bend_radius, perp_radius)
            crosssections.append(csec)
        t += t_step

    if not crosssections: return
    rs.AddLoftSrf(crosssections)
    rs.DeleteObjects(crosssections)


if __name__=="__main__":
    FlatWorm()