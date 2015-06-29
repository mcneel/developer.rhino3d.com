---
layout: toc-page
title: How This Site Works
author: dan@mcneel.com
categories: ['General']
platforms: ['Mac', 'Windows']
apis: ['DevDocs', 'Jekyll', 'Liquid']
languages: ['Markdown', 'Kramdown', 'YAML']
keywords: ['authoring', 'writing', 'editing', 'overview']
TODO: 1
origin: unset
order: 2
---

# How This Site Works

TODO: We need to come up with templates / conventions for content but for now add your markdown files.


## Markdown & Kramdown
{: .toc-header }

Use the [Rhino Developer Docs Style]({{ site.baseurl }}/guides/rhinodevdocs/style_guide/) guide as a reference when writing content for this site.

Nearly all content on this site uses [Markdown](http://daringfireball.net/projects/markdown/basics) as the base format.  We are using the [Kramdown](http://kramdown.gettalong.org/quickref.html) markdown parser, which is the default parser with Jekyll.  A complete guide to Markdown and Kramdown is beyond the scope of this guide.  For markdown syntax, refer to the [Kramdown Quick Reference](http://kramdown.gettalong.org/quickref.html) or use other files on this site as examples.


## Types of content
{: .toc-header }

There are 5 types of content on this site:

 1. [Pages](#pages)
 1. [Guides](#guides)
 1. [APIs](#apis)
 1. [Samples](#samples)
 1. [Glossary Entries](#glossary_entries)

All types of content - with the exception of APIs - begin with YAML, which the site uses to categories and sort the content into appropriate areas.


#### Pages
{: .toc-subheader }

Pages are interspersed throughout the site.  The [Welcome page]({{ site.baseurl }}/), the [Guides page]( {{ site.baseurl }}/guides), and RhinoCommon Samples page, are all examples of Pages.

Here is an example of the YAML for [a page]({{ site.baseurl }}/guides/general):

```yaml
---
layout: toc-page
title: General Guides
order: 0
---
```

The YAML fields for Pages determine:

* **layout**: The layout template used by Liquid (found in `/_layouts/`) on the page.
* **title**: This is the title of the page.  This is the html page title.
* **order**: The relative sort-order of this page in any collection of pages.

TODO: What about pages with permalinks?

#### Guides
{: .toc-subheader }

Guides are contained in the `/_guide_topics/` directory.  This very document you are reading is a Guide.

To create a new guide, simply create a new markdown file and place it in the `/_guide_topics/` folder.  The file must have a .md file extension and begin with some YAML that is used to determine what it is and where it should be placed on the site.

Here is an example of the YAML for this guide:

```yaml
---
layout: toc-page
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

The YAML fields for Guides determine:

* **layout**: The layout template used by Liquid (found in `/_layouts/`) on the guide.
* **title**: This is the title of the guide.  This is the html page title.
* **author**: The original - or responsible - author.
* **categories**: The category of the guide (General, Overview, Advanced).
* **platforms**: The operating systems this guide is relevant to.
* **apis**: The Rhino APIs that this guide pertains to.
* **languages**: The programming languages this guide references.
* **keywords**: Keywords related to this guide (un-used, as of yet).
* **order**: The relative sort-order of this guide in any list.


#### APIs
{: .toc-subheader }

The [API documentation]({{ site.baseurl }}/api/) is automatically generated from source-code and cannot be edited "by hand."

#### Samples
{: .toc-subheader }

Samples are contained in the `/_samples/` directory.

Here is an example of the YAML for [this sample]({{ site.baseurl }}/samples/rhinocommon/extend_a_curve_object/):

```yaml
---
layout: code-sample
title: Extend a Curve Object
author: dale@mcneel.com
categories: ['Curves']
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#', 'Python', 'VB.NET']
keywords: ['Extend', 'Curve', 'Sample']
order: 1
description: This shows how to extend a curve object
---
```

The YAML fields for Samples determine:

* **layout**: The layout template used by Liquid (found in `/_layouts/`) on the sample.
* **title**: This is the title of the sample.  This is the html page title.
* **author**: The original - or responsible - author.
* **categories**: The category of the sample (Recipes, Snippet, Boilerplate).
* **platforms**: The operating systems this sample is relevant to.
* **apis**: The Rhino APIs that this sample pertains to.
* **languages**: The programming languages this sample references.
* **keywords**: Keywords related to this sample (un-used, as of yet).
* **order**: The relative sort-order of this sample in any list.
* **description**: A brief description of what the sample does.

#### Glossary Entries
{: .toc-subheader }

Lorem ipsum

## Templates
{: .toc-header }

Lorem ipsum
