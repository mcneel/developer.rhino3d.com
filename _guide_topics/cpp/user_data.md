---
title: User Data
description: This guide covers user data using C/C++.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Fundamentals']
origin: http://wiki.mcneel.com/developer/userdata
order: 1
keywords: ['rhino']
layout: toc-guide-page
TODO: 'downloadable samples should be moved to GitHub and linked'
---

# {{ page.title }}

{% include byline.html %}

{{ page.description }}

## Overview

There are two basic ways plugins can store information in Rhino *.3dm* files:

1. *Document User Data*
1. *Object User Data*

For example, a rendering plugin might save a scene description as *Document User Data* and use *Object User Data* to attach rendering material information to individual surfaces.

## Document User Data

To save document user data your plugin must override three `CRhinoPlugIn` base class functions:

```cpp
CRhinoPlugIn::CallWriteDocument
CRhinoPlugIn::WriteDocument
CRhinoPlugIn::ReadDocument
```

When Rhino writes a *.3dm* file, it goes through all the plugins that are currently loaded.  First Rhino calls `CallWriteDocument()` to see if the plugin wants to save document user data.  If `CallWriteDocument()` returns `true`, Rhino saves information that identifies the plugin and then calls `WriteDocument()` when it is time for the plugin to save its document user data.

When Rhino reads a *.3dm* file and it encounters document user data, it uses the plugin identification information to load the plugin and then calls the plugin's `ReadDocument()` to read the plugin's document user data.

## Object User Data

Object user data can be attached to things like layers, materials, geometry objects, and object attributes.  In fact object user data can be attached to any class derived from `ON_Object`.  This user data is stored in a linked list on `ON_Object` and can be copied, transformed, and saved along with the parent object.  For example, you could attach object user data to a mesh.  When the mesh is copied the object user data is copied and attached to the copy.  When the mesh is transformed, the transformation is recorded by the object user data.  When the mesh is saved in a *.3dm* file, the object user data is saved too.

All object user data is saved in a class you write that is derived from the class `ON_UserData`.

### Attaching Object User Data to CRhinoObjects

The Rhino geometry table is where the bulk of the Rhino model is stored.  This is where the points, curves, meshes, surface, polysurfaces, annotation, render lights, and so on are stored.  Each member of the geometry table is derived from the `CRhinoObject` class.  There are three places you can attach object user data to a `CRhinoObject`:

1. The `CRhinoObject` geometry class
1. The `CRhinoObject` attributes class, and
1. The `CRhinoObject` itself.

Object user data attached to the geometry and attributes class persists through copys, transformations, and file IO.  Object user data attached directly on the `CRhinoObject` class is never saved in *.3dm* file.

To attach object user data to the `CRhinoObject` geometry use `CRhinoObject::AttachGeometryUserData()`.  This call attaches the user data to the `CRhinoObject.m_geometry` member.  This user data will persist when the object is copied, transformed, or saved in *.3dm* files.

To attach object user data to the `CRhinoObject` attributes, use `CRhinoObject::AttachAttributeUserData()`.  This call attaches the user data to the `CRhinoObject.m_attributes` member.  This user data will persist when the object is copied, transformed, or saved in *.3dm* files.

To attach object user data to the `CRhinoObject` itself, use `CRhinoObject::AttachUserData()`.  This user data is attached to the `CRhinoObject` class itself and will never be saved in *.3dm* files.  It is a good place to attach runtime information that applies only to the specific class it is attached to.  In general, object user data attached directly to a `CRhinoObject` class will have `m_userdata_copycount = 0` and will have an `Archive()` function that returns `false`.

## Samples

The first sample, *CMyUserData1*, shows how to make a simple piece of user data that is not saved in *.3dm* files.  The second sample, *CMyUserData2*, shows how to make a piece of user data that is saved in *.3dm* files.

You can download the source for the next two samples here: <a href="{{ site.baseurl }}/files/myuserdataexample.zip"><span class="glyphicon glyphicon-download"></span></a> [mcneelcodesigning.zip]({{ site.baseurl }}/files/myuserdataexample.zip)

### CMyUserData1

```cpp
class CMyUserData1 : public ON_UserData
{
public:

  /*
  Returns:
   Uuid used to identify this type of user data.
   This is the value saved in m_userdata_uuid and
   passed to ON_Object::GetUserData().
  */
  static ON_UUID Id();

  CMyUserData1();
  ~CMyUserData1();

  //... download example for more details

  ON_wString m_my_string;
};
```

