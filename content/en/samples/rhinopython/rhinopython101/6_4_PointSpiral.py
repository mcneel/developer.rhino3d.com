import rhinoscriptsyntax as rs
import math


def pointspiral():
    t = -5
    while t<=5:
        point = t*math.sin(5*t), t*math.cos(5*t), t
        print(point)
        rs.AddPoint(point)
        t+=0.025


if __name__=="__main__":
    pointspiral()