---
layout: tab-page
title: Authoring content
author: dan@mcneel.com
categories: ['General']
platforms: ['Mac', 'Windows']
apis: ['DevDocs', 'Jekyll', 'Liquid']
languages: ['Markdown', 'Kramdown', 'YAML']
keywords: ['authoring', 'writing', 'editing']
order: 2
---

# Authoring content

We need to come up with templates / conventions for content but for now add your markdown files.

## Markdown & Kramdown

Nearly all content on this site uses [Markdown](http://daringfireball.net/projects/markdown/basics) as the base format.  We are using the [Kramdown](http://kramdown.gettalong.org/quickref.html) markdown parser, the default parser with Jekyll.

Kramdown has support for LaTeX to PNG rendering via [MathJax](http://www.mathjax.org/).  

ex:  
$$y = {\sqrt{x^2+(x-1)} \over x-3} + \left| 2x \over x^{0.5x} \right|$$  


## Types of content

There are 5 types of content:

 1. Pages
 1. Guides
 1. APIs
 1. Samples
 1. Glossary Entries

All types of content - with the exception of APIs - begin with YAML, which the site uses to categories and sort the content into appropriate areas.

### Pages

Pages are interspersed throughout the site.  The Welcome page, the Guides page, and RhinoCommon Samples page, are all examples of Pages.

Here is an example of the YAML for [a page]({{ site.baseurl }}/guides/general):

```yaml
---
layout: tab-page
title: General Guides
order: 0
---
```

### Guides

Guides are contained in the `/_guide_topics/` directory.  This very document you are reading is a Guide.

Here is an example of the YAML for this guide:

```yaml
---
layout: tab-page
title: Authoring content
author: dan@mcneel.com
categories: ['General']
platforms: ['Mac', 'Windows']
apis: ['DevDocs', 'Jekyll', 'Liquid']
languages: ['Markdown']
keywords: ['authoring', 'writing', 'editing']
order: 2
---
```

### APIs

The [API documentation]({{ site.baseurl }}/api/) is automatically generated from source-code and cannot be edited "by hand."

### Samples

Samples are contained in the `/_samples/` directory.

Here is an example of the YAML for a sample:


### Glossary Entries

Lorem ipsum
