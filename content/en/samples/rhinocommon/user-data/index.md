+++
aliases = ["/en/5/samples/rhinocommon/user-data/", "/en/6/samples/rhinocommon/user-data/", "/en/7/samples/rhinocommon/user-data/", "/en/wip/samples/rhinocommon/user-data/"]
authors = [ "steve" ]
categories = [ "Adding Objects" ]
description = "RhinoCommon object plugin user data"
keywords = [ "info", "rhinocommon", "object", "plugin", "user", "data" ]
languages = [ "C#", "Python" ]
sdk = [ "RhinoCommon" ]
title = "User Data"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 0
+++

<div class="codetab-content" id="cs">

```cs

// You must define a Guid attribute for your user data derived class
// in order to support serialization. Every custom user data class
// needs a custom Guid
[Guid("7098A105-CD3C-4192-A9AC-0F21017098DC")]
public class MyCustomData : Rhino.DocObjects.Custom.UserData
{
  public int IntegerData{ get; set; }
  public string StringData {get; set;}

  // Your UserData class must have a public parameterless constructor
  public MyCustomData(){}

  public MyCustomData(int i, string s)
  {
    IntegerData = i;
    StringData = s;
  }

  public override string Description
  {
    get { return "Some Custom Properties"; }
  }

  public override string ToString()
  {
    return String.Format("integer={0}, string={1}", IntegerData, StringData);
  }

  protected override void OnDuplicate(Rhino.DocObjects.Custom.UserData source)
  {
    MyCustomData src = source as MyCustomData;
    if (src != null)
    {
      IntegerData = src.IntegerData;
      StringData = src.StringData;
    }
  }

  // return true if you have information to save
  public override bool ShouldWrite
  {
    get
    {
      // make up some rule as to if this should be saved in the 3dm file
      if (IntegerData > 0 && !string.IsNullOrEmpty(StringData))
        return true;
      return false;
    }
  }

  protected override bool Read(Rhino.FileIO.BinaryArchiveReader archive)
  {
    Rhino.Collections.ArchivableDictionary dict = archive.ReadDictionary();
    if (dict.ContainsKey("IntegerData") && dict.ContainsKey("StringData"))
    {
      IntegerData = (int)dict["IntegerData"];
      StringData = dict["StringData"] as String;
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
    //  archive.WriteInt(IntegerData);
    //  archive.WriteString(StringData);
    var dict = new Rhino.Collections.ArchivableDictionary(1, "MyCustomData");
    dict.Set("IntegerData", IntegerData);
    dict.Set("StringData", StringData);
    archive.WriteDictionary(dict);
    return true;
  }
}

partial class Examples
{
  public static Rhino.Commands.Result Userdata(RhinoDoc doc)
  {
    Rhino.DocObjects.ObjRef objref;
    var rc = Rhino.Input.RhinoGet.GetOneObject("Select Face", false, Rhino.DocObjects.ObjectType.Surface, out objref);
    if (rc != Rhino.Commands.Result.Success)
      return rc;

    var face = objref.Face();

    // See if user data of my custom type is attached to the geomtry
    // We need to use the underlying surface in order to get the user data
    // to serialize with the file.
    var ud = face.UnderlyingSurface().UserData.Find(typeof(MyCustomData)) as MyCustomData;
    if (ud == null)
    {
      // No user data found; create one and add it
      int i = 0;
      rc = Rhino.Input.RhinoGet.GetInteger("Integer Value", false, ref i);
      if (rc != Rhino.Commands.Result.Success)
        return rc;

      ud = new MyCustomData(i, "This is some text");
      face.UnderlyingSurface().UserData.Add(ud);
    }
    else
    {
      RhinoApp.WriteLine("{0} = {1}", ud.Description, ud);
    }
    return Rhino.Commands.Result.Success;
  }
}
```

</div>

<div class="codetab-content" id="py">

```python
#! python 3
import Rhino
import System
from System.Runtime.InteropServices import GuidAttribute
from clr import GetClrType


# You must define a Guid attribute for your user data derived class
# in order to support serialization. Every custom user data class
# needs a custom Guid.
@GuidAttribute("7098A105-CD3C-4192-A9AC-0F21017098DC")
class MyCustomData(Rhino.DocObjects.Custom.UserData):
    # Your UserData class must have a public parameterless constructor
    def __init__(self, i=0, s=""):
        super().__init__()
        self.IntegerData = i
        self.StringData = s

    @property
    def Description(self):
        return "Some Custom Properties"

    def ToString(self):
        return "integer={0}, string={1}".format(self.IntegerData, self.StringData)

    def OnDuplicate(self, source):
        src = source
        if isinstance(src, MyCustomData):
            self.IntegerData = src.IntegerData
            self.StringData = src.StringData

    # return true if you have information to save
    @property
    def ShouldWrite(self):
        # make up some rule as to if this should be saved in the 3dm file
        if self.IntegerData > 0 and self.StringData:
            return True
        return False

    def Read(self, archive):
        d = archive.ReadDictionary()
        if d.ContainsKey("IntegerData") and d.ContainsKey("StringData"):
            self.IntegerData = int(d["IntegerData"])
            self.StringData = str(d["StringData"])
        return True

    def Write(self, archive):
        # you can implement File IO however you want... but the dictionary class makes
        # issues like versioning in the 3dm file a bit easier.  If you didn't want to use
        # the dictionary for writing, your code would look something like.
        #
        #  archive.Write3dmChunkVersion(1, 0)
        #  archive.WriteInt(IntegerData)
        #  archive.WriteString(StringData)
        d = Rhino.Collections.ArchivableDictionary(1, "MyCustomData")
        d.Set("IntegerData", self.IntegerData)
        d.Set("StringData", self.StringData)
        archive.WriteDictionary(d)
        return True


def RunCommand():
    rc, objref = Rhino.Input.RhinoGet.GetOneObject(
        "Select Face", False, Rhino.DocObjects.ObjectType.Surface
    )
    if rc != Rhino.Commands.Result.Success:
        return rc

    face = objref.Face()

    # See if user data of my custom type is attached to the geometry.
    # We need to use the underlying surface in order to get the user data
    # to serialize with the file.
    ud = face.UnderlyingSurface().UserData.Find(GetClrType(MyCustomData))
    if ud is None:
        # No user data found; create one and add it
        rc, i = Rhino.Input.RhinoGet.GetInteger("Integer Value", False, 0)
        if rc != Rhino.Commands.Result.Success:
            return rc

        ud = MyCustomData(i, "This is some text")
        face.UnderlyingSurface().UserData.Add(ud)
    else:
        Rhino.RhinoApp.WriteLine("{0} = {1}", ud.Description, ud)
    return Rhino.Commands.Result.Success


if __name__ == "__main__":
    RunCommand()
```

</div>
