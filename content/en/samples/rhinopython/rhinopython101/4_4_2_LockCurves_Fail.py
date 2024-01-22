#Try running this script on an empty file, it will crash.
import rhinoscriptsyntax as rs

def lockcurves_fail():
    rs.LockObjects(rs.ObjectsByType(4))


if __name__=="__main__":
    lockcurves_fail()