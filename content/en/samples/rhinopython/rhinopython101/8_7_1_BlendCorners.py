import rhinoscriptsyntax as rs


def blendcorners():
    polyline_id = rs.GetObject("Polyline to blend", 4, True, True)
    if not polyline_id: return

    vertices = rs.PolylineVertices(polyline_id)
    if not vertices: return

    radius = rs.GetReal("Blend radius", 1.0, 0.0)
    if radius is None: return

    between = lambda a,b: (a+b)/2.0
    newverts = []
    for i in range(len(vertices)-1):
        a = vertices[i]
        b = vertices[i+1]
        segmentlength = rs.Distance(a, b)
        vec_segment = rs.PointSubtract(b, a)
        vec_segment = rs.VectorUnitize(vec_segment)

        if radius<(0.5*segmentlength):
            vec_segment = rs.VectorScale(vec_segment, radius)
        else:
            vec_segment = rs.VectorScale(vec_segment, 0.5*segmentlength)

        w1 = rs.PointAdd(a, vec_segment)
        w2 = rs.PointSubtract(b, vec_segment)
        newverts.append(a)
        newverts.append(between(a,w1))
        newverts.append(w1)
        newverts.append(between(w1,w2))
        newverts.append(w2)
        newverts.append(between(w2,b))
    newverts.append(vertices[len(vertices)-1])
    rs.AddCurve(newverts, 5)
    rs.DeleteObject(polyline_id)


if __name__=="__main__":
    blendcorners()