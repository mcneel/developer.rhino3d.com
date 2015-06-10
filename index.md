---
layout: default
---

#### The beginnings of a new developer docs site.  

So far the focus has been on how the technology works so we can come up with a structure that allows easy editing of content.  Styling and making it look pretty will come later.  Some of you have more experience than I in web development so feel free to join the fun.  

The site is hosted on [GitHub Pages](https://pages.github.com/) and we are using [Jekyll](http://jekyllrb.com/) as our static site generator.  Jekyll is what runs under GitHub Pages but we also chose it because it seems to be the standard among [many](https://staticsitegenerators.net/).  Jekyll was first conceived for blog sites but also well suited for documentation sites.  The idea is to create the structure using a combination of html and markdown files and have the content, [guides]({{ '/guides' | prepend: site.baseurl }}) and [samples]({{ '/samples' | prepend: site.baseurl }}) (for now), be in markdown (and LaTeX?) only if possible for maximum portability in case we later switch platform.  [Liquid](https://github.com/Shopify/liquid/wiki) is the template engine in Jekyll and we'll also use [Bootstrap](http://getbootstrap.com/).  

The [Kramdown] markdown parser, the default parser with Jekyll, has support for LaTeX to PNG rendering via [MathJax](http://www.mathjax.org/).  

ex:  
$$y = {\sqrt{x^2+(x-1)} \over x-3} + \left| 2x \over x^{0.5x} \right|$$
