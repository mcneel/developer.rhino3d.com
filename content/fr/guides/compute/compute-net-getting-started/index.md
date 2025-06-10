+++
aliases = ["/en/5/guides/compute/compute-net-getting-started/", "/en/6/guides/compute/compute-net-getting-started/", "/en/7/guides/compute/compute-net-getting-started/", "/en/wip/guides/compute/compute-net-getting-started/"]
authors = [ "steve", "scottd", "pedro" ]
categories = [ "Getting Started", "Client" ]
description = "Ce guide couvre tous les outils nécessaires pour démarrer avec le service Rhino Compute en CSharp."
keywords = [ "first", "RhinoCommon", "Plugin", "compute" ]
languages = [ "Csharp" ]
sdk = [ "Compute", "RhinoCommon" ]
title = "Appeler Compute avec .NET"
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

Dans ce guide, nous allons expliquer comment vous pouvez tirer parti de [Rhino Compute&trade;](https://www.rhino3d.com/compute) à partir de votre environnement de développement .NET sous Windows pour effectuer des opérations géométriques dans votre application.

Pour pouvoir effectuer des requêtes HTTP, Rhino.Compute doit fonctionner sur un serveur, soit localement, soit à distance. Si vous ne l’avez pas encore configuré, veuillez consulter l’un de ces guides :
- [Exécuter Rhino.Compute localement](https://developer.rhino3d.com/guides/compute/development/)
- [Déploiement sur les serveurs de production](https://developer.rhino3d.com/guides/compute/deploy-to-iis/)

## Conditions préalables

Avant de continuer, assurez-vous que vous avez les bons outils. Ce guide suppose que vous disposez d’un :

- système d’exploitation Windows. Rhino.Compute ne fonctionne que sous Windows 7 ou une version postérieure.
- environnement de développement. Vous aurez besoin de l’un des IDE de Microsoft Visual Studio :
    - [Visual Studio 2022](https://visualstudio.microsoft.com/downloads/). L’IDE le plus complet pour les développeurs .NET sous Windows.
    - [Visual Studio Code](https://code.visualstudio.com/). Un IDE multiplateforme autonome. Il est gratuit et en open source.

{{< call-out "note" "Remarque" >}}
Nous vous recommandons de procéder à l’installation normale.
{{< /call-out >}}

## Mise en place d’un projet Compute avec Visual Studio

Une fois que votre serveur Rhino.Compute est opérationnel (qu’il soit local ou distant) vous allez avoir besoin de quelques outils pour communiquer avec lui. Voici une description détaillée de ces outils :

- [Rhino3dm](https://www.nuget.org/packages/Rhino3dm) -  Le wrapper .NET pour [OpenNurbs](https://developer.rhino3d.com/guides/opennurbs/) qui contient les fonctions de lecture et d’écriture des objets de géométrie de Rhino. Comme il s’agit d’un package NuGet, vous pouvez le télécharger directement à l’aide du gestionnaire de paquets NuGet.
- [NewtonSoft.JSON](https://www.nuget.org/packages/Newtonsoft.Json/) - La très populaire bibliothèque JSON. RhinoCompute.cs appelle directement ce package car les informations sont définies au format JSON intégrées dans le corps d’un POST REST. Comme rhino3dm, il est également disponible en tant que package NuGet.
- [RhinoCompute.cs](https://github.com/mcneel/compute.rhino3d/blob/8.x/src/compute.geometry/RhinoCompute.cs) - Il s’agit d’un paquet en cours de développement destiné à ajouter des classes disponibles dans RhinoCommon, mais pas disponibles via Rhino3dm. RhinoCompute réalise des appels dans RhinoCompute pour ces fonctions.

Les instructions suivantes expliquent pas à pas comment configurer un projet de base afin d’utiliser Rhino.Compute :

### Nouveau fichier

1. Si vous ne l’avez pas encore fait, **lancez Visual Studio**. Pour les besoins de ce guide, nous utilisons Visual Studio 2022 Community Edition et C#.
1. Dans le menu de droite, cliquez sur **Create a new project**.
{{< image url="/images/calling_net_01.png" alt="/images/calling_net_01.png" class="image_left" width="100%" >}}
1. L’assistant de création de projet s’ouvre.  Dans la colonne de droite, vous trouverez une liste de tous les modèles de projets disponibles. Pour les filtrer, saisissez le mot *console*.
1. Sélectionnez la version C# du modèle **Console App** et cliquez sur **Next**.
{{< image url="/images/calling_net_02.png" alt="/images/calling_net_02.png" class="image_left" width="100%" >}}
1. Pour les besoins de ce guide, nous appellerons notre module de démonstration *TestCompute*. Saisissez le nom de votre choix dans l’espace prévu à cet effet sous **Project name**.
{{< image url="/images/calling_net_03.png" alt="/images/calling_net_03.png" class="image_left" width="100%" >}}
1. En dessous du nom, sous **Location**, vous pouvez sélectionner un emplacement pour ce projet sur votre appareil. Cette option est facultative et dépend de la manière dont vous souhaitez structurer votre projet.
{{< image url="/images/calling_net_04.png" alt="/images/calling_net_04.png" class="image_left" width="100%" >}}
1. Cliquez sur le bouton **Next**. **Remarque** : vous pouvez placer la solution et le projet dans le même répertoire pour simplifier le chemin d’accès à la racine.
{{< image url="/images/calling_net_05.png" alt="/images/calling_net_05.png" class="image_left" width="100%" >}}
1. Sélectionnez le framework cible pour votre projet en fonction de vos spécifications. Dans ce guide, nous choisirons **.NET 8.0 (Long Term Support)**.
{{< image url="/images/calling_net_06.png" alt="/images/calling_net_06.png" class="image_left" width="100%" >}}
1. Une fois que vous avez cliqué sur **Create**, une nouvelle solution appelée *TestCompute* s’ouvre.
{{< image url="/images/calling_net_07.png" alt="/images/calling_net_07.png" class="image_left" width="100%" >}}

### Installation des paquets NuGet
  
1. Cliquez avec le bouton droit de la souris sur le nom de votre projet dans la section Solution Explorer et sélectionnez **Manage NuGet Packages...**.
{{< image url="/images/calling_net_nuget_01.png" alt="/images/calling_net_nuget_01.png" class="image_left" width="100%" >}}
1. Dans la partie gauche de la boîte de dialogue, cliquez sur **Browse**.
{{< image url="/images/calling_net_nuget_02.png" alt="/images/calling_net_nuget_02.png" class="image_left" width="100%" >}}
1. Dans le champ de recherche, saisissez **rhino3dm** et attendez que les résultats apparaissent.
1. Cliquez sur le premier. Vous trouverez d’autres paquets commençant par *Rhino3dmIO*, mais tous ont été abandonnés.
{{< image url="/images/calling_net_nuget_03.png" alt="/images/calling_net_nuget_03.png" class="image_left" width="100%" >}}
1. Cliquez sur le bouton **Install**.
{{< image url="/images/calling_net_nuget_04.png" alt="/images/calling_net_nuget_04.png" class="image_left" width="100%" >}}
1. Recherchez à présent **Newtonsoft.JSON**. Sélectionnez une option *NewtonSoft.JSON* et cliquez sur le bouton **Install**.
1. Fermez la boîte de dialogue de gestion des paquets NuGet.  Les paquets NuGet sont à présent installés et prêts à être utilisés.

Ce que nous venons de faire :

- Nous avons installé les paquets NuGet *Rhino3dm* et *NewtonSoft.JSON* dans notre projet.
- Notre projet référence maintenant les ensembles *Rhino3dm* et *Newtonsoft.JSON*.

### Inclure RhinoCompute.cs dans le projet

RhinoCompute.cs est un package qui ajoute les méthodes à appeler dans le serveur Rhino.Compute.  Il est organisé de la même manière que les appels RhinoCommon.

1. Téléchargez le fichier source [RhinoCompute.cs](https://github.com/mcneel/compute.rhino3d/blob/8.x/src/compute.geometry/RhinoCompute.cs) à partir du [répertoire GitHub compute.rhino3d](https://github.com/mcneel/compute.rhino3d). Cliquez sur l’icône de **téléchargement du fichier brut** et enregistrez-le à l’endroit de votre choix sur votre appareil.
{{< image url="/images/calling_net_compute_01.png" alt="/images/calling_net_compute_01.png" class="image_left" width="100%" >}}
2. Dans Visual Studio, à l'aide du menu déroulant du **projet**, cliquez sur **Add > Existing Item...**.
{{< image url="/images/calling_net_compute_02.png" alt="/images/calling_net_compute_02.png" class="image_left" width="100%" >}}
3. Sélectionnez le fichier que vous venez de télécharger et ajoutez-le au projet.

Ce que nous venons de faire :

- Nous venons d’installer le fichier source [RhinoCompute.cs](https://github.com/mcneel/compute.rhino3d/blob/8.x/src/compute.geometry/RhinoCompute.cs) et ses fonctions sont à présent disponibles dans notre projet.

## Première utilisation de Rhino.Compute

Pour commencer, nous allons créer une application console simple qui montre le flux de travail standard pour appeler des méthodes à l’aide de Rhino.Compute. Le guide ci-dessous présente un exemple simple d’utilisation locale de *Rhino3dm* pour lire, écrire et créer des géométries de Rhino.  Nous utiliserons ensuite Rhino.Compute pour gérer une fonction qui n’existe pas dans *Rhino3dm*.

{{< call-out "note" "Remarque" >}}
Pour simplifier cet exemple, Rhino.Compute fonctionne localement en utilisant l’adresse Web par défaut : http://localhost:6500. Aucune clé API n’est requise dans ce cas. Si vous envoyez une requête à une VM distante configurée pour demander une clé API, vous devrez fournir cette information dans l’en-tête de la requête HTTP.
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
            // Uses standard Rhino3dm methods locally to create a sphere.
            var sphere = new Rhino.Geometry.Sphere(Rhino.Geometry.Point3d.Origin, 12);
            var sphereAsBrep = sphere.ToBrep();

            // the following function calls rhino.compute to get access to something not
            // available in Rhino3dm. In this case send a Brep to Compute and get a Mesh back.
            var meshes = MeshCompute.CreateFromBrep(sphereAsBrep);

            // Use regular Rhino3dm local calls to count the vertices in the mesh.
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

L’exemple ci-dessus crée d’abord une sphère en utilisant *Rhino3dm*. Ensuite, nous appelons Rhino.Compute pour créer un maillage à partir de cet objet Brep. Puis, Rhino.Compute renvoie le maillage.  Enfin, nous utilisons *Rhino3dm* pour parcourir le maillage et compter le nombre de sommets.

<table class="multiline">
<tr>
<th>Ligne</th>
<th>Description</th>
</tr>
<tr>
<td>5</td>
<td>Inclure l’ensemble Rhino.Compute à partir du paquet RhinoCompute.cs.</td>
</tr>
<tr>
<td>19</td>
<td>Ici, la sphère Brep OpenNurbs est envoyée à Compute pour être convertie en maillage.  Le maillage est renvoyé sous la forme d’un maillage OpenNurbs.</td>
</tr>
</table>

## Voir les résultats de Compute

Prenons à présent un autre exemple. Il est souvent nécessaire de calculer l’intersection entre des objets. Les intersections ne sont pas dans OpenNurbs, mais elles font partie de Rhino.Compute. Voici un tutoriel pour créer deux cercles, trouver leur intersection, puis convertir les cercles en une image SVG à afficher.

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
            // create a couple Circles using a local copy of Rhino3dmIo
            var c1 = new Circle(new Point3d(0, 0, 0), 100);
            var c2 = new Circle(new Point3d(30, 30, 0), 70);

            // call compute to perform a curve boolean operation
            var intersectionCurves = Rhino.Compute.CurveCompute.CreateBooleanIntersection(c1.ToNurbsCurve(), c2.ToNurbsCurve());
            Mesh[] intersectionMeshes = null;
            if (intersectionCurves != null)
            {
                // use local Rhino3dmIo to create a Brep from the curves
                var brep = Brep.CreateTrimmedPlane(c1.Plane, intersectionCurves);

                // call compute to mesh the Brep
                intersectionMeshes = Rhino.Compute.MeshCompute.CreateFromBrep(brep, MeshingParameters.FastRenderMesh);
            }

            // just some helper routines to create an SVG file of the results so we can see what was generated
            string path = "circle_intersection.svg";
            WriteSvgFile(path, c1, c2, intersectionMeshes);
            System.Diagnostics.Process.Start(path);
        }


        /// <summary>
        /// Very basic SVG file creation routine to make an SVG that displays two circles and a mesh.
        /// Kept simple just for this sample; there are much better SVG toolkits available that could
        /// be used for general purpose routines.
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

## Étapes suivantes

**Félicitations !**  Vous disposez à présent des outils nécessaires pour utiliser le serveur [Rhino Compute](https://www.rhino3d.com/compute). *Et maintenant ?*

1. Téléchargez le [répertoire d’exemples de Compute sur GitHub](https://github.com/mcneel/rhino-developer-samples/tree/8/compute/cs).
1. Les bibliothèques sont encore très récentes et changent rapidement. Essayez-les ou impliquez-vous. Posez vos questions ou partagez vos travaux sur le [Forum de discussion Compute](https://discourse.mcneel.com/c/serengeti/compute-rhino3d).

<!-- 
**Notes de bas de page**

[^1]: Visual Studio Code is Microsoft's cross-platform source code editor for Windows, Linux, and macOS.  At the time of this writing, Visual Studio code does not yet support the features required to author RhinoCommon plugins.

[^2]: Visual Studio Online is Microsoft's online counterpart to the desktop edition of Visual Studio (referred to as Visual Studio "approprié » ci-dessus).  Nous n’avons pas essayé d’utiliser Visual Studio Online pour déboguer les modules RhinoCommon, car il serait difficile du point de vue logistique d’avoir une copie de Rhino en cours d’exécution.

[^3]: Visual Studio "approprié » est la version de bureau de Visual Studio... nous n’utilisons l’adjectif « approprié » que pour la distinguer de Visual Studio Code et de Visual Studio Online.  Dans les guides suivants, nous l’appellerons simplement « Visual Studio ».

[^4]: Visual Studio Express for Windows *Desktop* (also named "Express for Desktop" sur certaines pages) offre une plateforme de développement dont la politique de licences est moins stricte que celle de l'édition Community. Pour plus de détails, veuillez consulter le contrat de licence de l’utilisateur final, disponible lors de l’installation. Dans cette édition, le débogage de Rhino peut être lancé, mais l’emplacement de l’exécutable de Rhino (rhino.exe), généralement disponible sur la page de propriétés du projet, dans l’onglet Debug, ne peut pas être modifié dans l’interface utilisateur. Une fois l’assistant terminé, l’emplacement de l’exécutable de Rhino ne peut être modifié que dans le XML du fichier *.csproj* résultant, dans le dossier principal de la solution. -->