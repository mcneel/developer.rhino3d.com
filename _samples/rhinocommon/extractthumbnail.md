---
layout: code-sample
title: Extract Preview Image
author: 
categories: ['Other'] 
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
keywords: ['extract', 'preview', 'image']
order: 82
description:  
---



```cs
public class ExtractThumbnailCommand : Command
{
  public override string EnglishName { get { return "csExtractThumbnail"; } }

  protected override Result RunCommand(RhinoDoc doc, RunMode mode)
  {
    var gf = RhinoGet.GetFileName(GetFileNameMode.OpenImage, "*.3dm", "select file", null);
    if (gf == string.Empty || !System.IO.File.Exists(gf))
      return Result.Cancel;

    var bitmap = Rhino.FileIO.File3dm.ReadPreviewImage(gf);
    // convert System.Drawing.Bitmap to BitmapSource
    var image_source = System.Windows.Interop.Imaging.CreateBitmapSourceFromHBitmap(bitmap.GetHbitmap(), IntPtr.Zero,
      Int32Rect.Empty, System.Windows.Media.Imaging.BitmapSizeOptions.FromEmptyOptions());

    // show in WPF window
    var window = new Window();
    var image = new Image {Source = image_source};
    window.Content = image;
    window.Show();

    return Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Public Class ExtractThumbnailCommand
  Inherits Command
  Public Overrides ReadOnly Property EnglishName() As String
    Get
      Return "vbExtractThumbnail"
    End Get
  End Property

  Protected Overrides Function RunCommand(doc As RhinoDoc, mode As RunMode) As Result
    Dim gf = RhinoGet.GetFileName(GetFileNameMode.OpenImage, "*.3dm", "select file", Nothing)
    If gf = String.Empty OrElse Not System.IO.File.Exists(gf) Then
      Return Result.Cancel
    End If

    Dim bitmap = Rhino.FileIO.File3dm.ReadPreviewImage(gf)
    ' convert System.Drawing.Bitmap to BitmapSource
    Dim imageSource = System.Windows.Interop.Imaging.CreateBitmapSourceFromHBitmap(bitmap.GetHbitmap(), IntPtr.Zero, Int32Rect.Empty, System.Windows.Media.Imaging.BitmapSizeOptions.FromEmptyOptions())

    ' show in WPF window
    Dim window = New Window()
    Dim image = New Image()
    image.Source = imageSource

    window.Content = image
    window.Show()

    Return Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
import Rhino
import rhinoscriptsyntax as rs
from scriptcontext import doc

import clr
clr.AddReference("System.Windows.Forms")
import System.Windows.Forms

def RunCommand():

  fn = rs.OpenFileName(title="select file", filter="Rhino files|*.3dm||")
  if fn == None:
    return

  bitmap = doc.ExtractPreviewImage(fn)

  f = System.Windows.Forms.Form()
  f.Height = bitmap.Height
  f.Width = bitmap.Width
  pb = System.Windows.Forms.PictureBox()
  pb.Image = bitmap
  pb.Height = bitmap.Height  #SizeMode = System.Windows.Forms.PictueBoxSizeMode.AutoSize
  pb.Width = bitmap.Width
  f.Controls.Add(pb);
  f.Show();

if __name__ == "__main__":
  RunCommand()
```
{: #py .tab-pane .fade .in}


