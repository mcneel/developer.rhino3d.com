+++
aliases = ["/en/5/samples/rhinocommon/instance-definition-names/", "/en/6/samples/rhinocommon/instance-definition-names/", "/en/7/samples/rhinocommon/instance-definition-names/", "/wip/samples/rhinocommon/instance-definition-names/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to print the instance definition names."
keywords = [ "instance", "definition", "names" ]
languages = [ "C#", "Python", "VB" ]
sdk = [ "RhinoCommon" ]
title = "Instance Definition Names"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/rhinocommonsamples/printinstancedefinitions"
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
  public static Result InstanceDefinitionNames(RhinoDoc doc)
  {
    var instance-definition-names = (from instance_definition in doc.InstanceDefinitions
                                     where instance_definition != null && !instance_definition.IsDeleted
                                     select instance_definition.Name);

    foreach (var n in instance-definition-names)
      RhinoApp.WriteLine("Instance definition = {0}", n);

    return Result.Success;
  }
}
```

</div>


<div class="codetab-content" id="vb">

```vbnet
Partial Friend Class Examples
  Public Shared Function InstanceDefinitionNames(ByVal doc As RhinoDoc) As Result
	Dim instance-definition-names = (
	    From instance_definition In doc.InstanceDefinitions
	    Where instance_definition IsNot Nothing AndAlso Not instance_definition.IsDeleted
	    Select instance_definition.Name)

	For Each n In instance-definition-names
	  RhinoApp.WriteLine("Instance definition = {0}", n)
	Next n

	Return Result.Success
  End Function
End Class
```

</div>


<div class="codetab-content" id="py">

```python
from scriptcontext import doc

def RunCommand():
    instanceDefinitionNames = [instanceDefinition.Name for instanceDefinition in doc.InstanceDefinitions if instanceDefinition != None and not instanceDefinition.IsDeleted]

    for n in instanceDefinitionNames:
        print "instance definition = {0}".format(n)

if __name__ == "__main__":
    RunCommand()
```

</div>
