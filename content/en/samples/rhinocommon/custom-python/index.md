+++
aliases = ["/en/5/samples/rhinocommon/custom-python/", "/en/6/samples/rhinocommon/custom-python/", "/en/7/samples/rhinocommon/custom-python/", "/en/wip/samples/rhinocommon/custom-python/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to run a custom python script from within a command."
keywords = [ "custom", "python" ]
languages = [ "C#", "Python" ]
sdk = [ "RhinoCommon" ]
title = "Custom Python"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = ""
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
  public static Rhino.Commands.Result CustomPython(RhinoDoc doc)
  {
    if (null == m_python)
    {
      m_python = Rhino.Runtime.PythonScript.Create();
      if (null == m_python)
      {
        RhinoApp.WriteLine("Error: Unable to create an instance of the python engine");
        return Rhino.Commands.Result.Failure;
      }
    }
    m_python.ScriptContextDoc = new CustomPythonDoc(doc);

    const string script = @"
import rhinoscriptsyntax as rs
rs.AddLine((0,0,0), (10,10,10))
";
    m_python.ExecuteScript(script);
    return Rhino.Commands.Result.Success;
  }

  static Rhino.Runtime.PythonScript m_python;
}

// our fake RhinoDoc
public class CustomPythonDoc
{
  readonly RhinoDoc m_doc;
  public CustomPythonDoc(RhinoDoc doc)
  {
    m_doc = doc;
  }

  readonly CustomObjectTable m_table = new CustomObjectTable();
  public CustomObjectTable Objects
  {
    get { return m_table; }
  }

  public Rhino.DocObjects.Tables.ViewTable Views
  {
    get
    {
      return m_doc.Views;
    }
  }

}

public class CustomObjectTable
{
  public Guid AddLine(Rhino.Geometry.Point3d p1, Rhino.Geometry.Point3d p2)
  {
    Rhino.Geometry.Line l = new Rhino.Geometry.Line(p1, p2);
    if (l.IsValid)
    {
      Guid id = Guid.NewGuid();
      m_lines_dict.Add(id, l);
      return id;
    }
    return Guid.Empty;
  }

  readonly System.Collections.Generic.Dictionary<Guid, Rhino.Geometry.Line> m_lines_dict = new System.Collections.Generic.Dictionary<Guid, Rhino.Geometry.Line>();
}
```

</div>

<div class="codetab-content" id="py">

```python
#! python 3
# This sample demonstrates how to host the Python script engine from a C#
# command and run a custom Python script against a "fake" RhinoDoc. From
# Python you do not need to host the engine: you can simply call the
# rhinoscriptsyntax API directly, which is the script the C# host above
# would execute.
import rhinoscriptsyntax as rs


def RunCommand():
    rs.AddLine((0, 0, 0), (10, 10, 10))


if __name__ == "__main__":
    RunCommand()
```

</div>
