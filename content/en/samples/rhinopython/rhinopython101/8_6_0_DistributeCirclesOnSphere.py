import rhinoscriptsyntax as rs
import math


def DistributeCirclesOnSphere():
    sphere_radius = rs.GetReal("Radius of sphere", 10.0, 0.01)
    if not sphere_radius: return

    circle_radius = rs.GetReal("Radius of packing circles", 0.05*sphere_radius, 0.001, 0.5*sphere_radius)
    if not circle_radius: return

    vertical_count = int( (math.pi*sphere_radius)/(2*circle_radius) )

    rs.EnableRedraw(False)
    phi = -0.5*math.pi
    phi_step = math.pi/vertical_count
    while phi<0.5*math.pi:
        horizontal_count = int( (2*math.pi*math.cos(phi)*sphere_radius)/(2*circle_radius) )
        if horizontal_count==0: horizontal_count=1
        theta = 0
        theta_step = 2*math.pi/horizontal_count
        while theta<2*math.pi-1e-8:
            circle_center = (sphere_radius*math.cos(theta)*math.cos(phi), sphere_radius*math.sin(theta)*math.cos(phi), sphere_radius*math.sin(phi))
            circle_normal = rs.PointSubtract(circle_center, (0,0,0))
            circle_plane = rs.PlaneFromNormal(circle_center, circle_normal)
            rs.AddCircle(circle_plane, circle_radius)
            theta += theta_step
        phi += phi_step
    rs.EnableRedraw(True)


if __name__=="__main__":
    DistributeCirclesOnSphere()