The `CMyUserData1` class must always be on the heap (constructed by calling the C/C++ new operator).  The class's constructor must initialize two `ON_UserData` fields, `m_userdata_uuid`, `m_application_uuid`.  In addition, if you want the object user data copied whenever its parent object is copied, you have to set `m_userdata_copycount` to one...

```cpp
ON_UUID CMyUserData1::Id()
{
  // Use Microsoft's guidgen to get a unique id.
  // {1129B130-B840-...}
  static const ON_UUID id = { 0x1129b130, 0xb840, ... };
  return id;
}

CMyUserData1::CMyUserData1()
{
  m_userdata_uuid = CMyUserData1::Id();
  m_application_uuid = MyPlugIn().PlugInID();
  m_userdata_copycount = 1;  enable copying
}

// ... download example for more details
```

Attaching object user data to a parent object is a simple matter...

```cpp
ON_Mesh* pMesh = ...;
CMyUserData1* pMyUserData1 = new CMyUserData1();
pMyUserData1->m_my_string = L"How, now, brown cow?";
if ( pMesh->AttachUserData(pMyUserData1) )
{
  // It worked.  The mesh class will manage the user
  // data and delete it at the appropriate time.
  RhinoApp().Print("User data attached.\n"):
}
else
{
  // It didn't work.  This usually means that
  // the parent object already has this kind
  // of user data attached.
  RhinoApp().Print("User data not attached.\n");
  delete pMyUserData;
}
pMyUserData = 0;
```

The user data's *UUID* is used to retrieve the user data from a parent object...

```cpp
ON_Mesh* pMesh = ...;
ON_UserData1* pUserData = pMesh->GetUserData(CMyUserData1::Id());
CMyUserData1** pMyUserData1 = static_cast<CMyUserData1**>(pUserData);
if ( pMyUserData1 )
{
  RhinoApp().Print("Got user data.\n"):
}
else
{
  RhinoApp().Print("My user data is not on the mesh.\n"):
}
```

### CMyUserData2

Make sure you completely understand the *CMyUserData1* sample above before studying this sample.

To have your user data saved in files, you have to add several IO related functions and add full openNURBS object support to your class...

```cpp
class CMyUserData2 : public ON_UserData
{
  // openNURBS classes that are saved in .3dm files require
  // an ON_OBJECT_DECLARE call in their declaration.
  ON_OBJECT_DECLARE(CMyUserData2);

public:

 static ON_UUID Id();

 CMyUserData2();
 ~CMyUserData2();

  // override virtual ON_UserData::Archive()
  BOOL Archive() const;

  // override virtual ON_UserData::Write()
  BOOL Write(ON_BinaryArchive& binary_archive) const;

  // override virtual ON_UserData::Read()
  BOOL Read(ON_BinaryArchive& binary_archive);

  // ... download example for more details

 ON_wString m_my_string;
 ON_3dPoint m_my_point;
};
```

Again, the `CMyUserData2` class must always be on the heap (constructed by calling the C/C++ new operator).  To support file IO, the definition of `CMyUserData2` must contain the `ON_OBJECT_DECLARE` macro.

The cpp file where the class is implemented must contain the `ON_OBJECT_IMPLEMENT` macro shown here:

```cpp
ON_OBJECT_IMPLEMENT(CMyUserData2,ON_UserData,"0D8FA7AB-F8A4-...");
```

The construction code for `CMyUserData2` looks like:

```cpp
ON_UUID CMyUserData2::Id()
{
  return CMyUserData2::m_CMyUserData2_class_id.Uuid();
}

CMyUserData2::CMyUserData2()
{
  m_userdata_uuid = CMyUserData2::Id();
  m_application_uuid = MyPlugIn().PlugInID();
  m_userdata_copycount = 1;  // enable copying

  // initialize your data members here
  m_my_point.Set(0.0,0.0,0.0);
}
```

The `CMyUserData2::Archive()`, `CMyUserData2::Read()`, `CMyUserData2::Write()` functions look something like this...

