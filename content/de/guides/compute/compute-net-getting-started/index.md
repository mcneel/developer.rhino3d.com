+++
aliases = ["/en/5/guides/compute/compute-net-getting-started/", "/en/6/guides/compute/compute-net-getting-started/", "/en/7/guides/compute/compute-net-getting-started/", "/en/wip/guides/compute/compute-net-getting-started/"]
authors = [ "steve", "scottd", "pedro" ]
categories = [ "Getting Started", "Client" ]
description = "Diese Anleitung behandelt alle notwendigen Werkzeuge, die für den Einstieg in den Rhino Compute Service in Csharp erforderlich sind."
keywords = [ "first", "RhinoCommon", "Plugin", "compute" ]
languages = [ "Csharp" ]
sdk = [ "Compute", "RhinoCommon" ]
title = "Aufrufen von Compute mit .NET"
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

In diesem Leitfaden erfahren Sie, wie Sie [Rhino Compute&trade;](https://www.rhino3d.com/compute) in Ihrer .NET-Entwicklungsumgebung unter Windows nutzen können, um geometrische Operationen in Ihrer Anwendung durchzuführen.

Um HTTP-Anfragen stellen zu können, muss Rhino.Compute auf einem Server ausgeführt werden, entweder lokal oder remote. Wenn Sie es noch nicht eingerichtet haben, konsultieren Sie bitte einen der folgenden Leitfäden:
- [Rhino.Compute lokal ausführen](https://developer.rhino3d.com/guides/compute/development/)
- [Verteilung auf Produktionsservern](https://developer.rhino3d.com/guides/compute/deploy-to-iis/)

## Voraussetzungen

Bevor Sie fortfahren, vergewissern Sie sich bitte, dass Sie die richtigen Werkzeuge benötigen. Dieser Leitfaden wurde konzipiert für die Verwendung eines:

- Windows-Betriebssystem. Rhino.Compute läuft nur auf Windows 7 oder neuer.
- Entwicklungsumgebung. Sie benötigen eine der IDEs von Microsoft Visual Studio:
    - [Visual Studio 2022](https://visualstudio.microsoft.com/downloads/). Die umfassendste IDE für .NET-Entwickler auf Windows.
    - [Visual Studio Code](https://code.visualstudio.com/). Eine eigenständige plattformübergreifende IDE. Es ist kostenlos und Open Source.

{{< call-out "note" "Anmerkung" >}}
Es wird empfohlen, die Typische Installation auszuführen.
{{< /call-out >}}

## Einrichten eines Compute-Projekts in Visual Studio

Sobald Sie Ihren Rhino.Compute-Server eingerichtet haben und dieser läuft (entweder lokal oder remote), gibt es einige Werkzeuge, die für die Kommunikation mit ihm unerlässlich sind. Hier finden Sie die ausführlichen Beschreibungen dieser Werkzeuge:

- [Rhino3dm](https://www.nuget.org/packages/Rhino3dm) -  Der Dotnet-Wrapper für [OpenNurbs](https://developer.rhino3d.com/guides/opennurbs/), der die Funktionen zum Lesen und Schreiben von Rhino-Geometrie-Objekten enthält. Da es als NuGet-Paket verfügbar ist, können Sie es direkt mit dem NuGet-Paketmanager herunterladen.
- [NewtonSoft.JSON](https://www.nuget.org/packages/Newtonsoft.Json/) - Die äußerst beliebte JSON-Bibliothek. Dieses Paket wird direkt von RhinoCompute.cs aufgerufen, da die Informationen im JSON-Format, eingebettet in den Trägerkörper eines REST POST, definiert sind. Wie rhino3dm ist es auch als NuGet-Paket verfügbar.
- [RhinoCompute.cs](https://github.com/mcneel/compute.rhino3d/blob/8.x/src/compute.geometry/RhinoCompute.cs) - Hier handelt es sich um ein in Arbeit befindliches Paket, das zum Hinzufügen von Klassen gedacht ist, die in RhinoCommon, aber nicht über Rhino3dm verfügbar sind. RhinoCompute.cs führt für diese Funktionen Aufrufe in Rhino.Compute aus.

Hier finden Sie eine Schritt-für-Schritt-Anleitung zum Einrichten eines Basisprojekts zur Verwendung von Rhino.Compute:

### Neue Datei

1. Falls noch nicht geschehen, **starten Sie Visual Studio**. Für die Zwecke dieser Anleitung verwenden wir Visual Studio 2022 Community Edition und C#.
1. Klicken Sie im rechten Menü auf **Neues Projekt erstellen**...
{{< image url="/images/calling_net_01.png" alt="/images/calling_net_01.png" class="image_left" width="100%" >}}
1. Der Assistent für Neue Projekte sollte erscheinen.  In der rechten Spalte finden Sie eine Liste mit allen möglichen Projektvorlagen, aus denen Sie wählen können. Um sie zu filtern, geben Sie das Wort *Console* ein.
1. Wählen Sie die C#-Version der Vorlage **Console App** und klicken Sie auf **Weiter**.
{{< image url="/images/calling_net_02.png" alt="/images/calling_net_02.png" class="image_left" width="100%" >}}
1. Für die Zwecke dieses Leitfadens werden wir unser Demo-Plugin *TestCompute* nennen. Geben Sie den gewünschten Namen in das dafür vorgesehene Feld **Projektname** ein.
{{< image url="/images/calling_net_03.png" alt="/images/calling_net_03.png" class="image_left" width="100%" >}}
1. Unterhalb des Namens können Sie einen **Ort** für dieses Projekt auf Ihrem Gerät auswählen. Dies ist optional, je nachdem, wie Sie Ihr Projekt strukturieren möchten.
{{< image url="/images/calling_net_04.png" alt="/images/calling_net_04.png" class="image_left" width="100%" >}}
1. Klicken Sie auf die Schaltfläche **Weiter**. **Hinweis**: Sie können die Projektmappe und das Projekt im selben Verzeichnis ablegen, um den Stammpfad zu vereinfachen.
{{< image url="/images/calling_net_05.png" alt="/images/calling_net_05.png" class="image_left" width="100%" >}}
1. Wählen Sie das Ziel-Framework für Ihr Projekt nach Ihren Vorgaben aus. In diesem Leitfaden werden wir **.NET 8.0 (Long Term Support)** wählen.
{{< image url="/images/calling_net_06.png" alt="/images/calling_net_06.png" class="image_left" width="100%" >}}
1. Sobald Sie auf **Erstellen** klicken, sollte eine neue Lösung namens *TestCompute* geöffnet werden...
{{< image url="/images/calling_net_07.png" alt="/images/calling_net_07.png" class="image_left" width="100%" >}}

### Schritte zur Installation der NuGet-Pakete
  
1. Klicken Sie im Projektmappen-Explorer mit der rechten Maustaste auf Ihren Projektnamen und wählen Sie **NuGet-Pakete verwalten ...**.
{{< image url="/images/calling_net_nuget_01.png" alt="/images/calling_net_nuget_01.png" class="image_left" width="100%" >}}
1. Klicken Sie auf der linken Seite des Dialogs auf **Durchsuchen**.
{{< image url="/images/calling_net_nuget_02.png" alt="/images/calling_net_nuget_02.png" class="image_left" width="100%" >}}
1. Geben Sie in das Suchfeld **rhino3dm** ein und warten Sie, bis die Ergebnisse angezeigt werden.
1. Klicken Sie auf das erste. Es gibt noch weitere Pakete, die mit *Rhino3dmIO* beginnen, die aber alle nicht mehr weiterentwickelt werden.
{{< image url="/images/calling_net_nuget_03.png" alt="/images/calling_net_nuget_03.png" class="image_left" width="100%" >}}
1. Klicken Sie auf die Schaltfläche **Installieren**.
{{< image url="/images/calling_net_nuget_04.png" alt="/images/calling_net_nuget_04.png" class="image_left" width="100%" >}}
1. Fahren Sie mit der Suche nach **Newtonsoft.JSON** fort. Klicken Sie auf eine *NewtonSoft.JSON*-Option und klicken Sie auf die Schaltfläche **Installieren** .
1. Schließen Sie das Dialogfeld NuGet-Pakete verwalten.  Die Nuget-Pakete sind installiert und einsatzbereit.

Änderungen, die vorgenommen wurden:

- Die *Rhino3dm*- und *NewtonSoft.JSON*-NuGet-Pakete wurden in Ihrem Projekt installiert.
- Ihr Projekt referenziert nun die *Rhino3dm*- und *Newtonsoft.JSON*-Assemblies.

### RhinoCompute.cs in das Projekt mit einschließen

RhinoCompute.cs ist ein Paket, das die Methoden für die Aufrufe im Rhino.Compute-Server hinzufügt.  Es ist ähnlich wie die RhinoCommon-Aufrufe organisiert.

1. Laden Sie die [RhinoCompute.cs](https://github.com/mcneel/compute.rhino3d/blob/8.x/src/compute.geometry/RhinoCompute.cs)-Quelldatei aus dem [compute.rhino3d-github-Repo](https://github.com/mcneel/compute.rhino3d) herunter. Klicken Sie auf das Symbol **Download raw file** und speichern Sie sie an einem beliebigen Ort auf Ihrem Gerät.
{{< image url="/images/calling_net_compute_01.png" alt="/images/calling_net_compute_01.png" class="image_left" width="100%" >}}
2. Wählen Sie in Visual Studio über das Pulldown-Menü **Projekt** die Option **Vorhandenes Element hinzufügen...**
{{< image url="/images/calling_net_compute_02.png" alt="/images/calling_net_compute_02.png" class="image_left" width="100%" >}}
3. Wählen Sie die soeben heruntergeladene Datei aus und fügen Sie sie dem Projekt hinzu.

Änderungen, die vorgenommen wurden:

- Die [RhinoCompute.cs](https://github.com/mcneel/compute.rhino3d/blob/8.x/src/compute.geometry/RhinoCompute.cs)-Quelldatei ist nun installiert und ihre Funktionen sind in Ihrem Projekt verfügbar.

## Die erste Verwendung von Rhino.Compute

Lassen Sie uns zunächst eine einfache Konsolenanwendung erstellen, die den Standardarbeitsablauf für Aufrufmethoden mit Rhino.Compute zeigt. Die folgende Anleitung zeigt ein einfaches Beispiel für die lokale Verwendung von *Rhino3dm* zum Lesen, Schreiben und Erstellen von Rhino-Geometrie.  Dann werden wir Rhino.Compute verwenden, um eine Funktion zu behandeln, die in *Rhino3dm* nicht existiert.

{{< call-out "note" "Anmerkung" >}}
Um dieses Beispiel zu vereinfachen, läuft Rhino.Compute lokal unter der Standard-Webadresse: http://localhost:6500. In diesem Fall ist kein API-Schlüssel erforderlich. Wenn Sie eine Anfrage an eine Remote-VM senden, die so konfiguriert ist, dass ein API-Schlüssel erforderlich ist, müssen Sie diese Informationen im HTTP-Anfrage-Header angeben.
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

Das obige Beispiel erzeugt zunächst eine Kugel mit *Rhino3dm*. Dann machen wir einen Aufruf an Rhino.Compute, um ein Netz aus diesem Brep-Objekt zu erstellen. Rhino.Compute gibt uns dann das Netz.  Schließlich verwenden wir *Rhino3dm*, um durch das Netz zu gehen und die Scheitelpunkte zu zählen.

<table class="multiline">
<tr>
<th>Linie</th>
<th>Beschreibung</th>
</tr>
<tr>
<td>5</td>
<td>Fügen Sie die Rhino.Compute Assembly aus dem RhinoCompute.cs-Paket ein.</td>
</tr>
<tr>
<td>19</td>
<td>Hier wird die OpenNurbs-Brep-Sphäre an Compute gesendet, um sie in ein Netz zu konvertieren.  Das Netz wird als OpenNurbs-Netz zurückgegeben.</td>
</tr>
</table>

## Die Ergebnisse von Compute sehen

Sehen wir uns nun ein anderes Beispiel an. In vielen Fällen muss die Schnittmenge von Objekten berechnet werden. Schnittpunkte sind nicht in OpenNurbs, aber sie sind Teil von Rhino.Compute. Hier ist eine Anleitung, um zwei Kreise zu erstellen, ihren Schnittpunkt zu finden und die Kreise dann in ein SVG-Bild zu konvertieren, um sie anzuzeigen.

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
            Polygonnetz[] intersectionMeshes = null;
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

## Weitere Schritte:

**Herzlichen Glückwunsch!**  Sie haben die Werkzeuge, um den [Rhino.Compute-Server](https://www.rhino3d.com/compute) zu verwenden. *Was nun?*

1. Laden Sie das [Compute Samples Repo von GitHub](https://github.com/mcneel/rhino-developer-samples/tree/8/compute/cs) herunter.
1. Die Bibliotheken sind noch sehr neu und verändern sich schnell. Probieren Sie sie aus oder beteiligen Sie sich. Stellen Sie Fragen oder teilen Sie Ihre Arbeit im [Compute-Diskussionsforum](https://discourse.mcneel.com/c/serengeti/compute-rhino3d) mit.

<!-- 
**Fußnoten**

[^1]: Visual Studio Code is Microsoft's cross-platform source code editor for Windows, Linux, and macOS.  At the time of this writing, Visual Studio code does not yet support the features required to author RhinoCommon plugins.

[^2]: Visual Studio Online is Microsoft's online counterpart to the desktop edition of Visual Studio (referred to as Visual Studio "eigentlich" oben).  Wir haben die Verwendung von Visual Studio Online zum Debuggen von RhinoCommon-Plugins nicht getestet, da es sich als logistisch schwierig erweisen würde, eine Kopie von Rhino laufen zu lassen.

[^3]: Visual Studio "eigentlich" ist die Desktop-Version von Visual Studio... wir fügen den Beinamen "eigentlich" nur hinzu, um sie von Visual Studio Code und Visual Studio Online zu unterscheiden.  In den folgenden Handbüchern wird dies einfach als "Visual Studio" bezeichnet.

[^4]: Visual Studio Express for Windows *Desktop* (also named "Express for Desktop" auf einigen Seiten) bietet eine Entwicklungsplattform mit einer weniger strengen Lizenzierungspolitik als die Community-Edition. Ausführliche Informationen finden Sie in der EULA, die während der Installation verfügbar ist. In dieser Edition kann das Debugging von Rhino gestartet werden, aber der Speicherort der ausführbaren Rhino-Datei (rhino.exe), der normalerweise in der Projekteigenschaftsseite auf dem Reiter Debug verfügbar ist, kann in der Benutzeroberfläche nicht geändert werden. Nach Beendigung des Assistenten kann der Speicherort der ausführbaren Rhino-Datei nur im XML der resultierenden *.csproj* -Datei im Hauptordner der Lösung bearbeitet werden. -->