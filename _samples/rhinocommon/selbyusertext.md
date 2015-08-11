---
layout: code-sample
title: Select by User Text
author: 
categories: ['Picking and Selection'] 
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
keywords: ['select', 'user', 'text']
order: 147
description:  
---



```cs
public class ex_selbyusertext : Rhino.Commands.SelCommand
{
  public override string EnglishName{ get { return "SelByUserText"; } }

  string m_key = string.Empty;
  protected override Rhino.Commands.Result RunCommand(RhinoDoc doc, Rhino.Commands.RunMode mode)
  {
    // You don't have to override RunCommand if you don't need any user input. In
    // this case we want to get a key from the user. If you return something other
    // than Success, the selection is canceled
    return Rhino.Input.RhinoGet.GetString("key", true, ref m_key);
  }

  protected override bool SelFilter(Rhino.DocObjects.RhinoObject rhObj)
  {
    string s = rhObj.Attributes.GetUserString(m_key);
    return !string.IsNullOrEmpty(s);
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Inherits Rhino.Commands.SelCommand

Public Overrides ReadOnly Property EnglishName() As String
  Get
    Return "vbSelByUserText"
  End Get
End Property

Dim m_key As String = String.Empty
Protected Overrides Function RunCommand(ByVal doc As RhinoDoc, ByVal mode As Rhino.Commands.RunMode) As Rhino.Commands.Result
  ' You don't have to override RunCommand if you don't need any user input. In
  ' this case we want to get a key from the user. If you return something other
  ' than Success, the selection is canceled
  Return Rhino.Input.RhinoGet.GetString("key", True, m_key)
End Function

Protected Overrides Function SelFilter(rhObj As Rhino.DocObjects.RhinoObject) As Boolean
  Dim s As String = rhObj.Attributes.GetUserString(m_key)
  Return Not String.IsNullOrEmpty(s)
End Function
```
{: #vb .tab-pane .fade .in}


```python
no python code sample available
```
{: #py .tab-pane .fade .in}


