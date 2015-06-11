---
layout: tab-page
title: guides
permalink: /guides/
order: 2
---

# All Guides
---

## RhinoCommon (Cross-Platform)
---

### About RhinoCommon

- What is it?  Why?  Blah blah blah

### Getting Started

- Installing the tools (Windows)
- Installing the tools (Mac)
- Hello Rhino (Cross-Platform)
- Debugging Hello Rhino (Windows)
- Debugging Hello Rhino (Mac)

### Plugin Fundamentals

- [How the Commands Work](http://wiki.mcneel.com/developer/runrhinocommandfromplugincommand) - Needs porting
- [Event Watchers](http://wiki.mcneel.com/developer/rhinocommonsamples/dotneteventwatcher) - Needs porting

### Advanced

- [Display Conduits](http://wiki.mcneel.com/developer/rhinocommonsamples/displayconduit) - Needs porting
- Rendering
- Custom Objects

## C/C++ (Windows)
---

TODO

## Rhino.Python (Cross-Platform)
---

TODO

## Grasshopper (Windows)
---

TODO

## RhinoScript (Windows)
---

TODO

## Eto (Cross-Platform)
---

TODO


## openNURBS Toolkit (Cross-Platform)
---

TODO


## Render Development Kit (RDK)
---

TODO


## Rhino Application Platform (RAP)
---

TODO


## RhinoMobile
---

TODO


## Zoo License Manager
---

TODO


## Developer Docs - This Website
---

<div class="trigger">
  <ul>
  {% for topic in site.guide_topics %}
    {% if topic.title %}
    <li><a class="page-link" href="{{ topic.url | prepend: site.baseurl }}">{{ topic.title }}</a></li>
    {% endif %}
  {% endfor %}
  </ul>
</div>
