+++
aliases = ["/5/samples/rhinocommon/replace-the-color-picking-dialog/", "/6/samples/rhinocommon/replace-the-color-picking-dialog/", "/7/samples/rhinocommon/replace-the-color-picking-dialog/", "/wip/samples/rhinocommon/replace-the-color-picking-dialog/"]
authors = [ "steve" ]
categories = [ "Picking and Selection" ]
description = "Demonstrates how to replace Rhino's color picking dialog."
keywords = [ "replace", "rhinos", "color", "picking", "dialog" ]
languages = [ "C#", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Replace the Color Picking Dialog"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/replacecolordialog"
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

</div>


<div class="codetab-content" id="vb">

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

</div>


<div class="codetab-content" id="py">

```python
# No Python sample available
```

</div>
