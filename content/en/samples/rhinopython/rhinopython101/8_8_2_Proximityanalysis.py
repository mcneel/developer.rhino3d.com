#Script written by David Rutten and converted to python by Steve Baer
#Script copyrighted by Robert McNeel & Associates
#Script version 19 January 2011
import rhinoscriptsyntax as rs
import math

def ProximityAnalysis():
    mesh_id = rs.GetObject("Mesh for proximity analysis", 32, True, True)
    if not mesh_id: return

    brep_id = rs.GetObject("Surface for proximity test", 8+16, False, True)
    if not brep_id: return

    vertices = rs.MeshVertices(mesh_id)
    faces = rs.MeshFaceVertices(mesh_id)
    arrD = VertexValueArray(vertices, brep_id)
    minD = min(arrD)
    maxD = max(arrD)
    colors = []
    for i in range(len(vertices)):
        proxFactor = (arrD[i]-minD)/(maxD-minD)
        colors.append( (255, 255*proxFactor, 255*proxFactor) )
    rs.AddMesh(vertices, faces, vertex_colors=colors)
    rs.DeleteObject(mesh_id)


def VertexValueArray(points, id):
    return [DistanceTo(point, id) for point in points]

def DistanceTo(pt, id):
    ptCP = rs.BrepClosestPoint(id,pt)
    if ptCP:
        d = rs.Distance(pt, ptCP[0])
        return math.log10(d+1)


if __name__=="__main__":
    ProximityAnalysis()