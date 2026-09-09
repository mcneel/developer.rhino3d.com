+++
title = "Help Panel"
description = "Provides information on help panel in script editor"
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

    /* keep both menu tables on the same column grid */
    .main-content table { table-layout: fixed; width: 100%; }
    .main-content table thead { display: none; }
    .main-content table th:first-child,
    .main-content table td:first-child { width: 40%; }
</style>

## Help Panel

Help panel lists the libraries available to your scripts and lets you search them. Choose **Help > Toggle Help Panel** to show or hide it. Libraries are loaded the first time the panel is opened:

<!-- SCREENSHOT: Help panel open on the left side of editor window, tree collapsed to top-level libraries -->
![](help-panel.png)

## Libraries

The tree has three levels:

- **Libraries** at the top level, with their version
- **Modules, Namespaces, and Classes** in between
- **Entries** at the bottom: functions, methods, properties, and other members

Python scripts also list `rhinoscriptsyntax`, `rhinoscript`, `scriptcontext`, and `rhinocompat`. Rhino and Grasshopper libraries are listed last:

<!-- SCREENSHOT: tree expanded a few levels deep, showing library > namespace > class > method icons -->
![](help-tree.png)

## Searching

Type in the search box to filter all libraries at once. Matching items are expanded, and libraries without a match are grayed out. Use the toggles on the panel header to change how the search term is matched:

- **Match Case**
- **Match Whole Word**
- **Regular Expressions**

Press the *Up* or *Down* arrow keys in the search box to step through your previous search terms. The search term and expanded items are remembered between sessions:

<!-- SCREENSHOT: search box with a term typed, matches expanded, non-matching libraries grayed out, header toggles visible -->
![](help-search.png)

## Reading Documentation

Select an entry to see its documentation. Entries that have an online documentation page open in a **Help** tab next to your script tabs:

<!-- SCREENSHOT: Help tab open in tab strip showing an online docs page for a selected entry -->
![](help-tab.png)

Entries that only have a description are shown in the help card next to the *Terminal*, so your script stays open:

<!-- SCREENSHOT: help card tray at bottom of editor next to Terminal tab, showing description of selected entry -->
![](help-card.png)

## Older Rhino Libraries

Choose **Help > Toggle Rhino 7 Libraries in Help** to also list the libraries of the previous Rhino version:

<!-- SCREENSHOT: help tree with legacy Rhino 7 libraries added to the list -->
![](help-legacy.png)

## Tip Dots

Choose **Help > Toggle Tip Dots** to show or hide tip dots on editor controls and dialogs. This is an editor-wide option and is not specific to the help panel:

<!-- SCREENSHOT: an editor dialog or control with tip dots visible -->
![](help-tipdots.png)

## Online Help

The **Help** menu also links to online resources:

|  |  |
| --- | --- |
| **Help > Help Topics** | [RhinoScriptSyntax API](https://developer.rhino3d.com/api/RhinoScriptSyntax/) |
| **Help > Scripting Guide** | [Scripting Guides](https://developer.rhino3d.com/guides/scripting/) |
| **Help > Acknowledgments** | [Script Editor Acknowledgments](https://www.rhino3d.com/acknowledgments/#script-editor) |

These items are listed when editing a Python script:

|  |  |
| --- | --- |
| **Help > Rhino.Python Fundamentals** | [RhinoScriptSyntax API](https://developer.rhino3d.com/api/RhinoScriptSyntax/) |
| **Help > Rhino.Python Online** | [Rhino.Python Guides](https://developer.rhino3d.com/guides/rhinopython/) |
| **Help > Rhino.Python Samples** | [Rhino.Python Samples](https://developer.rhino3d.com/samples/#rhinopython) |
| **Help > Scripting Discussion on Discourse** | [Scripting Forum](https://discourse.mcneel.com/c/scripting/11) |

<!-- SCREENSHOT: Help menu open showing all items -->
![](help-menu.png)
