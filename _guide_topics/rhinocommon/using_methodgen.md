---
title: Using methodgen
description: This guide covers the automatic pInvoke call generator and enum synchronization utility called methodgen.
author: giulio@mcneel.com
apis: ['RhinoCommon']
languages: ['C#']
platforms: ['Windows', 'Mac']
categories: ['Advanced']
origin: unset
order: 6
keywords: ['Native', 'RhinoCommon', 'Plugin', 'Library', 'PInvoke', 'methodgen', 'AutoNativeMethods']
layout: toc-guide-page
---

# {{ page.title }}

{{ page.description }}

It builds on top of concepts from the [Wrapping Native Libraries]({{ site.baseurl }}/guides/rhinocommon/wrapping_native_libraries) guide.


## Overview

Wrapping a C/C++ library for .NET consumption is a large task.  Usually, there is a C/C++ library with every C exported function, that will link to or be itself the content of the exported functionality (we call this *lib_C*, in a directory called *lib_C_dir*), and a C# library that will provide access to the exported functionality (*lib_CS*, in *lib_CS_dir*).

Besides other more high-level restructuring, wrapping usually involves:

1. Creating a large amount of C functions to be exported for PInvoke,
2. The definition of some helper enum values that have the only purpose of helping C - C# communication, and
3. Copying many public C++ enum values to C#

For each of these tasks, we wrote a tool, *methodgen.exe*, that automatically writes most of the boilerplate code.


## methodgen in your project

To run the tool, place it in a folder that is a parent folder to both your C and your C# solutions.  Then, add a prebuild event to your project, either using the standard Visual Studio or Xamarin Studio interface, of by adding this code to the `.csproj` solution:

```
<PropertyGroup Condition=" '$(Configuration)' == 'Release' Or '$(Configuration)' == 'Debug' ">
  <PreBuildEvent>$(ProjectDir)..\methodgen.exe lib_C_dir lib_CS_dir</PreBuildEvent>
</PropertyGroup>
```

Each path can be relative.  Every *.h* and *.cpp* file in *lib_C_dir* will be parsed.

A file called *AutoNativeMethods.cs*, and another one called *AutoNativeEnums.cs* if required, will be placed in *lib_CS_dir* at the end of the process.  This will happen in the following 3 steps...


## 1. Export C functions to C\#

*methodgen.exe* looks for every line starting with `RH_C_FUNCTION` in every *.h* and *.cpp* file in *cpp_dir*.

We define the `RH_C_FUNCTION` macro directive like this:

```cpp
#define RH_C_FUNCTION extern "C" __declspec(dllexport)
```

A typical exported C function will look like this:

```cpp
RH_C_FUNCTION int ON_Brep_SplitEdgeAtParameters(ON_Brep* pBrep, int edge_index, int count, /*ARRAY*/const double* parameters)
{
  int rc = 0;
  if (pBrep && count>0 && parameters)
    rc = pBrep->SplitEdgeAtParameters(edge_index, count, parameters);
  return rc;
}
```

Inside *AutoNativeMethods.cs*, in an `_internal partial class_` called `UnsafeNativeMethods`, *methodgen.exe* will create these lines of code:

```cs
[DllImport(Import.lib, CallingConvention=CallingConvention.Cdecl )]
internal static extern int ON_Brep_SplitEdgeAtParameters(IntPtr pBrep, int edgeIndex, int count, double[] parameters);
```

### Parsing function parameter and return types

Every parameter to the function will undergo some transformation to be useful in C# as follows:

- `const` will be removed.  It might be a good idea to name parameter variables in a predictable manner relative to const-ness of the data that is passed.
- Any `type*` will be transformed to a generic `IntPtr`.  As an exception, if the pointer refers to a fundamental type (such as `int`, `unsigned char`), this will be passed as a inbuilt C# type, with the keyword `ref` prefixed.
- Fundamental types will be translated to the corresponding C# type.  The `unsigned` modifier will usually be removed. E.g., `unsigned int` will be transformed in `uint`.  `unsigned char` will become `byte`.
- `/*ARRAY*/` allows to treat pointers to fundamental types (such as `int`, `double`) as C# arrays, rather than `ref` values.  The `/*ARRAY*/` string token must not contain extra spaces (see example above).
- Enum types exported with `RH_C_SHARED_ENUM` will be translated to the defined C# counterpart (see below for details).


