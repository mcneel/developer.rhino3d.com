+++
aliases = ["/en/5/samples/rhinocommon/visual-analysis-modes/", "/en/6/samples/rhinocommon/visual-analysis-modes/", "/en/7/samples/rhinocommon/visual-analysis-modes/", "/en/wip/samples/rhinocommon/visual-analysis-modes/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to set the visual analysis mode to Z analysis for user-specified objects."
keywords = [ "visual", "analysis", "modes" ]
languages = [ "C#", "Python" ]
sdk = [ "RhinoCommon" ]
title = "Visual Analysis Modes"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/analysismode"
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
  public static Rhino.Commands.Result AnalysisMode_on(RhinoDoc doc)
  {
    // make sure our custom visual analysis mode is registered
    var zmode = Rhino.Display.VisualAnalysisMode.Register(typeof(ZAnalysisMode));

    const ObjectType filter = Rhino.DocObjects.ObjectType.Surface | Rhino.DocObjects.ObjectType.PolysrfFilter | Rhino.DocObjects.ObjectType.Mesh;
    Rhino.DocObjects.ObjRef[] objs;
    var rc = Rhino.Input.RhinoGet.GetMultipleObjects("Select objects for Z analysis", false, filter, out objs);
    if (rc != Rhino.Commands.Result.Success)
      return rc;

    int count = 0;
    for (int i = 0; i < objs.Length; i++)
    {
      var obj = objs[i].Object();

      // see if this object is alreay in Z analysis mode
      if (obj.InVisualAnalysisMode(zmode))
        continue;

      if (obj.EnableVisualAnalysisMode(zmode, true))
        count++;
    }
    doc.Views.Redraw();
    RhinoApp.WriteLine("{0} objects were put into Z-Analysis mode.", count);
    return Rhino.Commands.Result.Success;
  }

  public static Rhino.Commands.Result AnalysisMode_off(RhinoDoc doc)
  {
    var zmode = Rhino.Display.VisualAnalysisMode.Find(typeof(ZAnalysisMode));
    // If zmode is null, we've never registered the mode so we know it hasn't been used
    if (zmode != null)
    {
      foreach (Rhino.DocObjects.RhinoObject obj in doc.Objects)
      {
        obj.EnableVisualAnalysisMode(zmode, false);
      }
      doc.Views.Redraw();
    }
    RhinoApp.WriteLine("Z-Analysis is off.");
    return Rhino.Commands.Result.Success;
  }
}

/// <summary>
/// This simple example provides a false color based on the world z-coordinate.
/// For details, see the implementation of the FalseColor() function.
/// </summary>
public class ZAnalysisMode : Rhino.Display.VisualAnalysisMode
{
  Interval m_z_range = new Interval(-10,10);
  Interval m_hue_range = new Interval(0,4*Math.PI / 3);
  private const bool m_show_isocurves = true;

  public override string Name { get { return "Z-Analysis"; } }
  public override Rhino.Display.VisualAnalysisMode.AnalysisStyle Style { get { return AnalysisStyle.FalseColor; } }

  public override bool ObjectSupportsAnalysisMode(Rhino.DocObjects.RhinoObject obj)
  {
    if (obj is Rhino.DocObjects.MeshObject || obj is Rhino.DocObjects.BrepObject)
      return true;
    return false;
  }

  protected override void UpdateVertexColors(Rhino.DocObjects.RhinoObject obj, Mesh[] meshes)
  {
    // A "mapping tag" is used to determine if the colors need to be set
    Rhino.Render.MappingTag mt = GetMappingTag(obj.RuntimeSerialNumber);

    for (int mi = 0; mi < meshes.Length; mi++)
    {
      var mesh = meshes[mi];
      if( mesh.VertexColors.Tag.Id != this.Id )
      {
        // The mesh's mapping tag is different from ours. Either the mesh has
        // no false colors, has false colors set by another analysis mode, has
        // false colors set using different m_z_range[]/m_hue_range[] values, or
        // the mesh has been moved.  In any case, we need to set the false
        // colors to the ones we want.
        System.Drawing.Color[] colors = new System.Drawing.Color[mesh.Vertices.Count];
        for (int i = 0; i < mesh.Vertices.Count; i++)
        {
          double z = mesh.Vertices[i].Z;
          colors[i] = FalseColor(z);
        }
        mesh.VertexColors.SetColors(colors);
        // set the mesh's color tag
        mesh.VertexColors.Tag = mt;
      }
    }
  }

  public override bool ShowIsoCurves
  {
    get
    {
      // Most shaded analysis modes that work on breps have the option of
      // showing or hiding isocurves.  Run the built-in Rhino ZebraAnalysis
      // to see how Rhino handles the user interface.  If controlling
      // iso-curve visability is a feature you want to support, then provide
      // user interface to set this member variable.
      return m_show_isocurves;
    }
  }

  /// <summary>
  /// Returns a mapping tag that is used to detect when a mesh's colors need to
  /// be set.
  /// </summary>
  /// <returns></returns>
  Rhino.Render.MappingTag GetMappingTag(uint serialNumber)
  {
    Rhino.Render.MappingTag mt = new Rhino.Render.MappingTag();
    mt.Id = this.Id;

    // Since the false colors that are shown will change if the mesh is
    // transformed, we have to initialize the transformation.
    mt.MeshTransform = Transform.Identity;

    // This is a 32 bit CRC or the information used to set the false colors.
    // For this example, the m_z_range and m_hue_range intervals control the
    // colors, so we calculate their crc.
    uint crc = RhinoMath.CRC32(serialNumber, m_z_range.T0);
    crc = RhinoMath.CRC32(crc, m_z_range.T1);
    crc = RhinoMath.CRC32(crc, m_hue_range.T0);
    crc = RhinoMath.CRC32(crc, m_hue_range.T1);
    mt.MappingCRC = crc;
    return mt;
  }

