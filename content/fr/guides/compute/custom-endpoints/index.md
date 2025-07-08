+++
aliases = ["/en/5/guides/compute/custom-endpoints/", "/en/6/guides/compute/custom-endpoints/", "/en/7/guides/compute/custom-endpoints/", "/en/wip/guides/compute/custom-endpoints/"]
authors = [ "steve", "will" ]
categories = [ "Getting Started" ]
description = "Étendre Compute avec des points de terminaison personnalisés"
keywords = [ "developer", "compute", "plug-in" ]
languages = [ "C#", "VB" ]
sdk = [ "Compute" ]
title = "Extension de Compute avec des points de terminaison personnalisés"
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

<!-- publié à l’origine sur Discourse: https://discourse.mcneel.com/t/extending-rhinocompute-server-with-plugins/84266 -->

Par défaut, Compute expose une longue liste de points de terminaison, conçus pour exposer les fonctionnalités dans RhinoCommon et pour permettre la résolution des définitions de Grasshopper et des scripts Python. Mais Compute peut être étendu avec vos propres points de terminaison personnalisés en enregistrant des fonctions dans un module de Rhino. Compute se charge de la sérialisation.

Commencez par définir une classe statique dans votre module et ajoutez la nouvelle fonction en tant que méthode statique (vous pouvez en ajouter plusieurs !).

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

Ensuite, dans la méthode `OnLoad` de la classe `PlugIn` du module, enregistrez la fonction. Ce code est appelé une fois lorsque le module est chargé par Rhino.

```csharp
protected override LoadReturnCode OnLoad(ref string errorMessage)
{
  Rhino.Runtime.HostUtils.RegisterComputeEndPoint("Rhino.CustomEndPoint", typeof(MyCustomComputeFunctions));

  return base.OnLoad(ref errorMessage);
}
```

Vous devrez installer votre module dans Rhino, à la fois localement pour les tests et sur tous les serveurs sur lesquels Compute fonctionne.

Une fois cette opération terminée, vous pourrez ouvrir le point de terminaison `/sdk` dans un navigateur et voir les nouvelles fonctions listées au bas de la page.

{{< call-out "note" "Remarque" >}}
Consultez l’exemple <a href="https://github.com/mcneel/rhino-developer-samples/tree/7/compute/cs/ComputePlugIn" class="alert-link">ComputePlugIn</a> dans le répertoire Rhino Developer Samples.
{{< /call-out >}}