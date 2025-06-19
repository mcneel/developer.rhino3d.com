+++
aliases = ["/en/5/guides/compute/compute-net-getting-started/", "/en/6/guides/compute/compute-net-getting-started/", "/en/7/guides/compute/compute-net-getting-started/", "/en/wip/guides/compute/compute-net-getting-started/"]
authors = [ "steve", "scottd", "pedro" ]
categories = [ "Getting Started", "Client" ]
description = "Questa guida illustra tutti gli strumenti necessari per iniziare a lavorare con Rhino Compute Service in Csharp."
keywords = [ "first", "RhinoCommon", "Plugin", "compute" ]
languages = [ "Csharp" ]
sdk = [ "Compute", "RhinoCommon" ]
title = "Chiamare Compute con .NET"
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

In questa guida viene illustrato come è sfruttare [Rhino Compute&trade;](https://www.rhino3d.com/compute) nell'ambiente di sviluppo .NET in Windows per eseguire operazioni geometriche nelle applicazioni.

Per poter effettuare richieste HTTP, è necessario che Rhino.Compute sia in esecuzione su un server, locale o remoto. Se non è stato ancora configurato, consultare una delle seguenti guide:
- [Eseguire Rhino.Compute in locale.](https://developer.rhino3d.com/guides/compute/development/)
- [Distribuzione sui server di produzione.](https://developer.rhino3d.com/guides/compute/deploy-to-iis/)

## Prerequisiti

Prima di continuare, assicurarsi di avere a disposizione gli strumenti adeguati. Questa guida richiede l’utilizzo di:

- Sistemi operativi supportati: Rhino.Compute funziona solo su Windows 7 o versione successiva.
- Ambiente di sviluppo. È necessario disporre di uno degli IDE di Microsoft Visual Studio.
    - [Visual Studio 2022](https://visualstudio.microsoft.com/downloads/). L'IDE più completo per gli sviluppatori .NET su Windows.
    - [Visual Studio Code](https://code.visualstudio.com/). IDE multipiattaforma standalone. Open source gratuito.

{{< call-out "note" "Nota" >}}
Si consiglia di avviare l'installazione tipica.
{{< /call-out >}}

## Impostazione di un progetto Compute in Visual Studio.

Una volta che il server Rhino.Compute è attivo e funzionante (in locale o remoto), esistono alcuni strumenti essenziali per comunicare con esso. Ecco le descrizioni dettagliate di questi strumenti:

- [Rhino3dm](https://www.nuget.org/packages/Rhino3dm) -  Il wrapper Dotnet per [OpenNurbs](https://developer.rhino3d.com/guides/opennurbs/) che contiene le funzioni per leggere e scrivere gli oggetti geometrici di Rhino. Poiché è disponibile come pacchetto NuGet, è possibile scaricarlo direttamente utilizzando NuGet Package Manager.
- [NewtonSoft.JSON](https://www.nuget.org/packages/Newtonsoft.Json/) - La libreria JSON molto popolare. Questo pacchetto viene richiamato direttamente da RhinoCompute.cs, in quanto le informazioni sono definite in formato JSON e inserite nel corpo di un POST REST. Come rhino3dm, è disponibile anche come pacchetto NuGet.
- [RhinoCompute.cs](https://github.com/mcneel/compute.rhino3d/blob/8.x/src/compute.geometry/RhinoCompute.cs) - Questo è un pacchetto in divenire che ha lo scopo di aggiungere classi disponibili in RhinoCommon, ma non disponibili tramite Rhino3dm. RhinoCompute chiama il server RhinoCompute per queste funzioni.

Ecco le istruzioni passo passo per impostare un progetto di base per utilizzare Rhino.Compute:

### File Nuovo

1. **Avviare Visual Studio** se non è stato ancora avviato. Ai fini di questa guida, consigliamo di utilizzare Visual Studio 2022 Community Edition.
1. Nel menu di destra, fare clic su **Create a new project**...
{{< image url="/images/calling_net_01.png" alt="/images/calling_net_01.png" class="image_left" width="100%" >}}
1. Viene visualizzata la procedura guidata per un nuovo progetto.  Nella colonna di destra si trova un elenco con tutti i possibili modelli di progetto tra cui scegliere. Per filtrare le varie alternative, digitare *console*.
1. Selezionare la versione C# del modello **Console App** e fare clic su **Next**.
{{< image url="/images/calling_net_02.png" alt="/images/calling_net_02.png" class="image_left" width="100%" >}}
1. Ai fini di questa guida, chiameremo il nostro plug-in demo *TestCompute*. Inserire il nome desiderato nello spazio sotto il campo **Project name**.
{{< image url="/images/calling_net_03.png" alt="/images/calling_net_03.png" class="image_left" width="100%" >}}
1. Sotto il nome, è possibile selezionare una posizione **Location** per questo progetto sul dispositivo. Questa opzione è facoltativa, a seconda di come si vuole strutturare il progetto.
{{< image url="/images/calling_net_04.png" alt="/images/calling_net_04.png" class="image_left" width="100%" >}}
1. Fare clic sul pulsante **Next**. **Nota**: È possibile posizionare la soluzione e il progetto nella stessa cartella per semplificare il percorso principale.
{{< image url="/images/calling_net_05.png" alt="/images/calling_net_05.png" class="image_left" width="100%" >}}
1. Selezionate il framework di destinazione per il progetto in base alle specifiche. In questa guida sceglieremo **.NET 8.0 (Long Term Support)**.
{{< image url="/images/calling_net_06.png" alt="/images/calling_net_06.png" class="image_left" width="100%" >}}
1. Dopo aver fatto clic su **Create**, si aprirà una nuova soluzione chiamata *TestCompute* ...
{{< image url="/images/calling_net_07.png" alt="/images/calling_net_07.png" class="image_left" width="100%" >}}

### Passi per installare i pacchetti NuGet
  
1. Fare clic con il pulsante destro del mouse sul nome del progetto in Solution Explorer e selezionare **Manage NuGet Packages...**
{{< image url="/images/calling_net_nuget_01.png" alt="/images/calling_net_nuget_01.png" class="image_left" width="100%" >}}
1. Sul lato sinistro della finestra di dialogo, fare clic su **Browse**.
{{< image url="/images/calling_net_nuget_02.png" alt="/images/calling_net_nuget_02.png" class="image_left" width="100%" >}}
1. Nella casella di ricerca inserire **rhino3dm** e attendere che vengano visualizzati i risultati.
1. Fare clic sul primo. È possibile trovare altri pacchetti che iniziano con *Rhino3dmIO*, ma tutti sono stati dismessi.
{{< image url="/images/calling_net_nuget_03.png" alt="/images/calling_net_nuget_03.png" class="image_left" width="100%" >}}
1. Fare clic sul pulsante **Installa**.
{{< image url="/images/calling_net_nuget_04.png" alt="/images/calling_net_nuget_04.png" class="image_left" width="100%" >}}
1. Continuare a cercare **Newtonsoft.JSON**. Fare clic su un'opzione *NewtonSoft.JSON* e sul pulsante **Install**.
1. Chiudere la finestra di dialogo Manage NuGet Packages.  I pacchetti Nuget sono installati e pronti all'uso.

Modifiche apportate:

- I pacchetti NuGet *Rhino3dm* e *NewtonSoft.JSON* sono stati installati nel progetto.
- Il progetto ora fa riferimento a *Rhino3dm* e *Newtonsoft.JSON*.

### Includere RhinoCompute.cs nel progetto

RhinoCompute.cs è un pacchetto che aggiunge i metodi di chiamata del server Rhino.Compute.  Le chiamate sono organizzate in modo simile alle chiamate di RhinoCommon.

1. Scaricare il file sorgente [RhinoCompute.cs](https://github.com/mcneel/compute.rhino3d/blob/8.x/src/compute.geometry/RhinoCompute.cs) dal [repository github compute.rhino3d](https://github.com/mcneel/compute.rhino3d). Fare clic sull'icona **Download raw file** e memorizzarlo ovunque sul dispositivo.
{{< image url="/images/calling_net_compute_01.png" alt="/images/calling_net_compute_01.png" class="image_left" width="100%" >}}
2. In Visual Studio, utilizzando il menu di scelta rapida **Project**, selezionare **Add Existing Item...**
{{< image url="/images/calling_net_compute_02.png" alt="/images/calling_net_compute_02.png" class="image_left" width="100%" >}}
3. Selezionare il file appena scaricato e aggiungerlo al progetto.

Modifiche apportate:

- Il file sorgente [RhinoCompute.cs](https://github.com/mcneel/compute.rhino3d/blob/8.x/src/compute.geometry/RhinoCompute.cs) è ora installato e le sue funzioni sono disponibili nel progetto.

## Il primo utilizzo di Rhino.Compute

Come punto di partenza, creiamo una semplice applicazione con console, che mostri il flusso di lavoro standard per chiamare i metodi utilizzando Rhino.Compute. La guida che segue mostra un semplice esempio di utilizzo di *Rhino3dm* in locale per leggere, scrivere e creare la geometria di Rhino.  Useremo poi Rhino.Compute per gestire una funzione che non esiste in *Rhino3dm*.

{{< call-out "note" "Nota" >}}
Per semplificare questo esempio, Rhino.Compute viene eseguito localmente utilizzando l'indirizzo web predefinito: http://localhost:6500. In questo caso, non è richiesta alcuna chiave API. Se si invia una richiesta a una macchina virtuale remota che è configurata per richiedere una chiave API, è necessario fornire tali informazioni nell'intestazione della richiesta HTTP.
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

L'esempio precedente crea prima una sfera usando *Rhino3dm*. Quindi, effettuiamo una chiamata a Rhino.Compute per creare una mesh da quell'oggetto Brep. Rhino.Compute restituisce quindi la mesh.  Infine, utilizziamo *Rhino3dm* per percorrere la mesh e contare il numero di vertici.

<table class="multiline">
<tr>
<th>Linea</th>
<th>Descrizione</th>
</tr>
<tr>
<td>5</td>
<td>Includere Rhino.Compute Assembly per RhinoCompute.cs Package.</td>
</tr>
<tr>
<td>19</td>
<td>Qui la sfera OpenNurbs Brep viene inviata a Compute per essere convertita in una mesh.  La mesh viene restituita come mesh OpenNurbs.</td>
</tr>
</table>

## Vedere i risultati di Compute

Vediamo ora un altro esempio. Spesso è necessario calcolare l'intersezione degli oggetti. Le intersezioni non sono presenti in OpenNurbs, ma fanno parte di Rhino.Compute. Ecco un'esercitazione per creare due cerchi, trovare la loro intersezione e quindi convertirli in un'immagine SVG da visualizzare.

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

## Passi successivi

**Ottimo lavoro!**  Disponi degli strumenti per utilizzare [Rhino Compute server](https://www.rhino3d.com/compute). *E adesso?*

1. Scarica il [repository con esempi di Compute da GitHub](https://github.com/mcneel/rhino-developer-samples/tree/8/compute/cs).
1. Le librerie sono ancora molto nuove e cambiano velocemente. Provale o partecipa! Porgi domande o condividi i tuoi progetti sul [Forum di discussione su Compute](https://discourse.mcneel.com/c/serengeti/compute-rhino3d).

<!-- 
**Note a piè di pagina**

[^1]: Visual Studio Code is Microsoft's cross-platform source code editor for Windows, Linux, and macOS.  At the time of this writing, Visual Studio code does not yet support the features required to author RhinoCommon plugins.

[^2]: Visual Studio Online is Microsoft's online counterpart to the desktop edition of Visual Studio (referred to as Visual Studio "propriamente detto").  Non abbiamo testato l'uso di Visual Studio Online per eseguire il debug dei plugin di RhinoCommon, poiché avere una copia di Rhino in esecuzione si rivelerebbe logisticamente difficile.

[^3]: Visual Studio "La versione "propriamente detta" è la versione desktop di Visual Studio... l'appellativo "propriamente detta" serve solo a distinguerla da Visual Studio Code e Visual Studio Online.  Nelle guide successive faremo riferimento a questo strumento semplicemente come "Visual Studio".

[^4]: Visual Studio Express for Windows *Desktop* (also named "Express for Desktop" in alcune pagine) offre una piattaforma di sviluppo con una politica di accordi di licenza meno rigida rispetto all'edizione Community. Per i dettagli completi, consultare l'EULA, disponibile durante l'installazione. In questa edizione è possibile avviare il debug di Rhino, ma la posizione dell'eseguibile di Rhino (rhino.exe), solitamente disponibile nella pagina delle proprietà del progetto, nel pannello Debug, non può essere modificata nell'interfaccia utente. Dopo il completamento della procedura guidata, la posizione dell'eseguibile di Rhino può essere modificata solo nell'XML del file *.csproj* risultante, nella cartella principale della soluzione. -->