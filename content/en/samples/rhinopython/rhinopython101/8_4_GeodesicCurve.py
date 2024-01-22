import rhinoscriptsyntax as rs

def geodesiccurve():
    surface_id = rs.GetObject("Select surface for geodesic curve solution", 8, True, True)
    if not surface_id: return

    vertices = getr2pathonsurface(surface_id, 10, "Start of geodesic curve", "End of geodesic curve")
    if not vertices: return

    tolerance = rs.UnitAbsoluteTolerance() / 10
    length = 1e300
    newlength = 0.0

    while True:
        print("Solving geodesic fit for %d samples" % len(vertices))
        vertices = geodesicfit(vertices, surface_id, tolerance)

        newlength = polylinelength(vertices)
        if abs(newlength-length)<tolerance: break
        if len(vertices)>1000: break
        vertices = subdividepolyline(vertices)
        length = newlength

    rs.AddPolyline(vertices)
    print("Geodesic curve added with length: ", newlength)


def geodesicfit(vertices, surface_id, tolerance):
    length = polylinelength(vertices)
    while True:
        vertices = smoothpolyline(vertices)
        vertices = projectpolyline(vertices, surface_id)
        newlength = polylinelength(vertices)
        if abs(newlength-length)<tolerance: return vertices
        length = newlength


def smoothpolyline(vertices):
    smooth = []
    smooth.append(vertices[0])

    for i in range(1, len(vertices)-1):
        prev = vertices[i-1]
        this = vertices[i]
        next = vertices[i+1]
        pt = (prev+this+next) / 3.0
        smooth.append(pt)
    smooth.append(vertices[len(vertices)-1])
    return smooth


def projectpolyline(vertices, surface_id):
    polyline = []
    for vertex in vertices:
        pt = rs.BrepClosestPoint(surface_id, vertex)
        if pt: polyline.append(pt[0])
    return polyline


def getr2pathonsurface(surface_id, segments, prompt1, prompt2):
    start_point = rs.GetPointOnSurface(surface_id, prompt1)
    if not start_point: return

    end_point = rs.GetPointOnSurface(surface_id, prompt2)
    if not end_point: return

    if rs.Distance(start_point, end_point)==0.0: return

    uva = rs.SurfaceClosestPoint(surface_id, start_point)
    uvb = rs.SurfaceClosestPoint(surface_id, end_point)

    path = []
    for i in range(segments):
        t = i / segments
        u = uva[0] + t*(uvb[0] - uva[0])
        v = uva[1] + t*(uvb[1] - uva[1])
        pt = rs.EvaluateSurface(surface_id, u, v)
        path.append(pt)
    return path



def subdividepolyline(vertices):
    subd = []
    for i in range(len(vertices)-1):
        #copy original vertex location
        subd.append( vertices[i] )
        #compute the average of the current vertex and the next one
        pt = (vertices[i]+vertices[i+1])/2.0
        subd.append(pt)
    #copy the last vertex (this is skipped by the loop)
    subd.append(vertices[len(vertices)-1])
    return subd


def polylinelength(vertices):
    length = 0.0
    for i in range(len(vertices)-1):
        length+= rs.Distance(vertices[i], vertices[i+1])
    return length


if __name__=="__main__":
    geodesiccurve()