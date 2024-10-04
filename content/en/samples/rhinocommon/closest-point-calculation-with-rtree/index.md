+++
aliases = ["/en/5/samples/rhinocommon/closest-point-calculation-with-rtree/", "/en/6/samples/rhinocommon/closest-point-calculation-with-rtree/", "/en/7/samples/rhinocommon/closest-point-calculation-with-rtree/", "/wip/samples/rhinocommon/closest-point-calculation-with-rtree/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to perform a closest point calculation using an RTree data structure."
keywords = [ "closest", "point", "calculations", "with", "rtree" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Closest Point Calculation with RTree"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/closestpoint"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 0

+++

<div class="codetab-content" id="cs">

```cs
partial class Examples
{
  static void SearchCallback(object sender, RTreeEventArgs e)
  {
    SearchData data = e.Tag as SearchData;
    if (data == null)
      return;
    data.HitCount = data.HitCount + 1;
    Point3f vertex = data.Mesh.Vertices[e.Id];
    double distance = data.Point.DistanceTo(vertex);
    if (data.Index == -1 || data.Distance > distance)
    {
      // shrink the sphere to help improve the test
      e.SearchSphere = new Sphere(data.Point, distance);
      data.Index = e.Id;
      data.Distance = distance;
    }
  }

  class SearchData
  {
    public SearchData(Mesh mesh, Point3d point)
    {
      Point = point;
      Mesh = mesh;
      HitCount = 0;
      Index = -1;
      Distance = 0;
    }

    public int HitCount { get; set; }
    public Point3d Point { get; private set; }
    public Mesh Mesh { get; private set; }
    public int Index { get; set; }
    public double Distance { get; set; }
  }

  public static Rhino.Commands.Result RTreeClosestPoint(RhinoDoc doc)
  {
    Rhino.DocObjects.ObjRef objref;
    var rc = Rhino.Input.RhinoGet.GetOneObject("select mesh", false, Rhino.DocObjects.ObjectType.Mesh, out objref);
    if (rc != Rhino.Commands.Result.Success)
      return rc;

    Mesh mesh = objref.Mesh();
    objref.Object().Select(false);
    doc.Views.Redraw();

    using (RTree tree = new RTree())
    {
      for (int i = 0; i < mesh.Vertices.Count; i++)
      {
        // we can make a C++ function that just builds an rtree from the
        // vertices in one quick shot, but for now...
        tree.Insert(mesh.Vertices[i], i);
      }

      while (true)
      {
        Point3d point;
        rc = Rhino.Input.RhinoGet.GetPoint("test point", false, out point);
        if (rc != Rhino.Commands.Result.Success)
          break;

        SearchData data = new SearchData(mesh, point);
        // Use the first vertex in the mesh to define a start sphere
        double distance = point.DistanceTo(mesh.Vertices[0]);
        Sphere sphere = new Sphere(point, distance * 1.1);
        if (tree.Search(sphere, SearchCallback, data))
        {
          doc.Objects.AddPoint(mesh.Vertices[data.Index]);
          doc.Views.Redraw();
          RhinoApp.WriteLine("Found point in {0} tests", data.HitCount);
        }
      }
    }
    return Rhino.Commands.Result.Success;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Private Shared Sub SearchCallback(ByVal sender As Object, ByVal e As RTreeEventArgs)
	Dim data As SearchData = TryCast(e.Tag, SearchData)
	If data Is Nothing Then
	  Return
	End If
	data.HitCount = data.HitCount + 1
	Dim vertex As Point3f = data.Mesh.Vertices(e.Id)
	Dim distance As Double = data.Point.DistanceTo(vertex)
	If data.Index = -1 OrElse data.Distance > distance Then
	  ' shrink the sphere to help improve the test
	  e.SearchSphere = New Sphere(data.Point, distance)
	  data.Index = e.Id
	  data.Distance = distance
	End If
  End Sub

  Private Class SearchData
	Public Sub New(ByVal mesh As Mesh, ByVal point As Point3d)
	  Me.Point = point
	  Me.Mesh = mesh
	  HitCount = 0
	  Index = -1
	  Distance = 0
	End Sub

	Public Property HitCount() As Integer
	Private privatePoint As Point3d
	Public Property Point() As Point3d
		Get
			Return privatePoint
		End Get
		Private Set(ByVal value As Point3d)
			privatePoint = value
		End Set
	End Property
	Private privateMesh As Mesh
	Public Property Mesh() As Mesh
		Get
			Return privateMesh
		End Get
		Private Set(ByVal value As Mesh)
			privateMesh = value
		End Set
	End Property
	Public Property Index() As Integer
	Public Property Distance() As Double
  End Class

  Public Shared Function RTreeClosestPoint(ByVal doc As RhinoDoc) As Rhino.Commands.Result
	Dim objref As Rhino.DocObjects.ObjRef = Nothing
	Dim rc = Rhino.Input.RhinoGet.GetOneObject("select mesh", False, Rhino.DocObjects.ObjectType.Mesh, objref)
	If rc IsNot Rhino.Commands.Result.Success Then
	  Return rc
	End If

	Dim mesh As Mesh = objref.Mesh()
	objref.Object().Select(False)
	doc.Views.Redraw()

	Using tree As New RTree()
	  For i As Integer = 0 To mesh.Vertices.Count - 1
		' we can make a C++ function that just builds an rtree from the
		' vertices in one quick shot, but for now...
		tree.Insert(mesh.Vertices(i), i)
	  Next i

	  Do
		Dim point As Point3d = Nothing
		rc = Rhino.Input.RhinoGet.GetPoint("test point", False, point)
		If rc IsNot Rhino.Commands.Result.Success Then
		  Exit Do
		End If

		Dim data As New SearchData(mesh, point)
		' Use the first vertex in the mesh to define a start sphere
		Dim distance As Double = point.DistanceTo(mesh.Vertices(0))
		Dim sphere As New Sphere(point, distance * 1.1)
		If tree.Search(sphere, AddressOf SearchCallback, data) Then
		  doc.Objects.AddPoint(mesh.Vertices(data.Index))
		  doc.Views.Redraw()
		  RhinoApp.WriteLine("Found point in {0} tests", data.HitCount)
		End If
	  Loop
	End Using
	Return Rhino.Commands.Result.Success
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
import Rhino
import rhinoscriptsyntax as rs

# data passed to the RTree's SearchCallback function that
# we can use for recording what is going on
class SearchData:
    def __init__(self, mesh, point):
        self.HitCount = 0
        self.Mesh = mesh
        self.Point = point
        self.Index = -1
        self.Distance = 0


def SearchCallback(sender, e):
    data = e.Tag
    data.HitCount += 1
    vertex = data.Mesh.Vertices[e.Id]
    distance = data.Point.DistanceTo(vertex)
    if data.Index == -1 or data.Distance > distance:
        # shrink the sphere to help improve the test
        e.SearchSphere = Rhino.Geometry.Sphere(data.Point, distance)
        data.Index = e.Id
        data.Distance = distance

def RunSearch():
    id = rs.GetObject("select mesh", rs.filter.mesh)
    mesh = rs.coercemesh(id)
    if mesh:
        rs.UnselectObject(id)
        tree = Rhino.Geometry.RTree()
        # I can add a RhinoCommon function that just builds an rtree from the
        # vertices in one quick shot, but for now...
        for i,vertex in enumerate(mesh.Vertices): tree.Insert(vertex, i)

        while(True):
            point = rs.GetPoint("test point")
            if not point: break

            data = SearchData(mesh, point)
            # Use the first vertex in the mesh to define a start sphere
            distance = point.DistanceTo(mesh.Vertices[0])
            sphere = Rhino.Geometry.Sphere(point, distance * 1.1)
            if tree.Search(sphere, SearchCallback, data):
                rs.AddPoint(mesh.Vertices[data.Index])
                print "Found point in {0} tests".format(data.HitCount)

if __name__=="__main__":
    RunSearch()
```

</div>
