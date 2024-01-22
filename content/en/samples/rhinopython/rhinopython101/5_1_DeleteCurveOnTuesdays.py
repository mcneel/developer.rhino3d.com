import rhinoscriptsyntax as rs
import datetime


def deletecurvesontuesdays():
    object_id = rs.GetObject("Select an object to delete on tuesdays", 0, True, True)
    if object_id is None: return

    if rs.IsCurve(object_id):
        if rs.CurveLength(object_id)<1.0:
            if rs.IsCurveClosed(object_id):
                now = datetime.datetime.now()
                if now.weekday()==1:
                    rs.DeleteObject(object_id)
                else:
                    print("This software is a tryout version and runs only on Tuesdays.")
                    print("Please purchase the full product.")
            else:
                print("Curve was not closed")
        else:
            print("Curve was too long")
    else:
        print("Object was not a curve")


if __name__=="__main__":
    deletecurvesontuesdays()