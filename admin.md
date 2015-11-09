---
layout: fullwidth-page
title: Administration
permalink: /admin/
order: 1
---

# Administration

This site is the _future home_ of developer.rhino3d.com.

The goal of this site is to consolidate all the (now) scattered developer documentation into a single canonical site that is clear, easy-to-navigate, with consistent formatting and nomenclature.

The sources of content-to-be-consolidated are:

- [Rhino Developer Tools wiki](http://wiki.mcneel.com/developer/home)
- [C/C++ Knowledge Base](https://wiki.mcneel.com/developer/sdksamples/knowledgebasecpp) - a mix of samples, how-tos, and guides
- [RhinoCommon API references](http://4.rhino3d.com/5/rhinocommon/)
- [C++ SDK API references](http://4.rhino3d.com/5/rhinocppsdk/idx.html)
- [RhinoCommon samples on GitHub](https://github.com/mcneel/rhinocommon/tree/master/examples)
- [DaleF's CsCommands](https://github.com/dalefugier/SampleCsCommands/)
- [Doxygen Docs (on McNeel intranet)](http://phab.mcneel.com/docs/rhino/6/rhinocommon/)
- Dale Lear's Developer Meeting Notes
- RhinoScript and Rhino.Python Primers
- [Grasshopper SDK Help file (chm)](http://s3.amazonaws.com/files.na.mcneel.com/grasshopper/1.0/docs/en/GrasshopperSDK.chm).

---

## Dev Docs Guides

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  <li><a class="page-link" href="https://github.com/mcneel/developer-rhino3d-com/blob/gh-pages/README.md">Getting Started with Dev Docs</a></li>
  {% for topic in guides %}
    {% if topic.apis contains 'Developer Docs' %}
      {% if topic.title and topic.order %}
        <li><a class="page-link" href="{{ topic.url | prepend: site.baseurl }}">{{ topic.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

---

## TODO List

### Guides

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"title" %}
  <ol>
  {% for topic in guides %}
    {% if topic.TODO == 1 %}
      <li>
        <a class="page-link" href="{{ topic.url | prepend: site.baseurl }}">{{ topic.title }}</a>{% if topic.origin != 'unset' %} needs porting from: <a href="{{ topic.origin }}">{{ topic.origin }}</a>{% endif %}
      </li>
    {% endif %}
  {% endfor %}
  </ol>
</div>

### Samples

- Here we could report samples that are not passing tests (TODO TODO ...very meta).

**RhinoScript**

The following RhinoScript knowledge base articles from the wiki are really just samples and do not have enough explanatory content to be considered guides, so they should be evaluated as samples instead:

- [http://wiki.mcneel.com/developer/scriptsamples/addcurveendpoints](http://wiki.mcneel.com/developer/scriptsamples/addcurveendpoints)
- [http://wiki.mcneel.com/developer/scriptsamples/arcpointdistribution](http://wiki.mcneel.com/developer/scriptsamples/arcpointdistribution)
- [http://wiki.mcneel.com/developer/scriptsamples/batchsavesmall](http://wiki.mcneel.com/developer/scriptsamples/batchsavesmall)
- [http://wiki.mcneel.com/developer/scriptsamples/batchrender](http://wiki.mcneel.com/developer/scriptsamples/batchrender)
- [http://wiki.mcneel.com/developer/sdksamples/testnurbscurve](http://wiki.mcneel.com/developer/sdksamples/testnurbscurve)
- [http://wiki.mcneel.com/developer/scriptsamples/excelcurveproperties](http://wiki.mcneel.com/developer/scriptsamples/excelcurveproperties)
- [http://wiki.mcneel.com/developer/scriptsamples/batchconvertautocad](http://wiki.mcneel.com/developer/scriptsamples/batchconvertautocad)
- [http://wiki.mcneel.com/developer/scriptsamples/meshvolumecentroid](http://wiki.mcneel.com/developer/scriptsamples/meshvolumecentroid)
- [http://wiki.mcneel.com/developer/scriptsamples/circlepacking](http://wiki.mcneel.com/developer/scriptsamples/circlepacking)
- [http://wiki.mcneel.com/developer/scriptsamples/convertblocktogroup](http://wiki.mcneel.com/developer/scriptsamples/convertblocktogroup)
- [http://wiki.mcneel.com/developer/scriptsamples/countblocks](http://wiki.mcneel.com/developer/scriptsamples/countblocks)
- [http://wiki.mcneel.com/developer/scriptsamples/countobjects](http://wiki.mcneel.com/developer/scriptsamples/countobjects)
- [http://wiki.mcneel.com/developer/scriptsamples/countobjects](http://wiki.mcneel.com/developer/scriptsamples/countobjects)
- [http://wiki.mcneel.com/developer/scriptsamples/parametricellipsoid](http://wiki.mcneel.com/developer/scriptsamples/parametricellipsoid)
- [http://wiki.mcneel.com/developer/scriptsamples/icosahedron](http://wiki.mcneel.com/developer/scriptsamples/icosahedron)
- [http://wiki.mcneel.com/developer/scriptsamples/boxframe](http://wiki.mcneel.com/developer/scriptsamples/boxframe)
- [http://wiki.mcneel.com/developer/scriptsamples/exportblockcount](http://wiki.mcneel.com/developer/scriptsamples/exportblockcount)
- [http://wiki.mcneel.com/developer/scriptsamples/fibonaccispiral](http://wiki.mcneel.com/developer/scriptsamples/fibonaccispiral)
- [http://wiki.mcneel.com/developer/scriptsamples/squarepipe](http://wiki.mcneel.com/developer/scriptsamples/squarepipe)
- [http://wiki.mcneel.com/developer/scriptsamples/arraypolar](http://wiki.mcneel.com/developer/scriptsamples/arraypolar)
- [http://wiki.mcneel.com/developer/scriptsamples/isupperbound](http://wiki.mcneel.com/developer/scriptsamples/isupperbound)
- [http://wiki.mcneel.com/developer/scriptsamples/selectedgroups](http://wiki.mcneel.com/developer/scriptsamples/selectedgroups)
- [http://wiki.mcneel.com/developer/dividecurvedashed](http://wiki.mcneel.com/developer/dividecurvedashed)
- [http://wiki.mcneel.com/developer/scriptsamples/divideequidistance](http://wiki.mcneel.com/developer/scriptsamples/divideequidistance)
- [http://wiki.mcneel.com/developer/scriptsamples/steelshapes](http://wiki.mcneel.com/developer/scriptsamples/steelshapes)
- [http://wiki.mcneel.com/developer/scriptsamples/torsion](http://wiki.mcneel.com/developer/scriptsamples/torsion)
- [http://wiki.mcneel.com/developer/scriptsamples/superexplodeblock](http://wiki.mcneel.com/developer/scriptsamples/superexplodeblock)
- [http://wiki.mcneel.com/developer/scriptsamples/explodemesh](http://wiki.mcneel.com/developer/scriptsamples/explodemesh)
- [http://wiki.mcneel.com/developer/scriptsamples/exportcontrolpoints](http://wiki.mcneel.com/developer/scriptsamples/exportcontrolpoints)
- [http://wiki.mcneel.com/developer/scriptsamples/exportlayerobjects](http://wiki.mcneel.com/developer/scriptsamples/exportlayerobjects)
- [http://wiki.mcneel.com/developer/scriptsamples/geomview](http://wiki.mcneel.com/developer/scriptsamples/geomview)
- [http://wiki.mcneel.com/developer/scriptsamples/exportpointstoexcel](http://wiki.mcneel.com/developer/scriptsamples/exportpointstoexcel)
- [http://wiki.mcneel.com/developer/scriptsamples/extractinterpcrvpoints](http://wiki.mcneel.com/developer/scriptsamples/extractinterpcrvpoints)
- [http://wiki.mcneel.com/developer/scriptsamples/extractuvintersectpts](http://wiki.mcneel.com/developer/scriptsamples/extractuvintersectpts)
- [http://wiki.mcneel.com/developer/scriptsamples/batchextractthumbnails](http://wiki.mcneel.com/developer/scriptsamples/batchextractthumbnails)
- [http://wiki.mcneel.com/developer/scriptsamples/findclosestcurve](http://wiki.mcneel.com/developer/scriptsamples/findclosestcurve)
- [http://wiki.mcneel.com/developer/scriptsamples/platonics](http://wiki.mcneel.com/developer/scriptsamples/platonics)
- [http://wiki.mcneel.com/developer/scriptsamples/convertdotstotext](http://wiki.mcneel.com/developer/scriptsamples/convertdotstotext)
- [http://wiki.mcneel.com/developer/scriptsamples/isolatelayers](http://wiki.mcneel.com/developer/scriptsamples/isolatelayers)
- [http://wiki.mcneel.com/developer/scriptsamples/movecurvegrip](http://wiki.mcneel.com/developer/scriptsamples/movecurvegrip)
- [http://wiki.mcneel.com/developer/scriptsamples/macaddress](http://wiki.mcneel.com/developer/scriptsamples/macaddress)
- [http://wiki.mcneel.com/developer/scriptsamples/color](http://wiki.mcneel.com/developer/scriptsamples/color)
- [http://wiki.mcneel.com/developer/scriptsamples/seltext](http://wiki.mcneel.com/developer/scriptsamples/seltext)
- [http://wiki.mcneel.com/developer/scriptsamples/airfoil](http://wiki.mcneel.com/developer/scriptsamples/airfoil)
- [http://wiki.mcneel.com/developer/scriptsamples/importinterpcrv](http://wiki.mcneel.com/developer/scriptsamples/importinterpcrv)
- [http://wiki.mcneel.com/developer/scriptsamples/importtext](http://wiki.mcneel.com/developer/scriptsamples/importtext)
- [http://wiki.mcneel.com/developer/scriptsamples/jointhedots](http://wiki.mcneel.com/developer/scriptsamples/jointhedots)
- [http://wiki.mcneel.com/developer/scriptsamples/knotmultiplicity](http://wiki.mcneel.com/developer/scriptsamples/knotmultiplicity)
- [http://wiki.mcneel.com/developer/scriptsamples/liquiddropsimulation](http://wiki.mcneel.com/developer/scriptsamples/liquiddropsimulation)
- [http://wiki.mcneel.com/developer/scriptsamples/acadschemes](http://wiki.mcneel.com/developer/scriptsamples/acadschemes)
- [http://wiki.mcneel.com/developer/scriptsamples/igeschemes](http://wiki.mcneel.com/developer/scriptsamples/igeschemes)
- [http://wiki.mcneel.com/developer/scriptsamples/listknotvector](http://wiki.mcneel.com/developer/scriptsamples/listknotvector)
- [http://wiki.mcneel.com/developer/scriptsamples/createcenterpoint](http://wiki.mcneel.com/developer/scriptsamples/createcenterpoint)
- [http://wiki.mcneel.com/developer/scriptsamples/markline](http://wiki.mcneel.com/developer/scriptsamples/markline)
- [http://wiki.mcneel.com/developer/scriptsamples/matchobjectattributesex](http://wiki.mcneel.com/developer/scriptsamples/matchobjectattributesex)
- [http://wiki.mcneel.com/developer/scriptsamples/matchtext](http://wiki.mcneel.com/developer/scriptsamples/matchtext)
- [http://wiki.mcneel.com/developer/scriptsamples/morph](http://wiki.mcneel.com/developer/scriptsamples/morph)
- [http://wiki.mcneel.com/developer/scriptsamples/movesurfacegrip](http://wiki.mcneel.com/developer/scriptsamples/movesurfacegrip)
- [http://wiki.mcneel.com/developer/scriptsamples/pipeall](http://wiki.mcneel.com/developer/scriptsamples/pipeall)
- [http://wiki.mcneel.com/developer/scriptsamples/offsetcurve](http://wiki.mcneel.com/developer/scriptsamples/offsetcurve)
- [http://wiki.mcneel.com/developer/scriptsamples/positiononsrf](http://wiki.mcneel.com/developer/scriptsamples/positiononsrf)
- [http://wiki.mcneel.com/developer/scriptsamples/printsurfacepoints](http://wiki.mcneel.com/developer/scriptsamples/printsurfacepoints)
- [http://wiki.mcneel.com/developer/scriptsamples/rendernamedviews](http://wiki.mcneel.com/developer/scriptsamples/rendernamedviews)
- [http://wiki.mcneel.com/developer/scriptsamples/revolve](http://wiki.mcneel.com/developer/scriptsamples/revolve)
- [http://wiki.mcneel.com/developer/scriptsamples/rotateplaneparallel](http://wiki.mcneel.com/developer/scriptsamples/rotateplaneparallel)
- [http://wiki.mcneel.com/developer/scriptsamples/rotateone](http://wiki.mcneel.com/developer/scriptsamples/rotateone)
- [http://wiki.mcneel.com/developer/scriptsamples/savelayerstates](http://wiki.mcneel.com/developer/scriptsamples/savelayerstates)
- [http://wiki.mcneel.com/developer/scriptsamples/savefile](http://wiki.mcneel.com/developer/scriptsamples/savefile)
- [http://wiki.mcneel.com/developer/scriptsamples/savepluginlist](http://wiki.mcneel.com/developer/scriptsamples/savepluginlist)
- [http://wiki.mcneel.com/developer/scriptsamples/savevideoinfo](http://wiki.mcneel.com/developer/scriptsamples/savevideoinfo)
- [http://wiki.mcneel.com/developer/scriptsamples/dimscaletext](http://wiki.mcneel.com/developer/scriptsamples/dimscaletext)
- [http://wiki.mcneel.com/developer/scriptsamples/cutplane](http://wiki.mcneel.com/developer/scriptsamples/cutplane)
- [http://wiki.mcneel.com/developer/scriptsamples/flowalongsrf](http://wiki.mcneel.com/developer/scriptsamples/flowalongsrf)
- [http://wiki.mcneel.com/developer/scriptsamples/splitbrep](http://wiki.mcneel.com/developer/scriptsamples/splitbrep)
- [http://wiki.mcneel.com/developer/scriptsamples/selcrvdegree](http://wiki.mcneel.com/developer/scriptsamples/selcrvdegree)
- [http://wiki.mcneel.com/developer/scriptsamples/selnamedobject](http://wiki.mcneel.com/developer/scriptsamples/selnamedobject)
- [http://wiki.mcneel.com/developer/scriptsamples/selz](http://wiki.mcneel.com/developer/scriptsamples/selz)
- [http://wiki.mcneel.com/developer/scriptsamples/seltextheight](http://wiki.mcneel.com/developer/scriptsamples/seltextheight)
- [http://wiki.mcneel.com/developer/scriptsamples/seldimstyle](http://wiki.mcneel.com/developer/scriptsamples/seldimstyle)
- [http://wiki.mcneel.com/developer/scriptsamples/multilistbox](http://wiki.mcneel.com/developer/scriptsamples/multilistbox)
- [http://wiki.mcneel.com/developer/scriptsamples/sellinetype](http://wiki.mcneel.com/developer/scriptsamples/sellinetype)
- [http://wiki.mcneel.com/developer/scriptsamples/selplanarmesh](http://wiki.mcneel.com/developer/scriptsamples/selplanarmesh)
- [http://wiki.mcneel.com/developer/scriptsamples/setrendercolor](http://wiki.mcneel.com/developer/scriptsamples/setrendercolor)
- [http://wiki.mcneel.com/developer/scriptsamples/cameraangle](http://wiki.mcneel.com/developer/scriptsamples/cameraangle)
- [http://wiki.mcneel.com/developer/scriptsamples/hierarchiallayers](http://wiki.mcneel.com/developer/scriptsamples/hierarchiallayers)
- [http://wiki.mcneel.com/developer/scriptsamples/setcrvlength](http://wiki.mcneel.com/developer/scriptsamples/setcrvlength)
- [http://wiki.mcneel.com/developer/scriptsamples/splitpath](http://wiki.mcneel.com/developer/scriptsamples/splitpath)
- [http://wiki.mcneel.com/developer/scriptsamples/curvesplitter](http://wiki.mcneel.com/developer/scriptsamples/curvesplitter)
- [http://wiki.mcneel.com/developer/scriptsamples/straightencircles](http://wiki.mcneel.com/developer/scriptsamples/straightencircles)
- [http://wiki.mcneel.com/developer/scriptsamples/circletrimmer](http://wiki.mcneel.com/developer/scriptsamples/circletrimmer)
- [http://wiki.mcneel.com/developer/scriptsamples/unrollsrf](http://wiki.mcneel.com/developer/scriptsamples/unrollsrf)
- [http://wiki.mcneel.com/flamingo/flamingosdk/setmaterial](http://wiki.mcneel.com/flamingo/flamingosdk/setmaterial)
- [http://wiki.mcneel.com/flamingo/flamingosdk/flamingo2plantwireframe](http://wiki.mcneel.com/flamingo/flamingosdk/flamingo2plantwireframe)
- [http://wiki.mcneel.com/flamingo/flamingosdk/getflamingo2plant](http://wiki.mcneel.com/flamingo/flamingosdk/getflamingo2plant)
- [http://wiki.mcneel.com/flamingo/flamingosdk/getmaterial](http://wiki.mcneel.com/flamingo/flamingosdk/getmaterial)
- [http://wiki.mcneel.com/flamingo/flamingosdk/getmateriallist](http://wiki.mcneel.com/flamingo/flamingosdk/getmateriallist)
- [http://wiki.mcneel.com/flamingo/flamingosdk/getplantpointcloud](http://wiki.mcneel.com/flamingo/flamingosdk/getplantpointcloud)
- [http://wiki.mcneel.com/flamingo/flamingosdk/importmaterial](http://wiki.mcneel.com/flamingo/flamingosdk/importmaterial)
- [http://wiki.mcneel.com/flamingo/flamingosdk/mappinginformation](http://wiki.mcneel.com/flamingo/flamingosdk/mappinginformation)
- [http://wiki.mcneel.com/flamingo/flamingosdk/modifyplant](http://wiki.mcneel.com/flamingo/flamingosdk/modifyplant)
- [http://wiki.mcneel.com/flamingo/flamingosdk/plantfromobject](http://wiki.mcneel.com/flamingo/flamingosdk/plantfromobject)
- [http://wiki.mcneel.com/flamingo/flamingosdk/setmapping](http://wiki.mcneel.com/flamingo/flamingosdk/setmapping)
- [http://wiki.mcneel.com/flamingo/flamingosdk/setmaterial](http://wiki.mcneel.com/flamingo/flamingosdk/setmaterial)
- [http://wiki.mcneel.com/flamingo/flamingosdk/tagobjectasplant](http://wiki.mcneel.com/flamingo/flamingosdk/tagobjectasplant)
- [http://wiki.mcneel.com/flamingo/flamingosdk/untagobjectasplant](http://wiki.mcneel.com/flamingo/flamingosdk/untagobjectasplant)


### Misc

- [http://www.rhino3d.com/developer](http://www.rhino3d.com/developer) should redirect to [http://developer.rhino3d.com](http://developer.rhino3d.com) (this website) - the link is in all the .h files top comments

- Macros documentation sources: [Macros in Helpfile](http://docs.mcneel.com/rhino/5/help/en-us/information/rhinoscripting.htm), [Macros in Wiki](http://wiki.mcneel.com/rhino/basicmacros), [Using the MacroEditor](http://wiki.mcneel.com/developer/macroscriptsetup)

- **DO NOT** port any content that relates to pre-Rhino 5: this is old information.  Visual Studio 2010 for the C/C++ SDK was used for Rhino 5.

- Mitch's MicMac tools: http://wiki.mcneel.com/people/mitchheynick
