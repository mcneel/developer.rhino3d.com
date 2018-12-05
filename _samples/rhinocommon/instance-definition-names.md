---
title: Instance Definition Names
description: Demonstrates how to print the instance definition names.
authors: ['steve_baer']
author_contacts: ['stevebaer']
sdk: ['RhinoCommon']
languages: ['C#', 'Python', 'VB']
platforms: ['Windows', 'Mac']
categories: ['Other']
origin: http://wiki.mcneel.com/developer/rhinocommonsamples/printinstancedefinitions
order: 1
keywords: ['instance', 'definition', 'names']
layout: code-sample-rhinocommon
---

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
{: #cs .tab-pane .fade .in .active}


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
{: #vb .tab-pane .fade .in}


```python
from scriptcontext import doc

def RunCommand():
  instanceDefinitionNames = [instanceDefinition.Name for instanceDefinition in doc.InstanceDefinitions
                             if instanceDefinition != None and not instanceDefinition.IsDeleted]

  for n in instanceDefinitionNames:
    print "instance definition = {0}".format(n)

if __name__ == "__main__":
  RunCommand()
```
{: #py .tab-pane .fade .in}
