---
layout: toc-page
title: Rhino Developer Docs Style Guide
author: dan@mcneel.com
categories: ['General']
platforms: ['Mac', 'Windows']
apis: ['DevDocs', 'Jekyll', 'Liquid']
languages: ['Markdown']
keywords: ['style', 'guide']
TODO: 1
origin: unset
order: 3
---

# Rhino Developer Docs Style Guide
---

This is a sample page that serves as a quick reference for the syntax and structure of Rhino Developer Documentation content.  Below are examples of nearly all the available syntax using Markdown, Kramdown (a superset of Markdown), the table-of-contents UI widget, etc.

---

## Conventions
{: .toc-header }

Division of content:

`# Title` become H1 headers and are reserved for the title of the page only.

`## Header` become H2 headers and are reserved for major sections within the page.

`#### Sub Header` become H4 headers and are reserved for sub-sections within a major section.

Fonts:
TODO: Note on Segou UI on Windows, Helvetica on Mac

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

The UI-widget to the left of this paragraph is a the Table of Contents (TOC) for this page.  If you are authoring a page that requires a TOC, you can generate one automatically by using a TOC-enabled template (see Authoring Content for more information).  To get a TOC-enabled template to generate the TOC, you simply have to add the correct class decorations underneath the Headers and Sub Headers.

For example, to get a Header to show up in the TOC, you would type this:

```yaml
## Cool Header
{: .toc-header }
```

To get a Sub Header to show up in the TOC, you would type this:

```yaml
#### Sweet Sub Header
{: .toc-subheader }
```

**NOTE**: TOCs are only generated from **H2** and **H4** headers (.toc-header and .toc-subheader respectively).

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

The abbreviation after the first set of back-ticks is teh language code for syntax highlighting.  We are using a syntax highlighting plugin called highlight.js.  [Many languages](https://highlightjs.org/download/) are supported.  The most common language abbreviations used on this site are:

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

## Text Modifiers
{: .toc-header }

---

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
TODO
```

**Anchor Links**



---

#### Images
{: .toc-subheader }


---

#### Inline Code
{: .toc-subheader }


---

#### Footnotes
{: .toc-subheader }


---

#### Abbreviations
{: .toc-subheader }


---

#### HTML Elements
{: .toc-subheader }


---

#### Inline Attributes
{: .toc-subheader }
