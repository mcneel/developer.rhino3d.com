+++
aliases = ["/en/5/guides/compute/compute-net-getting-started/", "/en/6/guides/compute/compute-net-getting-started/", "/en/7/guides/compute/compute-net-getting-started/", "/en/wip/guides/compute/compute-net-getting-started/"]
authors = [ "steve", "scottd", "pedro" ]
categories = [ "Getting Started", "Client" ]
description = "Esta guía muestra todas las herramientas necesarias para empezar a utilizar Rhino Compute Service en Csharp"
keywords = [ "first", "RhinoCommon", "Plugin", "compute" ]
languages = [ "Csharp" ]
sdk = [ "Compute", "RhinoCommon" ]
title = "Llamar a Compute con .NET"
type = "guides"
weight = 5
override_last_modified = "2024-06-06T13:14:51Z"

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

En esta guía, detallaremos cómo puede aprovechar [Rhino Compute&trade;](https://www.rhino3d.com/compute) desde su entorno de desarrollo .NET en Windows para realizar operaciones geométricas en su aplicación.

Para poder realizar peticiones HTTP, es necesario tener Rhino.Compute ejecutándose en un servidor, ya sea local o remoto. Si aún no lo tiene configurado, consulte una de las siguientes guías:
- [Ejecutar Rhino.Compute localmente](https://developer.rhino3d.com/guides/compute/development/)
- [Implantación en servidores de producción](https://developer.rhino3d.com/guides/compute/deploy-to-iis/)

## Requisitos previos

Antes de continuar, asegúrese de que dispone de las herramientas adecuadas. Esta guía asume que usted tiene un:

- Sistema operativo Windows. Rhino.Compute solo funciona en Windows 7 o posterior.
- Entorno de desarrollo. Necesitará uno de los IDE de Microsoft Visual Studio
    - [Visual Studio 2022](https://visualstudio.microsoft.com/downloads/). El IDE más completo para desarrolladores .NET en Windows.
    - [Visual Studio Code](https://code.visualstudio.com/). Un IDE independiente multiplataforma. Es gratuito y de código abierto.

{{< call-out "note" "Nota" >}}
Se recomienda realizar la instalación típica.
{{< /call-out >}}

## Configurar un proyecto de Compute en Visual Studio

Una vez que tenga el servidor Rhino.Compute en funcionamiento (ya sea local o remoto), hay algunas herramientas que son esenciales para comunicarse con él. Estas son las herramientas:

- [Rhino3dm](https://www.nuget.org/packages/Rhino3dm) -  El wrapper Dotnet para [OpenNurbs](https://developer.rhino3d.com/guides/opennurbs/) que contiene las funciones para leer y escribir objetos geométricos de Rhino. Como está disponible como paquete NuGet, puede descargarlo directamente utilizando el administrador de paquetes NuGet.
- [NewtonSoft.JSON](https://www.nuget.org/packages/Newtonsoft.Json/) - La popular biblioteca JSON. RhinoCompute.cs llama directamente a este paquete, ya que la información se define en formato JSON incrustado en el cuerpo de un REST POST. Al igual que rhino3dm, también está disponible como paquete NuGet.
- [RhinoCompute.cs](https://github.com/mcneel/compute.rhino3d/blob/8.x/src/compute.geometry/RhinoCompute.cs) - Es un paquete en desarrollo para añadir clases disponibles en RhinoCommon, pero no disponibles a través de Rhino3dm. RhinoCompute realiza llamadas a RhinoCompute para estas funciones.

Estas son las instrucciones paso a paso para configurar un proyecto básico para utilizar Rhino.Compute:

### Archivo nuevo

1. Si aún no lo ha hecho, inicie **Visual Studio**. En esta guía utilizaremos Visual Studio 2022 Community Edition y C#.
1. En el menú de la derecha, haga clic en **Crear un nuevo proyecto**...
{{< image url="/images/calling_net_01.png" alt="/images/calling_net_01.png" class="image_left" width="100%" >}}
1. Aparecerá el asistente de Nuevo proyecto.  En la columna de la derecha encontrará una lista con todas las plantillas de proyecto posibles entre las que puede elegir. Para filtrar entre ellas, introduzca la palabra *console*.
1. Seleccione la versión C# de la plantilla **Console App** y haga clic en **Siguiente**.
{{< image url="/images/calling_net_02.png" alt="/images/calling_net_02.png" class="image_left" width="100%" >}}
1. Para esta guía, llamaremos a nuestro plugin de demostración *TestCompute*. Introduzca el nombre que desee en el espacio reservado para ello bajo el campo **Nombre del proyecto** .
{{< image url="/images/calling_net_03.png" alt="/images/calling_net_03.png" class="image_left" width="100%" >}}
1. Debajo del nombre, puede seleccionar una **Ubicación** para este proyecto en su dispositivo. Esto es opcional dependiendo de cómo quiera estructurar el proyecto.
{{< image url="/images/calling_net_04.png" alt="/images/calling_net_04.png" class="image_left" width="100%" >}}
1. Haga clic en el botón **Siguiente** . **Nota**: Puede colocar la solución y el proyecto en el mismo directorio para simplificar la ruta raíz.
{{< image url="/images/calling_net_05.png" alt="/images/calling_net_05.png" class="image_left" width="100%" >}}
1. Seleccione el marco de destino para su proyecto de acuerdo con sus especificaciones. En esta guía elegiremos **.NET 8.0 (Long Term Support)**.
{{< image url="/images/calling_net_06.png" alt="/images/calling_net_06.png" class="image_left" width="100%" >}}
1. Al hacer clic en **Crear** se abrirá una nueva solución llamada *TestCompute* ...
{{< image url="/images/calling_net_07.png" alt="/images/calling_net_07.png" class="image_left" width="100%" >}}

### Pasos para instalar los paquetes NuGet
  
1. Haga clic con el botón derecho en el nombre del proyecto en el Explorador de soluciones y seleccione **Administrar paquetes NuGet ...**.
{{< image url="/images/calling_net_nuget_01.png" alt="/images/calling_net_nuget_01.png" class="image_left" width="100%" >}}
1. En la parte izquierda del cuadro de diálogo, haga clic en **Buscar**.
{{< image url="/images/calling_net_nuget_02.png" alt="/images/calling_net_nuget_02.png" class="image_left" width="100%" >}}
1. En el cuadro de búsqueda, introduzca **rhino3dm** y espere a que aparezcan los resultados.
1. Haga clic en el primero. Encontrará otros paquetes que empiezan por *Rhino3dmIO*, pero han sido descatalogados.
{{< image url="/images/calling_net_nuget_03.png" alt="/images/calling_net_nuget_03.png" class="image_left" width="100%" >}}
1. Haga clic en el botón **Instalar** .
{{< image url="/images/calling_net_nuget_04.png" alt="/images/calling_net_nuget_04.png" class="image_left" width="100%" >}}
1. Continúe buscando **Newtonsoft.JSON**. Haga clic en una opción *NewtonSoft.JSON* y pulse el botón **Instalar** .
1. Cierre el cuadro de diálogo Gestionar paquetes NuGet.  Los paquetes Nuget están instalados y listos para usar.

Cambios realizados:

- Los paquetes NuGet *Rhino3dm* y *NewtonSoft.JSON* se han instalado en el proyecto.
- Su proyecto ahora hace referencia a los emsamblajes *Rhino3dm* y *Newtonsoft.JSON*.

### Incluir RhinoCompute.cs en el proyecto

RhinoCompute.cs es un paquete que añade los métodos para llamar al servidor Rhino.Compute.  Está organizado de forma similar a las llamadas de RhinoCommon.

1. Descargue el archivo fuente [RhinoCompute.cs](https://github.com/mcneel/compute.rhino3d/blob/8.x/src/compute.geometry/RhinoCompute.cs) del repositorio [compute.rhino3d github repo](https://github.com/mcneel/compute.rhino3d). Haga clic en el icono **Descargar archivo raw** y guárdelo en su dispositivo.
{{< image url="/images/calling_net_compute_01.png" alt="/images/calling_net_compute_01.png" class="image_left" width="100%" >}}
2. En Visual Studio, utilizando el desplegable **Proyecto** , seleccione **Añadir elemento existente...**.
{{< image url="/images/calling_net_compute_02.png" alt="/images/calling_net_compute_02.png" class="image_left" width="100%" >}}
3. Seleccione el archivo que acaba de descargar y añádalo al proyecto.

Cambios realizados:

- El archivo fuente [RhinoCompute.cs](https://github.com/mcneel/compute.rhino3d/blob/8.x/src/compute.geometry/RhinoCompute.cs) ya está instalado y sus funciones están disponibles en el proyecto.

## El primer uso de Rhino.Compute

Como punto de partida, vamos a crear una sencilla aplicación de consola que muestre el flujo de trabajo estándar para llamar a métodos utilizando Rhino.Compute. La siguiente guía muestra un ejemplo sencillo del uso local de *Rhino3dm* para leer, escribir y crear geometría de Rhino.  A continuación utilizaremos Rhino.Compute para manejar una función que no existe en *Rhino3dm*.

{{< call-out "note" "Nota" >}}
Para simplificar este ejemplo, Rhino.Compute se ejecuta localmente utilizando la dirección web predeterminada: http://localhost:6500. En este caso, no se requiere ninguna clave de API. Si está enviando una solicitud a una máquina virtual remota que está configurada para requerir una clave de API, deberá proporcionar esa información en el encabezado de solicitud HTTP.
{{< /call-out >}}

{{< div class="line-numbers" >}}
```C#
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Rhino.Compute;

namespace TestCompute
{
    class Program
    {
        static void Main(string[] args)
        {
            // Utiliza métodos estándar de Rhino3dm localmente para crear una esfera.
            var sphere = new Rhino.Geometry.Sphere(Rhino.Geometry.Point3d.Origin, 12);
            var sphereAsBrep = sphere.ToBrep();

            // la siguiente función llama a rhino.compute para acceder a algo no
            // disponible en Rhino3dm. En este caso, envíe un Brep a Compute y obtenga una Malla de vuelta.
            var meshes = MeshCompute.CreateFromBrep(sphereAsBrep);

            // Utilice las llamadas locales habituales de Rhino3dm para contar los vértices de la malla.
            Console.WriteLine($"Got {meshes.Length} meshes");
            for (int i = 0; i < meshes.Length; i++)
            {
                Console.WriteLine($"  {i + 1} mesh has {meshes[i].Vertices.Count} vertices");
            }

            Console.WriteLine("press any key to exit");
            Console.ReadKey();
        }
    }
}
```
{{< /div >}}

El ejemplo anterior crea primero una esfera utilizando *Rhino3dm*. A continuación, hacemos una llamada a Rhino.Compute para crear una malla a partir de ese objeto Brep. Rhino.Compute devuelve la malla.  Por último, usamos *Rhino3dm* para recorrer la malla y contar el número de vértices.

<table class="multiline">
<tr>
<th>Línea</th>
<th>Descripción</th>
</tr>
<tr>
<td>5</td>
<td>Incluir el ensamblaje de Rhino.Compute del paquete RhinoCompute.cs.</td>
</tr>
<tr>
<td>19</td>
<td>Aquí la esfera OpenNurbs Brep se envía a Compute para convertirla en una malla.  La malla se devuelve como malla OpenNurbs.</td>
</tr>
</table>

## Ver los resultados de Compute

Veamos ahora otro ejemplo. Muchas veces es necesario calcular la intersección de objetos. Las intersecciones no están en OpenNurbs, pero forman parte de Rhino.Compute. Aquí hay un tutorial para crear dos círculos, encontrar su intersección y, a continuación, convertir los círculos a una imagen SVG para mostrar.

```C#
using System.Collections.Generic;
using System.Text;
using Rhino.Geometry;

namespace CircleIntersection
{
    class Program
    {
        static void Main(string[] args)
        {
            // cree un par de círculos utilizando una copia local de Rhino3dmIo
            var c1 = new Circle(new Point3d(0, 0, 0), 100);
            var c2 = new Circle(new Point3d(30, 30, 0), 70);

            // llame a compute para realizar una operación booleana curva
            var intersectionCurves = Rhino.Compute.CurveCompute.CreateBooleanIntersection(c1.ToNurbsCurve(), c2.ToNurbsCurve());
            Malla[] intersectionMeshes = null;
            if (intersectionCurves != null)
            {
                // utilice Rhino3dmIo local para crear un Brep a partir de las curvas
                var brep = Brep.CreateTrimmedPlane(c1.Plane, intersectionCurves);

                // llame a compute para mallar el Brep
                intersectionMeshes = Rhino.Compute.MeshCompute.CreateFromBrep(brep, MeshingParameters.FastRenderMesh);
            }

            // solo algunas rutinas de ayuda para crear un archivo SVG de los resultados para que podamos ver lo que se generó
            string path = "circle_intersection.svg";
            WriteSvgFile(path, c1, c2, intersectionMeshes);
            System.Diagnostics.Process.Start(path);
        }


        /// <summary>
        /// Rutina muy básica de creación de archivos SVG para hacer un SVG que muestre dos círculos y una malla.
        /// Se ha mantenido simple solo para este ejemplo; hay mucho mejor SVG kits de herramientas disponibles que se podrían
        /// utilizar para rutinas generales.
        /// </summary>
        /// <param name="path"></param>
        /// <param name="circle1"></param>
        /// <param name="circle2"></param>
        /// <param name="intersectionMeshes"></param>
        static void WriteSvgFile(string path, Circle circle1, Circle circle2, Mesh[] intersectionMeshes)
        {
            var doc = new System.Xml.XmlDocument();
            doc.AppendChild(doc.CreateXmlDeclaration("1.0", "UTF-8", "no"));
            doc.XmlResolver = null;
            doc.AppendChild(doc.CreateDocumentType("svg", "-//W3C//DTD SVG 1.1//EN", "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd", null));
            var svgroot = doc.CreateElement("svg");

            var bbox = circle1.BoundingBox;
            bbox.Union(circle2.BoundingBox);
            var length = (bbox.Max - bbox.Min).Length;
            bbox.Inflate(length * 0.05);

            AppendAttribute(doc, svgroot, "viewBox", $"{bbox.Min.X} {bbox.Min.Y} {bbox.Max.X - bbox.Min.X} {bbox.Max.Y - bbox.Min.Y}");
            AppendAttribute(doc, svgroot, "version", "1.1");
            AppendAttribute(doc, svgroot, "xmlns", "http://www.w3.org/2000/svg");
            doc.AppendChild(svgroot);

            if (intersectionMeshes != null)
            {
                foreach (var mesh in intersectionMeshes)
                {
                    foreach (var face in mesh.Faces)
                    {
                        var elem = doc.CreateElement("polygon");
                        var attrib = doc.CreateAttribute("fill");
                        attrib.Value = "#008000"; // green
                        elem.Attributes.Append(attrib);
                        attrib = doc.CreateAttribute("stroke");
                        attrib.Value = "#008000"; // green
                        elem.Attributes.Append(attrib);
                        attrib = doc.CreateAttribute("points");
                        StringBuilder sb = new StringBuilder();
                        var points = new List<Rhino.Geometry.Point3d>();
                        points.Add(mesh.Vertices[face.A]);
                        points.Add(mesh.Vertices[face.B]);
                        points.Add(mesh.Vertices[face.C]);
                        if (face.IsQuad)
                            points.Add(mesh.Vertices[face.D]);
                        for (int i = 0; i < points.Count; i++)
                        {
                            if (i > 0)
                                sb.Append(", ");
                            sb.Append($"{points[i].X}, {points[i].Y}");
                        }
                        attrib.Value = sb.ToString().Trim();
                        elem.Attributes.Append(attrib);
                        svgroot.AppendChild(elem);
                    }
                }
            }

            svgroot.AppendChild(SvgCircle(circle1, doc));
            svgroot.AppendChild(SvgCircle(circle2, doc));

            doc.Save(path);
        }

        static void AppendAttribute(System.Xml.XmlDocument doc, System.Xml.XmlElement element, string name, string value)
        {
            var attr = doc.CreateAttribute(name);
            attr.Value = value;
            element.Attributes.Append(attr);
        }

        static System.Xml.XmlElement SvgCircle(Rhino.Geometry.Circle c, System.Xml.XmlDocument doc)
        {
            var elem = doc.CreateElement("circle");
            var attrib = doc.CreateAttribute("cx");
            attrib.Value = $"{c.Center.X}";
            elem.Attributes.Append(attrib);
            attrib = doc.CreateAttribute("cy");
            attrib.Value = $"{c.Center.Y}";
            elem.Attributes.Append(attrib);
            attrib = doc.CreateAttribute("r");
            attrib.Value = $"{c.Radius}";
            elem.Attributes.Append(attrib);
            attrib = doc.CreateAttribute("fill-opacity");
            attrib.Value = "0";
            elem.Attributes.Append(attrib);
            attrib = doc.CreateAttribute("stroke");
            attrib.Value = "#000000";
            elem.Attributes.Append(attrib);
            return elem;
        }
    }
}
```

## Próximos pasos

**¡Felicidades!**  Dispone de las herramientas para utilizar el servidor [Rhino.Compute](https://www.rhino3d.com/compute). *¿Y ahora qué?*

1. Descargue el repositorio [Compute Samples de GitHub](https://github.com/mcneel/rhino-developer-samples/tree/8/compute/cs).
1. Las bibliotecas son todavía muy nuevas y cambian rápidamente. Pruébelas o participe. Haga preguntas o comparta su trabajo en el [Foro de Compute](https://discourse.mcneel.com/c/serengeti/compute-rhino3d).

<!-- 
**Notas a pie de página**

[^1]: Visual Studio Code is Microsoft's cross-platform source code editor for Windows, Linux, and macOS.  At the time of this writing, Visual Studio code does not yet support the features required to author RhinoCommon plugins.

[^2]: Visual Studio Online is Microsoft's online counterpart to the desktop edition of Visual Studio (referred to as Visual Studio "proper" above).  We have not tested using Visual Studio Online to debug RhinoCommon plugins as having a copy of Rhino running would prove logistically difficult.

[^3]: Visual Studio "proper" is the desktop version of Visual Studio...we are only attaching the "proper" epithet to distinguish it from the Visual Studio Code and Visual Studio Online.  In subsequent guides this will be referred to as simply "Visual Studio."

[^4]: Visual Studio Express for Windows *Desktop* (also named "Express for Desktop" on some pages) offers a development platform that has a less strict licensing agreement policy than the Community edition. Please refer to the EULA for complete details, available during installation. In this edition, debugging of Rhino can be started, but the location of the Rhino executable (rhino.exe), usually available in the Project property page, in the Debug tab, cannot be changed in the UI. After Wizard completion, the location of the Rhino executable can only be edited in the XML of the resulting *.csproj* file, in the main folder of the solution. -->