import rhinoscriptsyntax as rs

def planeexample():
    origin = rs.GetPoint("Plane origin")
    if not origin: return

    ptX = rs.GetPoint("Plane X-axis", origin)
    if not ptX: return
    ptY = rs.GetPoint("Plane Y-axis", origin)
    if not ptY: return
	
    x = rs.Distance(origin, ptX)
    y = rs.Distance(origin, ptY)
    plane = rs.PlaneFromPoints(origin, ptX, ptY)
    rs.AddPlaneSurface(plane, 1.0, 1.0)
    rs.AddPlaneSurface(plane, x, y)


if __name__=="__main__":
    planeexample()