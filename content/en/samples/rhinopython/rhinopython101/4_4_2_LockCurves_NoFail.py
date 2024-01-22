import rhinoscriptsyntax as rs

def lockcurves_nofail():
    curves = rs.ObjectsByType(4)
    if not curves: return False
    rs.LockObjects(curves)
    return True


if __name__=="__main__":
    lockcurves_nofail()