# Draw a sine wave using points
import rhinoscriptsyntax as rs
import math

def drawsinewave():
    a = -8.0
    b = 8.0
    step = 0.25
    x = a
    while x<=b:
        y = 2*math.sin(x)
        rs.AddPoint( (x,y,0) )
        x += step


if __name__=="__main__":
    drawsinewave()