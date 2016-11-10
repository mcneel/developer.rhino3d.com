---
title: VBScript RegExp Objects
description: This guide discusses the VBScript RegExp object.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Advanced']
origin: http://wiki.mcneel.com/developer/scriptsamples/regexpobject
order: 1
keywords: ['script', 'Rhino', 'vbscript']
layout: toc-guide-page
---

# {{ page.title }}

{% include byline.html %}

{{ page.description }}

## Overview

The VBScript `RegExp` object matches strings against special text patterns, called regular expressions.

The `InStr` function can be used to search a string to see if it contains another string.  The `RegExp` object provides a far more sophisticated string searching facility by using regular expressions.

A regular expression is a string that describes a match pattern.  The match pattern provides a template that can be used to test another string, the search string, for a matching sub-string.  In its simplest form, the match pattern string is just a sequence of characters that must be matched.  For example, the pattern `"fred"` matches this exact sequence of characters and only this sequence.  More sophisticated regular expressions can match against items such as file names, path names, and Internet URLs.  Thus, the `RegExp` object is frequently used to validate data for correct form and syntax.

## Using RegExp

To test a search string against a match pattern, create a `RegExp` object and set the match pattern.  Then use the `.Test` method to test for a match.  For example:

```vbnet
Dim oRE, bMatch
Set oRE = New RegExp
oRE.Pattern = "fred"
bMatch = oRE.Test("His name was fred brown")
```

Regular expression objects are created using `the` New keyword.  This is an anomaly of VBScript, because it is the only object, apart from user-defined objects, that is created in this manner.  Once created in this way, the methods and properties of the object are accessed normally.

The `.Pattern` property defines the match pattern, and the `.Test` method tests the supplied string against this match pattern, returning True if the match pattern is found within the supplied string.  In the preceding example, `bMatch` is set to True as there is clearly a match.

The `.Execute` method of the `RegExp` object also checks for a pattern match, but it returns a `Matches` collection object that contains detailed information on each pattern match.  The `Matches` object is a normal collection object containing a `.Count` property and a default `.Item` property.  Each item in the `Matches` object is a `Match` object that describes a specific pattern match.  After the `.Execute` method is invoked, the returned `Matches` object contains a `Match` object for each match located in the search string.

Each `Match` item has three properties.  The `.Value` property contains the actual text in the search string that was matched.  The `.FirstIndex` property contains the index of the first character of the match in the search string.  The `.Length` property contains the length of the matched string.  Unlike other VBScript string indexes, the `.FirstIndex` property uses 0 as the index of the first character in the string.  Therefore, always add one to this value before using it with other VBScript string functions.

By default, the `.Execute` method only matches the first occurrence of the pattern.  If the `.Global` property is set to True, the method matches all the occurrences in the string and returns a `Match` object for each match.  For example:

```vbnet
Dim oRE, oMatches
Set oRE = New RegExp
oRE.Pattern = "two"
oRE.Global = True
Set oMatches = oRE.Execute("two times three equals three times two")
For Each oMatch In oMatches
  Rhino.Print "Match: " & oMatch.Value & " At: " & CStr(oMatch.FirstIndex + 1)
Next
```

This example lists all the matches against the pattern `"two"` in the specified string.

Simple match patterns, such as those shown in the previous example, provide no additional functionality over that provided by the `InStr` function.  Much more powerful searches are available, however, by using the special regular expression features of the search pattern.  These are most easily explored using the sample script shown below:

```vbnet
Sub TestRegExp(sPattern, sSearch)

  ' Do the regular expression match
  Dim oRE, oMatches
  Set oRE = New RegExp
  oRE.Global = True
  oRE.IgnoreCase = True
  oRE.Pattern = sPattern
  Set oMatches = oRE.Execute(sSearch)

  ' Now process all the matches (if any)
  Dim oMatch
  Rhino.Print "Pattern String: " & Chr(34) & sPattern & Chr(34)
  Rhino.Print "Search String: " & Chr(34) & sSearch & Chr(34) & VbCrLf
  Rhino.Print "Matches: " & CStr(oMatches.Count)
  Rhino.Print "    " & sSearch
  For Each oMatch In oMatches
    Rhino.Print "    " & String(oMatch.FirstIndex, " ") & String(oMatch.Length, "^")
  Next

End Sub
```

To use the script, call the subroutine two arguments.  Enter a match pattern as the first argument and a search string as the second argument.  If either argument contains spaces or special shell characters, enclose the argument in double quotes.  The script uses the `.Execute` method of the `RegExp` object to locate all matches and then displays these matches graphically.  Use this script to experiment with the various advanced regular expression features described in the following paragraphs.  (Several of the preceding `Rhino.Print` statements use the expression `Chr( )`.  This simply evaluates to a double quote character.)

## Regular Expression syntax

