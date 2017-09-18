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

# Migrate your Options, Document Properties and Object Properties Pages

This guide walks you through migrating existing Rhino 5, plug-in provided, Rhino Options, Document Properties and Object Properties pages to Rhino 6.

You can find instructions regarding migrating your Rhino 5 plugin project to Rhino 6  [here]({{ site.baseurl }}/guides/cpp/migrate-your-plugin-manual-windows).

## Migrating `CRhinoOptionsDialogPage` derived pages

The `CRhinoOptionsDialogPage`  class is used to add pages to both the Options and Document Properties dialog sections.   The following is a description of what has changed in the Rhino 6 SDK and some simple examples of how to migrate your existing Rhino 5 code.

### Virtual method changes

Several virtual methods in the `CRhinoOptionsDialogPage`  and the `CRhinoStackedDialogPage`  base class have changed in Rhino 6.   The following is a list of commonly accessed Rhino 5 virtual methods and there Rhino 6 equivalents.

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

   Your class will now use a Rhino provided template class which implements the `IRhinoOptionsPage` and `IRhinoWindow` interfaces.  The `IRhinoWindow` interface will wrap the `CDialog` class and provide direct access to window methods for creating, sizing, painting and destruction.  You can use any class that is derived from `CDialog` as long as the class constructor takes a resource Id and parent window.  The `TRhinoDialogWindow` template always passes a  `nullptr` as the parent window.

4. Modify the `CRhinoOptionsDialogPage`  required virtual methods as follows:

   #### Rhino 5 class

   ```
   class CDocumentPropertiesPage : public CRhinoOptionsDialogPage
   {
     DECLARE_DYNAMIC(CDocumentPropertiesPage)

   public:
     CDocumentPropertiesPage();   // standard constructor
     virtual ~CDocumentPropertiesPage();

     /////////////////////////////////////////////////////////////////////////////
     // CRhinoOptionsDialogPage required overrides
     const wchar_t* EnglishPageTitle();
     const wchar_t* LocalPageTitle();
     CRhinoCommand::result RunScript( CRhinoDoc& rhino_doc);
   //... the rest of your class
   };
   ```

   #### Rhino 6 class

   ```
   class CDocumentPropertiesPage : public TRhinoOptionsPage<CDialog>
   {
     DECLARE_DYNAMIC(CDocumentPropertiesPage)

   public:
     CDocumentPropertiesPage();   // standard constructor
     virtual ~CDocumentPropertiesPage();

     /////////////////////////////////////////////////////////////////////////////
     // CRhinoOptionsDialogPage required overrides
     const wchar_t* EnglishTitle() const override;
     const wchar_t* LocalTitle() const override;
     CRhinoCommand::result RunScript(CRhinoOptionsPageEventArgs& e) override;
     //... the rest of your class
   };
   ```

5. See the "*Virtual method changes*" section above for a list of virtual methods that will need to be modified for Rhino 6.

### CPP Implementation file changes

1. Open the CPP file containing your derived class implementation.

2. Replace all references to `CRhinoOptionsDialogPage` with `__base_clas`  which dereferences to `CDialog` in our case because we are deriving from `TRhinoOptionsPage<CDialog>.`

   #### Rhino 5 class

   ```
   IMPLEMENT_DYNAMIC(CDocumentPropertiesPage, CRhinoOptionsDialogPage)

   BEGIN_MESSAGE_MAP(CDocumentPropertiesPage, CRhinoOptionsDialogPage)
   END_MESSAGE_MAP()
   ```

   #### Rhino 6 class

   ```
   IMPLEMENT_DYNAMIC(CDocumentPropertiesPage, __base_class)

   BEGIN_MESSAGE_MAP(CDocumentPropertiesPage, __base_class)
   END_MESSAGE_MAP()
   ```

3. Modify your class constructor.

   #### Rhino 5 class

   ```
   CDocumentPropertiesPage::CDocumentPropertiesPage()
   : CRhinoOptionsDialogPage(CDocumentPropertiesPage::IDD)
   {
   }
   ```

   #### Rhino 6 class

   The `TRhinoOptionsPage<CDialog>` constructor takes three arguments:

   1. Contains the ID number of a dialog-box template resource.
   2. Contains the ID number of a icon resource which is not currently used on Windows and may be zero.
   3.  If true the host will delete this page when the parent dialog window closes.

   ```
   COptionsPage::COptionsPage()
   : TRhinoOptionsPage<CDialog>(COptionsPage::IDD, 0, true)
   {  
   }
   ```

4. Rename your `EnglishPageTitle` and `LocalPageTitle` methods to `EnglishTitle` and `LocalTitle`respectively and add a `const` decoration to the functions.

   #### Rhino 5 code

   ```
   const wchar_t* CDocumentPropertiesPage::EnglishPageTitle() { return L"Test Page"; }
   const wchar_t* CDocumentPropertiesPage::LocalPageTitle() { return EnglishPageTitle(); }
   ```

   #### Rhino 6 code

   ```
   const wchar_t* CDocumentPropertiesPage::EnglishTitle() const { return L"Test Page"; }
   const wchar_t* CDocumentPropertiesPage::LocalTitle() const { return EnglishTitle(); }
   ```

   ​

