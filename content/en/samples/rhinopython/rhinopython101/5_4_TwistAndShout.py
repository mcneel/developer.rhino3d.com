import rhinoscriptsyntax as rs
import math


def twistandshout():
    twist_angle = 0.0
    rs.EnableRedraw(False)
    z = 0
    while z<=5:
        twist_angle += math.pi/30
        a = 0
        while a<2*math.pi:
            x = 5 * math.sin(a + twist_angle)
            y = 5 * math.cos(a + twist_angle)
            rs.AddSphere((x,y,z), 0.5)
            a += math.pi/15
        z += 0.5
    rs.EnableRedraw(True)


if __name__=="__main__":
    twistandshout()