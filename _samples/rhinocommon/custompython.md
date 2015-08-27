---
layout: code-sample
author:
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
title: Custom Python
keywords: ['custom', 'python']
categories: ['Other']
description:
order: 1
---

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
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function CustomPython(ByVal doc As RhinoDoc) As Rhino.Commands.Result
	If Nothing Is m_python Then
	  m_python = Rhino.Runtime.PythonScript.Create()
	  If Nothing Is m_python Then
		RhinoApp.WriteLine("Error: Unable to create an instance of the python engine")
		Return Rhino.Commands.Result.Failure
	  End If
	End If
	m_python.ScriptContextDoc = New CustomPythonDoc(doc)

	Const script As String = "
import rhinoscriptsyntax as rs
rs.AddLine((0,0,0), (10,10,10))
"
	m_python.ExecuteScript(script)
	Return Rhino.Commands.Result.Success
  End Function

  Private Shared m_python As Rhino.Runtime.PythonScript
End Class

' our fake RhinoDoc
Public Class CustomPythonDoc
  Private ReadOnly m_doc As RhinoDoc
  Public Sub New(ByVal doc As RhinoDoc)
	m_doc = doc
  End Sub

  Private ReadOnly m_table As New CustomObjectTable()
  Public ReadOnly Property Objects() As CustomObjectTable
	Get
		Return m_table
	End Get
  End Property

  Public ReadOnly Property Views() As Rhino.DocObjects.Tables.ViewTable
	Get
	  Return m_doc.Views
	End Get
  End Property

End Class

Public Class CustomObjectTable
  Public Function AddLine(ByVal p1 As Rhino.Geometry.Point3d, ByVal p2 As Rhino.Geometry.Point3d) As Guid
	Dim l As New Rhino.Geometry.Line(p1, p2)
	If l.IsValid Then
	  Dim id As Guid = Guid.NewGuid()
	  m_lines_dict.Add(id, l)
	  Return id
	End If
	Return Guid.Empty
  End Function

  Private ReadOnly m_lines_dict As New System.Collections.Generic.Dictionary(Of Guid, Rhino.Geometry.Line)()
End Class
```
{: #vb .tab-pane .fade .in}

