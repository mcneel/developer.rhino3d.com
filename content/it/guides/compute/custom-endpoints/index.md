+++
aliases = ["/en/5/guides/compute/custom-endpoints/", "/en/6/guides/compute/custom-endpoints/", "/en/7/guides/compute/custom-endpoints/", "/en/wip/guides/compute/custom-endpoints/"]
authors = [ "steve", "will" ]
categories = [ "Getting Started" ]
description = "Estensione di Compute con endpoint personalizzati."
keywords = [ "developer", "compute", "plug-in" ]
languages = [ "C#", "VB" ]
sdk = [ "Compute" ]
title = "Estendere Compute con endpoint personalizzati"
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

Di default, Compute mostra un lungo elenco di endpoint, progettati per esporre le funzionalità di RhinoCommon e per consentire la risoluzione di definizioni Grasshopper e script Python. È anche possibile estendere Compute con endpoint personalizzati registrando le funzioni in un plug-in di Rhino. Compute gestisce la serializzazione.

Definire innanzitutto una classe statica nel plug-in e aggiungere la nuova funzione come metodo statico (è possibile aggiungerne più di uno).

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

Quindi, nel metodo `OnLoad` della classe `PlugIn` del plug-in, registrare la funzione. Questo codice viene richiamato una volta quando il plug-in viene caricato da Rhino.

```csharp
protected override LoadReturnCode OnLoad(ref string errorMessage)
{
  Rhino.Runtime.HostUtils.RegisterComputeEndPoint("Rhino.CustomEndPoint", typeof(MyCustomComputeFunctions));

  return base.OnLoad(ref errorMessage);
}
```

È necessario installare il plug-in in Rhino, sia localmente per i test che su tutti i server in cui viene eseguito Compute.

Una volta completata questa operazione, si dovrebbe essere in grado di aprire l'endpoint `/sdk` in un browser e vedere le nuove funzioni elencate in fondo alla pagina.

{{< call-out "note" "Nota" >}}
Consultare l'esempio <a href="https://github.com/mcneel/rhino-developer-samples/tree/7/compute/cs/ComputePlugIn" class="alert-link">ComputePlugIn</a> nel repository Rhino Developer Samples.
{{< /call-out >}}