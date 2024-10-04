+++
aliases = ["/en/5/guides/cpp/migrate-properties-pages-windows/", "/en/6/guides/cpp/migrate-properties-pages-windows/", "/en/7/guides/cpp/migrate-properties-pages-windows/", "/wip/guides/cpp/migrate-properties-pages-windows/"]
authors = [ "johnm" ]
categories = [ "Getting Started" ]
description = "This guide walks you through migrating existing Rhino 5, plug-in provided, Options, Document Properties and Object Properties pages to Rhino 6."
keywords = [ "c", "C/C++", "plugin", "options", "properties" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Migrate your Options, Document Properties and Object Properties Pages"
type = "guides"
weight = 7
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++

You can find instructions regarding migrating your Rhino 5 plugin project to Rhino 6  [here](/guides/cpp/migrate-your-plugin-manual-windows).

The code used in this document is available on GitHub [here](https://github.com/mcneel/rhino-developer-samples/tree/6/cpp/SampleMigration).

## Migrating `CRhinoPlugIn` derived class

The Rhino 5 `CRhinoPlugIn` class includes `AddPagesToObjectPropertiesDialog`, `AddPagesToOptionsDialog` and `AddPagesToDocumentPropertiesDialog` virtual methods which may be overridden when adding custom pages to the Options, Document Properties and Object Properties dialogs.  These methods have been modified in Rhino 6 and will require changes to your derived plug-in classes.

#### Rhino 5 code

```
void CSamplePropertiesPagesPlugIn::AddPagesToObjectPropertiesDialog(
  ON_SimpleArray<class CRhinoObjectPropertiesDialogPage*>& pages)
{
  pages.Append(&m_properties_page);
}

void CSamplePropertiesPagesPlugIn::AddPagesToOptionsDialog(
  HWND hwndParent,
  ON_SimpleArray<CRhinoOptionsDialogPage*>& pages)
{
  pages.Append(new COptionsPage());
}

void CSamplePropertiesPagesPlugIn::AddPagesToDocumentPropertiesDialog(
  CRhinoDoc& doc,
  HWND hwndParent,
  ON_SimpleArray<CRhinoOptionsDialogPage*>& pages)
{
  pages.Append(new CDocumentPropertiesPage(doc));
}
```

#### Rhino 6 code

```
void CSamplePropertiesPagesPlugIn::AddPagesToObjectPropertiesDialog(
  CRhinoPropertiesPanelPageCollection& collection)
{
  collection.Add(&m_properties_page);
}

void CSamplePropertiesPagesPlugIn::AddPagesToOptionsDialog(
  CRhinoOptionsPageCollection& collection)
{
  collection.AddPage(new COptionsPage());
}

void CSamplePropertiesPagesPlugIn::AddPagesToDocumentPropertiesDialog(
  CRhinoOptionsPageCollection& collection)
{
  collection.AddPage(new CDocumentPropertiesPage());
}
```

## Migrating `CRhinoOptionsDialogPage` derived pages

The `CRhinoOptionsDialogPage`  class is used to add pages to both the Options and Document Properties dialog sections.   The following is a description of what has changed in the Rhino 6 SDK and some simple examples of how to migrate your existing Rhino 5 code.

### Virtual method changes

Several virtual methods in the `CRhinoOptionsDialogPage`  and the `CRhinoStackedDialogPage`  base class have changed in Rhino 6.   The following is a list of commonly overridden Rhino 5 virtual methods and their Rhino 6 equivalents.

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

4. Modify the `CRhinoObjectPropertiesDialogPage` required virtual methods as follows:

   #### Rhino 5 class

   ```
   class CDocumentPropertiesPage : public CRhinoOptionsDialogPage
   {
     DECLARE_DYNAMIC(CDocumentPropertiesPage)

   public:
     CDocumentPropertiesPage(CRhinoDoc& doc);   // standard constructor
     virtual ~CDocumentPropertiesPage();

     /////////////////////////////////////////////////////////////////////////////
     // CRhinoOptionsDialogPage required overrides
     const wchar_t* EnglishPageTitle() override;
     const wchar_t* LocalPageTitle() override;
     CRhinoCommand::result RunScript( CRhinoDoc& rhino_doc) override;
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

  5. See the [Virtual method changes](#migrating-crhinooptionsdialogpage-derived-pages) section above for a list of virtual methods that will need to be modified for Rhino 6.

### CPP Implementation file changes

1. Open the CPP file containing your derived class implementation.

2. Replace all references to `CRhinoOptionsDialogPage` with `__base_class`  which dereferences to `CDialog` in our case because we are deriving from `TRhinoOptionsPage<CDialog>.`

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
   3. If true the host will delete this page when the parent dialog window closes.

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

5. Change the  `RunScript` override.

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

7. Change your `OnApply` method to `Apply` and add the new `CRhinoOptionsPageEventArgs` parameter.  Rhino 5 only called the  `OnApply`  when the dialog was closed, Rhino 6 calls `Apply`  whenever the page is hidden.

  #### Rhino 5 code

  ```
  int CDocumentPropertiesPage::OnApply()
  {
    // Set the document specific object color
    CApp::App().SetObjectColor(m_doc, m_color_button.Color());
    return true;
  }
  ```

  #### Rhino 6 code

  Renamed to `Apply` and now takes a `CRhinoOptionsPageEventArgs&` parameter.

  ```
  bool CDocumentPropertiesPage::Apply(CRhinoOptionsPageEventArgs& e)
  {
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

  Rhino 6 supports optionally adding "Restore Defaults" and "Apply" buttons by overriding the `ButtonsToDisplay`  method and returning the buttons to include or  `RhinoOptionPageButtons::None` to hide all optional buttons.  The base class implementation returns `RhinoOptionPageButtons::None` by default.

  ```
  RhinoOptionPageButtons ButtonsToDisplay() const override
  {
    // You may use the following to display both the "Restore Defaults" and "Apply" buttons:
    // return RhinoOptionPageButtons::DefaultButton | RhinoOptionPageButtons::ApplyButton
    // Just add the "Restore Defaults" button
    return RhinoOptionPageButtons::DefaultButton;
  }
  ```

  The `OnDefaults` method was replace by the `OnRestoreDefaultsClick` method and the Apply button calls the `Apply` method.

  ```
  void CDocumentPropertiesPage::OnRestoreDefaultsClick(CRhinoOptionsPageEventArgs& e)
  {
    // Get access to the CRhinoDoc associated with this page instance
    // CRhinoDoc* doc = e.Document();
    // Set the color button to the default application object color
    m_color_button.SetColor(CApp::DEFULLT_OBJECT_COLOR);
  }
  ```

## Migrating `CRhinoObjectPropertiesDialogPage` or `CRhinoObjectPropertiesDialogPageEx` derived pages

The `CRhinoObjectPropertiesDialogPage`  and `CRhinoObjectPropertiesDialogPageEx`  classes are used to add pages to the Rhino object properties panel in Rhino 5.  The following is a description of what has changed in the Rhino 6 SDK and some simple examples of how to migrate your existing Rhino 5 code.

### Virtual method changes

Several virtual methods in the `CRhinoObjectPropertiesDialogPage` ,  `CRhinoObjectPropertiesDialogPageEx`  and the `CRhinoStackedDialogPage`  base class have changed in Rhino 6.   The following is a list of commonly overridden Rhino 5 virtual methods and their Rhino 6 equivalents.

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
virtual CRhinoCommand::result RunScript(ON_SimpleArray<const CRhinoObject*>& objects) = 0;
// V6 equivalent
virtual CRhinoCommand::result RunScRunScript(IRhinoPropertiesPanelPageEventArgs& e) = 0;

// V5 Method
virtual BOOL AddPageToControlBar( const CRhinoObject* obj = NULL) const = 0;
// V6 equivalent
virtual bool IncludeInNavigationControl(IRhinoPropertiesPanelPageEventArgs& args) const = 0;

// V5 Method
virtual void InitControls( const CRhinoObject* new_obj = NULL) = 0;
// V6 equivalent, called when ever the page is hidden
virtual void UpdatePage(IRhinoPropertiesPanelPageEventArgs& e) = 0;

// V5 Method
virtual page_type PageType() const;
// V6 equivalent, can be used to add a Apply and/or Restore Defaults buttons to the
// main dialog.  Returns RhinoOptionPageButtons::None by default.
virtual RhinoPropertiesPanelPageType PageType() const;

// V5 Method
virtual int SelectedObjectCount() const;
const CRhinoObject* GetSelectedObject( int index) const;
// V6 equivalen
// You can call the following to get the IRhinoPropertiesPanelPageEventArgs associated
// with a specific page.  IRhinoPropertiesPanelPageEventArgs contains  ObjectCount and
// ObjectAt methods which provide access to the selected object list.
//IRhinoPropertiesPanelPageEventArgs* args = IRhinoPropertiesPanelPageEventArgs::FromPage(this);

// V5 Event watcher methods
virtual void OnCloseDocument(CRhinoDoc& doc );
virtual void OnNewDocument(CRhinoDoc& doc );
virtual void OnBeginOpenDocument(
  CRhinoDoc& doc,
  const wchar_t* filename,
  BOOL bMerge,
  BOOL bReference);
virtual void OnEndOpenDocument(
  CRhinoDoc& doc,
  const wchar_t* filename,
  BOOL bMerge,
  BOOL bReference);
virtual void OnBeginSaveDocument(
  CRhinoDoc& doc,
  const wchar_t* filename,
  BOOL bExportSelected);
virtual void OnEndSaveDocument(
  CRhinoDoc& doc,
  const wchar_t* filename,
  BOOL bExportSelected);
virtual void OnDocumentPropertiesChanged( CRhinoDoc& doc);
virtual void OnModifyObjectAttributes(
  CRhinoDoc& doc,
  CRhinoObject& object,
  const CRhinoObjectAttributes& old_attributes);
virtual void LayerTableEvent(
  CRhinoEventWatcher::layer_event event,
  const CRhinoLayerTable& layer_table, 
  int layer_index,
  const ON_Layer* old_settings);
virtual void LightTableEvent(
  CRhinoEventWatcher::light_event event,
  const CRhinoLightTable& light_table,
  int light_index,
  const ON_Light* old_settings);
virtual void MaterialTableEvent(
  CRhinoEventWatcher::material_event event,
  const CRhinoMaterialTable& material_table,
  int material_index,
  const ON_Material* old_settings);
virtual void GroupTableEvent(
  CRhinoEventWatcher::group_event event,
  const CRhinoGroupTable& group_table,
  int group_index,
  const ON_Group* old_settings);
virtual void FontTableEvent(
  CRhinoEventWatcher::font_event event,
  const CRhinoFontTable& font_table,
  int font_index,
  const ON_Font* old_settings);
virtual void DimStyleTableEvent(
  CRhinoEventWatcher::dimstyle_event event,
  const CRhinoDimStyleTable& dimstyle_table,
  int dimstyle_index,
  const ON_DimStyle* old_settings);
virtual void HatchPatternTableEvent(
  CRhinoEventWatcher::hatchpattern_event event,
  const CRhinoHatchPatternTable& hatchpattern_table,
  int hatchpattern_index,
  const ON_HatchPattern* old_settings);
virtual void LinetypeTableEvent(
  CRhinoEventWatcher::linetype_event event,
  const CRhinoLinetypeTable& linetype_table,
  int linetype_index,
  const ON_Linetype* old_settings);
void OnAppSettingsChanged(const CRhinoAppSettings& new_app_settings);
void OnUpdateObjectMesh(CRhinoDoc& doc, CRhinoObject& object, ON::mesh_type mesh_type);
void InstanceDefinitionTableEvent(
  CRhinoEventWatcher::idef_event event,
  const CRhinoInstanceDefinitionTable& idef_table,
  int idef_index,
  const ON_InstanceDefinition* old_settings);

//V6 equivalent, see the optional IRhinoPropertiesPanelPageEventWatcher interface
```

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
   CPropertiesPage : public TRhinoPropertiesPanelPage<CDialog>
   {
   ...
   };
   ```

   Your class will now use a Rhino provided template class which implements the `IRhinoPropertiesPanelPage` and `IRhinoWindow` interfaces.  The `IRhinoWindow` interface will wrap the `CDialog` class and provide direct access to window methods for creating, sizing, painting and destruction.  You can use any class that is derived from `CDialog` as long as the class constructor takes a resource Id and parent window.  The `TRhinoDialogWindow` template always passes a  `nullptr` as the parent window.

4. Modify the `CRhinoObjectPropertiesDialogPage`  required virtual methods as follows:

   #### Rhino 5 class

   ```
   class CPropertiesPage : public CRhinoObjectPropertiesDialogPageEx
   {
     DECLARE_DYNAMIC(CPropertiesPage)

   public:
     CPropertiesPage();   // standard constructor
     virtual ~CPropertiesPage();

     /////////////////////////////////////////////////////////////////////////////
     // CRhinoObjectPropertiesDialogPage required overrides
     void InitControls( const CRhinoObject* new_obj = NULL);
     BOOL AddPageToControlBar( const CRhinoObject* obj = NULL) const;
     CRhinoCommand::result RunScript( ON_SimpleArray<const CRhinoObject*>& objects);
     /////////////////////////////////////////////////////////////////////////////
     // CRhinoObjectPropertiesDialogPageEx required overrides
     HICON Icon(void) const;
     /////////////////////////////////////////////////////////////////////////////
     // CRhinoStackedDialogPag required overrides
     const wchar_t* EnglishPageTitle();
     const wchar_t* LocalPageTitle();
   //... the rest of your class
   };
   ```

   #### Rhino 6 class

   ```
   class CPropertiesPage : public TRhinoPropertiesPanelPage<CDialog>
   {
     DECLARE_DYNAMIC(CPropertiesPage)

   public:
     CPropertiesPage();   // standard constructor
     virtual ~CPropertiesPage();

     /////////////////////////////////////////////////////////////////////////////
     // CRhinoOptionsDialogPage required overrides
     void UpdatePage(IRhinoPropertiesPanelPageEventArgs& e) override;
     bool IncludeInNavigationControl(IRhinoPropertiesPanelPageEventArgs& e) const override;
     CRhinoCommand::result RunScript(IRhinoPropertiesPanelPageEventArgs& e) override;
     /////////////////////////////////////////////////////////////////////////////
     // CRhinoObjectPropertiesDialogPageEx required overrides
     // Handled by TRhinoPropertiesPanelPage, you can delete the Icon override
     //HICON Icon(void) const;
     /////////////////////////////////////////////////////////////////////////////
     // CRhinoStackedDialogPag required overrides
     const wchar_t* EnglishTitle() const override;
     const wchar_t* LocalTitle() const override;
     //... the rest of your class
   };
   ```

5. See the [Virtual method changes](#migrating-crhinoobjectpropertiesdialogpage-or-crhinoobjectpropertiesdialogpageex-derived-pages) section above for a list of virtual methods that will need to be modified for Rhino 6.

### CPP Implementation file changes

1. Open the CPP file containing your derived class implementation.

2. Replace all references to `CRhinoObjectPropertiesDialogPageEx` or `CRhinoObjectPropertiesDialogPage` with `__base_class`  which dereferences to `CDialog` in our case because we are deriving from `TRhinoOptionsPage<CDialog>.`

   #### Rhino 5 class

   ```
   IMPLEMENT_DYNAMIC(CPropertiesPage, CRhinoObjectPropertiesDialogPageEx)

   BEGIN_MESSAGE_MAP(CPropertiesPage, CRhinoObjectPropertiesDialogPageEx)
   END_MESSAGE_MAP()
   ```

   #### Rhino 6 class

   ```
   IMPLEMENT_DYNAMIC(CPropertiesPage, __base_class)

   BEGIN_MESSAGE_MAP(CPropertiesPage, __base_class)
   END_MESSAGE_MAP()
   ```

3. Modify your class constructor.

   #### Rhino 5 class

   ```
   CPropertiesPage::CPropertiesPage()
   : CRhinoObjectPropertiesDialogPageEx(CPropertiesPage::IDD, NULL)
   , m_icon(NULL)
   {
   }
   ```

   #### Rhino 6 class

   The `TRhinoPropertiesPanelPage<CDialog>` constructor takes three arguments:

   1. Contains the ID number of a dialog-box template resource.
   2. Contains the ID number of a icon resource.
   3. If true the host will delete this page when it is no longer referenced.

   ```
   CPropertiesPage::CPropertiesPage()
   : TRhinoPropertiesPanelPage<CDialog>(CPropertiesPage::IDD, IDI_PROPERTIES_PAGE, false)
   {
   }
   ```

4. Rename your `EnglishPageTitle` and `LocalPageTitle` methods to `EnglishTitle` and `LocalTitle`respectively and add a `const` decoration to the functions.

   #### Rhino 5 code

   ```
   const wchar_t* CPropertiesPage::EnglishPageTitle() { return L"Test Properties Page"; }
   const wchar_t* CPropertiesPage::LocalPageTitle() { return EnglishPageTitle(); }
   ```

   #### Rhino 6 code

   ```
   const wchar_t* CPropertiesPage::EnglishTitle() const { return L"Test Properties Page"; }
   const wchar_t* CPropertiesPage::LocalTitle() const { return EnglishTitle(); }
   ```

5. Remove the `CRhinoObjectPropertiesDialogPageEx::Icon` override, the icon resource Id is now passed to the base class constructor.

6. Change the  `RunScript` override.

   #### Rhino 5 code

   ```
   CRhinoCommand::result CPropertiesPage::RunScript(ON_SimpleArray<const CRhinoObject*>& objects)
   {
     return CRhinoCommand::success;
   }
   ```

   #### Rhino 6 code

   Replace the `CRhinoDoc&` argument with a `CRhinoOptionsPageEventArgs&`.

   ```
   CRhinoCommand::result CPropertiesPage::RunScript(IRhinoPropertiesPanelPageEventArgs& e)
   {
     return CRhinoCommand::success;
   }
   ```

7. Rename your `InitControls` method to `UpdatePage` and change the parameters accordingly.

   #### Rhino 5 code

   The selected object list is accessed via the `CRhinoObjectPropertiesDialogPage::SelectedObjectCount` and `CRhinoObjectPropertiesDialogPage::GetSelectedObject` methods in Rhino 5.

   ```
   void CPropertiesPage::InitControls( const CRhinoObject* new_obj)
   {
     int our_color_objects = 0;
     CRhinoDoc* doc = nullptr;
     for (int i = 0, count = SelectedObjectCount(); i < count; i++)
     {
       const CRhinoObject* object = GetSelectedObject(i);
       if (object && doc == NULL)
         doc = object->Document();
       if (IncludeObject(object) && IsOurColor(object))
         our_color_objects++;
     }
     ON_wString message;
     message.Format(L"%d Colored objects selected", our_color_objects);
     m_message_text.SetWindowText(message);
     if (doc)
       m_color_swatch.SetColor(CApp::App().ObjectColor(doc));
     else
       m_color_swatch.SetColor(::GetSysColor(COLOR_BTNFACE));
   }
   ```

   #### Rhino 6 code

   The  selected object list is accessed via the provided `IRhinoPropertiesPanelPageEventArgs` parameter in Rhino 6.

   ```
   void CPropertiesPage::UpdatePage(IRhinoPropertiesPanelPageEventArgs& e)
   {
     int our_color_objects = 0;
     CRhinoDoc* doc = nullptr;
     for (int i = 0, count = e.ObjectCount(); i < count; i++)
     {
       const CRhinoObject* object = e.ObjectAt(i);
       if (object && doc == NULL)
         doc = object->Document();
       if (IncludeObject(object) && IsOurColor(object))
         our_color_objects++;
     }
     ON_wString message;
     message.Format(L"%d Colored objects selected", our_color_objects);
     m_message_text.SetWindowText(message);
     if (doc)
       m_color_swatch.SetColor(CApp::App().ObjectColor(doc));
     else
       m_color_swatch.SetColor(::GetSysColor(COLOR_BTNFACE));
   }
   ```

8. Rename your `AddPageToControlBar` method to `IncludeInNavigationControl` , change the return type to `bool` and change the parameters accordingly.

   #### Rhino 5 code

   The selected object list is accessed via the `CRhinoObjectPropertiesDialogPage::SelectedObjectCount` and `CRhinoObjectPropertiesDialogPage::GetSelectedObject` methods in Rhino 5.

   ```
   BOOL CPropertiesPage::AddPageToControlBar( const CRhinoObject* obj) const
   {
     // Only care if one or more meshable object is selected
     for (int i = 0, count = SelectedObjectCount(); i < count; i++)
       if (IncludeObject(GetSelectedObject(i)))
         return true;
     return false;
   }
   bool CPropertiesPage::IncludeObject(const CRhinoObject* object) const
   {
     return object && object->Document() && object->IsMeshable(ON::render_mesh);
   }
   ```

   #### Rhino 6 code

   The  selected object list is accessed via the provided `IRhinoPropertiesPanelPageEventArgs` parameter in Rhino 6.

   ```
   bool CPropertiesPage::IncludeInNavigationControl(IRhinoPropertiesPanelPageEventArgs& e) const
   {
     // Only care if one or more mesh-able object is selected
     for (int i = 0, count = e.ObjectCount(); i < count; i++)
       if (IncludeObject(e.ObjectAt(i)))
         return true;
     return false;
   }
   bool CPropertiesPage::IncludeObject(const CRhinoObject* object) const
   {
     return object && object->Document() && object->IsMeshable(ON::render_mesh);
   }
   ```

   ​

9. Replace your object modification code with a call to `ModifyPage` and override `OnModifyPage` to preform the actual object modification.

   #### Rhino 5 code

   In Rhino 5 you would typically create a hidden test command and call it to modify the selected object list.  This is done to provide undo support and trigger the correct update events in the properties panel.

   ```
   class CPropertiesPageCommand : public CRhinoTestCommand
   {
   public:
     CPropertiesPageCommand()
     : m_by_layer(false)
     , m_page(nullptr)
     {
     }

     ~CPropertiesPageCommand()
     {
     }

     // Returns a unique UUID for this command.
     // If you try to use an id that is already being used, then
     // your command will not work.  Use GUIDGEN.EXE to make unique UUID.
   	UUID CommandUUID()
   	{
   		// {E547CD29-920F-4EF9-92EC-3F4AE9D9E619}
       static const GUID command_id =
       { 0xe547cd29, 0x920f, 0x4ef9, { 0x92, 0xec, 0x3f, 0x4a, 0xe9, 0xd9, 0xe6, 0x19 } };
       return command_id;
   	}

     // Returns the English command name.
   	const wchar_t* EnglishCommandName() { return L"TestPropertiesPageModifyObjects"; }

     // Returns the localized command name.
   	const wchar_t* LocalCommandName() const { return L"TestPropertiesPageModifyObjects"; }

     // Rhino calls RunCommand to run the command.
   	CRhinoCommand::result RunCommand( const CRhinoCommandContext& );

     bool m_by_layer;
     ON_SimpleArray<ON_UUID>m_object_ids;
     CPropertiesPage* m_page;

     CRhinoCommand::result MakeByLayer(ON_SimpleArray<const CRhinoObject*>& objectList);
     CRhinoCommand::result MakeObjectColor(ON_SimpleArray<const CRhinoObject*>& objectList);
   };

   // The one and only CPropertiesPageCommand object.  
   // Do NOT create any other instance of a CPropertiesPageCommand class.
   static class CPropertiesPageCommand thePropertiesPageCommand;

   CRhinoCommand::result CPropertiesPageCommand::RunCommand( const CRhinoCommandContext& context )
   {
     if (m_page == nullptr)
       return CRhinoCommand::failure;
     int modified = 0;
     for (int i = 0, count = m_object_ids.Count(); i < count; i++)
     {
       const CRhinoObject* object = context.m_doc.LookupObject(m_object_ids[i]);
       if (object && !object->IsDeleted())
       {
           modified += m_by_layer
           ? m_page->ToByLayer(object) 
           : m_page->ToObjectColor(object);
       }
     }
     m_object_ids.Empty();
     m_page->ModifiedMessage(m_by_layer, modified);
     m_page = nullptr;
     return modified > 0 ? CRhinoCommand::success : CRhinoCommand::nothing;
   }

   void CPropertiesPage::RunModifyCommand(bool byLayer)
   {
     thePropertiesPageCommand.m_object_ids.Empty();
     for (int i = 0, count = SelectedObjectCount(); i < count; i++)
     {
       const CRhinoObject* object = GetSelectedObject(i);
       if (!IncludeObject(object))
         continue;
       if (byLayer && object->Attributes().ColorSource() == ON::color_from_layer)
         continue;
       if (!byLayer && IsOurColor(object))
         continue;
       thePropertiesPageCommand.m_object_ids.Append(object->Attributes().m_uuid);
     }

     if (thePropertiesPageCommand.m_object_ids.Count() < 1)
     {
       ::RhinoMessageBox(RhinoApp().MainWnd(), L"Nothing modified!", LocalPageTitle(), MB_OK);
       return;
     }

     thePropertiesPageCommand.m_page = this;
     thePropertiesPageCommand.m_by_layer = byLayer;
     ON_wString macro;
     macro.Format(L"_noecho !_-%s", thePropertiesPageCommand.EnglishCommandName());
     RhinoApp().RunScript(macro);
   }

   void CPropertiesPage::OnBnClickedButton1()
   {
     RunModifyCommand(false);
   }

   void CPropertiesPage::OnBnClickedButton2()
   {
     RunModifyCommand(true);
   }

   int CPropertiesPage::ToByLayer(const CRhinoObject* object) const
   {
     if (!IncludeObject(object))
       return 0;
     ON_3dmObjectAttributes attribs(object->Attributes());
     if (attribs.ColorSource() == ON::color_from_layer)
       return 0;
     attribs.SetColorSource(ON::color_from_layer);
     return object->Document()->ModifyObjectAttributes(CRhinoObjRef(object), attribs) ? 1 : 0;
   }

   int CPropertiesPage::ToObjectColor(const CRhinoObject* object) const
   {
     if (!IncludeObject(object) || IsOurColor(object))
       return 0;
     ON_3dmObjectAttributes attribs(object->Attributes());
     attribs.SetColorSource(ON::color_from_object);
     attribs.m_color = CApp::App().ObjectColor(object->Document());
     return object->Document()->ModifyObjectAttributes(CRhinoObjRef(object), attribs) ? 1 : 0;
   }

   void CPropertiesPage::ModifiedMessage(bool byLayer, int modifiedCount) const
   {
     ON_wString message;
     if (modifiedCount < 1)
       message = L"Nothing was modified";
     else if (byLayer)
       message.Format(L"%d Objects were modified and are color by layer", modifiedCount);
     else
       message.Format(L"%d Objects colors were changed", modifiedCount);
     ::RhinoMessageBox(RhinoApp().MainWnd(), message, L"Test Object Properties Page", MB_OK);
   }
   ```

   #### Rhino 6 code

   In Rhino 6 you call `ModifyPage` on your page host and override `OnModifyPage` to modify the selected objects.  `ModifyPage` Will call `OnModifyPage`  when it is safe to modify objects.

   ```
   class CPropertiesPageCommand : public CRhinoTestCommand
   {
   public:
     CPropertiesPageCommand()
     : m_by_layer(false)
     , m_page(nullptr)
     {
     }

     ~CPropertiesPageCommand()
     {
     }

     // Returns a unique UUID for this command.
     // If you try to use an id that is already being used, then
     // your command will not work.  Use GUIDGEN.EXE to make unique UUID.
   	UUID CommandUUID()
   	{
   		// {E547CD29-920F-4EF9-92EC-3F4AE9D9E619}
       static const GUID command_id =
       { 0xe547cd29, 0x920f, 0x4ef9, { 0x92, 0xec, 0x3f, 0x4a, 0xe9, 0xd9, 0xe6, 0x19 } };
       return command_id;
   	}

     // Returns the English command name.
   	const wchar_t* EnglishCommandName() { return L"TestPropertiesPageModifyObjects"; }

     // Returns the localized command name.
   	const wchar_t* LocalCommandName() const { return L"TestPropertiesPageModifyObjects"; }

     // Rhino calls RunCommand to run the command.
   	CRhinoCommand::result RunCommand( const CRhinoCommandContext& );

     bool m_by_layer;
     ON_SimpleArray<ON_UUID>m_object_ids;
     CPropertiesPage* m_page;

     CRhinoCommand::result MakeByLayer(ON_SimpleArray<const CRhinoObject*>& objectList);
     CRhinoCommand::result MakeObjectColor(ON_SimpleArray<const CRhinoObject*>& objectList);
   };

   // The one and only CPropertiesPageCommand object.  
   // Do NOT create any other instance of a CPropertiesPageCommand class.
   static class CPropertiesPageCommand thePropertiesPageCommand;

   CRhinoCommand::result CPropertiesPageCommand::RunCommand( const CRhinoCommandContext& context )
   {
     if (m_page == nullptr)
       return CRhinoCommand::failure;
     int modified = 0;
     for (int i = 0, count = m_object_ids.Count(); i < count; i++)
     {
       const CRhinoObject* object = context.m_doc.LookupObject(m_object_ids[i]);
       if (object && !object->IsDeleted())
       {
           modified += m_by_layer
           ? m_page->ToByLayer(object) 
           : m_page->ToObjectColor(object);
       }
     }
     m_object_ids.Empty();
     m_page->ModifiedMessage(m_by_layer, modified);
     m_page = nullptr;
     return modified > 0 ? CRhinoCommand::success : CRhinoCommand::nothing;
   }

   void CPropertiesPage::RunModifyCommand(bool byLayer)
   {
     thePropertiesPageCommand.m_by_layer = byLayer;
     PropertiesPanelPageHost()->ModifyPage();
   }

   void CPropertiesPage::OnModifyPage(IRhinoPropertiesPanelPageEventArgs& args)
   {
     thePropertiesPageCommand.m_object_ids.Empty();
     for (int i = 0, count = args.ObjectCount(); i < count; i++)
     {
       const CRhinoObject* object = args.ObjectAt(i);
       if (!IncludeObject(object))
         continue;
       if (thePropertiesPageCommand.m_by_layer && object->Attributes().ColorSource() == ON::color_from_layer)
         continue;
       if (!thePropertiesPageCommand.m_by_layer && IsOurColor(object))
         continue;
       thePropertiesPageCommand.m_object_ids.Append(object->Attributes().m_uuid);
     }

     if (thePropertiesPageCommand.m_object_ids.Count() < 1)
     {
       ::RhinoMessageBox(RhinoApp().MainWnd(), L"Nothing modified!", LocalTitle(), MB_OK);
       return;
     }

     thePropertiesPageCommand.m_page = this;
     ON_wString macro;
     macro.Format(L"_noecho !_-%s", thePropertiesPageCommand.EnglishCommandName());
     RhinoApp().RunScript(args.DocumentRuntimeSerialNumber(), macro);
   }

   void CPropertiesPage::OnBnClickedButton1()
   {
     RunModifyCommand(false);
   }

   void CPropertiesPage::OnBnClickedButton2()
   {
     RunModifyCommand(true);
   }

   int CPropertiesPage::ToByLayer(const CRhinoObject* object) const
   {
     if (!IncludeObject(object))
       return 0;
     ON_3dmObjectAttributes attribs(object->Attributes());
     if (attribs.ColorSource() == ON::color_from_layer)
       return 0;
     attribs.SetColorSource(ON::color_from_layer);
     return object->Document()->ModifyObjectAttributes(CRhinoObjRef(object), attribs) ? 1 : 0;
   }

   int CPropertiesPage::ToObjectColor(const CRhinoObject* object) const
   {
     if (!IncludeObject(object) || IsOurColor(object))
       return 0;
     ON_3dmObjectAttributes attribs(object->Attributes());
     attribs.SetColorSource(ON::color_from_object);
     attribs.m_color = CApp::App().ObjectColor(object->Document());
     return object->Document()->ModifyObjectAttributes(CRhinoObjRef(object), attribs) ? 1 : 0;
   }

   void CPropertiesPage::ModifiedMessage(bool byLayer, int modifiedCount) const
   {
     ON_wString message;
     if (modifiedCount < 1)
       message = L"Nothing was modified";
     else if (byLayer)
       message.Format(L"%d Objects were modified and are color by layer", modifiedCount);
     else
       message.Format(L"%d Objects colors were changed", modifiedCount);
     ::RhinoMessageBox(RhinoApp().MainWnd(), message, L"Test Object Properties Page", MB_OK);
   }
   ```

10. Replace your `PageType` override with the new version that returns a `RhinoPropertiesPanelPageType` instead of a `page_type`.  This is an optional override and typically is only overridden to replace system pages such as the light page with a plug-in provided page.

  #### Rhino 5 code

  ```
  CRhinoObjectPropertiesDialogPageEx::page_type CPropertiesPage::PageType() const
  {
    return CRhinoObjectPropertiesDialogPageEx::custom_page;
  }
  ```

  #### Rhino 6 code

  ```
  RhinoPropertiesPanelPageType CPropertiesPage::PageType() const
  {
    return RhinoPropertiesPanelPageType::Custom;
  }
  ```
