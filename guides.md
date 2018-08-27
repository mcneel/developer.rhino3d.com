---
layout: toc-page
title: Guides
description: All the guides available for developing for Rhino or Grasshopper.
permalink: /guides/
order: 2
---

# Guides

---

## [General]({{ site.baseurl }}/guides/general)
{: #general }

*Guides that apply across platforms and SDKs*

### Overview

- [Developing Software In Public]({{ site.baseurl }}/guides/general/developing-software-in-public)
- [Rhino Technology Overview]({{ site.baseurl }}/guides/general/rhino-technology-overview)
- [Frequently Asked Questions (FAQ)]({{ site.baseurl }}/guides/general/frequently-asked-questions)

### Getting Started

- [Developer Prerequisites]({{ site.baseurl }}/guides/general/rhino-developer-prerequisites)
- [Developer Training]({{ site.baseurl }}/guides/general/developer-training)
- [Contributing]({{ site.baseurl }}/guides/general/contributing)

### Fundamentals

- [What is a Rhino Plugin?]({{ site.baseurl }}/guides/general/what-is-a-rhino-plugin)
- [Rhino Installer Engine]({{ site.baseurl }}/guides/general/rhino-installer-engine)
- [Simple Command Macros]({{ site.baseurl }}/guides/general/creating-command-macros/)

### [Essential Mathematics]({{ site.baseurl }}/guides/general/essential-mathematics)

- [Introduction]({{ site.baseurl }}/guides/general/essential-mathematics)  
- [Vector Mathematics]({{ site.baseurl }}/guides/general/essential-mathematics/vector-mathematics)  
- [Matrices and Transformations]({{ site.baseurl }}/guides/general/essential-mathematics/matrices-transformations)  
- [Parametric Curves and Surfaces]({{ site.baseurl }}/guides/general/essential-mathematics/parametric-curves-surfaces)  
- <a href="http://www.rhino3d.com/download/rhino/5.0/essentialmathematicsthirdedition/"><span class="glyphicon glyphicon-download"></span></a> [Download Essential Mathematics for Computational Design as a single PDF ](http://www.rhino3d.com/download/rhino/5.0/essentialmathematicsthirdedition/)

### This Site

- [How This Site Works]({{ site.baseurl }}/guides/general/how-this-site-works)
- [Getting Started with Developer Docs](https://github.com/mcneel/developer-rhino3d-com/blob/{{ site.git_branch | default: "master" }}/README.md)
- [Developer Docs Style Guide]({{ site.baseurl }}/guides/general/developer-docs-style-guide)

---

## [RhinoCommon]({{ site.baseurl }}/guides/rhinocommon) <img src="{{ site.baseurl }}/images/win-logo-small.png" alt="Windows" class="guide_icon"> <img src="{{ site.baseurl }}/images/mac-logo-small.png" alt="macOS" class="guide_icon">
{: #rhinocommon }

*The cross-platform .NET plugin SDK for Rhino.*

### Overview

- [What is RhinoCommon?]({{ site.baseurl }}/guides/rhinocommon/what-is-rhinocommon/)
- [What are Mono & Xamarin?]({{ site.baseurl }}/guides/rhinocommon/what-are-mono-and-xamarin/)
- [What's New/Changes?]({{ site.baseurl }}/guides/rhinocommon/whats-new/)

### Getting Started

- Installing Tools ([Windows]({{ site.baseurl }}/guides/rhinocommon/installing-tools-windows/), [Mac]({{ site.baseurl }}/guides/rhinocommon/installing-tools-mac/))
- Your First Plugin ([Windows]({{ site.baseurl }}/guides/rhinocommon/your-first-plugin-windows/), [Mac]({{ site.baseurl }}/guides/rhinocommon/your-first-plugin-mac/), [Cross-Platform]({{ site.baseurl }}/guides/rhinocommon/your-first-plugin-crossplatform/))
- Plugin Installers ([Windows]({{ site.baseurl }}/guides/rhinocommon/plugin-installers-windows/), [Mac]({{ site.baseurl }}/guides/rhinocommon/plugin-installers-mac/))

### Fundamentals

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.sdk contains 'RhinoCommon' and guide.categories contains 'Fundamentals' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Rendering

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.sdk contains 'RhinoCommon' and guide.categories contains 'Rendering' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Advanced

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  <li><a href="{{ site.baseurl }}/api/RhinoCommon">API Reference</a></li>
  <li><a href="https://github.com/picoe/Eto/wiki">Eto.Forms guides</a></li>
  {% for guide in guides %}
    {% if guide.sdk contains 'RhinoCommon' and guide.categories contains 'Advanced' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Zoo

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.sdk contains 'RhinoCommon' and guide.categories contains 'Zoo' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

---

## [Rhino.Python]({{ site.baseurl }}/guides/rhinopython) <img src="{{ site.baseurl }}/images/win-logo-small.png" alt="Windows" class="guide_icon"> <img src="{{ site.baseurl }}/images/mac-logo-small.png" alt="macOS" class="guide_icon">
{: #rhinopython }

*Quickly add functionality to Rhino or automate repetitive tasks.*

### Overview

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.sdk contains 'RhinoPython' and guide.categories contains 'Overview' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Getting Started

- Your First Python Script in Rhino ([Windows]({{ site.baseurl }}/guides/rhinopython/your-first-python-script-in-rhino-windows), [Mac]({{ site.baseurl }}/guides/rhinopython/your-first-python-script-in-rhino-mac), [Grasshopper]({{ site.baseurl }}/guides/rhinopython/your-first-python-script-in-grasshopper))
- [Where to get help...]({{ site.baseurl }}/guides/rhinopython/python-where-to-find-help)
- [Troubleshooting Installation]({{ site.baseurl }}/guides/rhinopython/python-troubleshooting-install)

### Python Editor for Windows

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.sdk contains 'RhinoPython' and guide.categories contains 'Python Windows' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Python in Grasshopper

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.sdk contains 'RhinoPython' and guide.categories contains 'GhPython' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>


### Fundamentals

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.sdk contains 'RhinoPython' and guide.categories contains 'Fundamentals' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Python in Rhino

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.sdk contains 'RhinoPython' and guide.categories contains 'Python in Rhino' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### [Rhino.Python 101]({{ site.baseurl }}/guides/rhinopython/primer-101)

&nbsp;&nbsp; [Introduction]({{ site.baseurl }}/guides/rhinopython/primer-101)  
&nbsp;&nbsp; [Where to find help]({{ site.baseurl }}/guides/rhinopython/primer-101/where-to-find-help/)  
&nbsp;&nbsp; 1. [What's it all about?]({{ site.baseurl }}/guides/rhinopython/primer-101/1-whats-it-all-about/)  
&nbsp;&nbsp; 2. [Python Essentials]({{ site.baseurl }}/guides/rhinopython/primer-101/2-python-essentials/)  
&nbsp;&nbsp; 3. [Script anatomy]({{ site.baseurl }}/guides/rhinopython/primer-101/3-script-anatomy/)  
&nbsp;&nbsp; 4. [Operators and functions]({{ site.baseurl }}/guides/rhinopython/primer-101/4-operators-and-functions/)  
&nbsp;&nbsp; 5. [Conditional execution]({{ site.baseurl }}/guides/rhinopython/primer-101/5-conditional-execution/)  
&nbsp;&nbsp; 6. [Tuples, Lists and Dictionaries]({{ site.baseurl }}/guides/rhinopython/primer-101/6-tuples-lists-dictionaries/)  
&nbsp;&nbsp; 7. [Classes]({{ site.baseurl }}/guides/rhinopython/primer-101/7-classes/)  
&nbsp;&nbsp; 8. [Geometry]({{ site.baseurl }}/guides/rhinopython/primer-101/8-geometry/)  

&nbsp;&nbsp; <a href="http://download.rhino3d.com/IronPython/5.0/RhinoPython101/"><span class="glyphicon glyphicon-download"></span></a> [Download the Rhino.Python 101 Primer as a single PDF ](http://download.rhino3d.com/IronPython/5.0/RhinoPython101/)  


### Intermediate

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.sdk contains 'RhinoPython' and guide.categories contains 'Intermediate' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Custom Dialogs in Eto

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.sdk contains 'RhinoPython' and guide.categories contains 'Eto' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>


### Other Resources

- [Rhino Scripting Forum (Discourse)](http://discourse.mcneel.com/c/scripting)  
- [Rhino.Python Samples]({{ site.baseurl }}/samples/#rhinopython)  
- [Rhino.Python Developer Samples GitHub](https://github.com/mcneel/rhino-developer-samples/tree/{{ site.git_branch | default: "master" }}/rhinopython)  
- [Designalyze Python Tutorials](http://designalyze.com/)
- [Plethora Project](https://www.plethora-project.com/education/2017/5/31/rhino-python-programming)
- [Steve Baer's Blog](http://stevebaer.wordpress.com/category/python/)
- [Python Beginner's Guide](http://wiki.python.org/moin/BeginnersGuide/Programmers)
- [Tutorials Point Python Series](http://www.tutorialspoint.com/python/index.htm)
- [Rhino.Python Dash Docset](http://discourse.mcneel.com/t/rhino-python-dash-docset/6399)
- [Nature of Code Video Tutorials](http://www.youtube.com/watch?v=Kyi_K85Gsm4&list=PL5Up_u-XkWgP7nB7XIevMTyBCZ7pvLBGP)

---

## [openNURBS]({{ site.baseurl }}/guides/opennurbs) <img src="{{ site.baseurl }}/images/win-logo-small.png" alt="Windows" class="guide_icon"> <img src="{{ site.baseurl }}/images/mac-logo-small.png" alt="macOS" class="guide_icon">
{: #opennurbs }

*Read/Write Rhino 3dm files in your application.*

### Overview

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.sdk contains 'openNURBS' and guide.categories contains 'Overview' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Getting Started

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.sdk contains 'openNURBS' and guide.categories contains 'Getting Started' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Fundamentals

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.sdk contains 'openNURBS' and guide.categories contains 'Fundamentals' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Advanced

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.sdk contains 'openNURBS' and guide.categories contains 'Advanced' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

---

## [C/C++]({{ site.baseurl }}/guides/cpp) <img src="{{ site.baseurl }}/images/win-logo-small.png" alt="Windows" class="guide_icon">
{: #cpp }

*Native SDK for Rhino for Windows plugins.*

### Overview

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.sdk contains 'C/C++' and guide.categories contains 'Overview' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Getting Started

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.sdk contains 'C/C++' and guide.categories contains 'Getting Started' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Fundamentals

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"title" %}
  <ul>
  {% for guide in guides %}
    {% if guide.sdk contains 'C/C++' and guide.categories contains 'Fundamentals' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Advanced

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"title" %}
  <ul>
  {% for guide in guides %}
    {% if guide.sdk contains 'C/C++' and guide.categories contains 'Advanced' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Rendering (RDK)

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.sdk contains 'C/C++' and guide.categories contains 'RDK' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Zoo

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.sdk contains 'C/C++' and guide.categories contains 'Zoo' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Troubleshooting

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"title" %}
  <ul>
  {% for guide in guides %}
    {% if guide.sdk contains 'C/C++' and guide.categories contains 'Troubleshooting' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

---

## [Grasshopper]({{ site.baseurl }}/guides/grasshopper) <img src="{{ site.baseurl }}/images/win-logo-small.png" alt="Windows" class="guide_icon"> <img src="{{ site.baseurl }}/images/mac-logo-small.png" alt="OS X" class="guide_icon">
{: #grasshopper }

*Create custom Grasshopper components and plugins.*

### Overview

- [What is a Grasshopper Component?]({{ site.baseurl }}/guides/grasshopper/what-is-a-grasshopper-component/)

### Getting Started

- Installing Tools ([Windows]({{ site.baseurl }}/guides/grasshopper/installing-tools-windows/), [Mac]({{ site.baseurl }}/guides/grasshopper/installing-tools-mac/))
- Your First Component ([Windows]({{ site.baseurl }}/guides/grasshopper/your-first-component-windows/), [Mac]({{ site.baseurl }}/guides/grasshopper/your-first-component-mac/))

### Fundamentals

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.sdk contains 'Grasshopper' and guide.categories contains 'Fundamentals' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Advanced

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.sdk contains 'Grasshopper' and guide.categories contains 'Advanced' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### In Depth

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.sdk contains 'Grasshopper' and guide.categories contains 'In Depth' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

---

## [RhinoScript]({{ site.baseurl }}/guides/rhinoscript) <img src="{{ site.baseurl }}/images/win-logo-small.png" alt="Windows" class="guide_icon">
{: #rhinoscript }

*RhinoScript is a scripting tool based on Microsoft's VBScript language. With RhinoScript, you can quickly add functionality to Rhino for Windows, or automate repetitive tasks.*

### Overview

- [What are VBScript and RhinoScript?]({{ site.baseurl }}/guides/rhinoscript/what-are-vbscript-rhinoscript)

### [RhinoScript 101]({{ site.baseurl }}/guides/rhinoscript/primer-101)

&nbsp;&nbsp; [Introduction]({{ site.baseurl }}/guides/rhinoscript/primer-101)  
&nbsp;&nbsp; [Where to find help]({{ site.baseurl }}/guides/rhinoscript/primer-101/where-to-find-help/)  
&nbsp;&nbsp; 1. [What's it all about?]({{ site.baseurl }}/guides/rhinoscript/primer-101/1-whats-it-all-about/)  
&nbsp;&nbsp; 2. [RhinoScript Essentials]({{ site.baseurl }}/guides/rhinoscript/primer-101/2-vbscript-essentials/)  
&nbsp;&nbsp; 3. [Script anatomy]({{ site.baseurl }}/guides/rhinoscript/primer-101/3-script-anatomy/)  
&nbsp;&nbsp; 4. [Operators and functions]({{ site.baseurl }}/guides/rhinoscript/primer-101/4-operators-and-functions/)  
&nbsp;&nbsp; 5. [Conditional execution]({{ site.baseurl }}/guides/rhinoscript/primer-101/5-conditional-execution/)  
&nbsp;&nbsp; 6. [Arrays]({{ site.baseurl }}/guides/rhinoscript/primer-101/6-arrays/)  
&nbsp;&nbsp; 7. [Geometry]({{ site.baseurl }}/guides/rhinoscript/primer-101/7-geometry/)  
&nbsp;&nbsp; <a href="http://www.rhino3d.com/download/rhino/5.0/rhinoscript101"><span class="glyphicon glyphicon-download"></span></a> [Download the RhinoScript 101 Primer as a single PDF ](http://www.rhino3d.com/download/rhino/5.0/rhinoscript101)

### Fundamentals

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.sdk contains 'RhinoScript' and guide.categories contains 'Fundamentals' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>


### Intermediate

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"title" %}
  <ul>
  {% for guide in guides %}
    {% if guide.sdk contains 'RhinoScript' and guide.categories contains 'Intermediate' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Advanced

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"title" %}
  <ul>
  {% for guide in guides %}
    {% if guide.sdk contains 'RhinoScript' and guide.categories contains 'Advanced' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Troubleshooting

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"title" %}
  <ul>
  {% for guide in guides %}
    {% if guide.sdk contains 'RhinoScript' and guide.categories contains 'Troubleshooting' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Other Resources

- [Pascal Golay's scripted utilities for Rhino](http://wiki.mcneel.com/people/pascalgolay)
- [RhinoScript Samples on GitHub](https://github.com/mcneel/rhinoscript)
- [RhinoScript Dash Docset](http://discourse.mcneel.com/t/rhinoscript-dash-docset/6382)
- [RhinoScript Help File On-Line](http://www.rhino3d.com/5/rhinoscript/index.html)

---

## [RhinoMobile]({{ site.baseurl }}/guides/rhinomobile) <img src="{{ site.baseurl }}/images/android-logo-small.png" alt="Android" class="guide_icon"> <img src="{{ site.baseurl }}/images/ios-logo-small.png" alt="iOS" class="guide_icon">
{: #rhinomobile }

*3D mobile application development.*

### Overview

- [What is RhinoMobile?]({{ site.baseurl }}/guides/rhinomobile/what-is-rhinomobile/)

### Getting Started

- Installing Tools ([Windows]({{ site.baseurl }}/guides/rhinomobile/installing-tools-windows/), [Mac]({{ site.baseurl }}/guides/rhinomobile/installing-tools-mac/))
- Your First App ([Windows]({{ site.baseurl }}/guides/rhinomobile/your-first-app-windows/), [Mac]({{ site.baseurl }}/guides/rhinomobile/your-first-app-mac/))

### Fundamentals

- [Using Simulators]({{ site.baseurl }}/guides/rhinomobile/using-simulators/)
- [Testing On Devices]({{ site.baseurl }}/guides/rhinomobile/testing-on-devices/)

---

## [Localization Services](https://www.rhino3d.com/localization) <img src="{{ site.baseurl }}/images/win-logo-small.png" alt="Windows" class="guide_icon"> <img src="{{ site.baseurl }}/images/mac-logo-small.png" alt="OS X" class="guide_icon">
{: #translation }

Our regional office in Europe provides a translation and localization service for third-party developers and anyone else interested in translating their products to French, German, Italian, Spanish, etc. [Details…](https://www.rhino3d.com/localization)