```cpp
BOOL CMyUserData2::Archive() const
{
  // If false is returned, nothing will be saved in 3dm archives.
  return true;
}

BOOL CMyUserData2::Write(ON_BinaryArchive& binary_archive) const
{
  // ... download example for more details about adding version support

  int minor_version = 0;
  bool rc = binary_archive.BeginWrite3dmChunk(
       TCODE_ANONYMOUS_CHUNK,
       1,
       minor_version
       );
  if (!rc)
    return false;

  // Write class members like this
  for (;;)
  {
    // version 1.0 fields
    rc = binary_archive.WriteString(m_my_string);
    if (!rc) break;

    rc = binary_archive.WritePoint(m_my_point);
    if (!rc) break;

    break;
  }

  if ( !binary_archive.EndWrite3dmChunk() )
   rc = false;

  return rc;
}

BOOL CMyUserData2::Read(ON_BinaryArchive& binary_archive)
{
  // ... download example for more details about adding version support

  int major_version = 0;
  int minor_version = 0;
  bool rc = binary_archive.BeginRead3dmChunk(
         TCODE_ANONYMOUS_CHUNK,
         &major_version,
         &minor_version
         );
  if (!rc)
    return false;

  // Read class members like this
  for (;;)
  {
    rc == ( 1 == major_version );
    if (!rc) break;

    // version 1.0 fields
    rc = binary_archive.ReadString(m_my_string);
    if (!rc) break;

    rc = binary_archive.ReadPoint(m_my_point);
    if (!rc) break;

    break;
  }

  // If BeginRead3dmChunk() returns true,
  // then EndRead3dmChunk() must be called,
  // even if a read operation failed.
  if ( !binary_archive.EndRead3dmChunk() )
    rc = false;

 return rc;
}
```

## User Data operator= and Copy Construction

In general, you do not need to explicitly override the default copy constructor and `operator=` that C/C++ generates for you.  Incorrectly implemented copy constructors and `operator=`s are a common source of bugs.  The C/C++ defaults will work perfectly if every member of your class is a built-in data type (`int`, `double`, ...) or a class that properly handles copy construction and `operator=` (`ON_NurbsCurve`, `ON_3dPoint`, `ON_Simple`/`ClassArray<>`, ...).

The main reason you have to explicitly implement a copy constructor and `operator=` is to handle fields that involve explicit heap allocation and deallocation.  In the sample below, the field `m_i_array` is an array of integers that is on the heap.

```cpp
class CMyUserData3 : public ON_UserData
{
  ON_OBJECT_DECLARE(CMyUserData3);
public:
  static ON_UUID Id();
  static ON_UUID ApplicationId();
  static CMyUserData3** Get(const ON_Object**);

  CMyUserData3();
  ~CMyUserData3();
  CMyUserData3(const CMyUserData3& src);
  CMyUserData3& operator=(const CMyUserData3& src);

  //...

  int m_i_count;
  int* m_i_array;
};

ON_OBJECT_IMPLEMENT(CMyUserData3,
                    ON_UserData,
                    <<guidgen generated uuid here>>
                    );

ON_UUID CMyUserData3::Id()
{
  return CMyUserData3::m_CMyUserData3_class_id.Uuid();
}

ON_UUID CMyUserData3::ApplicationId()
{
  return <<your plugin name>>().PlugInID();
}

CMyUserData3** CMyUserData3::Get(const ON_Object** object)
{
  return CMyUserData3::Cast( (object != 0)
                             ? object->GetUserData( CMyUserData3::Id() )
                          );
}

CMyUserData3::CMyUserData3()
{
  m_userdata_uuid = CMyUserData3::Id();
  m_application_uuid = CMyUserData3::ApplicationId();
  m_userdata_copycount = 1;

  // Initialize your class's fields
  m_i_count = 0;
  m_i_array = 0;
}

CMyUserData3::~CMyUserData3()
{
  // virtual function
  if ( 0 != m_i_array )
    onfree(m_i_array);
}
```

When the copy constructor is called, the memory for "this" is not initialized.  You must call the base class copy constructor, initialize all your class's fields, and then copy your class's fields...

