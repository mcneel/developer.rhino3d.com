---
layout: code-sample
title: Rename Instance Definition (Block)
author: 
categories: ['Blocks'] 
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
keywords: ['rename', 'instance', 'definition', '(block)']
order: 139
description:  
---



```cs
public class RenameBlockCommand : Command
{
  public override string EnglishName { get { return "csRenameBlock"; } }

  protected override Result RunCommand(RhinoDoc doc, RunMode mode)
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
{: #cs .tab-pane .fade .in .active}


```vbnet
Public Class RenameBlockCommand
  Inherits Command
  Public Overrides ReadOnly Property EnglishName() As String
    Get
      Return "vbRenameInstanceDefinition"
    End Get
  End Property

  Protected Overrides Function RunCommand(doc As RhinoDoc, mode As RunMode) As Result
    ' Get the name of the insance definition to rename
    Dim instanceDefinitionName As String = ""
    Dim rc = Rhino.Input.RhinoGet.GetString("Name of block to rename", True, instanceDefinitionName)
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

    ' Verify instance definition is rename-able
    If instanceDefinition.IsDeleted OrElse instanceDefinition.IsReference Then
      RhinoApp.WriteLine([String].Format("Unable to rename block ""{0}"".", instanceDefinitionName))
      Return Result.[Nothing]
    End If

    ' Get the new instance definition name
    Dim instanceDefinitionNewName As String = ""
    rc = Rhino.Input.RhinoGet.GetString("Name of block to rename", True, instanceDefinitionNewName)
    If rc <> Result.Success Then
      Return rc
    End If
    If [String].IsNullOrWhiteSpace(instanceDefinitionNewName) Then
      Return Result.[Nothing]
    End If

    ' Verify the new instance definition name is not already in use
    Dim existingInstanceDefinition = doc.InstanceDefinitions.Find(instanceDefinitionNewName, True)
    If existingInstanceDefinition IsNot Nothing AndAlso Not existingInstanceDefinition.IsDeleted Then
      RhinoApp.WriteLine([String].Format("Block ""{0}"" already exists.", existingInstanceDefinition))
      Return Result.[Nothing]
    End If

    ' change the block name
    If Not doc.InstanceDefinitions.Modify(instanceDefinition.Index, instanceDefinitionNewName, instanceDefinition.Description, True) Then
      RhinoApp.WriteLine([String].Format("Could not rename {0} to {1}", instanceDefinition.Name, instanceDefinitionNewName))
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
{: #py .tab-pane .fade .in}


