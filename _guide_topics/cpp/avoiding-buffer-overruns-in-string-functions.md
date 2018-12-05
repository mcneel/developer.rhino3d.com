---
title: Avoiding Buffer Overruns in String Functions
description: This guide discusses how to write safe string function using C/C++.
authors: ['dale_fugier']
sdk: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Fundamentals']
origin: http://wiki.mcneel.com/developer/bufferoverrun
order: 1
keywords: ['rhino', 'overruns', 'strings']
layout: toc-guide-page
---

 
## Overview

Buffer overruns can be caused by passing buffers to functions without also passing the buffer's size.

Consider the following function:

```cpp
int GetName( wchar_t* pInput )
{
  wchar_t* pBuffer = (wchar_t*)malloc(100);
  wcscpy( pBuffer, pInput ); // might overrun buffer!
  wcscat( pBuffer, L".txt"); // also might overrun buffer!
  <...>
}
```

## A Safer Method

Use the following techniques to write safer functions...

Add a `size_t` argument for buffer size...

```cpp
// Pass pointer to buffer and buffer size
int GetName( wchar_t* buffer, size_t buffer_size );

// Ex:
wchar_t buffer[100];
int rc = GetName( buffer, _countof(buffer) );

// Ex:
const size_t kBufLen = 100;
wchar_t* pBuffer = new wchar_t[kBufLen];
GetName( pBuffer, kBufLen );
<...>
delete pBuffer;

// Ex:
const size_t kBufLen = 100;
ON_wString strBuffer;
strBuffer.ReserveArray( kBufLen );
GetName( strBuffer.Array(), kBufLen );

// Ex:
const size_t kBufLen = 100;
CString strBuffer;
GetName( strBuffer.GetBuffer(kBufLen), kBufLen );
strBuffer.ReleaseBuffer();
```

Change buffer argument to use a string object reference...

```cpp
// Pass a reference to a ON_wString object
int GetName( ON_wString& str );
// Pass a reference to a CString object
int GetName( CString& str );

// Ex:
ON_wString str;
int rc = GetName( str );

// Ex:
CString str;
int rc = GetName( str );
```

...change buffer argument to a fixed size array reference...

```cpp
// Pass a reference to a fixed size array
int GetName( wchar_t(&buffer)[100] );

// Ex:
wchar_t buffer[100];
int rc = GetName( buffer );
```

Change buffer point argument to reference to a pointer...

```cpp
// Pass a reference to a pointer
// API allocates buffer, caller required to free it
int GetName( wchar_t*& pBuffer );

// Ex:
wchar_t* pBuffer = 0;
int rc = GetName( pBuffer );
<...>
delete pBuffer;
```
