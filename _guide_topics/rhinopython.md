---
title: Rhino.Python Guides
description: Quickly add functionality to Rhino or automate repetitive tasks.
platforms: ['Windows', 'Mac']
layout: guide-homepage
---

<!--the .snagit project for this image can be found next to the image -->
[<img src="{{ site.baseurl }}/images/rhinopython-guides-col1.png">]({{ site.baseurl }}/guides/rhinopython/what-is-rhinopython/)

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

- Your First Python Script in Rhino ([Windows]({{ site.baseurl }}/guides/rhinopython/your-first-python-script-in-rhino-windows), [Mac]({{ site.baseurl }}/guides/rhinopython/your-first-python-script-in-rhino-mac))

### Python Editor for Windows

<div class="trigger">
  {% assign guides = site.guide_topics | sort:"order" %}
  <ul>
  {% for guide in guides %}
    {% if guide.apis contains 'RhinoPython' and guide.categories contains 'Python Windows' %}
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
    {% if guide.apis contains 'RhinoPython' and guide.categories contains 'Fundamentals' %}
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
    {% if guide.apis contains 'RhinoPython' and guide.categories contains 'Python in Rhino' %}
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

### Other Resources

- [Rhino.Python 101](http://download.rhino3d.com/IronPython/5.0/RhinoPython101/)
- [Rhino Scripting Forum (Discourse)](http://discourse.mcneel.com/c/scripting)
- [Rhino.Python Samples]({{ site.baseurl }}/samples/#rhinopython)
- [Pascal Golay's Python Samples - GitHub](https://github.com/pgolay/PG_Scripts/tree/master/Python)
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
