---
layout: code-sample
author:
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
title: Instance Definition Names
keywords: ['instance', 'definition', 'names']
categories: ['Other']
description:
order: 1
---

```cs
partial class Examples
{
  public static Result InstanceDefinitionNames(RhinoDoc doc)
  {
    var instance_definition_names = (from instance_definition in doc.InstanceDefinitions 
                                     where instance_definition != null && !instance_definition.IsDeleted
                                     select instance_definition.Name);

    foreach (var n in instance_definition_names)
      RhinoApp.WriteLine("Instance definition = {0}", n);

    return Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function InstanceDefinitionNames(ByVal doc As RhinoDoc) As Result
	Dim instance_definition_names = (
	    From instance_definition In doc.InstanceDefinitions
	    Where instance_definition IsNot Nothing AndAlso Not instance_definition.IsDeleted
	    Select instance_definition.Name)

	For Each n In instance_definition_names
	  RhinoApp.WriteLine("Instance definition = {0}", n)
	Next n

	Return Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}

