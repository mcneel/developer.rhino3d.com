+++
aliases = ["/5/guides/general/developer-docs-style-guide/", "/6/guides/general/developer-docs-style-guide/", "/7/guides/general/developer-docs-style-guide/", "/wip/guides/general/developer-docs-style-guide/"]
authors = [ "dan" ]
categories = [ "This Site" ]
description = "This guide serves as an example and quick reference for the syntax and structure of this site."
keywords = [ "style", "guide" ]
languages = [ "Markdown", "toml" ]
sdk = [ "General" ]
title = "Developer Docs Style Guide"
type = "guides"
weight = 8

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

Below are examples of nearly all the available syntax using Markdown, the table-of-contents UI widget, etc.

## Conventions

### Site file naming

The naming convention for files - guides, samples, etc - is lowercase with `-` used as spaces.  This leads to more consistent and legible URLs.  In addition, Google recommends one construct compound URL names with `-` and not underbars (`_`).  For example, consider the name of this guide: "Style Guide".  The file name for this guide is `developer-docs-style-guide`.  Google treats a hyphen as a word separator, but does not treat an underscore that way.  Google treats and underscore as a word joiner — so "red_sneakers" is the same as "redsneakers."

In general, when considering new file names for *guides*, please imagine you are saying "Guide to _____".  This often leads to verbs ending in "-ing", the progressive or continuous verb tense.  Obviously, this is not a hard-and-fast rule, but rather a convention.

In general, when considering new file names for *samples*, please imagine you are saying "_____ sample".  As with guides, this is not a hard-and-fast rule, but rather a general convention.

### Division of content

`# Title` become H1 headers and are reserved for the title of the page only.

`## Header` become H2 headers and are reserved for major sections within the page.

`### Sub Header` become H3 headers and are reserved for sub-sections within a major section.

### Fonts

{{< call-out bug "OUT OF DATE" >}}
This fonts section needs to be updated.
{{< /call-out >}}

On Windows, this site attempts to use Segoe UI (font size: 16 px, font weight: 400,  line height: 1.6) and falls back to Frutiger Linotype, Dejavu Sans, Helvetica Neue, Helvetica, Arial, in that order.  On macOS, the site will (almost) certainly use Helvetica Neue or Helvetica (font size: 16 px, font weight: 300,  line height: 1.6).  The operating system-specific font weight is set in the footer using javascript.

### Paths & Filenames

`*Italics*` are used to denote filenames, paths, and file extensions.  For example:

Navigate to *C:\Program Files\Rhinoceros 5 (64-bit)\Plug-ins*.

### Bold

`**Bold**` (strong emphasis) is used in instructions to highlight critical instructions that are very important.  Bold should be **used sparingly** as it is often present in headers as natural division of content.

### Spelling & Case

The following spelling and case conventions are adopted on this site:

* "Plugins" is not hyphenated unless it refers to a place in the Rhino UI where it is hyphenated.
* "openNURBS" (not OpenNURBS, nor opennurbs, nor oPeNnURBs) unless it refers to a namespace in code where it is capitalized, or a path where it is not.

### Images & Screenshots

Please use image names without spaces (use a hypen - NOT an underscore - for word separation).  It is also safest to use lowercase filenames and extensions.

When feasible, it is best to use the _.svg_ vector format for images, especially for diagrams.

When using bitmap images, the preferred format is _.png_, but any browser-friendly bitmap format will work.

When capturing screenshots, consider that many people have high-DPI (aka: "Retina") displays.  Please capture all screenshots on a high-DPI display.

