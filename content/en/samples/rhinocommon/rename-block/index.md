+++
aliases = ["/en/5/samples/rhinocommon/rename-block/", "/en/6/samples/rhinocommon/rename-block/", "/en/7/samples/rhinocommon/rename-block/", "/wip/samples/rhinocommon/rename-block/"]
authors = [ "steve" ]
categories = [ "Blocks" ]
description = "Demonstrates how to rename an instance definition (block)."
keywords = [ "rename", "instance", "definition", "block" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Rename Block"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/renameblock"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 0

+++

<div class="codetab-content" id="cs">

```cs
partial class Examples
{
  public static Result RenameBlock(RhinoDoc doc)
  {
    // Get the name of the insance definition to rename
    var instance_definition_name = "";
    var rc = RhinoGet.GetString("Name of block to rename", true, ref instance_definition_name);
    if (rc != Result.Success)
      return rc;
    if (string.IsNullOrWhiteSpace(instance_definition_name))
      return Result.Nothing;

    // Verify instance definition exists
    var instance_definition = doc.InstanceDefinitions.Find(instance_definition_name, true);
    if (instance_definition == null) {
      RhinoApp.WriteLine("Block \"{0}\" not found.", instance_definition_name);
      return Result.Nothing;
    }

    // Verify instance definition is rename-able
    if (instance_definition.IsDeleted || instance_definition.IsReference) {
      RhinoApp.WriteLine("Unable to rename block \"{0}\".", instance_definition_name);
      return Result.Nothing;
    }

    // Get the new instance definition name
    string instance_definition_new_name = "";
    rc = RhinoGet.GetString("Name of block to rename", true, ref instance_definition_new_name);
    if (rc != Result.Success)
      return rc;
    if (string.IsNullOrWhiteSpace(instance_definition_new_name))
      return Result.Nothing;

    // Verify the new instance definition name is not already in use
    var existing_instance_definition = doc.InstanceDefinitions.Find(instance_definition_new_name, true);
    if (existing_instance_definition != null && !existing_instance_definition.IsDeleted) {
      RhinoApp.WriteLine("Block \"{0}\" already exists.", existing_instance_definition);
      return Result.Nothing;
    }

    // change the block name
    if (!doc.InstanceDefinitions.Modify(instance_definition.Index, instance_definition_new_name, instance_definition.Description, true)) {
      RhinoApp.WriteLine("Could not rename {0} to {1}", instance_definition.Name, instance_definition_new_name);
      return Result.Failure;
    }

    return Result.Success;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function RenameBlock(ByVal doc As RhinoDoc) As Result
	' Get the name of the insance definition to rename
	Dim instance_definition_name = ""
	Dim rc = RhinoGet.GetString("Name of block to rename", True, instance_definition_name)
	If rc IsNot Result.Success Then
	  Return rc
	End If
	If String.IsNullOrWhiteSpace(instance_definition_name) Then
	  Return Result.Nothing
	End If

	' Verify instance definition exists
	Dim instance_definition = doc.InstanceDefinitions.Find(instance_definition_name, True)
	If instance_definition Is Nothing Then
	  RhinoApp.WriteLine("Block ""{0}"" not found.", instance_definition_name)
	  Return Result.Nothing
	End If

	' Verify instance definition is rename-able
	If instance_definition.IsDeleted OrElse instance_definition.IsReference Then
	  RhinoApp.WriteLine("Unable to rename block ""{0}"".", instance_definition_name)
	  Return Result.Nothing
	End If

	' Get the new instance definition name
	Dim instance_definition_new_name As String = ""
	rc = RhinoGet.GetString("Name of block to rename", True, instance_definition_new_name)
	If rc IsNot Result.Success Then
	  Return rc
	End If
	If String.IsNullOrWhiteSpace(instance_definition_new_name) Then
	  Return Result.Nothing
	End If

	' Verify the new instance definition name is not already in use
	Dim existing_instance_definition = doc.InstanceDefinitions.Find(instance_definition_new_name, True)
	If existing_instance_definition IsNot Nothing AndAlso Not existing_instance_definition.IsDeleted Then
	  RhinoApp.WriteLine("Block ""{0}"" already exists.", existing_instance_definition)
	  Return Result.Nothing
	End If

	' change the block name
	If Not doc.InstanceDefinitions.Modify(instance_definition.Index, instance_definition_new_name, instance_definition.Description, True) Then
	  RhinoApp.WriteLine("Could not rename {0} to {1}", instance_definition.Name, instance_definition_new_name)
	  Return Result.Failure
	End If

	Return Result.Success
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
import rhinoscriptsyntax as rs
from scriptcontext import doc

def Rename():
    blockName = rs.GetString("block to rename")
    instanceDefinition = doc.InstanceDefinitions.Find(blockName, True)
    if not instanceDefinition:
        print "{0} block does not exist".format(blockName)
        return

    newName = rs.GetString("new name")
    instanceDefinition = doc.InstanceDefinitions.Find(newName, True)
    if instanceDefinition:
        print "the name '{0}' is already taken by another block".format(newName)
        return

    rs.RenameBlock(blockName, newName)

if __name__ == "__main__":
    Rename()
```

</div>
