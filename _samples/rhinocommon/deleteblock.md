---
layout: code-sample
title: Delete Instance Definition (Block)
author: 
categories: ['Blocks'] 
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
keywords: ['delete', 'instance', 'definition', '(block)']
order: 55
description:  
---



```cs
public class DeleteBlockCommand : Command
{
  public override string EnglishName { get { return "csDeleteInstanceDefinition"; } }

  protected override Result RunCommand(RhinoDoc doc, RunMode mode)
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
{: #cs .tab-pane .fade .in .active}


```vbnet
Public Class DeleteBlockCommand
  Inherits Command
  Public Overrides ReadOnly Property EnglishName() As String
    Get
      Return "vbDeleteInstanceDefinition"
    End Get
  End Property

  Protected Overrides Function RunCommand(doc As RhinoDoc, mode As RunMode) As Result
    ' Get the name of the instance definition to rename
    Dim instanceDefinitionName As String = ""
    Dim rc = Rhino.Input.RhinoGet.GetString("Name of block to delete", True, instanceDefinitionName)
    If rc <> Result.Success Then
      Return rc
    End If
    If [String].IsNullOrWhiteSpace(instanceDefinitionName) Then
      Return Result.[Nothing]
    End If

    ' Verify instance definition exists
    Dim instanceDefinition = doc.InstanceDefinitions.Find(instanceDefinitionName, True)
    If instanceDefinition Is Nothing Then
      RhinoApp.WriteLine([String].Format("Block ""{0}"" not found.", instanceDefinitionName))
      Return Result.[Nothing]
    End If

    ' Verify instance definition can be deleted
    If instanceDefinition.IsReference Then
      RhinoApp.WriteLine([String].Format("Unable to delete block ""{0}"".", instanceDefinitionName))
      Return Result.[Nothing]
    End If

    ' delete block and all references
    If Not doc.InstanceDefinitions.Delete(instanceDefinition.Index, True, True) Then
      RhinoApp.WriteLine([String].Format("Could not delete {0} block", instanceDefinition.Name))
      Return Result.Failure
    End If

    Return Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


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
{: #py .tab-pane .fade .in}


