+++
aliases = [ ]
authors = [ "callum", "curtis" ]
categories = [ "Eto" ]
description = "An introduction to Forms and Dialogs"
keywords = [ "rhino", "developer", "eto", "ui", "ux" ]
languages = [ "C#", "Python" ]
sdk = "eto"
title = "Forms and Dialogs"
type = "guides"

[admin]
TODO = ""
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]

+++

## What's the difference?
Dialogs are modal, Forms are non-modal. Which just means that when you show a dialog, the program blocks further input until the dialog is closed. A form however allows for input to continue. Let's look at a simple example.


<div class="codetab">
  <button class="tablinks" onclick="openCodeTab(event, 'cs')" id="defaultOpen">C#</button>
  <button class="tablinks" onclick="openCodeTab(event, 'py')">Python</button>
</div>

<div class="tab-content">
  <div class="codetab-content" id="cs">

  ```cs
  using Eto.Forms;

  var form = new Form();
  form.Show();

  var dialog = new Dialog();
  dialog.ShowModal(); // <-- Code execution stops here
  ```

  </div>

  <div class="codetab-content" id="py">

  ```py
  #! python3
  import scriptcontext as sc

  from Eto.Forms import Form, Dialog

  form = Form()
  form.Show()

  dialog = Dialog()
  dialog.ShowModal() # <-- Code execusion stops here
  ```

  </div>
</div>

If you paste this into your script editor and run, the Form will show, and then the dialog, however code written after the dialog will not be run until the dialog is closed. It is important to choose a Form or Dialog correctly. It can however be changed easily later on, without much work.

# Forms
Forms are best used when you want to present information or controls to the user that mix input between the form and the parent window, i.e Rhino. If you want users to be able to run commands and interact with Rhino, a form is the most flexible choice.

For example, a form would be best suited to a help window that the user might consult whilst using Rhino, or a window of controls a custom visibility mode on objects to help understand curvature.


# Dialogs

Dialogs are best used when you need to force the user to make a decision before continuing. For example, choosing a file to open, or alerting the user that an error has occured.

[Dialog](pages.picoe.ca/docs/api/html/N_Eto_Dialog.htm) is available in two flavours, `Dialog`, and `Dialog<T>`. 
`Dialog<T>` returns a result on closing which is very useful for obtaining the result of a user choice, such as Ok or Cancel or even a filename.

<!-- TODO : Research DialogDisplayMode> -->

## Semi-Model Dialogs
Dialogs can also be run as semi-modal, meaning, code execution is blocked, but the user can still input information to the command line and interact with Rhino.

<div class="codetab">
  <button class="tablinks1" onclick="openCodeTab(event, 'cs1')" id="defaultOpen1">C#</button>
  <button class="tablinks1" onclick="openCodeTab(event, 'py1')">Python</button>
</div>

<div class="tab-content">
  <div class="codetab-content1" id="cs1">

  ```cs
    var dialog = new Dialog();
    var parent = RhinoEtoApp.MainWindowForDocument(__rhino_doc__);
    
    // DefaultButton and AbortButton is required for SemiModal
    dialog.DefaultButton = new Button()
    dialog.AbortButton = new Button()

    dialog.ShowSemiModal(doc, parent);
  ```

  </div>
  <div class="codetab-content1" id="py1">

  ```py
  #! python3
  import scriptcontext as sc

  from Rhino.UI import RhinoEtoApp, EtoExtensions
  from Eto.Forms import Dialog, Button

  parent = RhinoEtoApp.MainWindowForDocument(sc.doc)

  dialog = Dialog()
  # DefaultButton and AbortButton is required for SemiModal
  dialog.DefaultButton = Button()
  dialog.AbortButton = Button()

  EtoExtensions.ShowSemiModal(dialog, sc.doc, parent)
  ```

  </div>
</div>



## Modal Summary
<table class="rounded">
  <tr>
    <th>Type</th>
    <th>Stops Code Execution</th>
    <th>Prevents input outside the window</th>
  </tr>
  <tr>
    <td><b>Form</b></td>
    <td>❌</td>
    <td>❌</td>
  </tr>
  <tr>
    <td><b>Dialog</b></td>
    <td>✔️</td>
    <td>✔️</td>
  </tr>
  <tr>
    <td><b>Dialog (SemiModal)</b></td>
    <td>✔️</td>
    <td>❌</td>
  </tr>
</table>