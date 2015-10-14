---
layout: bootstrap
---

# AddPictureFrame

Creates a picture frame and adds it to the document.
      

### Parameters:

  plane = The plane in which the PictureFrame will be created.  The bottom-left corner of picture will be at plane's origin. The width will be in the plane's X axis direction, and the height will be in the plane's Y axis direction.
  filename = The path to a bitmap or image file.
  width = If both dblWidth and dblHeight = 0, then the width and height of the PictureFrame will be the width and height of the image. If dblWidth = 0 and dblHeight is > 0, or if dblWidth > 0 and dblHeight = 0, then the non-zero value is assumed to be an aspect ratio of the image's width or height, which ever one is = 0. If both dblWidth and dblHeight are > 0, then these are assumed to be the width and height of in the current unit system.
  height =  If both dblWidth and dblHeight = 0, then the width and height of the PictureFrame will be the width and height of the image. If dblWidth = 0 and dblHeight is > 0, or if dblWidth > 0 and dblHeight = 0, then the non-zero value is assumed to be an aspect ratio of the image's width or height, which ever one is = 0. If both dblWidth and dblHeight are > 0, then these are assumed to be the width and height of in the current unit system.
  self_illumination =  If True, then the image mapped to the picture frame plane always displays at full intensity and is not affected by light or shadow.
  embed = If True, then the function adds the image to Rhino's internal bitmap table, thus making the document self-contained.
  use_alpha = If False, the picture frame is created without any transparency texture.  If True, a transparency texture is created with a "mask texture" set to alpha, and an instance of the diffuse texture in the source texture slot.
  make_mesh = If True, the function will make a PictureFrame object from a mesh rather than a plane surface.
Reterns:
  object identifier on success
  None on failure
      


