+++
title = "Search & Replace"
description = "Provides information on search and replace panel in script editor"
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

## Search & Replace

Search & Replace panel finds text in the script you are editing. Choose **Window > Toggle Search Panel** to show or hide it.

Type in the search box and the matches are listed under the script they were found in:

<!-- SCREENSHOT: search panel with a term typed, matches listed under the active script -->
![](search-panel.png)

Select a script to switch to it, or select a match to go to it in the editor:

<!-- SCREENSHOT: match selected in the panel and the editor scrolled to that match -->
![](search-goto.png)

## Search Options

Use the toggles on the panel header to change how the search term is matched:

- **Match Case**
- **Match Whole Word**
- **Regular Expressions**

Press the *Up* or *Down* arrow keys in the search box to step through your previous search terms. **Find Previous** and **Find Next** move between matches, and **Clear Search** empties the results:

<!-- SCREENSHOT: panel header with match case, whole word, and regex toggles, search box below -->
![](search-options.png)

## Searching All Open Scripts

Only the active script is searched by default. Use **Toggle Search Active or All Scripts** on the panel header to search all your open scripts instead:

<!-- SCREENSHOT: active-only toggle turned off, results grouped under several open scripts -->
![](search-active.png)

## Replacing

Type in the replace box to replace matches. **Replace** replaces the next match, and **Replace All** replaces every match found:

<!-- SCREENSHOT: replace box with text typed, showing Replace and Replace All buttons -->
![](search-replace.png)

Hover a row for its own replace button. On a script it replaces all matches in that script, and on a match it replaces just that one:

<!-- SCREENSHOT: replace button visible on a hovered script row and on a hovered match row -->
![](search-replace-row.png)
