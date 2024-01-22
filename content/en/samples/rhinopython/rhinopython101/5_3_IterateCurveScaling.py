# Iteratively scale down a curve until it becomes shorter than a certain length
import rhinoscriptsyntax as rs


def fitcurvetolength():
    curve_id = rs.GetObject("Select a curve to fit to length", 4, True, True)
    if curve_id is None: return
    
    length = rs.CurveLength(curve_id)

    length_limit = rs.GetReal("Length limit", 0.5 * length, 0.01 * length, length)
    if length_limit is None: return

    while True:
        if rs.CurveLength(curve_id)<=length_limit: break
        curve_id = rs.ScaleObject(curve_id, (0,0,0), (0.95, 0.95, 0.95))
        if curve_id is None:
            print("Something went wrong...")
            return

    print("New curve length: ", rs.CurveLength(curve_id))


if __name__=="__main__":
    fitcurvetolength()