## 2. Define helper enums for Marshalling

Enums that are found while scanning every *.h* and *.cpp* file in *cpp_dir* will be exported as nested enums in
*AutoNativeMethods.cs*, in the same `UnsafeNativeMethods` class.  These should be C enums.

For example:

```cpp
enum MeshBoolConst : int
{
  mbcHasVertexNormals = 0,
  mbcHasFaceNormals = 1,
  mbcHasTextureCoordinates = 2,
  mbcHasSurfaceParameters = 3,
  mbcHasPrincipalCurvatures = 4,
  mbcHasVertexColors = 5,
  mbcIsClosed = 6
};
```

This can then be used in `RH_C_FUNCTION` lines:

```cpp
RH_C_FUNCTION bool ON_Mesh_GetBool(const ON_Mesh* pMesh, enum MeshBoolConst which)
{
  bool rc = false;
  if (pMesh)
  {
    switch (which)
    {
    case mbcIsClosed:
      rc = pMesh->IsClosed();
      break;
  // other cases omitted
    }
  }
}
```

and will result in this C# enum and the possibility to call it without using any enum value (just the field name)...

```cs
internal enum MeshBoolConst : int
{
  HasVertexNormals = 0,
  HasFaceNormals = 1,
  HasTextureCoordinates = 2,
  HasSurfaceParameters = 3,
  HasPrincipalCurvatures = 4,
  HasVertexColors = 5,
  IsClosed = 6
}


[DllImport(Import.lib, CallingConvention=CallingConvention.Cdecl )]
[return: MarshalAs(UnmanagedType.U1)]
internal static extern bool ON_Mesh_GetBool(IntPtr pMesh, MeshBoolConst which);


//your code
UnsafeNativeMethods.ON_Mesh_GetBool(ptr, UnsafeNativeMethods.MeshBoolConst.IsClosed);
```

Notice that every enum field had some prefixed lower-case acronym, which is removed by *methodgen*.


## 3. Share enum values between the C++ and C\#

