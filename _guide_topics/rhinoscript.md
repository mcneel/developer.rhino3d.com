---
title: RhinoScript Guides
description: RhinoScript is a scripting tool based on Microsoft's VBScript language. With RhinoScript, you can quickly add functionality to Rhino for Windows, or automate repetitive tasks.
authors: unset
author_contacts: unset
sdk: unset
languages: unset
platforms: ['Windows']
categories: ['Unsorted']
origin: unset
order: 1
keywords: ['rhino', 'developer']
layout: guide-homepage
---

<!--the .snagit project for this image can be found next to the image -->
[<img src="{{ site.baseurl }}/images/rhinoscript-guides-col1.png">](http://www.rhino3d.com/download/rhino/5.0/rhinoscript101)

### Overview

- [What are VBScript and RhinoScript?]({{ site.baseurl }}/guides/rhinoscript/what-are-vbscript-rhinoscript)

### [RhinoScript 101]({{ site.baseurl }}/guides/rhinoscript/primer-101)

&nbsp;&nbsp; [Introduction]({{ site.baseurl }}/guides/rhinoscript/primer-101/)  
&nbsp;&nbsp; [Where to find help]({{ site.baseurl }}/guides/rhinoscript/primer-101/where-to-find-help/)  
&nbsp;&nbsp; 1. [What's it all about?]({{ site.baseurl }}/guides/rhinoscript/primer-101/1-whats-it-all-about/)  
&nbsp;&nbsp; 2. [RhinoScript Essentials]({{ site.baseurl }}/guides/rhinoscript/primer-101/2-vbscript-essentials/)  
&nbsp;&nbsp; 3. [Script anatomy]({{ site.baseurl }}/guides/rhinoscript/primer-101/3-script-anatomy/)  
&nbsp;&nbsp; 4. [Operators and functions]({{ site.baseurl }}/guides/rhinoscript/primer-101/4-operators-and-functions/)  
&nbsp;&nbsp; 5. [Conditional execution]({{ site.baseurl }}/guides/rhinoscript/primer-101/5-conditional-execution/)  
&nbsp;&nbsp; 6. [Arrays]({{ site.baseurl }}/guides/rhinoscript/primer-101/6-arrays/)  
&nbsp;&nbsp; 7. [Geometry]({{ site.baseurl }}/guides/rhinoscript/primer-101/7-geometry/)  
&nbsp;&nbsp; [Complete RhinoScript 101 Primer PDF](http://www.rhino3d.com/download/rhino/5.0/rhinoscript101)

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

<!--column-->

<!--the .snagit project for this image can be found next to the image -->
[<img src="{{ site.baseurl }}/images/rhinoscript-guides-col2.png">]({{ site.baseurl }}/guides/rhinoscript/comparing-arrays/)

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

<!--column-->

<!--the .snagit project for this image can be found next to the image -->
[<img src="{{ site.baseurl }}/images/rhinoscript-guides-col3.png">]({{ site.baseurl }}/guides/rhinoscript/array-utilities/)

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
