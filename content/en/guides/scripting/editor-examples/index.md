+++
aliases = ["/guides/scripting/examples/"]
title = "Examples Panel"
description = "Provides information on examples panel in script editor"
authors = ["ehsan"]

[included_in]
platforms = [ "Windows", "Mac" ]
since = 8

[page_options]
byline = true
toc = true
toc_type = "single"
block_webcrawlers = false
+++

<style>
    .main-content img { zoom: 50%; }
    code {
        background-color: #efefef;
        padding-left: 5px;
        padding-right: 5px;
        border-radius: 3px;
        font-size: 14px;
    }
</style>

## Examples Panel

Examples panel browses example scripts you can start from. Choose **Window > Toggle Examples Panel** to show or hide it:

![](examples-panel.png)

## Rhino Examples

Choose **Download Rhino Examples** on the panel header to download and browse the example scripts published by McNeel. Click the **>** in front of a folder to expand it:

![](examples-rhino.png)

## Your Own Examples

Use **Open Examples Directory** to browse a directory of your own example scripts instead, and **Clear Examples Browser** to empty the panel:

![](examples-directory.png)

## New Script From Example

Double-click an example to create a new script from it. The new script is a copy, so the example stays unchanged. You can also right-click and choose **New Script From Example**:

![](examples-new.png)

## Searching and Filtering

Type in the search box to list only the examples with matching names. Use **Filter** on the panel header to list examples of one language only:

![](examples-search.png)

## Adding, Renaming, and Deleting

In your own examples directory, right-click a folder and choose **Add Path** for a new folder, or **Add Example** for a new example of that language. Right-click an example to **Rename** or **Delete** it. Both menus also offer **Copy Path** and **Reveal in Finder** (**Reveal in File Explorer** on Windows):

![](examples-menus-a.png)
![](examples-menus-b.png)

These commands are not available while browsing the Rhino examples.
