---
layout: code-sample
title: Print Instance Definition (Block) Tree
author: 
categories: ['Other'] 
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
keywords: ['print', 'instance', 'definition', '(block)', 'tree']
order: 136
description:  
---



```cs
public class InstanceDefinitionTreeCommand : Command
{
  public override string EnglishName { get { return "csInstanceDefinitionTree"; } }

  protected override Result RunCommand(RhinoDoc doc, RunMode mode)
  {
    var instance_definitions = doc.InstanceDefinitions;
    var instance_definition_count = instance_definitions.Count;

    if (instance_definition_count == 0)
    {
      RhinoApp.WriteLine("Document contains no instance definitions.");
      return Result.Nothing;
    }

    var dump = new TextLog();
    dump.IndentSize = 4;

    for (int i = 0; i < instance_definition_count; i++)
      DumpInstanceDefinition(instance_definitions[i], ref dump, true);

    RhinoApp.WriteLine(dump.ToString());

    return Result.Success;
  }

  private void DumpInstanceDefinition(InstanceDefinition instanceDefinition, ref TextLog dump, bool isRoot)
  {
    if (instanceDefinition != null && !instanceDefinition.IsDeleted)
    {
      string node = isRoot ? "─" : "└";
      dump.Print(string.Format("{0} Instance definition {1} = {2}\n", node, instanceDefinition.Index, instanceDefinition.Name));

      if (instanceDefinition.ObjectCount  > 0)
      {
        dump.PushIndent();
        for (int i = 0; i < instanceDefinition.ObjectCount ; i++)
        {
          var obj = instanceDefinition.Object(i);
          if (obj == null) continue;
          if (obj is InstanceObject)
            DumpInstanceDefinition((obj as InstanceObject).InstanceDefinition, ref dump, false); // Recursive...
          else
            dump.Print("\u2514 Object {0} = {1}\n", i, obj.ShortDescription(false));
        }
        dump.PopIndent();
      }
    }
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Public Class InstanceDefinitionTreeCommand
  Inherits Command
  Public Overrides ReadOnly Property EnglishName() As String
    Get
      Return "vbInstanceDefinitionTree"
    End Get
  End Property

  Protected Overrides Function RunCommand(doc As RhinoDoc, mode As RunMode) As Result
    Dim instanceDefinitions = doc.InstanceDefinitions
    Dim instanceDefinitionCount = instanceDefinitions.Count

    If instanceDefinitionCount = 0 Then
      RhinoApp.WriteLine("Document contains no instance definitions.")
      Return Result.[Nothing]
    End If

    Dim dump = New TextLog()
    dump.IndentSize = 4

    For i As Integer = 0 To instanceDefinitionCount - 1
      DumpInstanceDefinition(instanceDefinitions(i), dump, True)
    Next

    RhinoApp.WriteLine(dump.ToString())

    Return Result.Success
  End Function

  Private Sub DumpInstanceDefinition(instanceDefinition As InstanceDefinition, ByRef dump As TextLog, isRoot As Boolean)
    If instanceDefinition IsNot Nothing AndAlso Not instanceDefinition.IsDeleted Then
      Dim node As String
      If isRoot Then
        node = "─"
      Else
        '"\u2500"; 
        node = "└"
      End If
      '"\u2514"; 
      dump.Print(String.Format("{0} Instance definition {1} = {2}" & vbLf, node, instanceDefinition.Index, instanceDefinition.Name))

      If instanceDefinition.ObjectCount > 0 Then
        dump.PushIndent()
        For i As Integer = 0 To instanceDefinition.ObjectCount - 1
          Dim obj = instanceDefinition.[Object](i)

          If obj Is Nothing Then Continue For

          If TypeOf obj Is InstanceObject Then
            DumpInstanceDefinition(TryCast(obj, InstanceObject).InstanceDefinition, dump, False)
          Else
            ' Recursive...
            dump.Print(String.Format("└ Object {0} = {1}" & vbLf, i, obj.ShortDescription(False)))
          End If
        Next
        dump.PopIndent()
      End If
    End If
  End Sub
End Class
```
{: #vb .tab-pane .fade .in}


```python
from scriptcontext import doc
import Rhino

def RunCommand():
  instanceDefinitions = doc.InstanceDefinitions
  instanceDefinitionCount = instanceDefinitions.Count

  if instanceDefinitionCount == 0:
    print "Document contains no instance definitions."
    return

  dump = Rhino.FileIO.TextLog()
  dump.IndentSize = 4

  for i in range(0, instanceDefinitionCount):
    DumpInstanceDefinition(instanceDefinitions[i], dump, True)

  print dump.ToString()

def DumpInstanceDefinition(instanceDefinition, dump, isRoot):
  if instanceDefinition != None and not instanceDefinition.IsDeleted:
    if isRoot:
      node = '-'
    else:
      node = '+'
    dump.Print(u"{0} Instance definition {1} = {2}\n".format(node, instanceDefinition.Index, instanceDefinition.Name))

    if instanceDefinition.ObjectCount  > 0:
      dump.PushIndent()
      for i in range(0, instanceDefinition.ObjectCount):
        obj = instanceDefinition.Object(i)
        if obj != None and type(obj) == Rhino.DocObjects.InstanceObject:
          DumpInstanceDefinition(obj.InstanceDefinition, dump, False) # Recursive...
        else:
          dump.Print(u"+ Object {0} = {1}\n".format(i, obj.ShortDescription(False)))
      dump.PopIndent()

if __name__ == "__main__":
  RunCommand()
```
{: #py .tab-pane .fade .in}


