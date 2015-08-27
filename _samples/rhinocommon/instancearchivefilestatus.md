---
layout: code-sample
author:
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
title: Instance Archive File Status
keywords: ['instance', 'archive', 'file', 'status']
categories: ['Other']
description:
order: 1
---

```cs
partial class Examples
{
  public static Rhino.Commands.Result InstanceArchiveFileStatus(Rhino.RhinoDoc doc)
  {
    for (int i = 0; i < doc.InstanceDefinitions.Count; i++)
    {
      Rhino.DocObjects.InstanceDefinition iDef = doc.InstanceDefinitions[i];
      Rhino.DocObjects.InstanceDefinitionArchiveFileStatus iDefStatus = iDef.ArchiveFileStatus;

      string status = "Unknown";
      switch (iDefStatus)
      {
        case Rhino.DocObjects.InstanceDefinitionArchiveFileStatus.NotALinkedInstanceDefinition:
          status = "not a linked instance definition.";
          break;
        case Rhino.DocObjects.InstanceDefinitionArchiveFileStatus.LinkedFileNotReadable:
          status = "archive file is not readable.";
          break;
        case Rhino.DocObjects.InstanceDefinitionArchiveFileStatus.LinkedFileNotFound:
          status = "archive file cannot be found.";
          break;
        case Rhino.DocObjects.InstanceDefinitionArchiveFileStatus.LinkedFileIsUpToDate:
          status = "archive file is up-to-date.";
          break;
        case Rhino.DocObjects.InstanceDefinitionArchiveFileStatus.LinkedFileIsNewer:
          status = "archive file is newer.";
          break;
        case Rhino.DocObjects.InstanceDefinitionArchiveFileStatus.LinkedFileIsOlder:
          status = "archive file is older.";
          break;
        case Rhino.DocObjects.InstanceDefinitionArchiveFileStatus.LinkedFileIsDifferent:
          status = "archive file is different.";
          break;
      }

      Rhino.RhinoApp.WriteLine("{0} - {1}", iDef.Name, status);
    }

    return Rhino.Commands.Result.Success;
  }
}
```
{: #cs .tab-pane .fade .in .active}


```vbnet
Partial Friend Class Examples
  Public Shared Function InstanceArchiveFileStatus(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
	For i As Integer = 0 To doc.InstanceDefinitions.Count - 1
	  Dim iDef As Rhino.DocObjects.InstanceDefinition = doc.InstanceDefinitions(i)
	  Dim iDefStatus As Rhino.DocObjects.InstanceDefinitionArchiveFileStatus = iDef.ArchiveFileStatus

	  Dim status As String = "Unknown"
	  Select Case iDefStatus
		Case Rhino.DocObjects.InstanceDefinitionArchiveFileStatus.NotALinkedInstanceDefinition
		  status = "not a linked instance definition."
		Case Rhino.DocObjects.InstanceDefinitionArchiveFileStatus.LinkedFileNotReadable
		  status = "archive file is not readable."
		Case Rhino.DocObjects.InstanceDefinitionArchiveFileStatus.LinkedFileNotFound
		  status = "archive file cannot be found."
		Case Rhino.DocObjects.InstanceDefinitionArchiveFileStatus.LinkedFileIsUpToDate
		  status = "archive file is up-to-date."
		Case Rhino.DocObjects.InstanceDefinitionArchiveFileStatus.LinkedFileIsNewer
		  status = "archive file is newer."
		Case Rhino.DocObjects.InstanceDefinitionArchiveFileStatus.LinkedFileIsOlder
		  status = "archive file is older."
		Case Rhino.DocObjects.InstanceDefinitionArchiveFileStatus.LinkedFileIsDifferent
		  status = "archive file is different."
	  End Select

	  Rhino.RhinoApp.WriteLine("{0} - {1}", iDef.Name, status)
	Next i

	Return Rhino.Commands.Result.Success
  End Function
End Class
```
{: #vb .tab-pane .fade .in}


```python
# No Python sample available
```
{: #py .tab-pane .fade .in}

