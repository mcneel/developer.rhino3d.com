---
layout: tab-page
title: RhinoCommon Guides
---

# RhinoCommon Guides
---

### Overview
<div class="trigger">
  <ul>
  {% for topic in site.guide_topics %}
    {% if topic.tags contains 'Guide' and topic.tags contains 'About' and topic.tags contains 'RhinoCommon' %}
      {% if topic.title  %}
        <li><a class="page-link" href="{{ topic.url | prepend: site.baseurl }}">{{ topic.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

### Getting Started
<div class="trigger">
  <ul>
  {% for topic in site.guide_topics %}
    {% if topic.tags contains 'Guide' and topic.tags contains 'GettingStarted' and topic.tags contains 'RhinoCommon' %}
      {% if topic.title  %}
        <li><a class="page-link" href="{{ topic.url | prepend: site.baseurl }}">{{ topic.title }}</a></li>
      {% endif %}
    {% endif %}
  {% endfor %}
  </ul>
</div>

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
