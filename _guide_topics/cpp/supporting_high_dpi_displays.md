---
title: Supporting High DPI Displays
description: This guide discusses the support of high resolution monitors.
author: dale@mcneel.com
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Advanced']
order: 1
keywords: ['C/C++', 'Rhino', 'Plugin']
layout: toc-guide-page
---

# {{ page.title }}

{{ page.description }}

## Overview

Super high resolution displays are now common on Windows-based systems, and those using Rhino expect it and 3rd party plug-ins to display correctly on them. Plug-in developers need to make sure their applications are DPI–aware. DPI-aware plug-ins adjust UI elements to scale appropriately to the system DPI. Plug-ins that are not DPI–aware, but are running on a high-DPI display setting, can suffer from many visual artifacts, including incorrect scaling of UI elements, clipped text, and blurry images.

Plug-in developers should run Rhino on high-DPI displays so they can find and fix display issues. Here is how you can configure Windows for high-DPI display:

### Windows 10

1. Right-click on your desktop and click **Display settings**.
1. Use the slider to select the text scaling and click **Apply**.
1. Logout of Windows and log back in.

### Windows 8/8.1

1. Right-click on your desktop and click **Screen resolution**.
1. Click the **Make text and other items larger or smaller**.
1. Use the slider to select the text scaling and click **Apply**.
1. Logout of Windows and log back in.

### Windows 7

1. Right-click on your desktop and click **Screen resolution**.
1. Click **Make text and other items larger or smaller**.
1. Select the text scaling and click **Apply**.
1. Logout of Windows and log back in.

## Common C++ Issues

Most high DPI issues that plug-ins will encounter are due to owner-drawn control. Here, developers have hard-coded sizes or locations, assuming the standard DPI setting. In these cases, custom drawn elements don’t appear correctly, or custom controls don’t work properly.

Other issues have to do with the use of bitmaps or icons that are too small at higher DPI settings or that don’t scale well.

The Rhino SDK has some new tools that developers can use to help make UI elements DPI-aware. See the ```CRhinoDpi``` class declaration in ```RhinoSdkDpi.h``` for more information.

### General

The ```CRhinoDpi``` class contains several static function to help with DPI-aware issues.

```CRhinoDpi::DpiScale``` returns the display DPI scale factor when Rhino started. Use this value as a multiplier when owner drawing.

```CRhinoDpi::Scale``` scales a value by the current DPI scale factor.

### Icons

Windows recommends that icon resources contain the following sizes: 16, 32, 48, and 256. All of the icon files (ICO) used by Rhino have been updated to support these sizes.

When loading icons, use ```CRhinoDpi::LoadIcon```. For example:

```cpp
virtual HICON Icon()
{ 
  const int const_icon_size = 24;
  int icon_size = CRhinoDpi::Scale(const_icon_size);
  return CRhinoDpi::LoadIcon(AfxGetInstanceHandle(), IDI_ICON, icon_size);
}
```

and:

```cpp
virtual HICON Icon(const CSize& size) const
{ 
  return CRhinoDpi::LoadIcon(AfxGetInstanceHandle(), IDI_ICON, size.cx, size.cy);
}
```

Note, if the requested icon is not a standard size, the ```CRhinoDpi::LoadIcon``` function scales down a larger image.

### Cursors

All of the cursors files (CUR) used by Rhino have been updated to support all of the sizes used by Windows 10.

When loading cursor resources, you should so in this manner:

```cpp
HCURSOR hCursor = (HCURSOR)::LoadImage(AfxGetInstanceHandle(), MAKEINTRESOURCE(IDC_CURSOR), IMAGE_CURSOR, 0, 0, LR_DEFAULTSIZE | LR_SHARED);
```

By not specifying a size and by using the ```LR_DEFAULTSIZE``` flag, Windows will automatically load the cursor size that is appropriate for the current DPI setting.

### List Controls with Image Lists

The problem with list controls is that the bitmaps, used by their image lists, do not scale very well. The solution is to convert the bitmap strip into individual icon files and then use ```CRhinoDpi::CreateImageList``` to create the image list.

For list controls that use an image list that has a single bitmap, you can do this:

