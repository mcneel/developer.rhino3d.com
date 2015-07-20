---
layout: toc-page
title: Guides
permalink: /guides/
order: 2
---

# Guides
{: .toc-title }

---

## General
{: .toc-header }

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

## RhinoCommon
{: .toc-header }

**Platforms**: <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon"> <img src="{{ site.baseurl }}/images/mac_logo_small.png" alt="OS X" class="guide_icon">

#### Overview
{: .toc-subheader }

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for topic in guides %}
    {% if topic.apis contains 'RhinoCommon' and topic.categories contains 'Overview' %}
      {% if topic.title and topic.order %}
        <li><a class="page-link" href="{{ topic.url | prepend: site.baseurl }}">{{ topic.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

#### Getting Started
{: .toc-subheader }

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for topic in guides %}
    {% if topic.apis contains 'RhinoCommon' and topic.categories contains 'GettingStarted' %}
      {% if topic.title and topic.order %}
        <li><a class="page-link" href="{{ topic.url | prepend: site.baseurl }}">{{ topic.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

#### Fundamentals
{: .toc-subheader }

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
- [How the Commands Work](http://wiki.mcneel.com/developer/runrhinocommandfromplugincommand) - Needs porting
- [Event Watchers](http://wiki.mcneel.com/developer/rhinocommonsamples/dotneteventwatcher) - Needs porting

#### Advanced
{: .toc-subheader }

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
- [Display Conduits](http://wiki.mcneel.com/developer/rhinocommonsamples/displayconduit) - Needs porting
- Rendering
- Custom Objects

---


## Rhino.Python
{: .toc-header }

**Platforms**: <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon"> <img src="{{ site.baseurl }}/images/mac_logo_small.png" alt="OS X" class="guide_icon">

#### Overview
{: .toc-subheader }
RhinoPython is a scripting tool that let's you quickly add functionality to Rhino or automate repetitive tasks.

#### Getting Started
{: .toc-subheader }

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

#### Learning Resources
{: .toc-subheader}

##### Python Applied to Rhino
- <a href="http://www.rhino3d.com/download/IronPython/5.0/RhinoPython101" target="_blank">RhinoPython101 Primer</a>
- <a href="http://discourse.mcneel.com/c/scripting" target="_blank">Rhino Scripting Forum</a>
- <a href="http://wiki.mcneel.com/developer/python%22" target="_blank">McNeel Python Scripting Wiki</a>

##### Learning Python
- <a href="https://docs.python.org/2/tutorial/index.html" target="_blank">The Python Tutorial</a>
- <a href="http://learnpythonthehardway.org/book/" target="_blank">Learn Python the Hard Way</a> (despite the title this is a beginner's book)
- <a href="https://automatetheboringstuff.com/" target="_blank">Automate The Boring Stuff With Python</a>

---

## openNURBS
{: .toc-header }

**Platforms**: <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon"> <img src="{{ site.baseurl }}/images/mac_logo_small.png" alt="OS X" class="guide_icon">

TODO


---

## C/C++
{: .toc-header }

**Platforms**: <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon">

TODO


---

## Grasshopper
{: .toc-header }

**Platforms**: <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon">

TODO


---

## RhinoScript
{: .toc-header }

**Platforms**: <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon">

TODO

#### Overview
{: .toc-subheader }
RhinoScript is a scripting tool based on Microsoft's VBScript language. With RhinoScript, you can quickly add functionality to Rhino, or automate repetitive tasks.

#### Learning Resources
{: .subgroup}

- [Microsoft VBScript User's Guide and Language Reference](http://msdn.microsoft.com/en-us/library/t0aew7h6(VS.85).aspx)
- [RhinoScript 101 Primer](http://www.rhino3d.com/download/rhino/5.0/rhinoscript101)
- [RhinoScript Help File On-Line](http://www.rhino3d.com/5/rhinoscript/index.html)
- [RhinoScript Dash Docset](http://discourse.mcneel.com/t/rhinoscript-dash-docset/6382)
- [RhinoScript Samples on GitHub](https://github.com/mcneel/rhinoscript)
- [RhinoScript Resources](http://www.microsoft.com/technet/scriptcenter/default.mspx)
- [Microsoft TechNet Script Center](http://www.microsoft.com/technet/scriptcenter/default.mspx)
- [Pascal Golay's scripted utilities for Rhino](http://wiki.mcneel.com/people/pascalgolay)

#### VBScript Basics
{: .subgroup}

<!-- TODO - This section could be auto Generated -->

- [VBScript Procedures]({{ site.baseurl }}/guides/rhinoscript/vbscript_procedures/)
- [VBScript Statements]({{ site.baseurl }}/guides/rhinoscript/vbscript_statements/)
- [VBScript String Literals]({{ site.baseurl }}/guides/rhinoscript/vbscript_string_literals/)
- [VBScript Variables]({{ site.baseurl }}/guides/rhinoscript/vbscript_variables/)


---

## RDK
{: .toc-header }

**Platforms**: <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon">

TODO


---

## RhinoMobile
{: .toc-header }

**Platforms**: <img src="{{ site.baseurl }}/images/android_logo_small.png" alt="Android" class="guide_icon"> <img src="{{ site.baseurl }}/images/ios_logo_small.png" alt="iOS" class="guide_icon">

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for topic in guides %}
    {% if topic.apis contains 'RhinoMobile' %}
      {% if topic.title and topic.order %}
        <li><a class="page-link" href="{{ topic.url | prepend: site.baseurl }}">{{ topic.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>



---

## Zoo
{: .toc-header }

**Platforms**: <img src="{{ site.baseurl }}/images/win_logo_small.png" alt="Windows" class="guide_icon">

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

## Developer Docs
{: .toc-header }

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
