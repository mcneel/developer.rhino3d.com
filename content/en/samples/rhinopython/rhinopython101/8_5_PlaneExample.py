import rhinoscriptsyntax as rs

def planeexample():
    ptOrigin = rs.GetPoint("Plane origin")

    ptX = rs.GetPoint("Plane X-axis", ptOrigin)

    ptY = rs.GetPoint("Plane Y-axis", ptOrigin)

    dX = rs.Distance(ptOrigin, ptX)
    dY = rs.Distance(ptOrigin, ptY)
    arrPlane = rs.PlaneFromPoints(ptOrigin, ptX, ptY)

    rs.AddPlaneSurface(arrPlane, 1.0, 1.0)
    rs.AddPlaneSurface(arrPlane, dX, dY)


if __name__=="__main__":
    planeexample()