See the [Text Modifiers > Images section](#images) of this guide for more information on inserting images.

## Headers

Headers demarcate major sections of the page, guide, etc.

Headers are created like this:

```markdown
## Headers
```

The example above is an H2 header.

Creating a header automatically creates an #anchor tag in the generated html.

For headers with multiple words, the markdown parser lowercases all the words, removes non-alphanumeric characters and adds dashes for spaces. For example, if we had a header like this:

```markdown
## This Is My Header
```

the resulting html anchor tag would be:

```markdown
#this-is-my-header
```

Read more about anchors [here](#heading-anchors).

### Sub Headers

Sub Headers demarcate sub-sections a major section underneath a header.

Sub Headers are created like this:

```markdown
### Sub Header
```

The example above is an H3 header, which we are calling a "Sub Header."

Just like with H2 headers, H3 headers also create an #anchor tag in the generated html.

### Heading Anchors

Anchors are auto generated from heading texts. They're formatted to be URL safe. In cases that it's really needed, an additional anchor tag can be specified.

#### Formatting

In the process of sanitizing the heading text to generate anchors, all characters will be lowercased. Spaces will be replaced by `-` and special character will be removed.

For example a heading reading:

```toml
### This & That
```

becomes:

```toml
#this--that
```

{{< call-out hint "Headings With Same Text" >}}
In pages that contain headings with idential text, the heading ID for the first occurance will be generated as normal. Next occurances of the same heading will have a numeric suffix like `-1`, `-2` and so on.
{{< /call-out >}}

#### Optional Explicit Anchors

Optionally, an additional anchor with explicit ID can be specified using [anchor shortcode](#anchor) (does not replace auto generated heading anchors). This can be useful for making sure lagacy links to headings work when migrating from another existing system to Hugo.

For example below heading in markdown:

```toml
### Heading Text {id="custom_anchor"}
```

Will generate two anchors:

```toml
#heading-text
```

and

```toml
#custom_anchor
```

## Table of Contents

The UI-widget to the left of this column is a the Table of Contents (TOC) for this page.  If you are authoring a page that requires a TOC, you can generate one automatically by toggling the `toc = true` frontmatter field (see [How This Site Works](/guides/general/how-this-site-works/#page-options) for more information).

{{< call-out "Note" "H2 and H3">}}
TOCs are only generated from *H2* and *H3* headers...*H4* (and smaller) headers are ignored by the TOC-enabled templates.
{{< /call-out >}}

For example, to get a Header to show up in the TOC, you would type this:

```markdown
## Cool Header
```

To get a Sub Header to show up in the TOC, you would type this:

```markdown
### Sweet Sub Header
```

## Structural Elements

### Paragraphs

Consecutive lines of text are considered to be one paragraph. You must add a blank line between paragraphs.

### Block Quotes

A blockquote is started using the > marker followed by an optional space; all following lines that are also started with the blockquote marker belong to the blockquote. You can use any block-level elements inside a blockquote:

```markdown
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

```markdown
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

```markdown
---
```

You can an example of one of these right here...

### Lists

You can create ordered lists and unordered lists.

**Ordered Lists**

Ordered lists are created by typing `1.` at the start of a line, like this:

```markdown
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

```markdown
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

```markdown
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

Markdown supports a syntax for creating simple tables. A line starting with a pipe character starts a table row. However, if the pipe characters is immediately followed by a dash (-), a separator line is created. Separator lines are used to split the table header from the table body (and optionally align the table columns) and to split the table body into multiple parts. If the pipe character is followed by an equal sign (=), the tables rows below it are part of the table footer.

Here is the syntax for a simple table:

```markdown
| A simple | table |
| with multiple | lines|
```

yields:

| A simple | table |
| with multiple | lines|

More complex tables can be added like this:

```markdown
| Header1 | Header2 | Header3 |
|:--------|:-------:|--------:|
| cell1   | cell2   | cell3   |
| cell4   | cell5   | cell6   |
| cell1   | cell2   | cell3   |
| cell4   | cell5   | cell6   |
| Foot1   | Foot2   | Foot3   |

```

yields:

| Header1 | Header2 | Header3 |
|:--------|:-------:|--------:|
| cell1   | cell2   | cell3   |
| cell4   | cell5   | cell6   |
| cell1   | cell2   | cell3   |
| cell4   | cell5   | cell6   |
| Foot1   | Foot2   | Foot3   |

## Text Modifiers

### Emphasis

Emphasis (bold and italic) can be added to text by surrounding the text with asterisks:

For example:

```markdown
I like *my* coffee **bold**.
```

yields:

I like *my* coffee **bold**.

### Links

**Simple Links**

A simple link can be created by surrounding the text with square brackets and the link URL with parentheses:

```markdown
This is a [link](http://www.rhino3d.com) to the Rhino 3D homepage.
```

yields:

This is a [link](http://www.rhino3d.com) to the Rhino 3D homepage.

You can also add title information to the link:

```markdown
A [link](http://www.rhino3d.com "Rhino 3D homepage") to the homepage.
```

yields:

A [link](http://www.rhino3d.com "Rhino 3D homepage") to the homepage.

There is another way to create links which does not interrupt the text flow. The URL and title are defined using a reference name and this reference name is then used in square brackets instead of the link URL:

```markdown
A [link][rhino3d homepage] to the homepage.

[rhino3d homepage]: http://www.rhino3d.com "Modeling tools for designers"
```

yields:

A [link][Rhino3D homepage] to the homepage.

[Rhino3D homepage]: http://www.rhino3d.com "Modeling tools for designers"

If the link text itself is the reference name, the second set of square brackets can be omitted:

```markdown
A link to the [Rhino3D homepage].

[Rhino3D homepage]: http://www.rhino3d.com "Modeling tools for designers"
```

yields:

A link to the [Rhino3D homepage].

**Anchor Links**

As discussed above, [Headers](#headers) and [Sub Headers](#sub-headers) automatically create anchors in the resulting rendered html output.

You can link to any anchor within a page using the hash `#` symbol in a normal link.  For example:

```markdown
[Sub Headers](#sub-headers) automatically create anchors in the resulting rendered html output
```

yields the sentence fragment shown above.

To create new anchors within the site, you can use html inline.  For example:

```html
<a id="top"></a>
```

was added to the [top of this page](#top).

### Images

Images can be created in a similar way to links: just use an exclamation mark before the square brackets. The link text will become the alternative text of the image and the link URL specifies the image source:

```markdown
![pluginlogo](/images/rhinodevlogo148x128.png)
```

yields:

![pluginlogo](/images/rhinodevlogo148x128.png)

### Inline Code

Text phrases can be easily marked up as code by surrounding them with back-ticks:

```markdown
To write a line to the command line use the `Rhino.RhinoApp.WriteLine` method.
```

yields:

To write a line to the command line use the `Rhino.RhinoApp.WriteLine` method.

**Footnotes**

Footnotes can easily be used in Markdown. Just set a footnote marker (consists of square brackets with a caret and the footnote name inside) in the text and somewhere else the footnote definition (which basically looks like a reference link definition):

```markdown
This is a text with a footnote[^1].

[^1]: This is an example of a footnote.
```

yields:

This is a text with a footnote[^1].

### MathJax & LaTeX

Markdown has support for LaTeX to PNG rendering via [MathJax](http://www.mathjax.org/).  

For example:

```LaTeX
{{< mathjax >}}$$y = {\sqrt{x^2+(x-1)} \over x-3} + \left| 2x \over x^{0.5x} \right|$${{< /mathjax >}}
```

yields:

{{< mathjax >}}$$y = {\sqrt{x^2+(x-1)} \over x-3} + \left| 2x \over x^{0.5x} \right|$${{< /mathjax >}}

See the [MathJax basic tutorial and quick reference on StackExchange](http://meta.math.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference).

## Shortcodes

[Shortcodes are Hugo's way](https://gohugo.io/content-management/shortcodes/) of inserting a html into your content that generate some special type of formatted output.  Hugo comes with some built-in shortcodes for things like inserting [Vimeo](https://gohugo.io/content-management/shortcodes/#vimeo) or [YouTube](https://gohugo.io/content-management/shortcodes/#vimeo) videos, [Instagram](https://gohugo.io/content-management/shortcodes/#instagram) or [Twitter](https://gohugo.io/content-management/shortcodes/#twitter) posts, etc. but we can author our own shortcodes to suit our needs.  

{{< call-out warning "Common Shortcode Mistakes" >}}

* Shortcodes are very picky about formatting: even the slightest missing brace can cause the site not to deploy.  Don't worry, you won't break the site, you just won't see your change go live until it is fixed.
* Shortcodes only work when used in the content of a post, not in the frontmatter. You may be tempted to use them in the frontmatter, but they don't work there.
* If you are referencing images, pease make sure to only use files with lowercase names and NO SPACES!

{{< /call-out >}}

So far, we've got the following shortcodes of our own:
  
### 3dm

Use the `3dm` shortcode to embed a 3D view of a 3dm file to a page.

```
{{</* 3dm path="path_to_file.3dm" camera=`{"x":0,"y":50,"z":50}` width="80%" height="400px" */>}}
```

yields:

{{< 3dm path="key.3dm" camera=`{"x":0,"y":50,"z":50}` width="80%" height="400px" >}}

and

```
{{</* 3dm path="path_to_file.3dm" width="80%" height="400px" background="transparent" settings=`{"controls":false, "camera":{"type":"orthographic", "zoom":8}}` animation=`{"frames":[{"title":"perspective","camera":{"x":10,"y":-30,"z":10},"layers":"*"},{"title":"right","camera":{"x":0,"y":40,"z":5},"layers":"*"},{"title":"front","camera":{"x":40,"y":0,"z":5},"layers":"*"}]}` */>}}
```

yields:

{{< 3dm path="logo.3dm" width="80%" height="400px" background="transparent" settings=`{"controls":false, "camera":{"type":"orthographic", "zoom":8}}` animation=`{"frames":[{"title":"perspective","camera":{"x":10,"y":-30,"z":10},"layers":"*"},{"title":"right","camera":{"x":0,"y":40,"z":5},"layers":"*"},{"title":"front","camera":{"x":40,"y":0,"z":5},"layers":"*"}]}` >}}

#### Required Arguments:

* `path`: *string*. Path to the 3dm file, for example file residing in the same folder as .md content file could be renference as `path="example.3dm"`.
* `width`: *String*. Pixel or Percentage value for width of the element.
* `height`: *String*. Pixel or Percentage value for height of the element.

#### Optional Arguments:

* `camera`: *JSON*. XYZ Position of the camera. Example: `` camera=`{"x":0,"y":50,"z":50}` ``
* `background`: *String*. Background color of the viewer. Example: `background="transparent"`
* `title`: *String*. Text overlay at the bottom of the element.
* `text_color`: *String*. Text color of the title. Example: `text_color="red"`
* `settings`: *JSON*. General settings for the viewer. Example: `` settings=`{"controls":false, "camera":{"type":"orthographic", "fov":50, "zoom":8}}` ``
* `animation`: *JSON*. Flip trhough set of predefined cameras, titles (TODO: and layers). Has two sub-objects; `settings` and `frames`. Example: `` animation=`{"settings":{"repeat":1, "eachDelay":2, "eachDuration":2}, "frames":[{"title":"left","camera":{"x":10,"y":-30,"z":10},"layers":"*"},{"title":"right","camera":{"x":0,"y":40,"z":5},"layers":"*"},{"title":"front","camera":{"x":40,"y":0,"z":5},"layers":"*"}]}` ``

### Anchor

Creates an empty div with the specified ID and can be used as an #anchor anywhere in the page:

`{{</* anchor "custom_anchor" */>}}`

{{< anchor "custom_anchor" >}}

produces an empty div above this line, and can be referenced with a link [#custom_anchor](#custom_anchor)

### Awesome (Font Awesome)

[{{< awesome fab fa-font-awesome-flag>}} Font Awesome](https://fontawesome.com/icons?d=gallery) provides a huge library of vector [icons](https://fontawesome.com/icons?d=gallery) that area easy to use with this sortcode:

`{{</* awesome fas fa-check small */>}}` produces: {{< awesome fas fa-check small >}}

You can also specify a size and a color like this:

`{{</* awesome id="fab fa-windows" size="small" color="#49abe9" */>}}` produces: {{< awesome id="fab fa-windows" size="small" color="#49abe9">}}

### BeforeAfter

You can create image-based before-and-after comparisons with the following shortcode:

```
{{</* beforeafter "/images/before.png" "/images/after.png" */>}}
```

produces:

{{< beforeafter "https://www.rhino3d.com/features/quadremesh/before.png" "https://www.rhino3d.com/features/quadremesh/after.png" >}}

You can also supply optional captions for the left and right images like this:

```
{{</* beforeafter "/images/before.png" "/images/after.png" "This text at left" "This text at right" */>}}
```

This shortcode uses the [twentytwenty](https://github.com/zurb/twentytwenty) jQuery widget.

### Call-Out

To call attention to a specific area of content on the page, use the call-out shortcode.

For example:

```
{{</* call-out danger "Here Be Dragons" */>}}
Don't click that button man...it's dangerous dude.
{{</* /call-out */>}}
```

produces:

{{< call-out danger "Here Be Dragons" >}}
Don't click that button man...it's dangerous dude.
{{< /call-out >}}

The following arguments can be passed to the shortcode to determine the type:
- {{< awesome "fas fa-pencil-alt fa-fw" >}} `note`
- {{< awesome "fas fa-list-ul fa-fw" >}} `abstract`
- {{< awesome "fas fa-info-circle fa-fw" >}} `info`
- {{< awesome "fas fa-lightbulb fa-fw" >}} `tip`
- {{< awesome "fas fa-check-circle fa-fw" >}} `success`
- {{< awesome "fas fa-question-circle fa-fw" >}} `question`
- {{< awesome "fas fa-exclamation-triangle fa-fw" >}} `warning`
- {{< awesome "fas fa-times-circle fa-fw" >}} `failure`
- {{< awesome "fas fa-skull-crossbones fa-fw" >}} `danger`
- {{< awesome "fas fa-bug fa-fw" >}} `bug`
- {{< awesome "fas fa-list-ol fa-fw" >}} `example`
- {{< awesome "fas fa-quote-right fa-fw" >}} `quote`


### Align

```
{{</* align left */>}}Left Wing{{</* /align */>}}
{{</* align center */>}}Centrist{{</* /align */>}}
{{</* align right */>}}Right Wing{{</* /align */>}}
```

produces

{{< align left >}}Left Wing{{< /align >}}
{{< align center >}}Centrist{{< /align >}}
{{< align right >}}Right Wing{{< /align >}}


### Center

Use the `center` shortcode to center images, text, etc. in the `div`.

For example:
```
{{</* center */>}}
This text is centered
{{</* /center */>}}
```

produces:

{{< center >}}
This text is centered
{{< /center >}}

You can center images too using the `image` argument like this:

```
{{</* center image */>}}
![This image is centered](logo.png)
{{</* /center */>}}
```

produces

{{< center image >}}
![This image is centered](logo.png)
{{< /center >}}

### Figure

Use the `figure` shortcode to insert images with captions like this:

```
{{</* figure src="/images/light-falloff-after.png" caption="Lights have a falloff value that can be set to inverse squared which mimics how light fades with distance." */>}}
```

produces:

{{< figure src="/images/light-falloff-after.png" caption="Lights have a falloff value that can be set to inverse squared which mimics how light fades with distance." >}}

Optionally, you can also use the [gallery](#gallery) and [load-photoswipe](#load-photoswipe) shortcodes to embed figures in a gallery and pop-up an image overlay when users click or tap on the image.

### Image (shortcode)

There is a basic `image` shortcode for doing simple sizing (this is an html resizing, not an actual image process - see `imgproc` below)...

Here is an example that changes the width of an image
```
{{</* image url="logo.png" width="250px" */>}}
```

produces

{{< image url="logo.png" width="250px" >}}

### Image Processing (imgproc)

Hugo comes with [a number of useful image processing routines like resizing and cropping](https://gohugo.io/content-management/image-processing/).  It's important to understand that these are not just css styles, but actual processes the generate entirely new derivative files based on the image you use as your input.  This is especially useful for generating thumbnails from large images so that a smaller (in kb) image is delivered in those situations where a larger one would cause slow pageloads.  Think of these image processing routines as the equivalent of opening up your file in a program like Photoshop and performing resizing, format, or cropping operations on them.

{{< call-out info "This only works on page-bundle images" >}}
Currently, this shortcode only works on page-bundle images and not on images in the static folder (the main images folder).  You will have to use GitHub to upload these into the proper spot.
{{< /call-out >}}

To use the Image Processing routines on the page, use the `imgproc` shortcode.

Here is an example that resizes an image:
```
{{</* imgproc "logo.png" "Resize" "48x48" */>}}
```

Make sure you close the final brace (not shown above, unfortunately) with a forward slash `/` like this...
```
/>}}
```

produces

{{< imgproc "logo.png" "Resize" "48x48" />}}

### Latest Rhino Version

Avoid writing the latest Rhino version in text.  Instead, the site itself knows which is the current shipping version.  So use the following shortcode:

`{{</* latest-rhino-version */>}}` produces {{< latest-rhino-version >}}

#### Standard size:

`{{</* new-label 6 */>}}` produces: {{< new-label 6 >}}

#### Small size:

`An inline {{</* new-label 6 small */>}} small new label` produces: 

An inline {{< new-label 6 small >}} small new label. There's a bug here that causes a line-wrap in the middle. Brian doesn't know how to fix it.

#### Bullet in list:

```  
  * {{</* new-label 6 bullet */>}} Feature description
  * A feature from a previous version
  * {{</* new-label 7 bullet */>}} A feature from a previous version
``` 

produces: 

  * {{< new-label 6 bullet >}} Feature description
  * A feature from a previous version
  * {{< new-label 7 bullet >}} A feature from a previous version


### Open Rhino

To open URL in Rhino, use the:

```
{{</* open-rhino 
    "https://docs.mcneel.com/rhino/6/training-command/en-us/samples/Clip.3dm"
    "Open Clip.3dm in Rhino"
     /*/>}}
```

to produce:

{{< open-rhino 
  "https://docs.mcneel.com/rhino/6/training-command/en-us/samples/Clip.3dm" 
  "Open Clip.3dm in Rhino" 
/>}}

To open Rhino by clicking an image:

```
{{</* open-rhino "https://docs.mcneel.com/rhino/6/training-command/en-us/samples/Clip.3dm" */>}}
![computelogo](/images/rhino_compute_logo.png)
{{</* /open-rhino */>}}
```

{{< open-rhino "https://docs.mcneel.com/rhino/6/training-command/en-us/samples/Clip.3dm" >}}
![computelogo](/images/rhino_compute_logo.png)
{{< /open-rhino >}}

### Row and Column

Use the `{{</* row */>}}` and `{{</* column */>}}` shortcodes together to create responsive flow layouts like this:

```
{{</* row */>}}
{{</* column */>}}
Row 1: Column 1
{{</* /column */>}}
{{</* column */>}}
Row 1: Column 2
{{</* /column */>}}
{{</* column */>}}
Row 1: Column 3
{{</* /column */>}}
{{</* /row */>}}
{{</* row */>}}
{{</* column */>}}
Row 2: Column 1
{{</* /column */>}}
{{</* column */>}}
Row 2: Column 2
{{</* /column */>}}
{{</* column */>}}
Row 2: Column 3
{{</* /column */>}}
{{</* /row */>}}
{{</* row */>}}
{{</* column */>}}
Row 3: Column 1
{{</* /column */>}}
{{</* column */>}}
Row 3: Column 2
{{</* /column */>}}
{{</* column */>}}
Row 3: Column 3
{{</* /column */>}}
{{</* /row */>}}
```

produces:

{{< row >}}

{{< column >}}
Row 1: Column 1
{{< /column >}}

{{< column >}}
Row 1: Column 2
{{< /column >}}

{{< column >}}
Row 1: Column 3
{{< /column >}}

{{< /row >}}

{{< row >}}

{{< column >}}
Row 2: Column 1
{{< /column >}}

{{< column >}}
Row 2: Column 2
{{< /column >}}

{{< column >}}
Row 2: Column 3
{{< /column >}}

{{< /row >}}

{{< row >}}

{{< column >}}
Row 3: Column 1
{{< /column >}}

{{< column >}}
Row 3: Column 2
{{< /column >}}

{{< column >}}
Row 3: Column 3
{{< /column >}}

{{< /row >}}

### Vimeo and YouTube Videos

#### Vimeo

We have extended [the built-in vimeo shortcode](https://gohugo.io/content-management/shortcodes/#vimeo) to support Autoplay and looping...

For example:

```
{{</* vimeo id="447325407" autoplay="1" loop="1" autopause="0" */>}}
```

produces:

{{< vimeo id="447325407" autoplay="1" loop="1" autopause="0" >}}

#### YouTube

Hugo has a [built-in youtube shortcode](https://gohugo.io/content-management/shortcodes/#youtube) that can be used to embed videos like this:

```
{{</* youtube TeTiZuSbQz8 */>}}
```

produces:

{{< youtube TeTiZuSbQz8 >}}

### What's New

{{< call-out failure TODO >}}
The What's New shortcode is not yet documented and may be rolled-into the command shortcode.
{{< /call-out >}}

### Wikipedia Link

Use: `{{</* wikipedia-link Cosmic_latte */>}}` to get: {{< wikipedia-link Cosmic_latte >}}

## Related topics

* [How This Site Works](/guides/general/how-this-site-works/)
* [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

**Footnotes**

[^1]: This is an example of a footnote.
