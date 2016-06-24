---
title: Replace the Color Picking Dialog
description: Demonstrates how to replace Rhino's color picking dialog.
author: steve@mcneel.com
apis: ['RhinoCommon']
languages: ['C#', 'VB']
platforms: ['Windows', 'Mac']
categories: ['Picking and Selection']
origin: http://wiki.mcneel.com/developer/rhinocommonsamples/replacecolordialog
order: 1
keywords: ['replace', 'rhinos', 'color', 'picking', 'dialog']
layout: code-sample-rhinocommon
---

```cs
partial class Examples
{
  private static ColorDialog m_dlg = null;

  public static Result ReplaceColorDialog(RhinoDoc doc)
  {
    Dialogs.SetCustomColorDialog(OnSetCustomColorDialog);
    return Result.Success;
  }

  static void OnSetCustomColorDialog(object sender, GetColorEventArgs e)
  {
    m_dlg = new ColorDialog();
    if (m_dlg.ShowDialog(null) == DialogResult.Ok)
    {
      var c = m_dlg.Color;
      e.SelectedColor = System.Drawing.Color.FromArgb (c.Ab, c.Rb, c.Gb, c.Bb);
    }
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Private Shared m_dlg As ColorDialog = Nothing

  Public Shared Function ReplaceColorDialog(ByVal doc As RhinoDoc) As Result
	Dialogs.SetCustomColorDialog(AddressOf OnSetCustomColorDialog)
	Return Result.Success
  End Function

  Private Shared Sub OnSetCustomColorDialog(ByVal sender As Object, ByVal e As GetColorEventArgs)
	m_dlg = New ColorDialog()
	If m_dlg.ShowDialog(Nothing) = DialogResult.Ok Then
	  Dim c = m_dlg.Color
	  e.SelectedColor = System.Drawing.Color.FromArgb(c.Ab, c.Rb, c.Gb, c.Bb)
	End If
  End Sub
End Class
```
{: #vb .tab-pane .fade .in}


```python
# No Python sample available
```
{: #py .tab-pane .fade .in}
