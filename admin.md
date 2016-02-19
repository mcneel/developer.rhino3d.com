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

- [Rhino Developer wiki](http://wiki.mcneel.com/developer/home)
- [RhinoCommon API references](http://4.rhino3d.com/5/rhinocommon/)
- [C++ SDK API references](http://4.rhino3d.com/5/rhinocppsdk/idx.html)
- [RhinoCommon samples on GitHub](https://github.com/mcneel/rhinocommon/tree/master/examples)
- [DaleF's CsCommands](https://github.com/dalefugier/SampleCsCommands/)
- [Doxygen Docs (on McNeel intranet)](http://phab.mcneel.com/docs/rhino/6/rhinocommon/)
- Dale Lear's Developer Meeting Notes
- RhinoScript and Rhino.Python Primers
- Mitch's MicMac tools: http://wiki.mcneel.com/people/mitchheynick
- [Grasshopper SDK Help file (chm)](http://s3.amazonaws.com/files.na.mcneel.com/grasshopper/1.0/docs/en/GrasshopperSDK.chm).

**DO NOT** port any content that relates to pre-Rhino 5: this is old information.  Visual Studio 2010 for the C/C++ SDK was used for Rhino 5.

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

The following guides have TODO items:

{% assign guides = site.guide_topics | sort:"title" | sort:"apis" %}
<div class="trigger">
  <ol>
  {% for topic in guides %}
    {% if topic.TODO %}
      <li>
        ({{ topic.apis }}) <a class="page-link" href="{{ topic.url | prepend: site.baseurl }}">{{ topic.title }}</a> {{ topic.TODO }} {% if topic.origin != 'unset' and topic.TODO == 'needs porting' %} from: <a href="{{ topic.origin }}">{{ topic.origin }}</a>{% endif %}
      </li>
    {% endif %}
  {% endfor %}
  </ol>
</div>


### Samples

The following samples have TODO items:

{% assign samples = site.samples | sort:"title" | sort:"apis" %}
<div class="trigger">
  <ol>
  {% for sample in samples %}
    {% if sample.TODO %}
      <li>
        ({{ sample.apis }}) <a class="page-link" href="{{ sample.url | prepend: site.baseurl }}">{{ sample.title }}</a>  {{ sample.TODO }} {% if sample.origin != 'unset'  and sample.TODO == 'needs porting' %} from: <a href="{{ sample.origin }}">{{ sample.origin }}</a>{% endif %}
    </li>
    {% endif %}
  {% endfor %}
  </ol>
</div>

### Misc

- Deprecate developer wiki - redirects, deprecated notices, etc.
- Move Dev Docs guides into the General Section of the page.
- Standardize file names (underscores, verbiage, length, etc).
- Entire Rhino.Python guides section needs complete reorganization and simplification.
- Zoo API should be consolidated into categories in C/C++ and RhinoCommon respectively.
- RDK API should be consolidated into categories in C/C++ and RhinoCommon respectively.
- Add filenaming conventions to style-guide: guides are "guides to..." "determining, adding..." etc.
- RhinoScript Guides and RhinoScript Samples need to be organized and curated more.
- C/C++ Samples need to be categorized and organized.
- We could report samples that are not passing tests.
- Standardize descriptions so they are only in the yaml.
- Standardize titles so they are on in the yaml - requires reworking TOC generator.
- Macros documentation sources: [Macros in Helpfile](http://docs.mcneel.com/rhino/5/help/en-us/information/rhinoscripting.htm), [Macros in Wiki](http://wiki.mcneel.com/rhino/basicmacros), [Using the MacroEditor](http://wiki.mcneel.com/developer/macroscriptsetup)
- Move all samples to mcneel/github - in coordination with Dale Fugier
- Link directly to samples on GitHub from gh-pages samples section for example: [https://github.com/mcneel/Rhino5Samples_CPP](https://github.com/mcneel/Rhino5Samples_CPP)
- Re-capture images on retina display and replace them
- What, Where, How, Why table on [homepage]({{ site.baseurl }}) does not work on iOS's Safari.  Fix it.
- Page width resizes each time templates are switched.  This is annoying.
- Add bylines to guides footer or some template?
- Update openNURBS links here: https://www.rhino3d.com/opennurbs
