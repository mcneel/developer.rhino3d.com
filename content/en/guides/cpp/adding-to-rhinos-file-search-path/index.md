+++
aliases = ["/en/5/guides/cpp/adding-to-rhinos-file-search-path/", "/en/6/guides/cpp/adding-to-rhinos-file-search-path/", "/en/7/guides/cpp/adding-to-rhinos-file-search-path/", "/wip/guides/cpp/adding-to-rhinos-file-search-path/"]
authors = [ "dale" ]
categories = [ "Advanced" ]
description = "This brief guide demonstrates how to add a file path to Rhino's file search path using C/C++."
keywords = [ "rhino", "search", "path" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Adding to Rhino's File Search Path"
type = "guides"
weight = 1
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/addsearchpath"
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

 
## Problem

You would like to add a file path to Rhino's file search path without having to script the Options command.

## Solution

Rhino's file search path is held by Rhino's `CRhinoDirectoryManager` object.  You can get the one and only `CRhinoDirectoryManager` singleton as follows:

```cpp
CRhinoDirectoryManager& dm = RhinoApp().RhinoDirectoryManager();
```

## Example

The following utility function demonstrates how to add (insert append or insert) to Rhino's file search path:

```cpp
int RhAddSearchPath( const wchar_t* pszFolder, int index = -1 )
{
  int rc = -1;
  if( 0 == pszFolder || 0 == pszFolder[0] )
    return -1;

  int rc = -1;
  if( CRhinoFileUtilities::DirExists(pszFolder) )
  {
    CRhinoDirectoryManager& dm = RhinoApp().RhinoDirectoryManager();
    const int path_count = dm.SearchPathCount();
    for( int i = 0; i < path_count; i++ )
    {
      if( 0 == on_wcsicmp(pszFolder, dm.SearchPath(i)) )
      {
        rc = i;
        break;
      }
    }

    if( rc == -1 )
    {
      index = RHINO_CLAMP( index, -1, path_count );
      if( index == -1 )
        rc = dm.AppendSearchPath( pszFolder );
      else if( dm.InsertSearchPath(index, pszFolder) )
        rc = index;
    }
  }
  return rc;
}
```
