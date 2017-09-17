---
title: Migrate your plugin project to Rhino 6 manually
description: This guide walks you through manually migrating your Rhino 5 plugin project to Rhino 6.
authors: ['Dale Fugier']
author_contacts: ['dale']
sdk: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Getting Started']
origin: unset
order: 7
keywords: ['c', 'C/C++', 'plugin']
layout: toc-guide-page
---


It is presumed you already have the necessary tools installed and are ready to go.  If you are not there yet, see [Installing Tools (Windows)]({{ site.baseurl }}/guides/cpp/installing-tools-windows).

## Migrating `CRhinoOptionsDialogPage` derived pages

### Header file changes

1. Open the H file containing your derived class.

2. Add the following include to your H file:

   ```
   #include "rhinoSdkTMfcPages.h"
   ```

3. Find your class declaration, for this example we will use the following:

   ```
   class CDocumentPropertiesPage : public CRhinoOptionsDialogPage
   {
   ....
   };
   ```

   Replace it with this:

   ```
   class CDocumentPropertiesPage : public TRhinoOptionsPage<CDialog>
   {
   ...
   };
   ```

   Your class will now use a Rhino provided template class which implements the `IRhinoOptionsPage` and `IRhinoWindow` interfaces.  The `IRhinoWindow` interface will wrap the `CDialog` class and provide direct access to window methods for creating, sizing, painting and destruction.  You can use any class that is derived from `CDialog` as long as the class constructor takes a resource Id and parent window.  The `TRhinoDialogWindow` template always pass `nullptr` as the parent window.

4. This is a list of Rhino 5 `CRhinoOptionsDialogPage` and `CRhinoStackedDialogPage` and there Rhino 6 equivalents.  You will need to modify these function declarations in your H file as well as there implementations.

   ```
   // V5 Method
   virtual const wchar_t* EnglishPageTitle() = 0;
   // V6 equivalent
   virtual const wchar_t* EnglishTitle() const = 0;

   // V5 Method
   virtual const wchar_t* LocalPageTitle() = 0;
   // V6 equivalent, returns EnglishTitle() by default
   virtual const wchar_t* LocalTitle() const;

   // V5 Method
   virtual CRhinoCommand::result RunScript( CRhinoDoc& rhino_doc) = 0;
   // V6 equivalent
   virtual CRhinoCommand::result RunScript(CRhinoOptionsPageEventArgs& e) = 0;

   // V5 Method
   virtual int OnActivate( BOOL bActive);
   // V6 equivalent, required in V6, called each time the page is displayed
   virtual void UpdatePage(CRhinoOptionsPageEventArgs& e) = 0;

   // V5 Method
   virtual int OnApply();
   // V6 equivalent, called when ever the page is hidden
   virtual bool Apply(CRhinoOptionsPageEventArgs& e);

   // V5 Method
   virtual bool ShowDefaultsButton(void);
   // V6 equivalent, can be used to add a Apply and/or Restore Defaults buttons to the
   // main dialog.  Returns RhinoOptionPageButtons::None by default.
   virtual RhinoOptionPageButtons ButtonsToDisplay() const;

   // V5 Method
   virtual void OnDefaults(void);
   // V6 equivalent
   virtual void OnRestoreDefaultsClick(CRhinoOptionsPageEventArgs& e);
   ```

### CPP Implementation file changes

1. Open the CPP file containing your derived class implementation.

2. Replace all references to `CRhinoOptionsDialogPage` with `__base_clas`  which dereferences to `CDialog` in our case because we derive from `TRhinoOptionsPage<CDialog>.`

3. Modify your class constructor to look something like this:

   ```
   COptionsPage::COptionsPage()
   : TRhinoOptionsPage<CDialog>(COptionsPage::IDD, 0, true)
   {
     
   }
   ```

   The arguments passed to the `TRhinoOptionsPage` constructor are the dialog resource Id, the icon resource Id and a Boolean telling the template to delete the page instance when the dialog closes.  The icon resource Id is currently not used by Windows and may be set to zero.

