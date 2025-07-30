+++
aliases = ["/en/5/guides/compute/custom-endpoints/", "/en/6/guides/compute/custom-endpoints/", "/en/7/guides/compute/custom-endpoints/", "/en/wip/guides/compute/custom-endpoints/"]
authors = [ "steve", "will" ]
categories = [ "Getting Started" ]
description = "Ampliar Compute con puntos de conexión personalizados"
keywords = [ "developer", "compute", "plug-in" ]
languages = [ "C#", "VB" ]
sdk = [ "Compute" ]
title = "Ampliar Compute con puntos de conexión personalizados"
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

De forma predeterminada, Compute expone una larga lista de puntos de conexión, diseñados para exponer funcionalidades en RhinoCommon, así como para permitir la resolución de definiciones de Grasshopper y scripts de Python. También es posible ampliar Compute con sus propios puntos de conexión personalizados registrando funciones en un plugin de Rhino. Compute se encarga de la serialización.

Primero defina una clase estática en su complemento y añada la nueva función como método estático (puede añadir más de uno).

``csharp
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

A continuación, en el método `OnLoad` de la clase `PlugIn` del plugin, registre la función. Este código se ejecuta una vez cuando Rhino carga el plugin.

``csharp
protected override LoadReturnCode OnLoad(ref string errorMessage)
{
  Rhino.Runtime.HostUtils.RegisterComputeEndPoint("Rhino.CustomEndPoint", typeof(MyCustomComputeFunctions));

  return base.OnLoad(ref errorMessage);
}
```

Deberá instalar su plugin en Rhino, tanto localmente para las pruebas como en cualquier servidor donde se ejecute Compute.

Una vez completado esto, debería poder abrir el punto de conexión `/sdk` en un navegador y ver las nuevas funciones listadas en la parte inferior de la página.

{{< call-out "note" "Nota" >}}
Consulte la <a href="https://github.com/mcneel/rhino-developer-samples/tree/7/compute/cs/ComputePlugIn" class="alert-link">muestra ComputePlugIn</a> en el repositorio de muestras para desarrolladores de Rhino.
{{< /call-out >}}