Similar to the [Define helper enums for Marshalling](#defining-helper-enums-for-marshalling) step, *methodgen* also allows to harvest enum values directly from any file (being that *.h*, *.cpp*, or anything else) that follows the convention explained here.

Again, every *.h* and *.cpp* file in *lib_C_dir* is parsed, looking for lines starting with `RH_C_SHARED_ENUM_PARSE_FILE`. `RH_C_SHARED_ENUM_PARSE_FILE` can be defined by you as an empty macro:

```cpp
#define RH_C_SHARED_ENUM_PARSE_FILE(path)
#define RH_C_SHARED_ENUM_PARSE_FILE3(path, sectionPrefix, sectionSuffix)
```

`path` becomes then a candidate for shared enum collection.  Every `path` file is then opened, and the tool searches for `#pragma region RH_C_SHARED_ENUM` and processes an enum till `#pragma endregion`.

The complete `RH_C_SHARED_ENUM` syntax will look like this:

```cpp
#pragma region RH_C_SHARED_ENUM [full_cpp_type] [full_cs_type] [options]
   //... enum
#pragma endregion
```

The above code is broken down as follows:

- `full_cpp_type`: the full C++ type name.  This should be the standard way to reference any instance.
- `full_cs_type`: the full C# type name.  This will be the standard way to reference the instance type in .NET.
- `options`: any combination of one single item within each of these sets, `(`**`public`**`|internal)`, `(`**`unnested`**`|nested)`, `(sbyte|byte|`**`int`**`|uint|short|ushort|long|ulong)`, `(flags)`, `(clsfalse)`; separated by a colon (`:`).  If an option from a set is not specified, the one in bold is used.  Sets without a bold item have the option turned off.

### Remarks on options

Keep the following in mind concerning options:

- `nested`: please use this option with care.  See the [.NET design guidelines for nested types on MSDN](https://msdn.microsoft.com/en-us/library/ms229027.aspx).  Keeping class design simple is paramount.
- `type` (`int`, `long`, etc): usually, just choose the corresponding .NET type that is CLSCompliant.  If you choose anything else than a type that is sized the same as the C++ one, you are responsible for differences in array sizes.  Automatic marshalling usually gets the size of single arguments right and casts accordingly.  If the size of the C# element is smaller than the C++ one, there will possibly be problems with uniqueness of fields.  If you use any non-CLS-compliant type, then you might have to add the next option.
- `clsfalse`: marks the resulting enum code with the `[CLSCompliant(false)]` attribute.  Only here for compatibility with already-defined C# enums.
- `flags`: marks the resulting enum code with the `[Flags]` attribute. Always mark the .NET type with this attribute if the enum is used as a bitmask.

### Enum design

<div class="bs-callout bs-callout-danger">
  <h4>WARNING</h4>
  Although similar in purpose, .NET and C++ enums differ considerably both in common usage and in formatting style conventions.  Here we list a few gotchas of which to be aware when defining shared enums.  Read the following list carefully.
</div>

Follow these rules when sharing enums:

- .NET enums are best defined as deriving from CLS-compliant types: `byte`, `short`, `int` and `long`.  When sharing a C++ enum that translates to `sbyte`, `ushort`, `uint`, `ulong`, it might be tempting to use one of these non-CLS-compliant types, and apply the provided option.  *This is a bad idea!*  The option is only there for support of already-existing enums.  Every method with non-CLS-compliant parameters will be non-CLS-compliant.  On the other hand, only a solvable issue with the first bit of high-valued enum fields needs to be addressed when translating an `unsigned int` enum to an `int` one in C#. .NET users of the library will find a library that is simpler to read as well.
- In an enum shared with .NET, do not define sentinel values or fields cautiously reserved for future use.  They are evil.  See the [Enum Design on MSDN](https://msdn.microsoft.com/en-us/library/ms229058%28v=vs.110%29.aspx) to better understand why.
- Because each enum field name will be the same as in .NET, it is best practice not to use constant prefixes like `k` in `kMyEnum`, and not to use `ALL_CAPS`.  Simply use `PascalCase` for enum field names.
- Consider using `class enums` in C++ to avoid naming collisions.  This is not an issue in .NET, because *methodgen* removes the `class` keyword automatically.
- Use .NET-type descriptions also in C++ to comment the enum and each of its field.  A `///<summary>` is usually sufficient.

To illustrate the above rules in action, in a parsed file, place:

```cpp
RH_C_SHARED_ENUM_PARSE_FILE3("../../../opennurbs/opennurbs_subd.h", "#if OPENNURBS_SUBD_WIP", "#endif")
```

Then, within that *opennurbs_subd.h* file:

```cpp
#pragma region RH_C_SHARED_ENUM [ON_SubD::SubDType] [Rhino.Geometry.SubD.SubDType] [nested:byte]
/// <summary>
/// Subdivision algorithm.
/// </summary>  
enum class SubDType : unsigned char
{
  ///<summary>
  /// Built-in Loop-Warren triangle with Bernstein-Levin-Zorin creases and darts.
  ///</summary>
  TriLoopWarren = 3,

  ///<summary>
  /// Built-in Catmull-Clark quad with Bernstein-Levin-Zorin creases and darts.
  ///</summary>
  QuadCatmullClark = 4,
};
#pragma endregion
```

This above will result in an enum called `SubDType`, placed inside a `_public partial_ class SubD`, inside *AutoNativeEnums.cs*.

---

## RH_C_PREPROCESSOR macro

Inside every *.h* and *.cpp* file in *lib_C_dir*, *methogen* keeps track of `#ifdef`, `#ifndef`, `#if defined`, `#elif defined`, `#else` and `#endif` lines marked with an `RH_C_PREPROCESSOR` suffix.  Lines with both preprocessor instructions and the mark will not be removed and will appear in *AutoNativeMethods.cs*, transformed to the appropriate C# representation.

The `RH_C_PREPROCESSOR` string can appear either in plain code or in a comment, provided it is the first word in the comment.  For example:

`#else //RH_C_PREPROCESSOR`

is just as valid as:

`#else RH_C_PREPROCESSOR`

This is because having extra tokens after `#endif` is non-standard C, and some compilers check against this condition.

---

## Related Topics

- [Wrapping Native Libraries]({{ site.baseurl }}/guides/rhinocommon/wrapping_native_libraries)
- [.NET design guidelines for nested types on MSDN](https://msdn.microsoft.com/en-us/library/ms229027.aspx)
- [Enum Design on MSDN](https://msdn.microsoft.com/en-us/library/ms229058%28v=vs.110%29.aspx)
