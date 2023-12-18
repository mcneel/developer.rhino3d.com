import rhinoscriptsyntax as rs
from random import random

def randommeshcolors():
    mesh_id = rs.GetObject("Mesh to randomize", 32, True, True)
    if not mesh_id: return

    verts = rs.MeshVertices(mesh_id)
    faces = rs.MeshFaceVertices(mesh_id)
    colors = []
    for vert in verts:
        rgb = random()*255, random()*255, random()*255
        colors.append(rgb)
    rs.AddMesh(verts, faces, vertex_colors=colors)
    rs.DeleteObject(mesh_id)


if __name__=="__main__":
    randommeshcolors()
    