4. Rename your `EnglishPageTitle` and `LocalPageTitle` methods to `EnglishTitle` and `LocalTitle`respectively and add a `const` decoration to the functions.

5. Change your `RunScript` method to:

  ```
  CRhinoCommand::result CDocumentPropertiesPage::RunScript(CRhinoOptionsPageEventArgs& e)
  {
    // Access to the document assoicated with this options page if the page
    CRhinoDoc* doc = e.Document();
  }
  ```

  ​

6. Change your`OnActivate`  method to `UpdatePage`and modify as appropriate.  This is an example of a Rhino 5  `OnActivate` method that initializes the page when it is activated and show and applies the page changes when the page is deactivated and hidden.

  ```
  int CDocumentPropertiesPage::OnActivate( BOOL bActive)
  {
    // Applychanges when the page is deactivated/hidden and 
    // initialize page values when the page is activated/shown.
    // This allows multiple pages to share settings values

    // Apply changes when the page is no longer active
    if (!bActive)
      return OnApply();

    // Initialize the page when activated
    m_color_button.SetColor(CApp::App().ObjectColor(RhinoApp().ActiveDoc()));
    return true;
  }
  ```

  This is the Rhino 6 version that simply initializes the page, this method gets called each time the page is made visible.

  ```
  void CDocumentPropertiesPage::UpdatePage(CRhinoOptionsPageEventArgs& e)
  {
    // Initialize the page when activated
    m_color_button.SetColor(CApp::App().ObjectColor(e.Document()));
  }
  ```

7. Change your `OnApply` method to `Apply` and add the new `CRhinoOptionsPageEventArgs` parameter.  Rhino 5 only called `OnApply` when the dialog was closed, Rhino 6 calls `Apply`  when the page is hidden.
  This is an example of a simple Rhino 5 `OnApply` method.

  ```

  int CDocumentPropertiesPage::OnApply()
  {
    // Set the document specific object color
    CApp::App().SetObjectColor(RhinoApp().ActiveDoc(), m_color_button.Color());
    return true;
  }
  ```

  This is the Rhino 6 version which uses the document passed to the `Apply` method.

  ```
  bool CDocumentPropertiesPage::Apply(CRhinoOptionsPageEventArgs& e)
  {
    // Set the document specific object color
    CApp::App().SetObjectColor(e.Document(), m_color_button.Color());
    return true;
  }
  ```

8. If `ShowDefaultsButton` was overridden and returns true to display the "Restore Defaults" button when your page is activated then you will need to replace it with `ButtonsToDisplay` and or the buttons to display together or return None.  Rhino 5 only allows a page to specify displaying of the "Restore Defaults" button.  Rhino 6 allows a page to specify a "Apply" button as well.  This is a simple Rhino 5 example.

  ```
  bool ShowDefaultsButton(void) override { return true; }
  ```

  This is how you would accomplish this in Rhino 6.

  ```
  RhinoOptionPageButtons ButtonsToDisplay() const override
  {
    // You may use the following to display both the "Restore Defaults" and "Apply" buttons:
    // RhinoOptionPageButtons::DefaultButton | RhinoOptionPageButtons::ApplyButton
    return RhinoOptionPageButtons::DefaultButton;
  }
  ```

  In addition you will need to change your `OnDefaults` override to `OnRestoreDefaultsClick`.  This is an example of a simple Rhino 5  `OnDefaults`  override.

  ```
  void CDocumentPropertiesPage::OnDefaults(void)
  {
    // Set the color button to the default application object color
    m_color_button.SetColor(CApp::DEFULLT_OBJECT_COLOR);
  }

  ```

  This is the Rhino 6 version.

  ```
  void CDocumentPropertiesPage::OnRestoreDefaultsClick(CRhinoOptionsPageEventArgs& e)
  {
    // Get access to the CRhinoDoc associated with this page instance
    CRhinoDoc* doc = e.Document();
    // Set the color button to the default application object color
    m_color_button.SetColor(CApp::DEFULLT_OBJECT_COLOR);
  }

  ```

  ​

9. ​

## Migrating CRhinoObjectPropertiesDialogPage derived pages

