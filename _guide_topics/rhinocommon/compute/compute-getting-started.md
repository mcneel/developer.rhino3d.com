---
title: Rhino Compute Service (Windows)
description: This guide covers all the necessary tools required to get started with the Rhino Compute Service
authors: ['Steve Baer', 'Scott Davidson']
author_contacts: ['stevebaer', 'scottd']
sdk: ['RhinoCommon', 'Compute']
languages: ['C#']
platforms: ['Windows']
categories: ['Getting Started']
origin:
order: 1
keywords: ['first', 'RhinoCommon', 'Plugin', 'compute']
layout: toc-guide-page
---


By the end of this guide, you should have all the tools installed necessary for using the [Rhino Compute Service](https://www.rhino3d.com/compute).

This guide presumes you have an:

- A PC running Microsoft Windows 7 or later.
- [Rhino for Windows](http://www.rhino3d.com/download)
- One of the IDEs from [Microsoft Visual Studio](https://visualstudio.microsoft.com/)
  - [Visual Studio Code 2017](https://code.visualstudio.com/?wt.mc_id=DX_841432) - Free, Open Source.
  - Or, [Visual Studio 2017](https://visualstudio.microsoft.com/vs/whatsnew/)

**note:** It is recommended that you install the *Typical* installation.

---

## Setting up a Compute Project in Visual Studio

There are a few tools which are essential to communicate with the Compute server. These include:

- [Rhino3dmIO.Desktop](https://www.nuget.org/packages/Rhino3dmIO.Desktop) -  The Dotnet wrapper for [OpenNurbs](https://developer.rhino3d.com/guides/opennurbs/) which contains the functions to read and write Rhino Geometry Objects. This is available as a NuGet package.
- [NewtonSoft.JSON](https://www.nuget.org/packages/Newtonsoft.Json/) - The very popular JSON library.  Compute communicates using a JSON format in the body of a REST POST. This is available as a NuGet Package. This package is called directly by RHinoCompute.cs.
- [RhinoCompute.cs](https://compute.rhino3d.com/sdk/csharp) - This is a work in progress package which is meant to add classes available in RhinoCommon, but not available through Rhino3dmIO. RhinoCompute makes calls into RhinoCompute for these functions.

Here are step by step instructions to setting up a basic project to use Compute:

#### File New

1. If you have not done so already, *launch Visual Studio* (for the purposes of this guide, we are using Visual Studio 2017 Community Edition and C#).
1. Navigate to *File* > *New* > *Project*...
![File New Project]({{ site.baseurl }}/images/your-first-plugin-windows-01.png)
1. A *New Project* wizard should appear.  In the left column, find the *Installed* > *Visual C#* section.  In the central list, select the *Console App (.NET Framework)* template...
![New Project]({{ site.baseurl }}/images/compute-start.png)
1. For the purposes of this Guide, we will name our demo plugin *TestCompute*.  At the bottom of the window, fill in the *Name* field.  *Browse* and select a location for this plugin on your disk...
1. Check *Create directory for solution*.  *Note*: This is optional depending on how you want to structure your projects.
1. Click the *OK* button.  *Note*: You don't have to add the project to source control for this demo.
1. For the purposes of this guide, we will *accept the defaults* and click *Finish*...
1. A *new solution* called *HelloRhinoCommon* should open...

#### Steps to install the NuGet packages

1. *Right-click* your project file in *Solution Explorer* and select *Manage NuGet Packages ...*.
1. On the left side of the dialog expand the *Online* option and select *nuget.org*.
1. In the top right search box type "Rhino3dmIO" and click on a *Rhino3dmIO.Desktop* option (there are 3: Rhino3dmIO.Desktop (Windows/macOS), Rhino3dmIO.iOS and Rhino3dmIO.Android) and click on the *Install* button.
1. Continue by typing in the search box type "Newtonsoft.JSON" and click on a *NewtonSoft.JSON* option and click on the *Install* button.
1. Close the *Manage NuGet Packages* dialog.  The Nuget packages are installed and ready to use.

Changes that were made:

- The *Rhino3dmIO.Desktop and NewtonSoft.JSON NuGet packages* are installed in your project.
- The project references the *Rhino3dmIO.Desktop* and *Newtonsoft.JSON* assembly.


#### Include RhinoCompute.cs in the project

RhinoCompute.cs is a the package which adds the methods to call into the compute server.  It is organized similar to RhinoCommon calls.

1. Download the [RhinoCompute.cs source file](https://compute.rhino3d.com/sdk/csharp) from compute.rhino3d.com into the project folder.
2. Using the *Project* pulldown > *Add Existing Item...*
3. Select the [RhinoCompute.cs source file](https://compute.rhino3d.com/sdk/csharp) to add it to the project.

Changes that were made:

- The [RhinoCompute.cs source file](https://compute.rhino3d.com/sdk/csharp) are installed in your project.
- The [RhinoCompute.cs source file](https://compute.rhino3d.com/sdk/csharp) helper functions are available to the project.

## The first use of Compute

As a place to start, a simple console app shows the standard workflow using Compute. This is the simplest example of using Rhino3DMio locally to read, write and create Rhino geometry.  Then use compute to handle a function that does not exist in Rhino3DMio.

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
            ComputeServer.ApiToken = "scottd@mcneel.com";

            // Uses standard Rhino3dmIO methods locally to create a sphere.
            var sphere = new Rhino.Geometry.Sphere(Rhino.Geometry.Point3d.Origin, 12);
            var sphereAsBrep = sphere.ToBrep();

            // the following function calls compute.rhino3d.com to get access to something not
            // available in Rhino3dmIO. In this case send a Brep to Compute and get a Mesh back.
            var meshes = MeshCompute.CreateFromBrep(sphereAsBrep);

            // Use regular Rhino3dmIO local calls to count the vertices in the mesh.
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
{: .line-numbers}

This example above first creates a sphere using Rhino3DMio locally. Then request Compute to mesh that BREP to Compute, the BREP sphere is meshed. Compute then returns the mesh.  Finally using the local Rhino3DMio package to walk through the mesh, the vertices are counted.

<table>
<tr>
<th>Line</th>
<th>Description</th>
</tr>
<tr>
<td>5</td>
<td>Include the Rhino.Compute Assembly from the RhinoCompute.cs Package.</td>
</tr>
<tr>
<td>13</td>
<td>All calls to the Compute Server must be accompanied by a token. At this time your email is correct token to use.  This is sent with each RhinoCompute.cs Posts.</td>
</tr>
<tr>
<td>21</td>
<td>Here the OpenNurbs Brep sphere is sent to Compute to convert to a mesh.  The Mesh is returned as a OpenNurbs Mesh.</td>
</tr>
</table>
{: .multiline}


## Seeing the results of Compute

Many times the intersection of objects may need to be calculated. Intersections are not in OpenNurbs, but are part of Compute. Here is a tutorial on creating two circles, finding their intersection, then converting the circles to an SVG image to display.

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
            Rhino.Compute.ComputeServer.ApiToken = "circleintersectionsample@mcneel.com";

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
        /// Very basic SVG file creation routine to make an SVG the displays two circles and a mesh.
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

---

## Next Steps

*Congratulations!*  You have the tools to use [Rhino Compute server](https://www.rhino3d.com/compute).  *Now what?*

1. See a list of the [2400+ API calls](https://compute.rhino3d.com/sdk) available for compute.rhino3d.com.
1. Download the [Compute Samples repo from GitHub](https://github.com/mcneel/compute.rhino3d.samples).

---

## Footnotes

[^1]: Visual Studio Code is Microsoft's cross-platform source code editor for Windows, Linux, and macOS.  At the time of this writing, Visual Studio code does not yet support the features required to author RhinoCommon plugins.

[^2]: Visual Studio Online is Microsoft's online counterpart to the desktop edition of Visual Studio (referred to as Visual Studio "proper" above).  We have not tested using Visual Studio Online to debug RhinoCommon plugins as having a copy of Rhino running would prove logistically difficult.

[^3]: Visual Studio "proper" is the desktop version of Visual Studio...we are only attaching the "proper" epithet to distinguish it from the Visual Studio Code and Visual Studio Online.  In subsequent guides this will be referred to as simply "Visual Studio."

[^4]: Visual Studio Express for Windows *Desktop* (also named "Express for Desktop" on some pages) offers a development platform that has a less strict licensing agreement policy than the Community edition. Please refer to the EULA for complete details, available during installation. In this edition, debugging of Rhino can be started, but the location of the Rhino executable (rhino.exe), usually available in the Project property page, in the Debug tab, cannot be changed in the UI. After Wizard completion, the location of the Rhino executable can only be edited in the XML of the resulting *.csproj* file, in the main folder of the solution.
