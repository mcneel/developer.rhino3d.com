+++
title = "Script Editing Features"
description = "Provides information on editing features in Script Editor"
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

Script Editor has a few editing features that can be changed or toggled for each specific language. These settings are toggled/set using two different methods:

- **Edit > Toggle** menu items: Affect the current session and are forgotten when Rhino restarts.

- **Editor Options** Dialog: Are persistent and are stored in editor configuration file to disk.

Depending on the type of feature, there might be a *Toggle* menu item or a setting in *Editor Options*, or *both*. Some features are language-specific and can be set independently by scripting language.

## Tabs or Spaces?

Choose **Edit > Toggle White Spaces** to toggle visibilty of white spaces (Tab or Space) in your scripts. See **Show White Spaces** in [Editing Options](/guides/scripting/editor-configs/#editing-options). This option is *Off* by default:

![](editor-tabsspaces.png)

**Edit > Convert Indentation to Tabs/Spaces** commands can be used to convert between Space and Tab indentations. When changing your scripts to [SDK-Mode](/guides/scripting/scripting-gh-python#sdk-mode) in Grasshopper, the indentation is detected and used in modified script:

![](editor-tabsspaces-gh.png)

## Indentation Guides

Indentation guides are vertical lines drawn at different indentation levels to help visually identifying scopes and blocks. See **Show Indentation Guides** in [Editing Options](/guides/scripting/editor-configs/#editing-options). This option is *On* by default:

![](editor-indentGuides.png)

## Minimap

Choose **Edit > Toggle Minimap** to toggle visibilty of minimap. It is effectively a thicker vertical scrollbar that shows a tiny preview of your script. You can scroll up and down the script using minimap. See **Show Minimap** in [Editing Options](/guides/scripting/editor-configs/#editing-options). This option is *Off* by default:

![](editor-minimap.png)

## Line Numbers

Pretty clear what they are! Choose **Edit > Toggle Line Numbers** to toggle their visibility:

![](editor-lineNumbers.png)

## Diagnostics (Linting)

As you are typing your script, the editor is continiously checking for syntax errors using the static analyzers provided by the language. These messages are categorized as **Errors**, **Warnings**, or **Info** and show up in the *Problems* panel at the bottom of the editor. The script text area also shows squiggly lines where these errors are located. You can click on each item in *Problems* panel to navigate the cursor to where the problem is:

![](editor-diags.png)

When there are messages in the *Problems* panel, its tab shows an icon with a count of messages listed in the panel:

![](editor-diags-problemsTab.png)

By default, the *Problems* panel only shows error messages. You can use the filter toggles on the panel to see other message types as well:

![](editor-diags-problemsFilter.png)


See **Diagnostics (Linting)** in [Language Support Options](/guides/scripting/editor-configs/#language-support-options) to turn diagnostics off for a specific language. This option is *On* by default.

## Autocompletion

Script editor has completion support for all languages. There are a few kinds of autocompletion:

- **Word Completion:** usually triggers when typing space or `.` and provides completion for methods, properties, function calls, etc:

  ![](editor-autocomplete-word.png)

- **Signature Completion** usually triggers when opening a `(` and provides function help and parameter list, as well as tracking and highlighting arguments as you type:

  ![](editor-autocomplete-signature.png)

- **Snippet Completion** usually triggers when typing space after a keyword and provides templates for common language constructs like `if` statements or `foreach` loops. It is *Off* by default. Choose **Edit > Toggle Snippet in Autocomplete** to toggle snippets on.
  
  ![](editor-autocomplete-snippet.png)


### Word-based Autocomplete

Editor can collect words already used in the script to help with autocomplete. However as it does not have a full understanding of the context and meaning of these collected words, this type of autocompletion is not always useful. This option is *Off* by default. Choose **Edit > Toggle Word-based Autocomplete** to turn it on. See **Autocompletion** in [Language Support Options](/guides/scripting/editor-configs/#language-support-options) to toggle this option on for a specific language:

![](editor-autocomplete-wordBased.png)

### Autocomplete in Function Help

Usually when typing up arguments to a function, we would like to keep the *Signature Completion* open so it can track the arguments being typed and help with each argument type or expected values. For this reason, autocompletion is momentarily stopped to keep the *Signature Completion* popup open:

![](editor-autocomplete-insignature.png)

To change this behaviour - for example to get the autocompletion for `os.` in example above - choose **Edit > Toggle Autocomplete in Function Help**. See **Autocompletion** in [Language Support Options](/guides/scripting/editor-configs/#language-support-options) to toggle this option for a specific language.