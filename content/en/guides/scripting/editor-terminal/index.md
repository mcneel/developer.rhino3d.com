+++
title = "Terminal Panel"
description = "Provides information on terminal panel in script editor"
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

    .language-csharp {
        font-size: .9em;
    }
</style>

## Terminal Panel

Terminal panel shows printed output of last executed script. You can toggle the terminal using the toggle button at the top-right of editor window.

The two *Copy* and *Clear* buttons can be used to copy or clear the terminal contents.

![](terminal.png)

## Line By Line Printing

By default, the output of a script is captured during execution and printed on the terminal all at once when execution is completed. This way the script is not slowed down by frequent UI updates.

When debugging a script, this behaviour changes and script output is printed on the terminal as the script is running. This helps seeing the messages being printed from your script during debug.

Sometimes it is desired to see the script output during normal execution. An examples is when a script is processing a series of files and needs to print its progress to the terminal. Waiting for the script to end without seeing any reports negates the point of reporting progress.

Use the *Line by Line* toggle on the terminal header to print script output during normal execution. You may also want to toggle auto-minimization from *Run > Toggle Minimize Editor On Execute* menu item to keep editor on screen:

![](terminal-linebyline.png)

