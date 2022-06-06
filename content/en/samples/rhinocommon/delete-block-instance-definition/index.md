+++
aliases = ["/5/samples/rhinocommon/delete-block-instance-definition/", "/6/samples/rhinocommon/delete-block-instance-definition/", "/7/samples/rhinocommon/delete-block-instance-definition/", "/wip/samples/rhinocommon/delete-block-instance-definition/"]
authors = [ "steve" ]
categories = [ "Blocks" ]
description = "Demonstrates how to delete a block instance definition given the name of the block."
keywords = [ "delete", "instance", "definition", "block" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Delete Block Instance Definition"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/deleteblock"
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
  public static Result DeleteBlock(RhinoDoc doc)
  {
    // Get the name of the instance definition to rename
    string instance_definition_name = "";
    var rc = RhinoGet.GetString("Name of block to delete", true, ref instance_definition_name);
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

    // Verify instance definition can be deleted
    if (instance_definition.IsReference) {
      RhinoApp.WriteLine("Unable to delete block \"{0}\".", instance_definition_name);
      return Result.Nothing;
    }

    // delete block and all references
    if (!doc.InstanceDefinitions.Delete(instance_definition.Index, true, true)) {
      RhinoApp.WriteLine("Could not delete {0} block", instance_definition.Name);
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
  Public Shared Function DeleteBlock(ByVal doc As RhinoDoc) As Result
	' Get the name of the instance definition to rename
	Dim instance_definition_name As String = ""
	Dim rc = RhinoGet.GetString("Name of block to delete", True, instance_definition_name)
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

	' Verify instance definition can be deleted
	If instance_definition.IsReference Then
	  RhinoApp.WriteLine("Unable to delete block ""{0}"".", instance_definition_name)
	  Return Result.Nothing
	End If

	' delete block and all references
	If Not doc.InstanceDefinitions.Delete(instance_definition.Index, True, True) Then
	  RhinoApp.WriteLine("Could not delete {0} block", instance_definition.Name)
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

def Delete():
    blockName = rs.GetString("block to delete")
    instanceDefinition = doc.InstanceDefinitions.Find(blockName, True)
    if not instanceDefinition:
        print "{0} block does not exist".format(blockName)
        return

    rs.DeleteBlock(blockName)

if __name__ == "__main__":
    Delete()
```

</div>
