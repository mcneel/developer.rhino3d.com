import rhinoscriptsyntax as rs

def iterativeshortencurve():
    curve_id = rs.GetObject("Open curve to smooth", 4, True)
    if curve_id is None or rs.IsCurveClosed(curve_id): return
    
    min = rs.Distance(rs.CurveStartPoint(curve_id), rs.CurveEndPoint(curve_id))
    max = rs.CurveLength(curve_id)
    goal = rs.GetReal("Goal length", 0.5*(min+max) , min, max)
    if goal is None: return

    while rs.CurveLength(curve_id)>goal:
        rs.EnableRedraw(False)
        curve_id = smoothcurve(curve_id, 0.1)
        rs.EnableRedraw(True)
        if curve_id is None: break


def smoothcurve(curve_id, s):
    curve_points = rs.CurvePoints(curve_id)
    new_curve_points = []

    new_curve_points.append(curve_points[0])
    for i in range(1, len(curve_points)-1):
        vm = smoothingvector(curve_points[i], curve_points[i-1], curve_points[i+1], s)
        new_curve_points.append( rs.PointAdd(curve_points[i], vm) )
    new_curve_points.append(curve_points[-1])

    knots = rs.CurveKnots(curve_id)
    degree = rs.CurveDegree(curve_id)
    weights = rs.CurveWeights(curve_id,0)
    newcurve_id = rs.AddNurbsCurve(new_curve_points, knots, degree, weights)
    if newcurve_id: rs.DeleteObject(curve_id)
    return newcurve_id


def smoothingvector(point, prev_point, next_point, s):
    pm = (prev_point+next_point)/2.0
    va = rs.VectorCreate(pm, point)
    vm = rs.VectorScale(va, s)
    return vm


if __name__=="__main__":
    iterativeshortencurve()
