---
layout: toc-page
title: Guides
permalink: /guides/
order: 2
---

# Guides

---

## General

*Guides that apply across platforms and SDKs*

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for topic in guides %}
    {% if topic.platforms contains 'Cross-Platform' and topic.apis contains 'General' %}
      {% if topic.title and topic.order %}
        <li><a class="page-link" href="{{ topic.url | prepend: site.baseurl }}">{{ topic.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

---

## RhinoCommon <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon"> <img src="{{ site.baseurl }}/images/mac_logo_small.png" alt="OS X" class="guide_icon">
{: #rhinocommon }

*The cross-platform .NET plugin SDK for Rhino.*

### Overview

- [What is RhinoCommon?]({{ site.baseurl }}/guides/rhinocommon/what_is_rhinocommon/)
- [What are Mono & Xamarin?]({{ site.baseurl }}/guides/rhinocommon/what_are_mono_and_xamarin/)


### Getting Started

- Installing Tools ([Windows]({{ site.baseurl }}/guides/rhinocommon/installing_tools_windows/), [Mac]({{ site.baseurl }}/guides/rhinocommon/installing_tools_mac/))
- Your First Plugin ([Windows]({{ site.baseurl }}/guides/rhinocommon/your_first_plugin_windows/), [Mac]({{ site.baseurl }}/guides/rhinocommon/your_first_plugin_mac/), [Cross-Platform]({{ site.baseurl }}/guides/rhinocommon/your_first_plugin_crossplatform/))
- Plugin Installers ([Windows]({{ site.baseurl }}/guides/rhinocommon/plugin_installers_windows/), [Mac]({{ site.baseurl }}/guides/rhinocommon/plugin_installers_mac/))


### Fundamentals

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for topic in guides %}
    {% if topic.apis contains 'RhinoCommon' and topic.categories contains 'Fundamentals' %}
      {% if topic.title and topic.order %}
        <li><a class="page-link" href="{{ topic.url | prepend: site.baseurl }}">{{ topic.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Advanced

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for topic in guides %}
    {% if topic.apis contains 'RhinoCommon' and topic.categories contains 'Advanced' %}
      {% if topic.title and topic.order %}
        <li><a class="page-link" href="{{ topic.url | prepend: site.baseurl }}">{{ topic.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

---

## Rhino.Python <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon"> <img src="{{ site.baseurl }}/images/mac_logo_small.png" alt="OS X" class="guide_icon">
{: #rhinopython }

*Quickly add functionality to Rhino or automate repetitive tasks.*

### Overview


### Getting Started

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for topic in guides %}
    {% if topic.apis contains 'RhinoPython' and topic.categories contains 'GettingStarted' %}
      {% if topic.title and topic.order %}
        <li><a class="page-link" href="{{ topic.url | prepend: site.baseurl }}">{{ topic.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Learning Resources

#### Python Applied to Rhino
- <a href="http://www.rhino3d.com/download/IronPython/5.0/RhinoPython101" target="_blank">RhinoPython101 Primer</a>
- <a href="http://discourse.mcneel.com/c/scripting" target="_blank">Rhino Scripting Forum</a>
- <a href="http://wiki.mcneel.com/developer/python%22" target="_blank">McNeel Python Scripting Wiki</a>

##### Learning Python
- <a href="https://docs.python.org/2/tutorial/index.html" target="_blank">The Python Tutorial</a>
- <a href="http://learnpythonthehardway.org/book/" target="_blank">Learn Python the Hard Way</a> (despite the title this is a beginner's book)
- <a href="https://automatetheboringstuff.com/" target="_blank">Automate The Boring Stuff With Python</a>

---

## openNURBS <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon"> <img src="{{ site.baseurl }}/images/mac_logo_small.png" alt="OS X" class="guide_icon">
{: #opennurbs }

*Read/Write Rhino 3dm files in your application.*

### Overview

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for topic in guides %}
    {% if topic.apis contains 'openNURBS' and topic.categories contains 'Overview' %}
      {% if topic.title and topic.order %}
        <li><a class="page-link" href="{{ topic.url | prepend: site.baseurl }}">{{ topic.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Getting Started

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for topic in guides %}
    {% if topic.apis contains 'openNURBS' and topic.categories contains 'GettingStarted' %}
      {% if topic.title and topic.order %}
        <li><a class="page-link" href="{{ topic.url | prepend: site.baseurl }}">{{ topic.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Fundamentals

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for topic in guides %}
    {% if topic.apis contains 'openNURBS' and topic.categories contains 'Fundamentals' %}
      {% if topic.title and topic.order %}
        <li><a class="page-link" href="{{ topic.url | prepend: site.baseurl }}">{{ topic.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Advanced

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for topic in guides %}
    {% if topic.apis contains 'openNURBS' and topic.categories contains 'Advanced' %}
      {% if topic.title and topic.order %}
        <li><a class="page-link" href="{{ topic.url | prepend: site.baseurl }}">{{ topic.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

---

## C/C++ <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon">
{: #cc }

*Native SDK for Rhino for Windows plugins.*

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for topic in guides %}
    {% if topic.apis contains 'C/C++' %}
      {% if topic.title and topic.order %}
        <li><a class="page-link" href="{{ topic.url | prepend: site.baseurl }}">{{ topic.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>


---

## Grasshopper <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon">
{: #grasshopper }

*Create custom Grasshopper components and plugins.*

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for topic in guides %}
    {% if topic.apis contains 'Grasshopper' %}
      {% if topic.title and topic.order %}
        <li><a class="page-link" href="{{ topic.url | prepend: site.baseurl }}">{{ topic.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>


---

## RhinoScript <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon">
{: #rhinoscript }

*Customize Rhino for Windows or automate repetitive tasks.*

### Overview

RhinoScript is a scripting tool based on Microsoft's VBScript language. With RhinoScript, you can quickly add functionality to Rhino, or automate repetitive tasks.

### Learning Resources

- [Microsoft VBScript User's Guide and Language Reference](http://msdn.microsoft.com/en-us/library/t0aew7h6(VS.85).aspx)
- [RhinoScript 101 Primer](http://www.rhino3d.com/download/rhino/5.0/rhinoscript101)
- [RhinoScript Help File On-Line](http://www.rhino3d.com/5/rhinoscript/index.html)
- [RhinoScript Dash Docset](http://discourse.mcneel.com/t/rhinoscript-dash-docset/6382)
- [RhinoScript Samples on GitHub](https://github.com/mcneel/rhinoscript)
- [RhinoScript Resources](http://www.microsoft.com/technet/scriptcenter/default.mspx)
- [Microsoft TechNet Script Center](http://www.microsoft.com/technet/scriptcenter/default.mspx)
- [Pascal Golay's scripted utilities for Rhino](http://wiki.mcneel.com/people/pascalgolay)

### VBScript Basics

<!-- TODO - This section could be auto Generated -->

- [VBScript Procedures]({{ site.baseurl }}/guides/rhinoscript/vbscript_procedures/)
- [VBScript Statements]({{ site.baseurl }}/guides/rhinoscript/vbscript_statements/)
- [VBScript String Literals]({{ site.baseurl }}/guides/rhinoscript/vbscript_string_literals/)
- [VBScript Variables]({{ site.baseurl }}/guides/rhinoscript/vbscript_variables/)

### All (uncategorized)

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"title" %}
  <ul>
  {% for topic in guides %}
    {% if topic.apis contains 'RhinoScript' %}
      {% if topic.title and topic.order %}
        <li><a class="page-link" href="{{ topic.url | prepend: site.baseurl }}">{{ topic.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

---

## RDK <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon">
{: #rdk }

*Renderer plugin development in Rhino for Windows.*

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for topic in guides %}
    {% if topic.apis contains 'RDK' %}
      {% if topic.title and topic.order %}
        <li><a class="page-link" href="{{ topic.url | prepend: site.baseurl }}">{{ topic.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>


---

## RhinoMobile <img src="{{ site.baseurl }}/images/android_logo_small.png" alt="Android" class="guide_icon"> <img src="{{ site.baseurl }}/images/ios_logo_small.png" alt="iOS" class="guide_icon">
{: #rhinomobile }

*3D mobile application development.*

- [What is RhinoMobile?]({{ site.baseurl }}/guides/rhinomobile/what_is_rhinomobile/)
- Installing Tools ([Windows]({{ site.baseurl }}/guides/rhinomobile/installing_tools_windows/), [Mac]({{ site.baseurl }}/guides/rhinomobile/installing_tools_mac/))
- Your First App ([Windows]({{ site.baseurl }}/guides/rhinomobile/your_first_app_windows/), [Mac]({{ site.baseurl }}/guides/rhinomobile/your_first_app_mac/))
- [Using Simulators]({{ site.baseurl }}/guides/rhinomobile/using_simulators/)
- [Testing On Devices]({{ site.baseurl }}/guides/rhinomobile/testing_on_devices/)

---

## Zoo <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon">
{: #zoo }

*Zoo license manager plugins in Rhino for Windows.*

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for topic in guides %}
    {% if topic.apis contains 'Zoo' %}
      {% if topic.title and topic.order %}
        <li><a class="page-link" href="{{ topic.url | prepend: site.baseurl }}">{{ topic.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>


---

## Developer Docs <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon"> <img src="{{ site.baseurl }}/images/mac_logo_small.png" alt="OS X" class="guide_icon">
{: #developer_docs }

*Guides to this very website.*

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