Within the match pattern, letters, digits, and most punctuation simply match a corresponding character in the search string.  A sequence of these characters matches the equivalent sequence in the search string.  However, some characters within the match pattern have special meaning.  For example, the `"."` (period) character matches any character except a new-line character.  Thus, the match pattern `"a.c"` matches `"abc"` or `"adc"` or `"a$c"`. The match pattern `".."` matches any sequence of two characters.

The special character `"^"` matches the start of the string.  Thus, the match pattern `"^abc"` matches the string `"abc"`, but not `"123abc"` because this string does not begin with `"abc"`.  Similarly, the special character `"$"` matches the end of the string, and so the pattern `"red$"` matches the search string `"fred"`, but not `"fred brown"`.

Using both these characters allows a regular expression to match complete strings.  For example, the pattern `"abc"` matches `"123 abc that"` and any other string containing `"abc"`, whereas the pattern `"^abc$"` only matches the exact string `"abc"`.

The three characters `*`, `+`, and `?` are called modifiers.  These characters modify the preceding character.  The `*` modifier matches the preceding character zero or more times, the `+` modifier matches the preceding character one or more times, and the `"?"` modifier matches the preceding character zero or one time.  For example, the pattern "a+" matches any sequence of one or more `"a"` characters, whereas the pattern `"ab*c"` matches `"abc"`, `"abbbbbc"`, and `"ac"`, but not `"adc"` or `"ab"`.

A list of characters enclosed in brackets is called a range and matches a single character in the search string with any of the characters in brackets.  For example, the pattern `"[0123456789]"` matches any digit character in the search string.  Ranges such as this, where the characters are sequential, can be abbreviated as `"[0-9]"`.  For example, the pattern `"[0-9a-zA-Z_]"` matches a digit, letter (either upper or lower case), or the underscore character.  If the first character of the range is `"^"`, the range matches all those characters that are not listed.  For example, `"[^0-9]"` matches any non-digit character.

Ranges can be combined with modifiers. For example, the pattern `"[0-9]+"` matches any sequence of one or more digit characters. The pattern `"[a-zA-Z][a-zA-Z_0-9]*"` matches a valid VBScript variable name, because it only matches sequences that start with a letter and are followed by zero or more letters, digits, or underscore characters.

To match a character an exact number of times, follow the character in the pattern by a count of matches required enclosed in braces.  For example, the pattern `"a{3}"` matches exactly three `"a"` characters, and it is equivalent to the pattern `"aaa"`.  If a comma follows the count, the character is matched at least that number of times. For example, `"a{5,}"` matches five or more `"a"` characters.  Finally, use two counts to specify a lower and upper bound. For example, the pattern `"a{4,8}"` matches between four and eight `"a"` characters.

As with other modifiers, the pattern count modifier can be combined with ranges.  For example, the pattern `"[0-9]{4}"` matches exactly four digits.

Use parentheses in the match pattern to group individual items together.  Modifiers can then be applied to the entire group of items. For example, the pattern `"(abc)+"` matches any number of repeats of the sequence `"abc"`.  The pattern `"(a[0-9]c){1,2}"` matches strings such as `"a0c"` and `"a4ca5c"`.

There is a difference between matching the pattern `"abc"` and the pattern `"(abc)+"` using the `RegExp` object.  Matching the pattern `"abc"` against the search string `"abcabcabc"` generates three individual matches and results in three `Match` objects in the Matches collection.  Matching the pattern `"(abc)+"` against the same string generates one match that matches the entire string.

The `"I"` vertical bar character separates lists of alternate sub-expressions.  For example, the pattern `"abIac"` matches the strings `"ab"` or `"ac"`. The vertical bar separates entire regular expressions.  The pattern `"^abIac$"` matches either the string `"ab"` at the start of the search string or the string `"ac"` at the end of the search string. Use parentheses to specify alternates within a larger pattern.  For example, the pattern `"^(abIac)$"` matches the exact strings `"ab"` or `"ac"` only.

To match any of the special characters literally in a pattern, they must be preceded by a back-slash character, which is known as an escape.  For example, to match a literal asterisk, use `"\*"` in the pattern.  To match a back-slash itself, use two back-slash characters in the match pattern.  The following characters must be escaped when used literally within a match pattern:

```regex
. (period) * + ? \ ( ) [ ] { } ^ $
```

There are also several additional escape sequences that provide useful shorthand for more complex patterns:

- The `"\d"` escape matches any digit, and it is equivalent to `"[0-9]"`. The `"\D"` escape matches any non-digit, and it is equivalent to `"[^0-9]"`.
- The `"\w"` escape matches any word character and is equivalent to `"[0-9a-zA-Z_]"`, and the `"\W"` escape matches any non-word character.
- The `"\b"` escape matches a word boundary, which is the boundary between any word character and a non-word character, whereas `"\B"` matches a non-word boundary.
- The `"\s"` escape matches any whitespace character, including space, tab, new-line, and so on, whereas the `"\S"` escape matches any non-whitespace character.

