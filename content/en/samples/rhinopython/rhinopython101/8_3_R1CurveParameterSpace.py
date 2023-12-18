import rhinoscriptsyntax as rs

def main():
    curve_id = rs.GetObject("Select a curve to sample", 4, True, True)
    if not curve_id: return
    
    rs.EnableRedraw(False)
    t = 0
    while t<=1.0:
        addpointat_r1_parameter(curve_id,t)
        t+=0.002
    rs.EnableRedraw(True)


def parametercolor(parameter):
    red = 255 * parameter
    if red<0: red=0
    if red>255: red=255
    return (red,0,255-red)


def addpointat_r1_parameter(curve_id, parameter):
    domain = rs.CurveDomain(curve_id)
    if not domain: return
    
    r1_param = domain[0] + parameter*(domain[1]-domain[0])
    r3point = rs.EvaluateCurve(curve_id, r1_param)
    if r3point:
        point_id = rs.AddPoint(r3point)
        rs.ObjectColor(point_id, parametercolor(parameter))


if __name__=="__main__":
    main()
