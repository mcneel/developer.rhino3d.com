+++
aliases = ["/en/5/guides/compute/custom-endpoints/", "/en/6/guides/compute/custom-endpoints/", "/en/7/guides/compute/custom-endpoints/", "/en/wip/guides/compute/custom-endpoints/"]
authors = [ "steve", "will" ]
categories = [ "Getting Started" ]
description = "Erweitern von Compute mit benutzerdefinierten Endpunkten"
keywords = [ "developer", "compute", "plug-in" ]
languages = [ "C#", "VB" ]
sdk = [ "Compute" ]
title = "Erweitern von Compute mit benutzerdefinierten Endpunkten"
type = "guides"
weight = 10
override_last_modified = "2021-02-03T14:08:07Z"

[admin]
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"
+++

<!-- originally posted to discourse: https://discourse.mcneel.com/t/extending-rhinocompute-server-with-plugins/84266 -->

Standardmäßig stellt Compute eine lange Liste von Endpunkten zur Verfügung, die entwickelt wurden, um Funktionen in RhinoCommon darzustellen sowie Grasshopper-Definitionen und zu lösende Python-Skripte zu aktivieren. Es ist auch möglich, Compute mit Ihren eigenen benutzerdefinierten Endpunkten zu erweitern, indem Sie Funktionen in einem Rhino-Plug-in registrieren. Compute übernimmt die Serialisierung.

Definieren Sie zunächst eine statische Klasse in Ihrem Plug-in und fügen Sie die neue Funktion als statische Methode hinzu (Sie können mehr als eine hinzufügen!).

```csharp
static class MyCustomComputeFunctions
{
  public static double Add(double, x, double y, double z) { return x+y+z; }

  public static double AdjustedArea(Curve curve, double adjuster)
  {
    var amp = Rhino.Geometry.AreaMassProperties.Compute(curve);
    return amp.Area * adjuster;
  }
}
```

Dann registrieren Sie die Funktion in der Methode `OnLoad` der Plug-in-Klasse `PlugIn`. Dieser Code wird einmal aufgerufen, wenn das Plug-in von Rhino geladen wird.

```csharp
protected override LoadReturnCode OnLoad(ref string errorMessage)
{
  Rhino.Runtime.HostUtils.RegisterComputeEndPoint("Rhino.CustomEndPoint", typeof(MyCustomComputeFunctions));

  return base.OnLoad(ref errorMessage);
}
```

Sie müssen Ihr Plug-in in Rhino installieren, sowohl lokal zum Testen als auch auf allen Servern, auf denen Compute läuft.

Sobald dies abgeschlossen ist, sollten Sie in der Lage sein, den Endpunkt `/sdk` in einem Browser zu öffnen und die neuen Funktionen unten auf der Seite zu sehen.

{{< call-out "note" "Anmerkung" >}}
Sehen Sie sich das <a href="https://github.com/mcneel/rhino-developer-samples/tree/7/compute/cs/ComputePlugIn" class="alert-link">ComputePlugIn-Beispiel</a> im Rhino Developer Samples Repository an.
{{< /call-out >}}