Finally, certain escapes can match non-printing characters, as follows:

- The `"\f"` escape matches a form-feed character.
- The `"\n"` escape matches a new-line character.
- The `"\r"` escape matches a carriage-return character.
- The `"\t"` escape matches a tab character.
- The `"\v"` escape matches a vertical tab character.
- The `"\onn"` escape matches a character whose octal code is `nn`.
- The `"\xnn"` escape matches a character whose hexadecimal code is `nn`.

The special escape `"\n"`, where n is a digit, matches the search text previously matched by a sub-expression in parentheses.  Each sub-expression in a match pattern is numbered from left to right, and the escape `"\n"` matches the nth sub-expression.  For example, the pattern `"(..)\1"` matches any two character sequence that repeats twice, such as `"abab"`.  The first sub-expression matches the first two characters, `"ab"`, and the `"\1"` escape then matches these same two characters again.

## RegExp Example

Regular expression match patterns provide a powerful way to validate the syntax of strings.  For example, a script can obtain strings from a formatted text file and parse it into recognizable tokens.  A regular expression can be used for this purpose.

This script is simplistic in that it simply breaks apart each argument at the `"="` sign - no attempt is made to check if the name and value parts are valid.  The following regular expression matches these command line arguments:

```regex
[^=]+=.*
```

This match pattern is interpreted as follows: The range `"[^=]"` matches any character that is not an `"="` sign.  The `"+"` modifier following the range means that the pattern matches any set of one or more characters that are not `"="` signs.  The next `"="` sign in the pattern matches a literal `"="` sign (that is, the separator between the name and value parts).  Finally, the `".*"` pattern matches any sequence of zero or more characters.

Parentheses can be used to make the meaning more clear.  For example:

```regex
([^=]+)=(.*)
```

This example is identical to the previous example, but the parentheses help make the individual parts of the pattern more understandable.

Typically, the name in the previous example should be restricted to a valid name.  We define valid names as a letter followed by zero or more letters, digits, or underscores.  This yields a new regular expression as follows:

```regex
([a-zA-Z]\w*)=(.*)
```

Here, the pattern `"[a-zA-Z]"` matches any single letter. Then the pattern `"\w*"` matches zero or more letters, digits, or underscores, using the `"\w"` escape as a shorthand for `"[0-9a-zA-Z]"`.

The previous regular expression does not allow spaces before or after the name.  For example, only the first of these strings matches the expression:

```
curve=123456
curve = 575888
curve  = 5544
```

The following regular expression corrects this by adding optional leading and trailing whitespace around the name:

```regex
(\s*)([a-zA-Z]\w*)(\s*)=(.*)
```

The new addition, `"\s*"`, matches zero or more whitespace characters.

## The .Replace Method

Matching patterns against strings allows a script to determine if a string follows a specific syntax, as shown in the previous examples.  The `RegExp` object can also be used to assist in modifying the search string.  This facility is provided by the `.Replace` method, which takes two arguments: the search string and a replacement string, and returns a new string in which all matches in the search string are replaced by the replacement string.  For example:

```vbnet
Set oRE = New RegExp
oRE.Global = True
oRE.Pattern = "a"
Wscript.Echo oRE.Replace("all a's are replaced", "X")
```

In this example, any `"a"` character in the search string is replaced by an `"X"` character.  The pattern and replacement strings do not need to be the same length.  For example:

```vbnet
oRE.Pattern = "\s+"
Wscript.Echo oRE.Replace("compress  all      whitespace    ", " ")
```

Here, all sequences of whitespace are replaced by a single space character.

Within the replacement string, the special character sequence `"$n"` is allowed.  If present, this sequence is replaced by the text matched by the nth sub-expression in the pattern.  For example:

```vbnet
oRE.Pattern = "^\s*(\w+)\s*=\s*(\w+)\s*$"
sSearch = "    this    = that"
Rhino.Print oRE.Replace(sSearch, "$1,$2")
```

This example works as follows:

The pattern contains both the start of string `"^"` and end of string `"$"` characters.  This means that the pattern either matches the entire search string or not at all.

The pattern matches any whitespace and sequence of one or more word characters, more whitespace, an `"="` sign, more whitespace, another set of word characters, and finally more whitespace.

Both the word patterns are in parentheses, marking them as sub-expressions 1 and 2 respectively.

When the `.Replace` method is invoked, it matches successfully against the entire search string.  This means that the replacement string replaces the entire contents of the search string, because this entire string matched the regular expression.  Thus, the string returned by `.Replace` is simply the replacement string.

The replacement string is `"$1,$2"`. As noted, the two sub-expressions in the pattern contain the two words matched in the search string, which in this case are `"this"` and `"that"`. Thus, the replacement string becomes `"this,that"`, and this is the value returned.

The result of this processing is that the `RegExp` object has validated the search string against the match pattern and extracted the required elements from the search string.
