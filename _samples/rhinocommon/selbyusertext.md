---
layout: code-sample
author:
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
title: Select by User Text
keywords: ['select', 'user', 'text']
categories: ['Picking and Selection']
description:
order: 1
---

```cs
partial class Examples
{
  static string m_key = string.Empty;
  public static Rhino.Commands.Result SelByUserText(RhinoDoc doc)
  {
    // You don't have to override RunCommand if you don't need any user input. In
    // this case we want to get a key from the user. If you return something other
    // than Success, the selection is canceled
    return Rhino.Input.RhinoGet.GetString("key", true, ref m_key);
  }

  protected static override bool SelFilter(Rhino.DocObjects.RhinoObject rhObj)
  {
    string s = rhObj.Attributes.GetUserString(m_key);
    return !string.IsNullOrEmpty(s);
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Private Shared m_key As String = String.Empty
  Public Shared Function SelByUserText(ByVal doc As RhinoDoc) As Rhino.Commands.Result
	' You don't have to override RunCommand if you don't need any user input. In
	' this case we want to get a key from the user. If you return something other
	' than Success, the selection is canceled
	Return Rhino.Input.RhinoGet.GetString("key", True, m_key)
  End Function

  Protected Shared Overrides Function SelFilter(ByVal rhObj As Rhino.DocObjects.RhinoObject) As Boolean
	Dim s As String = rhObj.Attributes.GetUserString(m_key)
	Return Not String.IsNullOrEmpty(s)
  End Function
End Class
```
{: #vb .tab-pane .fade .in}

