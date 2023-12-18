# This script will compute a bunch of cross-product vector based on a pointcloud
import rhinoscriptsyntax as rs


def vectorfield():
    cloud_id = rs.GetObject("Input pointcloud", 2, True, True)
    if cloud_id is None: return

    points = rs.PointCloudPoints(cloud_id)
    base_point = rs.GetPoint("Vector field base point")
    if base_point is None: return

    for point in points:
        vecbase = rs.VectorCreate(point, base_point)
        vecdir = rs.VectorCrossProduct(vecbase, (0,0,1))
        if vecdir:
            vecdir = rs.VectorUnitize(vecdir)
            vecdir = rs.VectorScale(vecdir, 2.0)
            AddVector(vecdir, point)


def AddVector(vecdir, base_point):
    tip_point = rs.PointAdd(base_point, vecdir)
    line = rs.AddLine(base_point, tip_point)
    if line: rs.CurveArrows(line, 2)


if __name__=="__main__":
    vectorfield()