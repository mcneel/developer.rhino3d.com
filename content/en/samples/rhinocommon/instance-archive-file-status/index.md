+++
aliases = ["/en/5/samples/rhinocommon/instance-archive-file-status/", "/en/6/samples/rhinocommon/instance-archive-file-status/", "/en/7/samples/rhinocommon/instance-archive-file-status/", "/en/wip/samples/rhinocommon/instance-archive-file-status/"]
authors = [ "steve" ]
categories = [ "Other" ]
description = "Demonstrates how to find the status of a file that contains an instance (block) definition."
keywords = [ "instance", "archive", "file", "status" ]
languages = [ "C#", "Python" ]
sdk = [ "RhinoCommon" ]
title = "Instance Archive File Status"
type = "samples/rhinocommon"
weight = 1

[admin]
TODO = ""
origin = ""
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

</div>

<div class="codetab-content" id="py">

```python
#! python 3
import Rhino
import scriptcontext as sc

def RunCommand():
    for i in range(sc.doc.InstanceDefinitions.Count):
        iDef = sc.doc.InstanceDefinitions[i]
        iDefStatus = iDef.ArchiveFileStatus

        status = "Unknown"
        if iDefStatus == Rhino.DocObjects.InstanceDefinitionArchiveFileStatus.NotALinkedInstanceDefinition:
            status = "not a linked instance definition."
        elif iDefStatus == Rhino.DocObjects.InstanceDefinitionArchiveFileStatus.LinkedFileNotReadable:
            status = "archive file is not readable."
        elif iDefStatus == Rhino.DocObjects.InstanceDefinitionArchiveFileStatus.LinkedFileNotFound:
            status = "archive file cannot be found."
        elif iDefStatus == Rhino.DocObjects.InstanceDefinitionArchiveFileStatus.LinkedFileIsUpToDate:
            status = "archive file is up-to-date."
        elif iDefStatus == Rhino.DocObjects.InstanceDefinitionArchiveFileStatus.LinkedFileIsNewer:
            status = "archive file is newer."
        elif iDefStatus == Rhino.DocObjects.InstanceDefinitionArchiveFileStatus.LinkedFileIsOlder:
            status = "archive file is older."
        elif iDefStatus == Rhino.DocObjects.InstanceDefinitionArchiveFileStatus.LinkedFileIsDifferent:
            status = "archive file is different."

        Rhino.RhinoApp.WriteLine("{0} - {1}", iDef.Name, status)

    return Rhino.Commands.Result.Success

if __name__ == "__main__":
    RunCommand()
```

</div>