5. Change the  `RunScript` 

  #### Rhino 5 code

  ```
  CRhinoCommand::result CDocumentPropertiesPage::RunScript(CRhinoDoc& rhino_doc)
  {
    return CRhinoCommand::success;
  }
  ```

  #### Rhino 6 code

  Replace the `CRhinoDoc&` argument with a `CRhinoOptionsPageEventArgs&`.

  ```
  CRhinoCommand::result CDocumentPropertiesPage::RunScript(CRhinoOptionsPageEventArgs& e)
  {
    // Access to the document assoicated with this options page if the page
    CRhinoDoc* doc = e.Document();
    return CRhinoCommand::success;
  }
  ```

  ​

6. Change your`OnActivate`  method to `UpdatePage`and modify as appropriate. 

  #### Rhino 5 code

  This Rhino 5  `OnActivate` method initializes the page when it is activated and shown and applies the page changes when the page is deactivated and hidden.

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

  #### Rhino 6 code

  This Rhino 6 method gets called each time the page is made activated and shown.  The Rhino 6 `Apply` method now gets called whenever the page is deactivated and hidden.

  ```
  void CDocumentPropertiesPage::UpdatePage(CRhinoOptionsPageEventArgs& e)
  {
    // Initialize the page when activated
    m_color_button.SetColor(CApp::App().ObjectColor(e.Document()));
  }
  ```
  ​

7. Change your `OnApply` method to `Apply` and add the new `CRhinoOptionsPageEventArgs` parameter.  Rhino 5 only called `OnApply` when the dialog was closed, Rhino 6 calls `Apply`  when the page is hidden.
  This is an example of a simple Rhino 5 `OnApply` method.

  #### Rhino 5 code

  ```
  int CDocumentPropertiesPage::OnApply()
  {
    // Set the document specific object color
    CApp::App().SetObjectColor(Document(), m_color_button.Color());
    return true;
  }
  ```

  #### Rhino 6 code

  Renamed to `Apply` and now takes a `CRhinoOptionsPageEventArgs&` parameter.

  ```
  bool CDocumentPropertiesPage::Apply(CRhinoOptionsPageEventArgs& e)
  {
    // The CRhinoOptionsPageEventArgs provides access the the CRhinoDoc
    // associated with this page
    // CRhinoDoc* doc = e.Document();
    // Set the document specific object color
    CApp::App().SetObjectColor(e.Document(), m_color_button.Color());
    return true;
  }
  ```

8. If your options page supports the "Restore Defaults" button you will need to do the following:

  #### Rhino 5 code

  ```
  bool CDocumentPropertiesPage::ShowDefaultsButton(void)
  {
    // Override and return true to display the "Restore Defaults" button
    return true;
  }
  // Called when the "Restore Defaults" button is clicked
  void CDocumentPropertiesPage::OnDefaults(void)
  {
    // Set the color button to the default application object color
    m_color_button.SetColor(CApp::DEFULLT_OBJECT_COLOR);
  }
  ```

  ####  Rhino 6 code

  Rhino 6 supports optionally adding "Restore Defaults" and "Apply" buttons by overriding the `ButtonsToDisplay`  method and returning the buttons to display or `RhinoOptionPageButtons::None` to hide all optional buttons.  The base class implementation returns `RhinoOptionPageButtons::None` by default.

  ```
  RhinoOptionPageButtons ButtonsToDisplay() const override
  {
    // You may use the following to display both the "Restore Defaults" and "Apply" buttons:
    // return RhinoOptionPageButtons::DefaultButton | RhinoOptionPageButtons::ApplyButton
    // Just add the "Restore Defaults" button
    return RhinoOptionPageButtons::DefaultButton;
  }
  ```

  The `OnDefaults` method was replace by the `OnRestoreDefaultsClick` method and the Apply button simply calls the `Apply` method.

  ```
  void CDocumentPropertiesPage::OnRestoreDefaultsClick(CRhinoOptionsPageEventArgs& e)
  {
    // Get access to the CRhinoDoc associated with this page instance
    // CRhinoDoc* doc = e.Document();
    // Set the color button to the default application object color
    m_color_button.SetColor(CApp::DEFULLT_OBJECT_COLOR);
  }
  ```

## Migrating `CRhinoObjectPropertiesDialogPageEx` derived pages

The `CRhinoObjectPropertiesDialogPageEx`  is used to add pages to the Rhino object properties panel.  The class provides the navigation control image, text and actual content page to be added.  The following is a description of what has changed in the Rhino 6 SDK and some simple examples of how to migrate your existing version 5 code.

### Header file changes

1. Open the H file containing your derived class.

2. Add the following include to your H file:

   ```
   #include "rhinoSdkTMfcPages.h"
   ```

3. Find your class declaration, for this example we will use the following:

   ```
   class CPropertiesPage : public CRhinoObjectPropertiesDialogPageEx
   {
   ....
   };
   ```

   Replace it with this:

   ```
   class CDocumentPropertiesPage : public TRhinoPropertiesPanelPage<CDialog>
   {
   ...
   };
   ```

   Your class will now use a Rhino provided template class which implements the `IRhinoPropertiesPanelPage` and `IRhinoWindow` interfaces.  The `IRhinoWindow` interface will wrap the `CDialog` class and provide direct access to window methods for creating, sizing, painting and destruction.  You can use any class that is derived from `CDialog` as long as the class constructor takes a resource Id and parent window.  The `TRhinoDialogWindow` template always pass `nullptr` as the parent window.


1. This is a list of Rhino 5 `CRhinoObjectPropertiesDialogPage` and `CRhinoStackedDialogPage` and there Rhino 6 equivalents.  You will need to modify these function declarations in your H file as well as there implementations.

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

### 