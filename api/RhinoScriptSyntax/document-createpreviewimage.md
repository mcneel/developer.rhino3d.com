---
layout: bootstrap
---

# CreatePreviewImage

Create a bitmap preview image of the current model
        

### Parameters:

- ***filename*** = name of the bitmap file to create
- ***view[opt]*** = title of the view. If omitted, the active view is used
- ***size[opt]*** = two integers that specify width and height of the bitmap
- ***flags[opt]*** = Bitmap creation flags. Can be the combination of:
    1 = honor object highlighting
    2 = draw construction plane
    4 = use ghosted shading
- ***wireframe[opt]*** = If True then a wireframe preview image. If False,
    a rendered image will be created
        

### Returns:


True or False indicating success or failure
        
