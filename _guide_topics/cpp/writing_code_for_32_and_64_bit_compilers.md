---
title: Writing Code for 32- and 64-bit Compilers
description: This guide outlines some considerations when writing C/C++ code for both 32- and 64-bit compilers.
author: dale@mcneel.com
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Advanced']
origin: http://wiki.mcneel.com/developer/sdksamples/migratevs2010/64bitcompatibility
order: 1
keywords: ['rhino', 'compilers']
layout: toc-guide-page
---

# {{ page.title }}

{{ page.description }}

## strlen

The return type of string length functions like `strlen` and `wcslen` is a `size_t`.  Since we will never have null terminated strings with more than 2,147,483,647 characters, simply use a cast like so:

```cpp
int length = (int)wcslen(str);  //(int) cast for 64 bit compilers
```

## fread and fwrite

The return type of `fread` and `fwrite` is a `size_t`.  Design your calls to `fread` and `fwrite` so that the count argument is never > 2,147,483,648 and use an int cast on the return type like so:

```cpp
int count = ...;  some number <= 2,147,483,648
if ( count != (int)fread( buffer, size, count, fp ) )
{
  //fread failed
  //handle file reading error
}
```

or

```cpp
int count = ...;  some number <= 2,147,483,648
if ( count != (int)fwrite( buffer, size, count, fp ) )
{
  //fwrite failed
  //handle file writing error
}
```

If you are compelled to write 9,223,372,036,854,775,808 bytes in a single call to `fwrite`, you can do so with:

```cpp
size_t size = 9223372036854775808;
void* buffer = ...;
FILE* fp = ...;
if ( 1 != fwrite( buffer, size, 1, fp ) )
{
  //failed to write 9223 terrabytes in a single call to fwrite - duh
  //printf("You're a looser\n");
}
```

## Sort functions that compare pointers

Use `INT_PTR` to store the difference between two pointers.

```cpp
//Sort functions have to return 32 bit ints
static int compar( const void** a, const void** b )
{
//pointer differences have to be INT_PTR (64 bit int on x64)
 INT_PTR i = ((const CTheRealType**)b)->pRhinoObject - ((const CTheRealType**)a)->pRhinoObject
  //Expect i to be > MAX_INT, so do something like this
 return ( (i<0) ? -1 : ( (i>0) ? 1 : 0 );
}
```

## size_t

The type `size_t` is 64 bits on a 64-bit compiler.  See the `strlen` and `fread` sections above for examples on dealing with this.

## Formatted printing

You really need to pay attention to the size of your integer arguments to formatted printing strings.

```cpp
int i = ...;
size_t sz = ...;
void* ptr = ...;
INT_PTR ip = ...;
hyper h = ...;
__int64 i64 = ...;
RhinoApp().Print("i = %d  sz = %Id ptr = %I08X ip = %Id h = %I64d i64 = %I64d\n",
                 i,sz,ptr,ip,h,i64);
```

## Windows SendMessage

If you cast the `WPARAM` and `LPARAM` arguments as (`WPARAM`) and (`LPARAM`), and put the return value in an `LRESULT`, everything works perfectly for both the 32- and 64-bit compilers.  Since the value of `smresult` can be an `int`, `pointer`, `handle`, whatever, cast `smresult` as shown below.

```cpp
LRESULT smresult = SendMessage((UNIT)id, (WPARAM)&gt, (LPARAM)sText);
int rc = (int)smresult ;  //In this case, I the rest of the code want
HWND hwnd = (HWND)smresult;
char** ptr = (char**)smresult;
```

## Windows SetWindowLong and GetWindowLong

Replace every single instance of Windows calls that pass pointers as mystery meat with the `Ptr` versions.

```cpp
//BAD            //GOOD
SetWindowLong -> SetWindowLongPtr
GetWindowLong -> GetWindowLongPtr
```

If you do this, then your code will work perfectly and compile cleanly on both 32- and 64-bit platforms.

The `Ptr` part of the function names is misleading.  The `Ptr` versions work when the return value or last argument has any type.

Bad:

```cpp
SetWindowLong( *pDockFrame, GWL_USERDATA, (LONG)this);
 WNDPROC wp = (WNDPROC)::GetWindowLong( *pDockFrame, GWL_WNDPROC);
 DWORD dwStyle = ::GetWindowLong( pMsg->hwnd, GWL_STYLE)
```

Good:

```cpp
SetWindowLongPtr( hwnd, id, (LONG_PTR)this);
WNDPROC wp = (WNDPROC)::GetWindowLongPtr( *pDockFrame, GWL_WNDPROC);
DWORD dwStyle = (DWORD)::GetWindowLongPtr( pMsg->hwnd, GWL_STYLE)
```

### Timers

The value returned by `Windows ::SetTimer()` needs to be saved in a `UINT_PTR`.
