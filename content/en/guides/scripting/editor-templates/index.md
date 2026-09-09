+++
title = "Templates Panel"
description = "Provides information on templates panel in script editor"
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

## Templates Panel

Templates panel browses a directory of scripts you use as starting points for new scripts. Choose **Window > Toggle Templates Panel** to show or hide it.

Use **Open Templates Directory** on the panel header to choose the directory, and **Clear Templates Browser** to empty the panel. Click the **>** in front of a folder to expand it. Folders are read as you expand them:

<!-- SCREENSHOT: templates panel with a templates directory open, a few templates listed -->
![](templates-panel.png)

## New Script From Template

Double-click a template to create a new script from it. The new script is a copy, so your template stays unchanged. You can also right-click and choose **New Script From Template**:

<!-- SCREENSHOT: new script created from a template, open in editor tab -->
![](templates-new.png)

## Editing a Template

To change the template itself, right-click it and choose **Edit**:

<!-- SCREENSHOT: right-click menu on a template with Edit highlighted -->
![](templates-edit.png)

## Searching and Filtering

Type in the search box to list only the templates with matching names. Use **Filter** on the panel header to list templates of one language only:

<!-- SCREENSHOT: search box with a term typed and Filter menu open showing languages -->
![](templates-search.png)

## Adding, Renaming, and Deleting

Right-click a folder and choose **Add Path** for a new folder, or **Add Template** for a new template of that language. Right-click a template to **Rename** or **Delete** it. Both menus also offer **Copy Path** and **Reveal in Finder** (**Reveal in File Explorer** on Windows):

<!-- SCREENSHOT: right-click menu on a templates folder and on a template, side by side -->
![](templates-menus.png)

These commands are only available when the directory can be modified.
