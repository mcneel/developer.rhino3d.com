+++
title = "ScriptEditor Command in Macros"
description = "Provides information on using ScriptEditor command in macros"
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

## ScriptEditor Command Options

*ScriptEditor* command has a few options that could be used in macros. Run `_-ScriptEditor` command in Rhino prompt to see these options (`-` is for non-interactive mode, and `_` ensures command works in all Rhino UI languages. [See Command Macros & Scripting](https://docs.mcneel.com/rhino/8/help/en-us/information/rhinoscripting.htm) for more):

- **Edit (E):** This is the default option when running ScriptEditor command in Rhino. It opens the standalone Script Editor and initialized all languages.
- **Run (R):** Runs given script using the new scripting infrastructure in Rhino 8. It can run scripts or script files of any supported language.
  - **Browse (B):** Using this suboption, allows to browse and select a script file
  - Run a script file in a macro this way 👉 `_-ScriptEditor _R "C:\path\to\script.py"` 
  - Run a script in a macro this way 👇:

```text
_-ScriptEditor _R (
    #! python 3
    print("Hello Rhino")
)
```
- **Open (O):**: Opens given script file in ScriptEditor
  - **Browse (B):** Using this suboption, allows to browse and open a script file
  - Open a script file to edit this way 👉 `_-ScriptEditor _O "C:\path\to\script.py"` 

## Script Search Paths

Normally you have specify the full script path in a macro like `_-ScriptEditor _R "C:\path\to\HelloWorld.py"` to run  the script. However, you can place your most common scripts under a directory, and add the path of that directory to [Rhino File Search Paths](https://docs.mcneel.com/rhino/8/help/en-us/options/files_search_paths.htm). When search paths are set up, you can run `_-ScriptEditor _R "HelloWorld.py"` and the command can find the script under specified search paths.

Please note that [Python Module Search Paths](/guides/scripting/editor-configs/#python-paths) are not searched for scripts. They are purely to search and find python modules.