```cpp
BOOL CMyDialog::OnInitDialog() 
{
  // ...
  const int size = CRhinoDpi::IconSize(CRhinoDpi::IconType::SmallIcon);
  CRhinoDpi::CreateImageList(m_image_list, AfxGetInstanceHandle(), IDI_MYICON, size);
  m_list_ctrl.SetImageList(&m_image_list, LVSIL_SMALL);
  // ...
}
```

For an image list that contains multiple bitmaps, you can do this:

```cpp
BOOL CMyDialog::OnInitDialog() 
{
  // ...
  const int size = CRhinoDpi::IconSize(CRhinoDpi::IconType::SmallIcon);
  unsigned int image_ids[4] = { IDI_MYICON0, IDI_MYICON1, IDI_MYICON2, IDI_MYICON3 };
  CRhinoDpi::CreateImageList(m_image_list, AfxGetInstanceHandle(), 4, image_ids, size);
  m_list_ctrl.SetImageList(&m_image_list, LVSIL_SMALL);
  // ...
}
```

### List Boxes

If you've derived your own list boxes, for the sake of owner drawing, then will need to make sure you are setting the item height for each item in the list. Otherwise, items will be scrunched together at higher DPI settings. Use ```CRhinoDpi::ListBoxItemHeight``` to determine this.

```cpp
void CMyListBox::PreSubclassWindow()
{
  // If the control was created with the LBS_OWNERDRAWFIXED style,
  // then this will set the item height for all items.
  if (GetStyle() & LBS_OWNERDRAWFIXED)
  {
    const int itemHeight = CRhinoDpi::ListBoxItemHeight(*(this));
    SetItemHeight(0, itemHeight);
  }
  CListBox::PreSubclassWindow();
}

void CMyListBox::MeasureItem(LPMEASUREITEMSTRUCT lpMeasureItemStruct)
{
  // CListBox::MeasureItem is only called if the control was created
  // with the LBS_OWNERDRAWVARIABLE style.
  static int itemHeight = CRhinoDpi::ListBoxItemHeight(*(this));
  if (nullptr != lpMeasureItemStruct)
    lpMeasureItemStruct->itemHeight = itemHeight;
}
```

There is also a new ```CRhinoUiListBox``` control that you can use in place of ```CListBox```, that will perform the above calculations for you. See ```RhinoSdkUiCheckListbox.h``` for details.

### Check List Boxes

The standard MFC ```CCheckListBox``` class does correctly handle mouse events at high DPI settings. If you are using this class, then modify your code to use ```CRhinoUiCheckListBox```.  See ```RhinoSdkUiCheckListbox.h``` for details.

### Combo Boxes

If you've derived your own combo boxes, for the sake of owner drawing, then will need to make sure you are setting the item height for each item in the list. Otherwise, items will be scrunched together at higher DPI settings. Use ```CRhinoDpi::ComboBoxItemHeight``` to determine this.

```cpp
void CMyComboBox::PreSubclassWindow()
{
  // If the control was created with the CBS_OWNERDRAWFIXED style,
  // then this will set the item height for all items.
  if (GetStyle() & CBS_OWNERDRAWFIXED)
  {
    const int itemHeight = CRhinoDpi::ComboBoxItemHeight(*(this));
    // Set the height of all list items
    SetItemHeight(0, itemHeight);
    // Set the height of the edit-control or static-text portion (Optional)
    SetItemHeight(-1, itemHeight);
  }
  CComboBox::PreSubclassWindow();
}

void CMyComboBox::MeasureItem(LPMEASUREITEMSTRUCT lpMeasureItemStruct)
{
  // CComboBox::MeasureItem is only called if the control was created
  // with the CBS_OWNERDRAWVARIABLE style.
  static int itemHeight = CRhinoDpi::ComboBoxItemHeight(*(this));
  if (nullptr != lpMeasureItemStruct)
    lpMeasureItemStruct->itemHeight = itemHeight;
}
```

### Check Boxes

If you are owner-drawing check boxes, then there is a good chance their sizes are either hard-coded or they were obtained by calling an incorrect Windows API function. The ```CRhinoDpi::CheckBoxSize``` and ```CRhinoDpi::MenuCheckSize``` static functions will help with this.
