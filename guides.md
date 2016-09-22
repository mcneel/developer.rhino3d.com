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

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.apis contains 'General' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

---

## [RhinoCommon]({{ site.baseurl }}/guides/rhinocommon) <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon"> <img src="{{ site.baseurl }}/images/mac_logo_small.png" alt="OS X" class="guide_icon">
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
  {% for guide in guides %}
    {% if guide.apis contains 'RhinoCommon' and guide.categories contains 'Fundamentals' %}
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
  {% for guide in guides %}
    {% if guide.apis contains 'RhinoCommon' and guide.categories contains 'Advanced' %}
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
    {% if guide.apis contains 'RhinoCommon' and guide.categories contains 'Zoo' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

---

## [Rhino.Python]({{ site.baseurl }}/guides/rhinopython) <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon"> <img src="{{ site.baseurl }}/images/mac_logo_small.png" alt="OS X" class="guide_icon">
{: #rhinopython }

*Quickly add functionality to Rhino or automate repetitive tasks.*

### Overview

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.apis contains 'RhinoPython' and guide.categories contains 'Overview' %}
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
    {% if guide.apis contains 'RhinoPython' and guide.categories contains 'Getting Started' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Learning Python

- <a href="https://docs.python.org/2/tutorial/index.html" target="_blank">The Python Tutorial</a>
- <a href="http://learnpythonthehardway.org/book/" target="_blank">Learn Python the Hard Way</a> (despite the title this is a beginner's book)
- <a href="https://automatetheboringstuff.com/" target="_blank">Automate The Boring Stuff With Python</a>

### Learning Rhino.Python

- <a href="http://www.rhino3d.com/download/IronPython/5.0/RhinoPython101" target="_blank">RhinoPython101 Primer</a>
- <a href="http://4.rhino3d.com/5/ironpython/index.html" target="_blank">Rhino.Python Programmer's Reference</a>
- <a href="http://discourse.mcneel.com/c/scripting" target="_blank">Rhino Scripting Forum</a>

---

## [openNURBS]({{ site.baseurl }}/guides/opennurbs) <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon"> <img src="{{ site.baseurl }}/images/mac_logo_small.png" alt="OS X" class="guide_icon">
{: #opennurbs }

*Read/Write Rhino 3dm files in your application.*

### Overview

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.apis contains 'openNURBS' and guide.categories contains 'Overview' %}
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
    {% if guide.apis contains 'openNURBS' and guide.categories contains 'Getting Started' %}
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
    {% if guide.apis contains 'openNURBS' and guide.categories contains 'Fundamentals' %}
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
    {% if guide.apis contains 'openNURBS' and guide.categories contains 'Advanced' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

---

## [C/C++]({{ site.baseurl }}/guides/cpp) <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon">
{: #cpp }

*Native SDK for Rhino for Windows plugins.*

### Overview

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.apis contains 'C/C++' and guide.categories contains 'Overview' %}
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
    {% if guide.apis contains 'C/C++' and guide.categories contains 'Getting Started' %}
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
    {% if guide.apis contains 'C/C++' and guide.categories contains 'Fundamentals' %}
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
    {% if guide.apis contains 'C/C++' and guide.categories contains 'Advanced' %}
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
    {% if guide.apis contains 'C/C++' and guide.categories contains 'RDK' %}
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
    {% if guide.apis contains 'C/C++' and guide.categories contains 'Zoo' %}
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
    {% if guide.apis contains 'C/C++' and guide.categories contains 'Troubleshooting' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

---

## [Grasshopper]({{ site.baseurl }}/guides/grasshopper) <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon">
{: #grasshopper }

*Create custom Grasshopper components and plugins.*

### Overview

- [What is a Grasshopper Component?]({{ site.baseurl }}/guides/grasshopper/what_is_a_grasshopper_component/)

### Getting Started

- [Installing Tools]({{ site.baseurl }}/guides/grasshopper/installing_tools_windows/)
- [Your First Component]({{ site.baseurl }}/guides/grasshopper/your_first_component_windows/)

### Fundamentals

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.apis contains 'Grasshopper' and guide.categories contains 'Fundamentals' %}
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
    {% if guide.apis contains 'Grasshopper' and guide.categories contains 'Advanced' %}
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
    {% if guide.apis contains 'Grasshopper' and guide.categories contains 'In Depth' %}
      {% if guide.title and guide.order %}
        <li><a class="page-link" href="{{ guide.url | prepend: site.baseurl }}" title="{{ guide.description }}">{{ guide.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

---

## [RhinoScript]({{ site.baseurl }}/guides/rhinoscript) <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon">
{: #rhinoscript }

*RhinoScript is a scripting tool based on Microsoft's VBScript language. With RhinoScript, you can quickly add functionality to Rhino for Windows, or automate repetitive tasks.*

### Overview

- [What are VBScript and RhinoScript?]({{ site.baseurl }}/guides/rhinoscript/what_are_vbscript_rhinoscript)

### Getting Started

- [RhinoScript 101 Primer](http://www.rhino3d.com/download/rhino/5.0/rhinoscript101)

### Fundamentals

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.apis contains 'RhinoScript' and guide.categories contains 'Fundamentals' %}
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
    {% if guide.apis contains 'RhinoScript' and guide.categories contains 'Intermediate' %}
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
    {% if guide.apis contains 'RhinoScript' and guide.categories contains 'Advanced' %}
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
    {% if guide.apis contains 'RhinoScript' and guide.categories contains 'Troubleshooting' %}
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

## [RhinoMobile]({{ site.baseurl }}/guides/rhinomobile) <img src="{{ site.baseurl }}/images/android_logo_small.png" alt="Android" class="guide_icon"> <img src="{{ site.baseurl }}/images/ios_logo_small.png" alt="iOS" class="guide_icon">
{: #rhinomobile }

*3D mobile application development.*

### Overview

- [What is RhinoMobile?]({{ site.baseurl }}/guides/rhinomobile/what_is_rhinomobile/)

### Getting Started

- Installing Tools ([Windows]({{ site.baseurl }}/guides/rhinomobile/installing_tools_windows/), [Mac]({{ site.baseurl }}/guides/rhinomobile/installing_tools_mac/))
- Your First App ([Windows]({{ site.baseurl }}/guides/rhinomobile/your_first_app_windows/), [Mac]({{ site.baseurl }}/guides/rhinomobile/your_first_app_mac/))

### Fundamentals

- [Using Simulators]({{ site.baseurl }}/guides/rhinomobile/using_simulators/)
- [Testing On Devices]({{ site.baseurl }}/guides/rhinomobile/testing_on_devices/)
