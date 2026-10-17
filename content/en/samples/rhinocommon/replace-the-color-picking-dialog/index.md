+++
aliases = ["/en/5/samples/rhinocommon/replace-the-color-picking-dialog/", "/en/6/samples/rhinocommon/replace-the-color-picking-dialog/", "/en/7/samples/rhinocommon/replace-the-color-picking-dialog/", "/en/wip/samples/rhinocommon/replace-the-color-picking-dialog/"]
authors = [ "steve" ]
categories = [ "Picking and Selection" ]
description = "Demonstrates how to replace Rhino's color picking dialog."
keywords = [ "replace", "rhinos", "color", "picking", "dialog" ]
languages = [ "C#", "Python" ]
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

<div class="codetab-content" id="py">

```python
#! python 3
import Rhino
import Eto.Forms as forms
import System

m_dlg = None

def OnSetCustomColorDialog(sender, e):
    global m_dlg
    m_dlg = forms.ColorDialog()
    if m_dlg.ShowDialog(None) == forms.DialogResult.Ok:
        c = m_dlg.Color
        e.SelectedColor = System.Drawing.Color.FromArgb(c.Ab, c.Rb, c.Gb, c.Bb)

def RunCommand():
    Rhino.UI.Dialogs.SetCustomColorDialog(OnSetCustomColorDialog)
    return Rhino.Commands.Result.Success

if __name__ == "__main__":
    RunCommand()
```

</div>