```cpp
CMyUserData3::CMyUserData3(const CMyUserData3& src )
{
  m_userdata_uuid = CMyUserData3::Id();
  m_application_uuid = CMyUserData3::ApplicationId();
  m_transform_count = 0;

  // DO NOT SET OTHER ON_UserData fields
  // In particular, do not set m_userdata_copycount

  Copy you class's fields
  m_i_count = 0;
  m_i_array = 0;
  if( src.m_i_count > 0 && src.m_i_array != 0 )
  {
    m_i_array = (int**)onmalloc(src.m_i_count**sizeof(m_i_array[0]));
    if ( m_i_array != 0 )
    {
      memcpy( m_i_array,
              src.m_i_array,
              src.m_i_count*sizeof(m_i_array[0])
           );
      m_i_count = src.m_i_count;
    }
  }
}
```

When `operator=` is called, "this" has already been constructed and may already have been used.  You must destroy any existing information, call the the base class `operator=`, and then copy your class's fields...

```cpp
CMyUserData3& CMyUserData3::operator=(const CMyUserData3& src)
{
  if ( this != &src )
  {
   // Destroy your class's existing information
   // (Otherwise you will leak memory if "this"
   // has been used before.)
   m_i_count = 0;
   if ( m_i_array != 0 )
   {
     onfree(m_i_array);
     m_i_array = 0
   }

   // Use the base class operator=() to correctly
   // copy all ON_UserData fields.
   ON_UserData::operator=(src);

   // Copy your class's fields
   if( src.m_i_count > 0 && src.m_i_array != 0 )
   {
     m_i_array = (int**)onmalloc(src.m_i_count**sizeof(m_i_array[0]));
     if ( m_i_array != 0 )
     {
       memcpy( m_i_array,
               src.m_i_array,
               src.m_i_count*sizeof(m_i_array[0])
             );
       m_i_count = src.m_i_count;
     }
   }
  }
  return *this;
}
```

## Sharing User Data Between Plugins

The best way to share user data between plugins is to have access to the plugins data controlled by a shared *DLL* - a *DLL* that is used by all interested plugins.  The user data class definitions and declarations, along with any helper functions used to access this data, are then added to and exported from this *DLL*.

The easiest way to make *DLLs* for Rhino plugins is to simply run the *Rhino Plugin Wizard* from Visual Studio.  When the wizard finishes, simply delete the plugins object (*cpp* and *h* files) and the command file.  Then change the output file extension from *rhp* to *dll*.  Now, you have a *MFC DLL* that links with the Rhino C/C++ SDK.

One important piece of information to keep in mind is that when you create a class derived from `ON_UserData` and you expect this data to be serialized in a *3dm* file, then you must assign the owning plugins's *UUID* to the `ON_UserData::m_application_uuid` data member.  This is how Rhino knows what plugins to load when it encounters plugin user data when reading a *3dm* file.  Note, it is not important what plugins's *UUID* is assigned to the user data because all of the plugins are going to dynamically load the *DLL* when they are loaded anyway.  But, some plugin must be "in charge."

For example:

```cpp
ON_UUID CPlugInUserData::PlugInId()
{
  // Copied from PlugIn1PlugIn.cpp

  // {F8B054CD-19A3-4D46-AB7E-DB3E8EF8CF5B}
  static const GUID PlugIn1PlugIn_UUID =
  { 0xF8B054CD, 0x19A3, 0x4D46, { 0xAB, 0x7E, 0xDB, 0x3E, 0x8E, 0xF8, 0xCF, 0x5B } };
  return PlugIn1PlugIn_UUID;
}

CPlugInUserData::CPlugInUserData()
{
  m_userdata_uuid = CPlugInUserData::Id();

  /*
  CRITICAL:
    m_application_uuid must be assigned the uuid of the plugin
    that will be responsible for reading and writing our user data.
    In this example, we'll use PlugIn1 as our primary plugin.
  */
  m_application_uuid = CPlugInUserData::PlugInId();

  m_userdata_copycount = 1; // enable copying

  // initialize your data members here
  m_point.Set( 0.0, 0.0, 0.0 );
  m_string = L;
}
```

This plugin sample contains two plugin projects and one *DLL* project:  

<a href="{{ site.baseurl }}/files/testshareduserdata.zip"><span class="glyphicon glyphicon-download"></span></a> [testshareduserdata.zip]({{ site.baseurl }}/files/testshareduserdata.zip)

To load the sample, just download and extract into some folder, and then open *Test.sln* is Visual Studio.

## Related Topics

- [Attaching User Data to Brep Components]({{ site.baseurl }}/samples/cpp/attaching_user_data_to_brep_components)