  System.Drawing.Color FalseColor(double z)
  {
    // Simple example of one way to change a number into a color.
    double s = m_z_range.NormalizedParameterAt(z);
    s = Rhino.RhinoMath.Clamp(s, 0, 1);
    return System.Drawing.Color.FromArgb((int)(s * 255), 0, 0);
  }

}
```

</div>

<div class="codetab-content" id="py">

```python
#! python 3
import math
import Rhino
import System
import scriptcontext as sc
from clr import GetClrType


# This simple example provides a false color based on the world z-coordinate.
# For details, see the implementation of the FalseColor() function.
class ZAnalysisMode(Rhino.Display.VisualAnalysisMode):
    def __init__(self):
        super().__init__()
        self.m_z_range = Rhino.Geometry.Interval(-10, 10)
        self.m_hue_range = Rhino.Geometry.Interval(0, 4 * math.pi / 3)
        self.m_show_isocurves = True

    @property
    def Name(self):
        return "Z-Analysis"

    @property
    def Style(self):
        return Rhino.Display.VisualAnalysisMode.AnalysisStyle.FalseColor

    def ObjectSupportsAnalysisMode(self, obj):
        if isinstance(obj, Rhino.DocObjects.MeshObject) or isinstance(obj, Rhino.DocObjects.BrepObject):
            return True
        return False

    def UpdateVertexColors(self, obj, meshes):
        # A "mapping tag" is used to determine if the colors need to be set
        mt = self.GetMappingTag(obj.RuntimeSerialNumber)

        for mi in range(len(meshes)):
            mesh = meshes[mi]
            if mesh.VertexColors.Tag.Id != self.Id:
                # The mesh's mapping tag is different from ours. Either the mesh has
                # no false colors, has false colors set by another analysis mode, has
                # false colors set using different m_z_range[]/m_hue_range[] values, or
                # the mesh has been moved.  In any case, we need to set the false
                # colors to the ones we want.
                colors = System.Array.CreateInstance(System.Drawing.Color, mesh.Vertices.Count)
                for i in range(mesh.Vertices.Count):
                    z = mesh.Vertices[i].Z
                    colors[i] = self.FalseColor(z)
                mesh.VertexColors.SetColors(colors)
                # set the mesh's color tag
                mesh.VertexColors.Tag = mt

    @property
    def ShowIsoCurves(self):
        # Most shaded analysis modes that work on breps have the option of
        # showing or hiding isocurves.  Run the built-in Rhino ZebraAnalysis
        # to see how Rhino handles the user interface.  If controlling
        # iso-curve visability is a feature you want to support, then provide
        # user interface to set this member variable.
        return self.m_show_isocurves

    def GetMappingTag(self, serialNumber):
        """Returns a mapping tag that is used to detect when a mesh's colors need to be set."""
        mt = Rhino.Render.MappingTag()
        mt.Id = self.Id

        # Since the false colors that are shown will change if the mesh is
        # transformed, we have to initialize the transformation.
        mt.MeshTransform = Rhino.Geometry.Transform.Identity

        # This is a 32 bit CRC or the information used to set the false colors.
        # For this example, the m_z_range and m_hue_range intervals control the
        # colors, so we calculate their crc.
        crc = Rhino.RhinoMath.CRC32(serialNumber, self.m_z_range.T0)
        crc = Rhino.RhinoMath.CRC32(crc, self.m_z_range.T1)
        crc = Rhino.RhinoMath.CRC32(crc, self.m_hue_range.T0)
        crc = Rhino.RhinoMath.CRC32(crc, self.m_hue_range.T1)
        mt.MappingCRC = crc
        return mt

    def FalseColor(self, z):
        # Simple example of one way to change a number into a color.
        s = self.m_z_range.NormalizedParameterAt(z)
        s = Rhino.RhinoMath.Clamp(s, 0, 1)
        return System.Drawing.Color.FromArgb(int(s * 255), 0, 0)


def AnalysisMode_on():
    # make sure our custom visual analysis mode is registered
    zmode = Rhino.Display.VisualAnalysisMode.Register(GetClrType(ZAnalysisMode))

    filter = (
        Rhino.DocObjects.ObjectType.Surface
        | Rhino.DocObjects.ObjectType.PolysrfFilter
        | Rhino.DocObjects.ObjectType.Mesh
    )
    rc, objs = Rhino.Input.RhinoGet.GetMultipleObjects("Select objects for Z analysis", False, filter)
    if rc != Rhino.Commands.Result.Success:
        return rc

    count = 0
    for i in range(len(objs)):
        obj = objs[i].Object()

        # see if this object is already in Z analysis mode
        if obj.InVisualAnalysisMode(zmode):
            continue

        if obj.EnableVisualAnalysisMode(zmode, True):
            count += 1
    sc.doc.Views.Redraw()
    Rhino.RhinoApp.WriteLine("{0} objects were put into Z-Analysis mode.", count)
    return Rhino.Commands.Result.Success


def AnalysisMode_off():
    zmode = Rhino.Display.VisualAnalysisMode.Find(GetClrType(ZAnalysisMode))
    # If zmode is None, we've never registered the mode so we know it hasn't been used
    if zmode is not None:
        for obj in sc.doc.Objects:
            obj.EnableVisualAnalysisMode(zmode, False)
        sc.doc.Views.Redraw()
    Rhino.RhinoApp.WriteLine("Z-Analysis is off.")
    return Rhino.Commands.Result.Success


if __name__ == "__main__":
    AnalysisMode_on()
```

</div>
