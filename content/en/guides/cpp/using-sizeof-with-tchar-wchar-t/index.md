+++
aliases = ["/en/5/guides/cpp/using-sizeof-with-tchar-wchar-t/", "/en/6/guides/cpp/using-sizeof-with-tchar-wchar-t/", "/en/7/guides/cpp/using-sizeof-with-tchar-wchar-t/", "/wip/guides/cpp/using-sizeof-with-tchar-wchar-t/"]
authors = [ "dale" ]
categories = [ "Fundamentals" ]
description = "This guide outlines some common mistakes using sizeof when dealing with UNICODE strings."
keywords = [ "rhino", "sizeof", "UNICODE", "TCHAR", "wchar_t" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Using the sizeof operator with TCHAR and wchar_t"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/countof"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++


## Discussion

The `sizeof` keyword gives the amount of storage, in bytes, associated with a variable or a type.  It does not return number of elements in an array, such as an array of characters.

Mistakes using the `sizeof` operator when dealing with UNICODE strings is very common.  For example:

```cpp
char szBuffer[24];
GetWindowText( hWnd, szBuffer, sizeof(szBuffer) ); // OK

wchar_t wszBuffer[24];
GetWindowText( hWnd, wszBuffer, sizeof(wszBuffer) ); // WRONG
```

In the above examples, the first block of code works because the char data type just happens to take up only one byte of storage.  Thus, the `sizeof` operator, when used on an array of chars just happens to work.  The other example is incorrect for a `wchar_t` requires two bytes of storage.  Thus, you have just told the `GetWindowText` that the buffer you have passed in is bigger than it really is.  This can crash your plugin.

The following is the proper method for using the sizeof operator when using UNICODE text strings...

```cpp
wchar_t wszBuffer[24];
GetWindowText( hWnd, wszBuffer, sizeof(wszBuffer)/sizeof(wchar_t) );
```

If you find yourself writing the above statement frequently, you might consider adding the following macro to your project:

```cpp
#define _countof(array) (sizeof(array)/sizeof(array[0]))

wchar_t wszBuffer[24];
GetWindowText( hWnd, wszBuffer, _countof(wszBuffer) );
```

The `TCHAR` data type definition is based on whether or not your plugins compile as MBCS or as UNICODE.  Rhino 6 plugins are compiled as UNICODE.  Thus, a TCHAR in Rhino 6 will be a `wchar_t`.

To be safe in all cases, you should use the following convention when dealing with TCHARs:

```cpp
TCHAR tchBuffer[24];
GetWindowText( hWnd, tchBuffer, sizeof(tchBuffer)/sizeof(TCHAR) );
```

In doing this, your code will be safe when compiled as either MBCS or UNICODE.
