---
layout: tab-page
title: Write and Edit content
order: 1
tags: ['Guide', 'DevDocs']
---

We need to come up with templates / conventions for content but for now add your markdown files in the following directories:  

  - guides under \_guide_topics  
  - samples under \_samples
  - blog posts under \_posts  
    see [Jekyll docs](http://jekyllrb.com/docs/posts/) for post name conventions.

#### Kramdown

The [Kramdown] markdown parser, the default parser with Jekyll, has support for LaTeX to PNG rendering via [MathJax](http://www.mathjax.org/).  

ex:  
$$y = {\sqrt{x^2+(x-1)} \over x-3} + \left| 2x \over x^{0.5x} \right|$$  

See the [guides]({{ '/guides' | prepend: site.baseurl }}) to read about how to [run jekyll locally]({{ '/guides/setup_jekyll' | prepend: site.baseurl }}) or [write content]({{ '/guides/write_content' | prepend: site.baseurl }}).
