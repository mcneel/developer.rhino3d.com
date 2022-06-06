+++
aliases = ["/5/guides/general/developer-docs-style-guide/", "/6/guides/general/developer-docs-style-guide/", "/7/guides/general/developer-docs-style-guide/", "/wip/guides/general/developer-docs-style-guide/"]
authors = [ "dan" ]
categories = [ "This Site" ]
description = "This guide serves as an example and quick reference for the syntax and structure of this site."
keywords = [ "style", "guide" ]
languages = [ "Markdown", "Kramdown", "YAML" ]
sdk = [ "General" ]
title = "Developer Docs Style Guide"
type = "guides"
weight = 8
override_last_modified = "2021-09-03T08:29:10Z"

[admin]
TODO = ""
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++

<a id="top"></a> <!-- this is just a sample anchor -->


{{< call-out "warning" "Transition underway" >}}
This site is undergoing a transition from Jekyll to Hugo. This page is out-of-date while this warning is in place.
{{< /call-out >}}

Below are examples of nearly all the available syntax using Markdown, Kramdown (a superset of Markdown), the table-of-contents UI widget, etc.

Some portions of this page were adapted from the [Kramdown Quick Reference](http://kramdown.gettalong.org/quickref.html).

## Conventions

### Site file naming

The naming convention for files - guides, samples, etc - is lowercase with `-` used as spaces.  This leads to more consistent and legible URLs.  In addition, Google recommends one construct compound URL names with `-` and not underbars (`_`).  For example, consider the name of this guide: "Developer Docs Style Guide".  The file name for this guide is `developer-docs-style-guide`.  Google treats a hyphen as a word separator, but does not treat an underscore that way.  Google treats and underscore as a word joiner — so "red_sneakers" is the same as "redsneakers."

In general, when considering new file names for *guides*, please imagine you are saying "Guide to _____".  This often leads to verbs ending in "-ing", the progressive or continuous verb tense.  Obviously, this is not a hard-and-fast rule, but rather a convention.

In general, when considering new file names for *samples*, please imagine you are saying "_____ sample".  As with guides, this is not a hard-and-fast rule, but rather a general convention.

### Division of content

`# Title` become H1 headers and are reserved for the title of the page only.

`## Header` become H2 headers and are reserved for major sections within the page.

`### Sub Header` become H3 headers and are reserved for sub-sections within a major section.

### Fonts

On Windows, this site attempts to use Segoe UI (font size: 16 px, font weight: 400,  line height: 1.6) and falls back to Frutiger Linotype, Dejavu Sans, Helvetica Neue, Helvetica, Arial, in that order.  On macOS, the site will (almost) certainly use Helvetica Neue or Helvetica (font size: 16 px, font weight: 300,  line height: 1.6).  The operating system-specific font weight is set in the footer using javascript.

### Paths & Filenames

`*Italics*` are used to denote filenames, paths, and file extensions.  For example:

Navigate to *C:\Program Files\Rhinoceros 5 (64-bit)\Plug-ins*.

### Bold

`**Bold**` (strong emphasis) is used in instructions to highlight critical instructions that are very important.  Bold should be **used sparingly** as it is often present in headers as natural division of content.

### Spelling & Case

The following spelling and case conventions are adopted on this site:

- "Plugins" is not hyphenated unless it refers to a place in the Rhino UI where it is hyphenated.
- "openNURBS" (not OpenNURBS, nor opennurbs, nor oPeNnURBs) unless it refers to a namespace in code where it is capitalized, or a path where it is not.

### Images & Screenshots

When feasible, it is best to use the *.svg* vector format for images, especially for diagrams.

When using bitmap images, the preferred format is *.png*, but any browser-friendly bitmap format will work.

When capturing screenshots, consider that many people have high-DPI (aka: "Retina") displays.  Please capture all screenshots on a high-DPI display.

See the [Text Modifiers > Images section](#images) of this guide for more information on inserting images.

## Headers

Headers demarcate major sections of the page, guide, etc.

Headers are created like this:

```yaml
## Headers
```

The example above is an H2 header.  

Creating a header automatically creates an #anchor tag in the generated html.  

For headers with multiple words, Kramdown lowercases all the words and adds dashes for spaces. For example, if we had a header like this:

```yaml
## All Your Base Are Belong to Us
```

the resulting html anchor tag would be:

```yaml
#all-your-base-are-belong-to-us
```

### Sub Headers

Sub Headers demarcate sub-sections a major section underneath a header.

Sub Headers are created like this:

```yaml
### Sub Header
```

The example above is an H3 header, which we are calling a "Sub Header."

Just like with H3 headers, H3 headers also create an #anchor tag in the generated html.

## Table of Contents

The UI-widget to the left of this column is a the Table of Contents (TOC) for this page.  If you are authoring a page that requires a TOC, you can generate one automatically by using a TOC-enabled layouts (see [How This Site Works](/guides/general/how-this-site-works/) for more information).  To get a TOC-enabled templates to generate the TOC automatically from the H1, H2 and H3 headers.

For example, to get the main title to show up in the TOC, you would type this:

```yaml
# The Title
```

To get a Header to show up in the TOC, you would type this:

```yaml
## Cool Header
```

To get a Sub Header to show up in the TOC, you would type this:

```yaml
### Sweet Sub Header
```

**Note**: TOCs are only generated from *H1*, *H2*, and *H3* headers...*H4* (and smaller) headers are ignored by the TOC-enabled templates.

## Structural Elements

### Paragraphs

Consecutive lines of text are considered to be one paragraph. You must add a blank line between paragraphs.

### Block Quotes

A blockquote is started using the > marker followed by an optional space; all following lines that are also started with the blockquote marker belong to the blockquote. You can use any block-level elements inside a blockquote:

```kramdown
> This is a sample block quote
>
> >Nested blockquotes are also possible.
```
Yields:

> This is a sample block quote
>
> >Nested blockquotes are also possible.

### Code Blocks

To create a code block, surround the code with three back-ticks, followed by a language abbreviation.  For example:

```kramdown
```cs
```

...followed by the code...

```cs
public static Rhino.Commands.Result AddCircle(Rhino.RhinoDoc doc)
{
  Rhino.Geometry.Point3d center = new Rhino.Geometry.Point3d(0, 0, 0);
  const double radius = 10.0;
  Rhino.Geometry.Circle c = new Rhino.Geometry.Circle(center, radius);
  if (doc.Objects.AddCircle(c) != Guid.Empty)
  {
    doc.Views.Redraw();
    return Rhino.Commands.Result.Success;
  }
  return Rhino.Commands.Result.Failure;
}
```
...and finally closed by three back-ticks.

The abbreviation after the first set of back-ticks is the language code for syntax highlighting.  We are using a syntax highlighting plugin called highlight.js.  [Many languages](https://highlightjs.org/download/) are supported.  The most common language abbreviations used on this site are:

- `cs` is C#
- `vbnet` is Visual Basic
- `python` is Python
- `cpp` is C/C++

A complete list of language aliases can be found in [the individual source files](https://github.com/isagalaev/highlight.js/tree/master/src/languages) for highlight.js.

### Horizontal Rules

Horizontal rules (lines) are created by using three dashes:

```kramdown
---
```

You can an example of one of these right here...

### Lists

You can create ordered lists and unordered lists.

**Ordered Lists**

Ordered lists are created by typing `1.` at the start of a line, like this:

```kramdown
This is an ordered list:

1. Item one.
1. Item two.
1. Item three.
```

yields:

This is an ordered list:

1. Item one.
1. Item two.
1. Item three.

Nested ordered lists are also possible.  For example:

```kramdown
This is a nested ordered list:

1. Do item one.
   1. Item one subtask one.
   1. Item one subtask two.
1. Do item two.
1. Do item three.
```

yields:

This is a nested ordered list:

1. Do item one.
   1. Item one subtask one.
   1. Item one subtask two.
1. Do item two.
1. Do item three.

**Unordered Lists**

Unordered lists (bullet lists) are created using the dash (-) symbol at the beginning of a line:

```kramdown
This is a bullet list:

- Item one
- Item two
- Item three
```

yields:

This is a bullet list:

- Item one
- Item two
- Item three

### Tables

Kramdown supports a syntax for creating simple tables. A line starting with a pipe character starts a table row. However, if the pipe characters is immediately followed by a dash (-), a separator line is created. Separator lines are used to split the table header from the table body (and optionally align the table columns) and to split the table body into multiple parts. If the pipe character is followed by an equal sign (=), the tables rows below it are part of the table footer.

Here is the syntax for a simple table:

```kramdown
| A simple | table |
| with multiple | lines|
```

yields:

| A simple | table |
| with multiple | lines|

More complex tables can be added like this:

```kramdown
| Header1 | Header2 | Header3 |
|:--------|:-------:|--------:|
| cell1   | cell2   | cell3   |
| cell4   | cell5   | cell6   |
|----
| cell1   | cell2   | cell3   |
| cell4   | cell5   | cell6   |
|=====
| Foot1   | Foot2   | Foot3

```

yields:

| Header1 | Header2 | Header3 |
|:--------|:-------:|--------:|
| cell1   | cell2   | cell3   |
| cell4   | cell5   | cell6   |
|----
| cell1   | cell2   | cell3   |
| cell4   | cell5   | cell6   |
|=====
| Foot1   | Foot2   | Foot3


### Warnings

Warnings are used in text to call out major traps, gotchas, or caveats in guides.  HTML is required to create warnings.  For example:

```html
<div class="bs-callout bs-callout-danger">
  <h4>WARNING</h4>
  <p><b>Early-adopters</b>: the following steps will <b>NOT</b> work with the currently released Rhinoceros (5.x.x).  You will need to use WIP version of Rhinoceros.</p>
</div>
```

yields:

<div class="bs-callout bs-callout-danger">
  <h4>WARNING</h4>
  <p><b>Early-adopters</b>: the following steps will <b>NOT</b> work with the currently released Rhinoceros (5.x.x).  You will need to use WIP version of Rhinoceros.</p>
</div>


## Text Modifiers

### Emphasis

Emphasis (bold and italic) can be added to text by surrounding the text with asterisks:

For example:

```kramdown
I like *my* coffee **bold**.
```

yields:

I like *my* coffee **bold**.

### Links

**Simple Links**

A simple link can be created by surrounding the text with square brackets and the link URL with parentheses:

```kramdown
This is a [link](http://www.rhino3d.com) to the Rhino 3D homepage.
```

yields:

This is a [link](http://www.rhino3d.com) to the Rhino 3D homepage.

You can also add title information to the link:

```kramdown
A [link](http://www.rhino3d.com "Rhino 3D homepage") to the homepage.
```

yields:

A [link](http://www.rhino3d.com "Rhino 3D homepage") to the homepage.

There is another way to create links which does not interrupt the text flow. The URL and title are defined using a reference name and this reference name is then used in square brackets instead of the link URL:

```kramdown
A [link][rhino3d homepage] to the homepage.

[rhino3d homepage]: http://www.rhino3d.com "Modeling tools for designers"
```

yields:

A [link][Rhino3D homepage] to the homepage.

[Rhino3D homepage]: http://www.rhino3d.com "Modeling tools for designers"

If the link text itself is the reference name, the second set of square brackets can be omitted:

```kramdown
A link to the [Rhino3D homepage].

[Rhino3D homepage]: http://www.rhino3d.com "Modeling tools for designers"
```

yields:

A link to the [Rhino3D homepage].


**Anchor Links**

As discussed above, [Headers](#headers) and [Sub Headers](#sub-headers) automatically create anchors in the resulting rendered html output.

You can link to any anchor within a page using the hash `#` symbol in a normal link.  For example:

```kramdown
[Sub Headers](#sub-headers) automatically create anchors in the resulting rendered html output
```

yields the sentence fragment shown above.

To create new anchors within the site, you can use html inline.  For example:

```html
<a id="top"></a>
```

was added to the [top of this page](#top).

**Internal Links**

If you're linking to another part of the Devloper Docs then make sure you use the `{% raw %}{% endraw %}` tag. For example:

```kramdown
[Guides]({% raw %}{% endraw %}/guides/)
```

### Images

Images can be created in a similar way to links: just use an exclamation mark before the square brackets. The link text will become the alternative text of the image and the link URL specifies the image source:

```kramdown
![pluginlogo](/images/rhinodevlogo148x128.png)
```

yields:

![pluginlogo](/images/rhinodevlogo148x128.png)

**Note**: Use the `site.baseurl` macro.  See the source of this page for this section for an example.

### Inline Code

Text phrases can be easily marked up as code by surrounding them with back-ticks:

```kramdown
To write a line to the command line use the `Rhino.RhinoApp.WriteLine` method.
```

yields:

To write a line to the command line use the `Rhino.RhinoApp.WriteLine` method.

**Footnotes**

Footnotes can easily be used in Kramdown. Just set a footnote marker (consists of square brackets with a caret and the footnote name inside) in the text and somewhere else the footnote definition (which basically looks like a reference link definition):

```kramdown
This is a text with a footnote[^1].

[^1]: This is an example of a footnote.
```

yields:

This is a text with a footnote[^1].

### Abbreviations

Abbreviations will work once you add an abbreviation definition.  So you can just write the text and add the definitions later on.  For example:

```kramdown
For optimal code reuse, use the MVC paradigm.

*[MVC]: Model View Controller
```

yields:

For optimal code reuse, use the MVC paradigm.

*[MVC]: Model View Controller

Abbreviations are case-sensitive.

### MathJax & LaTeX

Kramdown has support for LaTeX to PNG rendering via [MathJax](http://www.mathjax.org/).  

For example:

```LaTeX
{{< mathjax >}}$$y = {\sqrt{x^2+(x-1)} \over x-3} + \left| 2x \over x^{0.5x} \right|$${{< /mathjax >}}
```

yields:

{{< mathjax >}}$$y = {\sqrt{x^2+(x-1)} \over x-3} + \left| 2x \over x^{0.5x} \right|$${{< /mathjax >}}

See the [MathJax basic tutorial and quick reference on StackExchange](http://meta.math.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference).

### Video Player embed

Use the includes codes to quickly include an embedded player for Vimeo or Youtube.

The Id code is the ID of the video to embed from Youtube or Vimeo. Ignore the "\\" escape characters.

Youtube code:

```kramdown
\{\% include youtube_player.html id=\"8BNyMC4EBcw\" \%\}
```

Vimeo code:

```kramdown
\{\% include vimeo_player.html id=\"8BNyMC4EBcw\" \%\}
```

## Related topics

- [How This Site Works](/guides/general/how-this-site-works/)
- [Kramdown Quick Reference](http://kramdown.gettalong.org/quickref.html)

**Footnotes**

[^1]: This is an example of a footnote.
