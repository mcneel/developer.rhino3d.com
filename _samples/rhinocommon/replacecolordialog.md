---
layout: code-sample
title: Replace Rhino's Color Picking Dialog
author: 
categories: ['Other'] 
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
keywords: ['replace', 'rhinos', 'color', 'picking', 'dialog']
order: 142
description:  
---



```cs
public class ReplaceColorDialogCommand : Command
{
  public override string EnglishName { get { return "csReplaceColorDialog"; } }

  private ColorDialog m_dlg = null;

  protected override Result RunCommand(RhinoDoc doc, RunMode mode)
  {
    Dialogs.SetCustomColorDialog(OnSetCustomColorDialog);
    return Result.Success;
  }

  void OnSetCustomColorDialog(object sender, GetColorEventArgs e)
  {
    m_dlg = new ColorDialog();
    if (m_dlg.ShowDialog(null) == DialogResult.OK)
    {
      var c = m_dlg.Color;
      e.SelectedColor = c;
    }
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Public Class ReplaceColorDialogCommand
  Inherits Command
  Public Overrides ReadOnly Property EnglishName() As String
    Get
      Return "vbReplaceColorDialog"
    End Get
  End Property

  Private m_dlg As ColorDialog = Nothing

  Protected Overrides Function RunCommand(doc As RhinoDoc, mode As RunMode) As Result
    Dialogs.SetCustomColorDialog(AddressOf OnSetCustomColorDialog)
    Return Result.Success
  End Function

  Private Sub OnSetCustomColorDialog(sender As Object, e As GetColorEventArgs)

    m_dlg = New ColorDialog()
    If m_dlg.ShowDialog(Nothing) = DialogResult.OK Then
      Dim c = m_dlg.Color
      e.SelectedColor = c
    End If
  End Sub
End Class
```
{: #vb .tab-pane .fade .in}


```python
from Rhino import *
from Rhino.Commands import *
from Rhino.UI import *
from System.Windows.Forms import *

m_dlg = None

def RunCommand():
  Dialogs.SetCustomColorDialog(OnSetCustomColorDialog)
  return Result.Success

def OnSetCustomColorDialog(sender, e):
  m_dlg = ColorDialog()
  if m_dlg.ShowDialog(None) == DialogResult.OK:
    c = m_dlg.Color
    e.SelectedColor = c

if __name__ == "__main__":
  RunCommand()
```
{: #py .tab-pane .fade .in}


