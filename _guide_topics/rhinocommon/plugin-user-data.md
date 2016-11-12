---
title: Plugin User Data
description: This guide gives an overview of user data and how to use it with RhinoCommon.
authors: ['Steve Baer']
author_contacts: ['stevebaer']
apis: ['RhinoCommon']
languages: ['C#']
platforms: ['Windows', 'Mac']
categories: ['Fundamentals']
origin: https://wiki.mcneel.com/developer/rhinocommonsamples/userdata
order: 1
keywords: ['RhinoCommon', 'Object', 'Plugin', 'User', 'Data']
layout: toc-guide-page
---

# {{ page.title }}

{% include byline.html %}

{{ page.description }}

There are two basic ways plugins can store information in Rhino .3dm files:

1. [Document User Data](#document-user-data)
1. [Object User Data](#object-user-data)

For example, a rendering plugin might save a scene descriptions as document user data and use object user data to attach rendering material information to individual surfaces.

## Document User Data

To save document user data your plugin must override three PlugIn base class functions:

```cs
PlugIn.ShouldCallWriteDocument
PlugIn.WriteDocument
PlugIn.ReadDocument
```

SDK references for these functions can be found [here]({{ site.baseurl }}/api/RhinoCommon/html/Methods_T_Rhino_PlugIns_PlugIn.htm).

When Rhino writes a .3dm file, it goes through all the plugins that are currently loaded. First Rhino calls `ShouldCallWriteDocument()` to see if the plugin wants to save document user data.  If `ShouldWriteDocument()` returns true, Rhino saves information that identifies the plugin and then calls `WriteDocument()` when it is time for the plugin to save its “document” user data.

When Rhino reads a .3dm file and it encounters document user data, it uses the plugin identification information to load the plugin and then calls the plugin's `ReadDocument()` to read the plugin's “document” user data.

## Object User Data

Object user data can be attached to things like layers, materials, geometry objects, and object attributes. In fact object user data can be attached to any class derived from CommonObject. This user data is stored in a linked list on CommonObject and can be copied, transformed and saved along with the parent object. For example, you could attach object user data to a mesh. When the mesh is copied the object user data would be copied and attached to the copy. When the mesh is transformed, the transformation would be recored by the object user data. When the mesh is saved in a .3dm file, the object user data will be saved too.

There are three forms of object user data:

1. User strings
1. UserDictionary
1. Custom UserData

It is *recommended to typically use the User Strings or the UserDictionary on an object* since the data is automatically serialized for you and it is easily shared between plugins and scripts.

In the case that you want to write your own private custom user data, you would derive a class from `Rhino.DocObjects.Custom.UserData`. Here's a sample:

```cs
using System;
using Rhino;
using System.Runtime.InteropServices;

namespace examples_cs
{
  // You must define a Guid attribute for your user data derived class
  // in order to support serialization. Every custom user data class
  // needs a custom Guid
  [Guid("DAAA9791-01DB-4F5F-B89B-4AE46767C783")]
  public class PhysicalData : Rhino.DocObjects.Custom.UserData
  {
    public int Weight{ get; set; }
    public double Density {get; set;}


    // Your UserData class must have a public parameterless constructor
    public PhysicalData(){}

    public PhysicalData(int weight, double density)
    {
      Weight = weight;
      Density = density;
    }

    public override string Description
    {
      get { return "Physical Properties"; }
    }

    public override string ToString()
    {
      return String.Format("weight={0}, density={1}", Weight, Density);
    }

    protected override void OnDuplicate(Rhino.DocObjects.Custom.UserData source)
    {
      PhysicalData src = source as PhysicalData;
      if (src != null)
      {
        Weight = src.Weight;
        Density = src.Density;
      }
    }

    // return true if you have information to save
    public override bool ShouldWrite
    {
      get
      {
        if (Weight > 0 && Density > 0)
          return true;
        return false;
      }
    }

    protected override bool Read(Rhino.FileIO.BinaryArchiveReader archive)
    {
      Rhino.Collections.ArchivableDictionary dict = archive.ReadDictionary();
      if (dict.ContainsKey("Weight") && dict.ContainsKey("Density"))
      {
        Weight = (int)dict["Weight"];
        Density = (double)dict["Density"];
      }
      return true;
    }
    protected override bool Write(Rhino.FileIO.BinaryArchiveWriter archive)
    {
      // you can implement File IO however you want... but the dictionary class makes
      // issues like versioning in the 3dm file a bit easier.  If you didn't want to use
      // the dictionary for writing, your code would look something like.
      //
      //  archive.Write3dmChunkVersion(1, 0);
      //  archive.WriteInt(Weight);
      //  archive.WriteDouble(Density);
      var dict = new Rhino.Collections.ArchivableDictionary(1, "Physical");
      dict.Set("Weight", Weight);
      dict.Set("Density", Density);
      archive.WriteDictionary(dict);
      return true;
    }
  }


  [Guid("ca9a110e-3969-49ec-9d59-a7c2ee0b85bd")]
  public class ex_userdataCommand : Rhino.Commands.Command
  {
    public override string EnglishName { get { return "cs_userdataCommand"; } }

    protected override Rhino.Commands.Result RunCommand(RhinoDoc doc, Rhino.Commands.RunMode mode)
    {
      Rhino.DocObjects.ObjRef objref;
      var rc = Rhino.Input.RhinoGet.GetOneObject("Select Object", false, Rhino.DocObjects.ObjectType.AnyObject, out objref);
      if (rc != Rhino.Commands.Result.Success)
        return rc;

      // See if user data of my custom type is attached to the geomtry
      var ud = objref.Geometry().UserData.Find(typeof(PhysicalData)) as PhysicalData;
      if (ud == null)
      {
        // No user data found; create one and add it
        int weight = 0;
        rc = Rhino.Input.RhinoGet.GetInteger("Weight", false, ref weight);
        if (rc != Rhino.Commands.Result.Success)
          return rc;

        ud = new PhysicalData(weight, 12.34);
        objref.Geometry().UserData.Add(ud);
      }
      else
      {
        RhinoApp.WriteLine("{0} = {1}", ud.Description, ud);
      }
      return Rhino.Commands.Result.Success;
    }
  }
}
```

---

## Related topics

- [Rhino.PlugIns.PlugIn Methods (API Reference)]({{ site.baseurl }}/api/RhinoCommon/html/Methods_T_Rhino_PlugIns_PlugIn.htm)
- [RhinoCommon object plugin user data]({{ site.baseurl }}/samples/rhinocommon/user-data/)
