+++
title = "Explorer Panel"
description = "Provides information on explorer panel in script editor"
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

## Explorer Panel

Explorer panel browses a directory of scripts on your machine. Choose **Window > Toggle Explorer Panel** to show or hide it.

Use **Open Directory** on the panel header to choose a directory, and **Clear Explorer** to empty the panel. Click the **>** in front of a folder to expand it. Folders are read as you expand them, so large directories stay responsive:

<!-- SCREENSHOT: explorer panel with a directory open, a few folders expanded showing scripts -->
![](explorer-panel.png)

To browse the directory of a script that is already open, right-click the script tab at the top of the editor window and choose **Explore Path**:

<!-- SCREENSHOT: right-click menu on a script tab at top of editor window, with Explore Path highlighted -->
![](explorer-explorepath.png)

## Opening Scripts

Double-click a script to open it in the editor. You can also right-click and choose **Open**:

<!-- SCREENSHOT: script opened from explorer, shown in editor tab -->
![](explorer-open.png)

## Searching and Filtering

Type in the search box to list only the scripts with matching names. Use **Filter** on the panel header to list scripts of one language only. **Include Projects** controls whether scripts inside script projects are listed:

<!-- SCREENSHOT: search box with a term typed and Filter menu open showing languages and Include Projects -->
![](explorer-search.png)

## Adding, Renaming, and Deleting

Right-click a folder and choose **Add Path** for a new folder, or **Add Script** for a new script of that language. Right-click a script to **Rename** or **Delete** it. Both menus also offer **Copy Path** and **Reveal in Finder** (**Reveal in File Explorer** on Windows):

<!-- SCREENSHOT: right-click menu on a folder and on a script, side by side -->
![](explorer-menus.png)

These commands are only available when the directory can be modified.
