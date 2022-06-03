+++
authors = [ "dale" ]
categories = [ "Advanced" ]
description = "This guide demonstrates how to replace Rhino's color picker using C/C++."
keywords = [ "rhino", "color", "picker" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Creating a Custom Color Picker"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/replacecolordialog"
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

 
## How To

To replace Rhino's color picking dialog, derive a new class from `CRhinoReplaceColorDialog` and override the `ColorDialog()` virtual function.  Note, if more that one `CRhinoReplaceColorDialog`-derived classes exist, then the last `CRhinoReplaceColorDialog`-derived object created will be displayed.

The following sample code demonstrates how to replace Rhino's color picking dialog.  In this example, we will simply replace it with the Windows standard color picking dialog...

```cpp
class CMyColorDialog : public CRhinoReplaceColorDialog
{
public:
  CMyColorDialog() : CRhinoReplaceColorDialog(::AfxGetStaticModuleState()) {};
  virtual ~CMyColorDialog() {};
  bool CMyColorDialog::ColorDialog( HWND hWndParent,
                                    ON_Color& color,
                                    bool bIncludeButtonColors,
                                    const wchar_t* lpsDialogTitle )
  {
    CColorDialog dlg( color, CC_ANYCOLOR|CC_FULLOPEN, CWnd::FromHandle(hWndParent) );
    if( IDOK != dlg.DoModal() )
      return false;
    color = dlg.GetColor();
    return true;
  }
};
```

Now, create a new Rhino command and add a pointer to the above class as a public data member. Do not forget to initialize it's value to `NULL` in the command classes constructor.  For example:

```cpp
CMyColorDialog* m_pMyColorDialog;
// ...
CTestCommand::CTestCommand() : pMyColorDialog(NULL) {}
```

Finally, in your new command classes `RunCommand()` member, install the new color picker.  For example:

```cpp
CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
{
  if( m_pMyColorDialog )
  {
    delete m_pMyColorDialog;
    m_pMyColorDialog = NULL;
    RhinoApp().Print( L"Rhino color dialog restored.\n" );
  }
  else
  {
    m_pMyColorDialog = new CMyColorDialog;
    if( m_pMyColorDialog )
      RhinoApp().Print( L"Rhino color dialog replaced.\n" );
    else
      RhinoApp().Print( L"Error replacing Rhino color dialog.\n" );
  }
  return CRhinoCommand::success;
}
```

For more information on the `CRhinoReplaceColorDialog` class, see it's declaration in *rhinoSdkUtilities.h*.
