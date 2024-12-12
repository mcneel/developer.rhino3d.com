+++
aliases = [ ]
authors = [ "callum", "curtis" ]
categories = [ "Eto" ]
description = "Using the already available dialogs available in Eto makes your application more consistent with Rhino and the operating system your Plug-in is running on. It also saves you time and effort."
keywords = [ "rhino", "developer", "eto", "ui", "ux" ]
languages = [ "C#", "Python" ]
sdk = "eto"
title = "Existing Dialogs"
type = "guides"

[admin]
TODO = ""
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]

+++

## Message Box
[MessageBox](http://pages.picoe.ca/docs/api/html/T_Eto_Forms_MessageBox.htm) is a very simple and highly useful dialog for handling control flow and allowing users to make informed decisions.

{{< row >}}
{{< column >}}

<div class="codetab">
  <button class="tablinks" onclick="openCodeTab(event, 'cs')" id="defaultOpen">C#</button>
  <button class="tablinks" onclick="openCodeTab(event, 'py')">Python</button>
</div>

<div class="tab-content">
  <div class="codetab-content" id="cs">

  ```cs
using Eto.Forms;

var result = MessageBox.Show("Would you like to save before closing?",
                             MessageBoxButtons.YesNo,
                             MessageBoxType.Question,
                             MessageBoxDefaultButton.Yes);

if (result != DialogResult.Yes)
{
    MessageBox.Show("Model discarded successfully!", MessageBoxButtons.OK, MessageBoxType.Information);
}
else
{
    MessageBox.Show("Model saved successfully before closing.", MessageBoxButtons.OK, MessageBoxType.Information);
}
  ```

  </div>

  <div class="codetab-content" id="py">

  ```py
import scriptcontext as sc

from Eto.Forms import *
from Rhino.UI import RhinoEtoApp

parent = RhinoEtoApp.MainWindowForDocument(sc.doc)

result = MessageBox.Show("Would you like to save before closing?",
                             MessageBoxButtons.YesNo,
                             MessageBoxType.Question,
                             MessageBoxDefaultButton.Yes)

if result != DialogResult.Yes:
    MessageBox.Show("Model discarded successfully!", MessageBoxButtons.OK, MessageBoxType.Information)

else:
    MessageBox.Show("Model saved successfully before closing.", MessageBoxButtons.OK, MessageBoxType.Information)
  ```

  </div>
</div>

{{< /column >}}
{{< column >}}

![Message Boxes](/images/eto/controls/message-boxes.png)

{{< /column >}}
{{< /row >}}


## Color Picker
The Color Picker is a button that shows the [ColorDialog](http://api.etoforms.picoe.ca/html/T_Eto_Forms_ColorDialog.htm). The Color Dialog can also be used separately.

{{< row >}}
{{< column >}}

<div class="codetab">
  <button class="tablinks1" onclick="openCodeTab(event, 'cs1')" id="defaultOpen">C#</button>
  <button class="tablinks1" onclick="openCodeTab(event, 'py1')">Python</button>
</div>

<div class="tab-content">
  <div class="codetab-content1" id="cs1">

  ```cs
  using Eto.Forms;

  var dialog = new Dialog()
  {
    Width = 80,
    Height = 80,
    Padding = 8,
    Content = new ColorPicker();
  }
  
  dialog.ShowModal();
  ```

  </div>

  <div class="codetab-content1" id="py1">

  ```py
from Eto.Forms import *
from Eto.Drawing import Padding

dialog = Dialog()
dialog.Width = 80
dialog.Height = 80
dialog.Padding = Padding(8)
dialog.Content = ColorPicker()

dialog.ShowModal()
  ```

  </div>
</div>

{{< /column >}}
{{< column >}}

![Color Picker](/images/eto/controls/colour-picker.png)

{{< /column >}}
{{< /row >}}


## File Dialogs
File dialogs make prompting users to choose new and existing files simple.

If you need to prompt for a folder, there is the [SelectFoldereDialog](http://pages.picoe.ca/docs/api/html/T_Eto_Forms_SelectFolderDialog.htm)

{{< call-out warning "Your Data is Safe" >}}
  The below example **does not** save or open any files you choose.
  It only shows dialogs that assist in getting file names.
{{< /call-out >}}

{{< row >}}
{{< column >}}

<div class="codetab">
  <button class="tablinks2" onclick="openCodeTab(event, 'cs2')" id="defaultOpen">C#</button>
  <button class="tablinks2" onclick="openCodeTab(event, 'py2')">Python</button>
</div>

<div class="tab-content">
  <div class="codetab-content2" id="cs2">

  ```cs
using Eto.Forms;

var parent = Rhino.UI.RhinoEtoApp.MainWindowForDocument(__rhino_doc__);

var openDialog = new OpenFileDialog()
{
    Filters = {
        new FileFilter("Any", "*.*")
    },
    CurrentFilterIndex = 0,
    CheckFileExists = true,
    MultiSelect = true,
    Title = "Pick a file, any file"
};

var result = openDialog.ShowDialog(parent);
if (result == DialogResult.Cancel)
{
    MessageBox.Show("No File chosen!", MessageBoxType.Information);
    return;
}

var saveDialog = new SaveFileDialog()
{
    Title = "Save your file",
    Directory = openDialog.Directory,
    FileName = openDialog.FileName
};

result = saveDialog.ShowDialog(parent);

if (result == DialogResult.Cancel)
{
    MessageBox.Show("File not saved!", MessageBoxType.Information);
    return;
}
  ```

  </div>

  <div class="codetab-content2" id="py2">

  ```py
import scriptcontext as sc

from Eto.Forms import *
from Rhino.UI import RhinoEtoApp
import Rhino

parent = Rhino.UI.RhinoEtoApp.MainWindowForDocument(sc.doc);

openDialog = OpenFileDialog()
openDialog.Filters.Add(FileFilter("Any", "*.*"));
openDialog.CurrentFilterIndex = 0
openDialog.CheckFileExists = True
openDialog.MultiSelect = True
openDialog.Title = "Pick a file, any file"

result = openDialog.ShowDialog(parent);
if result == DialogResult.Cancel:
    MessageBox.Show("No File chosen!", MessageBoxType.Warning)
else:
    saveDialog = SaveFileDialog()
    saveDialog.Title = "Save your file"
    saveDialog.Directory = openDialog.Directory
    saveDialog.FileName = openDialog.FileName

    result = saveDialog.ShowDialog(parent)

    if result == DialogResult.Cancel:
        MessageBox.Show("File not saved!", MessageBoxType.Warning)
    else:
        MessageBox.Show("File saved", MessageBoxType.Information)
  ```

  </div>
</div>

{{< /column >}}
{{< column >}}

![File Dialogs](/images/eto/controls/file-dialogs.png)

{{< /column >}}
{{< /row >}}

