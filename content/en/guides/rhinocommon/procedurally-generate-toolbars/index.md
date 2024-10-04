+++
aliases = ["/en/en/5/guides/rhinocommon/procedurally-generate-toolbars/", "/en/6/guides/rhinocommon/procedurally-generate-toolbars/", "/en/7/guides/rhinocommon/procedurally-generate-toolbars/", "/wip/guides/rhinocommon/procedurally-generate-toolbars/"]
authors = [ "dale" ]
categories = [ "Advanced" ]
description = "This guide covers the generation of toolbar button images."
keywords = [ "Native", "RhinoCommon", "Plugin", "Toolbar" ]
languages = [ "C#" ]
sdk = [ "RhinoCommon" ]
title = "Procedurally Generate Toolbars"
type = "guides"
weight = 6
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++


## Question

I am trying to generate a toolbar without using Rhino. Having a toolbar with correct macros is done and working, but the bitmap (icons) part is still problematic

I’m not sure if the issue is with the image generation or the GUID system of Rhino.

For each icon size, the script takes all the icons needed and makes a big one, resulting in a column of icons. Then the image is translated to ```Base64``` format.

Rhino does not recognize these images. They are not displayed. And upon saving the toolbar, all the previous icon data is replaced with a blank image.


## Answer

Toolbar bitmaps are stored in a grid with 250 columns and enough rows to accommodate the total item count. New items are added to then end of the last row until the row fills up at which time a new row is added to the bitmap.  Rhino writes the bitmap as a PNG file to a stream and then writes the raw bitmap to the RUI file. 

Here is some sample code for writing:

```c#
const string NODE_BITMAPITEM = "bitmap_item";
const string NODE_BITMAP = "bitmap";
...
public void Write(System.Xml.XmlWriter writer, string elementName)
{
  writer.WriteStartElement(elementName);
  {
    writer.WriteAttributeString("item_width", m_item_size.Width.ToString());
    writer.WriteAttributeString("item_height", m_item_size.Height.ToString());
    foreach (KeyValuePair<Guid, BitmapItem> kvp in m_id_list)
    {
      writer.WriteStartElement(NODE_BITMAPITEM);
      {
        writer.WriteAttributeString("guid", kvp.Key.ToString());
        writer.WriteAttributeString("index", kvp.Value.m_index.ToString());
      }
      writer.WriteEndElement();
    }
    writer.WriteStartElement(NODE_BITMAP);
    {
      if (null != FullBitmap)
      {
        try
        {
          using (var stream = new MemoryStream())
          {
            FullBitmap.Save(stream, System.Drawing.Imaging.ImageFormat.Png);
            byte[] bytes = stream.GetBuffer();
            if (null != bytes && bytes.Length > 0)
              writer.WriteString(Convert.ToBase64String(bytes, Base64FormattingOptions.InsertLineBreaks));
          }
        }
        catch (Exception ex)
        {
          Rhino.Runtime.HostUtils.ExceptionReport(ex);
        }
      }
    }
    writer.WriteEndElement();
  }
  writer.WriteEndElement();
}
```

## Related Topics

- [Creating and Deploying Plugin Toolbars](/guides/rhinocommon/create-deploy-plugin-toolbar)

- [Localizing Plugin Toolbars](/guides/rhinocommon/localize-plugin-toolbar)

  ​
