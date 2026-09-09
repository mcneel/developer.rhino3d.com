+++
title = "Problems Panel"
description = "Provides information on problems panel in script editor"
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

## Problems Panel

Problems panel lists the problems found in your script as you type. Choose **Window > Toggle Problems Tray** or click the *Problems* tab to show or hide it.

The panel lists problems of the current script only, and its title shows how many were found:

<!-- SCREENSHOT: problems tray open in console area with a few errors listed, tab title showing count -->
![](problems-panel.png)

These are not execution errors. Errors reported while running a script are printed on the [Terminal](/guides/scripting/editor-terminal).

## Problems

Each problem shows an icon for its severity, the message, the message id, and where it is in the script. Hover over a problem to see the full message:

<!-- SCREENSHOT: close-up of problem rows showing severity icons, message, id in parens, and position -->
![](problems-item.png)

Select a problem to go to its line. If the problem belongs to another open script, that script is opened first:

<!-- SCREENSHOT: problem selected in tray and caret moved to the matching line in the script above -->
![](problems-goto.png)

## Warnings and Info Messages

Only errors are listed by default. Use the two toggles on the panel header to also list warnings and info messages:

- **Toggle Warnings Messages**
- **Toggle Info Messages**

Both toggles are remembered between sessions:

<!-- SCREENSHOT: panel header toggles enabled, with warnings and infos now listed -->
![](problems-toggles.png)

## Copy Message

Right-click a problem and choose **Copy Message** to copy its message to clipboard:

<!-- SCREENSHOT: right-click context menu on a problem showing Copy Message -->
![](problems-copy.png)

## Turning Diagnostics Off

Problems are collected by the language linter. Turn off **Diagnostics (Linting)** in [Editing Options](/guides/scripting/editor-configs/#editing-options) to stop collecting them. The script is no longer highlighted and the panel stays empty. **Show Hints** controls hint messages separately:

<!-- SCREENSHOT: Editor Options dialog with Diagnostics (Linting) and Show Hints options -->
![](problems-options.png)
