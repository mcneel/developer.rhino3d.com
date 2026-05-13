+++
aliases = ["/en/5/samples/rhinocommon/delete-block-instance-definition/", "/en/6/samples/rhinocommon/delete-block-instance-definition/", "/en/7/samples/rhinocommon/delete-block-instance-definition/", "/en/wip/samples/rhinocommon/delete-block-instance-definition/"]
authors = [ "steve" ]
categories = [ "Blocks" ]
description = "Demonstrates how to delete a block instance definition given the name of the block."
keywords = [ "delete", "instance", "definition", "block" ]
languages = [ "C#", "Python" ]
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

<div class="codetab-content" id="py">

```python
import rhinoscriptsyntax as rs
from scriptcontext import doc

def Delete():
    blockName = rs.GetString("block to delete")
    instanceDefinition = doc.InstanceDefinitions.Find(blockName, True)
    if not instanceDefinition:
        print("{0} block does not exist".format(blockName))
        return

    rs.DeleteBlock(blockName)

if __name__ == "__main__":
    Delete()
```

</div>
