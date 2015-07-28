---
layout: toc-guide-page
title: Style Guide
author: dan@mcneel.com
categories: ['General']
platforms: ['Mac', 'Windows']
apis: ['Developer Docs', 'Jekyll', 'Liquid']
languages: ['Markdown']
keywords: ['style', 'guide']
TODO: 0
origin: unset
order: 3
---

<a id="top"></a> <!-- this is just a sample anchor -->

# Style Guide
{: .toc-title }

---

This is a sample page that serves as a quick reference for the syntax and structure of Rhino Developer Documentation content.  Below are examples of nearly all the available syntax using Markdown, Kramdown (a superset of Markdown), the table-of-contents UI widget, etc.

Some portions of this page were adapted from the [Kramdown Quick Reference](http://kramdown.gettalong.org/quickref.html).

---

## Conventions
{: .toc-header }

#### Division of content
{: .toc-subheader }

`# Title` become H1 headers and are reserved for the title of the page only.

`## Header` become H2 headers and are reserved for major sections within the page.

`#### Sub Header` become H4 headers and are reserved for sub-sections within a major section.

#### Fonts
{: .toc-subheader }

On Windows, this site attempts to use Segoe UI (font size: 16 px, font weight: 400,  line height: 1.6) and falls back to Frutiger Linotype, Dejavu Sans, Helvetica Neue, Helvetica, Arial, in that order.  On Mac OS X, the site will (almost) certainly use Helvetica Neue or Helvetica (font size: 16 px, font weight: 300,  line height: 1.6).  The operating system-specific font weight is set in the footer using javascript.

#### Paths & Filenames
{: .toc-subheader }

`*Italics*` are used to denote filenames, paths, and file extensions.  For example:

Navigate to *C:\Program Files\Rhinoceros 5 (64-bit)\Plug-ins*.

#### Bold in Instructions
{: .toc-subheader }

`**Bold**` (strong emphasis) is used in instructions to highlight keywords for the individual instruction.  It is frequently used to hightlight the **verb** and/or the **object** of a sentence.  For example:

1. Click the **OK** button to accept your changes.

---

## Headers
{: .toc-header }

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

---

#### Sub Headers
{: .toc-subheader }

Sub Headers demarcate sub-sections a major section underneath a header.

Sub Headers are created like this:

```yaml
#### Sub Header
```

The example above is an H4 header, which we are calling a "Sub Header."

Just like with H2 headers, H4 headers also create an #anchor tag in the generated html.

---

## Table of Contents
{: .toc-header }

The UI-widget to the left of this column is a the Table of Contents (TOC) for this page.  If you are authoring a page that requires a TOC, you can generate one automatically by using a TOC-enabled layouts (see [How This Site Works]({{ site.baseurl }}/guides/rhinodevdocs/how_this_site_works/) for more information).  To get a TOC-enabled template to generate the TOC, you simply have to add the correct class decorations underneath the Headers and Sub Headers.

For example, to get the main title to show up in the TOC, you would type this:

```yaml
# The Title
{: .toc-title }
```

To get a Header to show up in the TOC, you would type this:

```yaml
## Cool Header
{: .toc-header }
```

To get a Sub Header to show up in the TOC, you would type this:

```yaml
#### Sweet Sub Header
{: .toc-subheader }
```

**NOTE**: TOCs are only generated from **H1**, **H2**, and **H4** headers (`.toc-title`, `.toc-header`, and `.toc-subheader` respectively).

---

## Structural Elements
{: .toc-header }

---

#### Paragraphs
{: .toc-subheader }

Consecutive lines of text are considered to be one paragraph. You must add a blank line between paragraphs.

---

#### Block Quotes
{: .toc-subheader }

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

---

#### Code Blocks
{: .toc-subheader }

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
- `vbnet` is VB.NET
- `python` is Python
- `c++` is C/C++

---

#### Horizontal Rules
{: .toc-subheader }

Horizontal rules (lines) are created by using three dashes:

```kramdown
---
```

You can an example of one of these right here...

---

#### Lists
{: .toc-subheader }

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

---

#### Tables
{: .toc-subheader }

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
{: rules="groups"}
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
{: rules="groups"}

---

#### HTML Elements
{: .toc-subheader }

Kramdown allows you to use block-level HTML tags (`div`, `p`, `pre`, etc) to markup whole blocks of text – just start a line with a block-level HTML tag. Kramdown syntax is normally not processed inside an HTML tag but this can be changed with the `parse_block_html` option. If this options is set to true, then the content of a block-level HTML tag is parsed by Kramdown either as block level or span-level text, depending on the tag.

Here is an example of using HTML elements:

```html
<div style="float: right">
Something that stays right and is not wrapped in a para.
</div>

{::options parse_block_html="true" /}

<div>
This is wrapped in a para.
</div>
<p>
This can contain only *span* level elements.
</p>
```

yields:

<div style="float: right">
Something that stays right and is not wrapped in a para.
</div>

{::options parse_block_html="true" /}

<div>
This is wrapped in a para.
</div>
<p>
This can contain only *span* level elements.
</p>

---

#### Block Attributes
{: .toc-subheader }

You can assign any attribute to a block-level element. Just directly follow the block with a *block inline attribute list* (or short: block IAL). A block IAL consists of a left curly brace, followed by a colon, the attribute definitions and a right curly brace.

Here is a simple example which sets the title attribute of a block quote:

```kramdown
> A nice blockquote
{: title="Blockquote title"}
```

yields:

> A nice blockquote
{: title="Blockquote title"}

Block attributes are used to generate the [classes for the TOC](#table-of-contents).

---

#### Warnings
{: .toc-subheader }

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


---

## Text Modifiers
{: .toc-header }


#### Emphasis
{: .toc-subheader }

Emphasis (bold and italic) can be added to text by surrounding the text with asterisks:

For example:

```kramdown
I like *my* coffee **bold**.
```

yields:

I like *my* coffee **bold**.

---

#### Links
{: .toc-subheader }

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

---

#### Images
{: .toc-subheader }

Images can be created in a similar way to links: just use an exclamation mark before the square brackets. The link text will become the alternative text of the image and the link URL specifies the image source:

```kramdown
![pluginlogo]({{ site.baseurl }}/images/rhinocommonlogo256x256.png)
```

yields:

![pluginlogo]({{ site.baseurl }}/images/rhinocommonlogo256x256.png)

**NOTE**: Use the `site.baseurl` macro.  See the source of this page for this section for an example.

---

#### Inline Code
{: .toc-subheader }

Text phrases can be easily marked up as code by surrounding them with back-ticks:

```kramdown
To write a line to the command line use the `Rhino.RhinoApp.WriteLine` method.
```

yields:

To write a line to the command line use the `Rhino.RhinoApp.WriteLine` method.

---

#### Footnotes
{: .toc-subheader }

Footnotes can easily be used in Kramdown. Just set a footnote marker (consists of square brackets with a caret and the footnote name inside) in the text and somewhere else the footnote definition (which basically looks like a reference link definition):

```kramdown
This is a text with a footnote[^1].

[^1]: This is an example of a footnote.
```

yields:

This is a text with a footnote[^1].

[^1]: This is an example of a footnote.

---

#### Abbreviations
{: .toc-subheader }

Abbreviations will work once you add an abbreviation definition.  So you can just write the text and add the definitions later on.  For example:

```kramdown
For optimal code reuse, use the MVC paradigm.

*[MVC]: Model View Controller
```

yields:

For optimal code reuse, use the MVC paradigm.

*[MVC]: Model View Controller

Abbreviations are case-sensitive.

---

#### HTML Elements
{: .toc-subheader }

HTML is not only supported on the block-level but also on the span-level:

```html
This is <span style="color: red">written in red</span>.
```

yields:

This is <span style="color: red">written in red</span>.

---

#### Inline Attributes
{: .toc-subheader }

As with a block-level element you can assign any attribute to a span-level elements using a *span inline attribute list* (or short: span IAL). A span IAL has the same syntax as a block IAL and must immediately follow the span-level element:

```html
This is *red*{: style="color: red"}.
```

yields:

This is *red*{: style="color: red"}.

---

#### MathJax & LaTeX
{: .toc-subheader }

Kramdown has support for LaTeX to PNG rendering via [MathJax](http://www.mathjax.org/).  

For example:

```LaTeX
$$y = {\sqrt{x^2+(x-1)} \over x-3} + \left| 2x \over x^{0.5x} \right|$$
```

yields:

$$y = {\sqrt{x^2+(x-1)} \over x-3} + \left| 2x \over x^{0.5x} \right|$$

---

## Related topics
{: .toc-header }

- [How This Site Works]({{ site.baseurl }}/guides/rhinodevdocs/how_this_site_works/)
- [Kramdown Quick Reference](http://kramdown.gettalong.org/quickref.html)

---

## Footnotes
{: .toc-header }
