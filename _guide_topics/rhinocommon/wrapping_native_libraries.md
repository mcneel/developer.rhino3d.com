---
layout: toc-guide-page
title: Wrapping Native Libraries
author: dan@mcneel.com
categories: ['Advanced']
platforms: ['Cross-Platform']
apis: ['RhinoCommon']
languages: ['C#']
keywords: ['Native', 'RhinoCommon', 'Plugin', 'Library', 'PInvoke']
TODO: 0
origin: unset
order: 5
---

# Wrapping Native Libraries

This guide demonstrates how to wrap a C/C++ library in order to call into it from .NET.  

## Overview

We present a sample solution that uses Platform Invoke (PInvoke), which allows .NET code to call functions that are implemented in a C/C++ DLL (Windows) or dylib (Mac OS X).  It is important to understand that the main utility of this advanced approach is in the ability to call the same C/C++ code on both platforms from .NET.  

First, we will build a simple C/C++ library that adds two numbers together.  After that, we will examine the wrapping .NET code required to call into our library from a RhinoCommon plugin on both Windows and Mac.

### Prerequisites

This guide does not presume you are a C/C++ or .NET expert, but assumes you have a functional working knowledge of both.  This is an advanced guide; that said, the intent of this guide is to illustrate basic considerations of wrapping a C/C++ library and the logistical issues calling it from a RhinoCommon plugin on both Windows and Mac.

