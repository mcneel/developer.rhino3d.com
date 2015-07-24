---
layout: code-sample
title: Print Instance Definition (Block) Names
author: 
categories: ['Other'] 
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
keywords: ['print', 'instance', 'definition', '(block)', 'names']
order: 135
description:  
---



```cs
public class InstanceDefinitionNamesCommand : Command
{
  public override string EnglishName { get { return "csInstanceDefinitionNames"; } }

  protected override Result RunCommand(RhinoDoc doc, RunMode mode)
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
Public Class ex_printinstancedefinitions
  Inherits Command
  Public Overrides ReadOnly Property EnglishName() As String
    Get
      Return "vbInstanceDefinitionNames"
    End Get
  End Property

  Protected Overrides Function RunCommand(doc As RhinoDoc, mode As RunMode) As Result
    Dim instanceDefinitionNames = (From instanceDefinition In doc.InstanceDefinitions
                                   Where instanceDefinition IsNot Nothing AndAlso Not instanceDefinition.IsDeleted
                                   Select instanceDefinition.Name)

    For Each n As String In instanceDefinitionNames
      RhinoApp.WriteLine([String].Format("Instance definition = {0}", n))
    Next

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


