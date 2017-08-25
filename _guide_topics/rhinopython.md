---
title: Rhino.Python Guides
description: Quickly add functionality to Rhino or automate repetitive tasks.
authors: unset
author_contacts: unset
sdk: unset
languages: unset
platforms: ['Windows', 'Mac']
categories: ['Unsorted']
origin: unset
order: 1
keywords: ['rhino', 'developer']
layout: guide-homepage
---

<!--the .snagit project for this image can be found next to the image -->
[<img src="{{ site.baseurl }}/images/rhinopython-guides-col1.png">]({{ site.baseurl }}/guides/rhinopython/what-is-rhinopython/)

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



<!--column-->

<!--the .snagit project for this image can be found next to the image -->
[<img src="{{ site.baseurl }}/images/rhinopython-guides-col2.png">](https://docs.python.org/2/tutorial/index.html)

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


<!--column-->

<!--the .snagit project for this image can be found next to the image -->
[<img src="{{ site.baseurl }}/images/rhinopython-guides-col3.png">](http://www.rhino3d.com/download/IronPython/5.0/RhinoPython101)

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


### Other Resources

- [Rhino Scripting Forum (Discourse)](http://discourse.mcneel.com/c/scripting)  
- [Rhino.Python Samples]({{ site.baseurl }}/samples/#rhinopython)  
- [Rhino.Python Developer Samples GitHub](https://github.com/mcneel/rhino-developer-samples/tree/{{ site.git_branch | default: "master" }}/rhinopython)  
- [Designalyze Python Tutorials](http://designalyze.com/)
- [Plethora Project](http://www.plethora-project.com/2011/09/12/rhino-python-tutorials/)
- [Steve Baer's Blog](http://stevebaer.wordpress.com/category/python/)
- [Python Beginner's Guide](http://wiki.python.org/moin/BeginnersGuide/Programmers)
- [Tutorials Point Python Series](http://www.tutorialspoint.com/python/index.htm)
- [Rhino.Python Dash Docset](http://discourse.mcneel.com/t/rhino-python-dash-docset/6399)
- [Nature of Code Video Tutorials](http://www.youtube.com/watch?v=Kyi_K85Gsm4&list=PL5Up_u-XkWgP7nB7XIevMTyBCZ7pvLBGP)


<!--column-->

<!--the .snagit project for this image can be found next to the image -->
[<img src="{{ site.baseurl }}/images/rhinopython-guides-col3.png">](http://www.rhino3d.com/download/IronPython/5.0/RhinoPython101)