We will be analyzing a sample solution called **[SampleNativeLibrary](https://github.com/dalefugier/SampleNativeLibrary)**.  Please clone or download this repository.  **SampleNativeLibrary** builds against the RhinoWIP (on Windows) and Rhino 5 for Mac (on OS X).  (On Windows, it is possible to use Rhino 5, but you will have to change the RhinoCommon references).

It is presumed you already have *all* the necessary tools installed and are ready to go.  If you are not there yet, see both [Installing Tools (Windows)]({{ site.baseurl }}/guides/rhinocommon/installing_tools_windows) and [Installing Tools (Mac)]({{ site.baseurl }}/guides/rhinocommon/installing_tools_mac).  It is also helpful to have read and understood [Your First Plugin (Cross-Platform)]({{ site.baseurl }}/guides/rhinocommon/your_first_plugin_crossplatform).

<div class="bs-callout bs-callout-danger">
  <h4>WARNING</h4>
  <p>Other methods to create a .Net binding to a C# library exist. A notorious one is based on the compilation of the C++ library with the C++/CLI compiler. To keep things compatible with the Apple Mac OS, and because the IJW (it just works) technology sometimes does not, we suggest to use PInvoke.</p>
</div>


## SampleLibrary

Let's begin by taking a look at an absurdly simple C/C++ "library" - SampleLibrary - that does one thing: add two numbers together.  We'll start on Windows, but it really doesn't matter if you start on a OS X, nearly everything that follows applies on each platform...

### Windows

1. Open **SampleNativeLibrary.sln** in **Visual Studio**.
1. In the Solution Explorer, you will notice there are three projects...two C# (.csproj) projects and one C++ project.  Expand the **SampleLibrary** C++ project...
![SampleNativeLibrary]({{ site.baseurl }}/images/wrapping_native_libraries_02.png)
1. The **SampleLibrary** (.vcxproj) is just a boilerplate C++ project (created using the regular Shared MFC C++ project wizard) that was created by Visual Studio.  *There is nothing fancy going on here at all; much of the code is not even relevant to this guide*.
1. Open the **SampleLibrary.cpp** file and take a look.  Nearly all of the code in this file is auto-generated boilerplate.  The only important section to pay attention to is:

        SAMPLELIBRARY_C_FUNCTION
        double Add(int a, double b)
        {
          return a + b;
        }  

    ...even if you are not a C/C++ programmer, this C function should be clear to you.  `Add` takes a native `int` and a native `double`, and returns the sum of the inputs as a native `double`.  Take note of the `SAMPLELIBRARY_C_FUNCTION` decoration above the implementation...we will talk about that in a moment.
1. In the **Header Files** filter, find and open the **SampleLibraryInclude.h** header file.  The first thing to note is that there are two well `#defined` sections to this header: one that relates to Windows (`#if defined (_WIN32)`) and one that relates to Mac (`#if defined(__APPLE__)`).  The code in these #defines are basically telling the linker to export functions in a specific way.  The reason they are different on each platform is that Dynamic Link Libraries (DLLs) are implemented differently in Windows and OS X - each platform has a unique way of telling the linker what to do with the library.  How this works is not really important at this juncture, just know that these MACROs tell the linker to export the functions.  More importantly...
1. Take a look at the function declaration at the bottom of the file:

        SAMPLELIBRARY_C_FUNCTION
        double Add(int a, double b);

    ...is decorated with the same `SAMPLELIBRARY_C_FUNCTION`.
1. This is the decoration that tells the linker to make the function available to outside callers.  By decorating with this macro, the linker adds information to the DLL that makes these functions public.  Without this decoration, these functions would not be available outside the the assembly (.dll or .dylib).  By providing this decoration, we are doing the .NET equivalent of making them "public".
1. Do a "sanity check" and **Build** SampleLibrary to make sure that all your tools are working as expected.  SampleLibrary should build without errors as the native *SampleLibrary.dll* in the project */bin* folder.  Ok, now that we know roughly what is in the native SampleLibrary on Windows, let's take a look at it on Mac OS X...

### Mac

1. Launch **Xcode** and open **SampleLibrary.xcodeproj**.  (Unlike Visual Studio on Windows, on OS X, we cannot do all of our development in a single IDE, but we have to build our native C/C++ **SampleLibrary** using the native Apple Tools - Xcode and xcodebuild).
1. In the **Project Navigator**, notice that this project is referencing the *exact same source code* as its Windows counterpart...
![SampleLibrary on OS X]({{ site.baseurl }}/images/wrapping_native_libraries_03.png)
1. Instead of building a .dll, on OS X we are building **libSampleLibrary.dylib** which - despite the extension - amounts to exactly the same thing as a dll.  For all intents and purposes, SampleLibrary does exactly the same thing on OS X that it does on Windows and the source is the same.
1. **Build** SampleLibrary using Xcode to make sure that it builds successfully.  
1. **Quit** Xcode.  On OS X, we are actually going to use command line `xcodebuild` from Xamarin Studio to build our native library, but we'll talk about that below.

Now that we have examined the simple native SampleLibrary, let's turn our attention to the .NET portion of our wrapping code...

## SampleNativeLibrary

SampleNativeLibrary is the .NET project that calls into the SampleLibrary.  On each platform, we are using the exact same wrapping source code, just using cloned .csproj projects on each platform.  (For more information on this cross-platform strategy, see the [Your First Plugin (Cross-Platform)]({{ site.baseurl }}/guides/rhinocommon/your_first_plugin_crossplatform) guide).  

Let's take a look at SampleNativeLibrary on Windows using Visual Studio first...

### Windows

1. If you have not done so already, open the **SampleNativeLibrary.sln** in **Visual Studio**.
1. If you have not done so already, build **SampleLibrary**.  Verify that *SampleLibrary.dll* is present in your */bin* folder.
1. Now, let's turn our attention to the **SampleRhino.Win** project.  Make sure that **SampleRhino.Win** is set as the Startup Project and expand it so you can see the source files...
![SampleRhino on Windows]({{ site.baseurl }}/images/wrapping_native_libraries_04.png)
1. Before we do anything, let's build and test the plugin.  Build **SampleRhino.Win**.
1. Load the **SampleRhino.rhp** in Rhino and run the **SampleRhinoCommand**.  You will be prompted to enter two numbers.  Once you have done that you should see the result in a dialog box...
![SampleRhino plugin test]({{ site.baseurl }}/images/wrapping_native_libraries_05.png)
1. The "additional" calculation for this command was all performed in the native C/C++ SampleLibrary.dll.  Return to **Visual Studio**.  Let's take a look at how the `Add` function is being called.
1. Open **SampleRhinoCommand.cs** and find the `RunCommand` method.  After prompting the user to enter two numbers, we see the following code

        var result = RhinoMath.UnsetValue;
        try
        {
          result = UnsafeNativeMethods.Add(first, second);
        }
        catch (Exception ex)
        {
          RhinoApp.WriteLine(ex.Message);        
          return Result.Failure;
        }
1. The `Add(first, second)` method is being called on the `UnsafeNativeMethods` class.  Open **UnsafeNativeMethods.cs**.  Let's go through this class line-by-line.
1. The necessary functionality to use PInvoke is contained in the `System.Runtime.InteropServices` namespace, specifically the `DllImport` function.
1. **UnsafeNativeMethods.cs** contains the class:

        internal static class Import
        {
          public const string lib = "SampleLibrary.dll";
        }

    ...which declares a `lib` string member.  On Windows, it is necessary to explicitly state the name of the native dll being called (on OS X, a *.dll.config* file is used to point to a .dylib - see below).
1. The `UnsafeNativeMethods` class itself contains a single function...

        internal static extern double Add(int a, double b);

    ...does this look familiar?
1. The `Add` function is decorated with an [Attribute](https://msdn.microsoft.com/en-us/library/z0w1kczw.aspx):

        [DllImport(Import.lib, CallingConvention = CallingConvention.Cdecl)]

    ...this important bit of metadata tells the runtime to look in the native library and call the associated function with a specific language (C) calling convention when the `Add` method is called from .NET.  **This is the point at which the link between the managed .NET code and the unmanaged C/C++ code is established.**
1. Since we are bridging the world of managed and unmanaged code, **we need to be very careful about the types of variables we are using**.  To illustrate this point, let's change the code and see what happens...
1. In **UnsafeNativeMethods** change the function declaration of `Add` to accept `double`s (instead of `int`s) as the first argument...

        internal static extern double Add(double a, double b);
1. **Build** the plugin.  No errors or warnings, right?   Now run the plugin and test the **SampleRhinoCommand** with this change.  Try adding 2 + 2.  What happens?  **2 + 2 no longer equals 4**.  That's bad (hopefully, Rhino did not crash).  The compiler did not detect the error we introduced.  Change the type of argument `a` back to an `int`, rather than a `double` and save the file.
1. **You must ensure that the function in .NET exactly matches the function declaration in the header file made in the unmanaged code** (in this case, in *SampleLibraryInclude.h*).  Managing these correspondences is challenging with all but the most trivial libraries.  In [Using methodgen]({{ site.baseurl }}/guides/rhinocommon/using_methodgen), we will discuss a way of generating these function signatures using a utility program we wrote to maintain RhinoCommon.  Before we do that, let's turn our attention to...

### Mac

1. If you have not done so already, open the **SampleNativeLibrary.sln** in **Xamarin Studio**.
1. The native **SampleLibrary** project cannot be built from Xamarin Studio.  As mentioned above, Xamarin Studio is a .NET only IDE; it cannot build C/C++ projects like Visual Studio.  (We will work around this limitation in a moment).
1. First, let's turn our attention to the **SampleRhino.Mac** project.  Make sure that **SampleRhino.Mac** is set as the Startup Project and expand it so you can see the source files...
![SampleRhino on Mac]({{ site.baseurl }}/images/wrapping_native_libraries_06.png)
1. Just as with **SampleLibrary**, **SampleRhino** is exactly the same source on both platform: the platform-specific *.csproj* files are referencing exactly the same *.cs* files.
1. **Build**, run, and test **SampleRhinoCommand** in Rhino for Mac.  Everything should work as expected.  No surprises here...all the code is the same (if you skipped the [Windows section above](#windows-1), read it now; all of it applies on OS X).
1. There is one critical difference between how the Windows and OS X wrapping works and it has little to do with code.  As we saw above, **UnsafeNativeMethods.cs** contains the class:

        internal static class Import
        {
          public const string lib = "SampleLibrary.dll";
        }

    ...which declares a `lib` string member.  On Windows, it was necessary to explicitly state the name of the native dll being called.  On OS X, this works a little differently.  In order to understand what is different, let's look at how **SampleLibrary.dll** gets built on OS X...
1. In the [SampleLibrary (Mac) section above](#mac), we built SampleLibrary using Xcode.  We mentioned in passing that we could build this using `xcodebuild` command line from Xamarin Studio.  Let's take a look.
1. In the **Solution Explorer**, **double-click** the name of the **SampleRhino.Mac** project to bring up the **Project Options** dialog.  Navigate to the **Build** > **Custom Commands** section...
![SampleRhino.Mac Project Options]({{ site.baseurl }}/images/wrapping_native_libraries_07.png)
1. There are 5 **Custom Commands**:
    1. **Before Build**: This before build steps runs a python script called *build_native.py* that uses `xcodebuild` to build the *SampleLibrary.xcodeproj*, which builds *libSampleLibrary.dylib*.
    1. **After Build 1**: This after build step copies the *SampleLibrary.dll.config* file from the */SampleLibrary* folder to the target folder.  *SampleLibrary.dll.config* creates a mapping between calls to *SampleLibrary.dll* and *libSampleLibrary.dylib*...

            <configuration>
               <dllmap dll=“SampleLibrary.dll” target="libSampleLibrary.dylib" />
            </configuration>

        On OS X, both the *.dll.config* file and the *.dylib* must be in the same folder as the calling .NET dll.
    1. **After Build 2**: This after build step copies *libSampleLibrary.dylib* to the same folder as the calling .NET dll.
    1. **After Clean 1**: This after build step deletes the *libSampleLibrary.dylib* when a clean is performed.
    1. **After Clean 1**: This after build step deletes the *SampleLibrary.dll.config* when a clean is performed.
1. When you **Build** and run **SampleRhino.Mac** you can watch the build steps in the **output** (right) side of the **Errors** panel.  You may notice that *build_native.py* will only build *libSampleLibrary.dylib* if it does not find a previous version.  You can overwrite this with the `-o   --overwrite` command argument if you want to build the native library every time you build the .NET wrapping dll.

---

## Next Steps

You have seen how a basic C/C++ library can be wrapped and called from .NET in a Rhino Plugin.  You have also seen what can go wrong when a native method's export declaration is out-of-sync with its .NET counterpart.  **Now what?**

Check out the [Using methodgen]({{ site.baseurl }}/guides/rhinocommon/using_methodgen) guide for instructions on programmatically generating UnsafeNativeMethods export declarations.

---

## Related topics

- [Microsoft Platform Invoke Tutorial on MSDN](https://msdn.microsoft.com/en-us/library/aa288468(VS.71).aspx)
- [Interop with Native Libraries on mono-project.org](http://www.mono-project.com/docs/advanced/pinvoke/)
- [Attributes on MSDN](https://msdn.microsoft.com/en-us/library/z0w1kczw.aspx)
- [Moose sample on GitHub](https://github.com/dalefugier/Moose)
- [Your First Plugin (Cross-Platform)]({{ site.baseurl }}/guides/rhinocommon/your_first_plugin_crossplatform)
- [Using methodgen]({{ site.baseurl }}/guides/rhinocommon/using_methodgen)
