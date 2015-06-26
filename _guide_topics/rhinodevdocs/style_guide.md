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

This is a sample page that serves as a quick reference for the syntax and structure of Rhino Developer Documentation content.  Below are examples of all the available using Markdown, Kramdown (a superset of Markdown), the table-of-contents UI widget, etc.

---

## Structure
{: .toc-header }

On this site, the convention is:

```# Title``` become H1 headers and are reserved for the title of the page only.

```## Header``` become H2 headers and are reserved for major sections within the page.

```#### Sub Header``` become H4 headers and are reserved for sub-sections within a major section.


## Headers
{: .toc-header }

Headers are created like this:

``` ## Headers ```

The example above is an H2 header.  

Creating a header automatically creates an #anchor tag in the generated html.  

For headers with multiple words, Kramdown lowercases all the words and adds dashes for spaces. For example, if we had a header like this:

``` ## All Your Base Are Belong to Us ```

the resulting html anchor tag would be:

```#all-your-base-are-belong-to-us```


#### Sub Headers
{: .toc-subheader }
