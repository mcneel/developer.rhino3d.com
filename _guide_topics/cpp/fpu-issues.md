---
title: FPU Issues
description: This guide discusses math errors and floating point unit issues.
authors: ['Dale Fugier']
author_contacts: ['dale']
sdk: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Troubleshooting']
origin: http://wiki.mcneel.com/developer/sdksamples/fpusloppycall
order: 1
keywords: ['rhino', 'errors', 'floating-point']
layout: toc-guide-page
---

 
## Problem

When your plugin tries to perform a certain calculation, you get the following text in Visual Studio's output window:

```
[[developer:opennurbs:home|opennurbs]] ERROR # 2 .\rhino3MathErrorHandling.cpp:154 Serious math library or floating point errors occurred.

[[developer:opennurbs:home|opennurbs]] ERROR # 3 .\opennurbs_plus_fpu.cpp:289 ON_FPU_BeforeSloppyCall - fpu STAT is already dirty. See source comment for next steps.
```

## Workaround

These two opennurbs errors are most likely related.

Sometimes it is impossible to avoid calling code that performs invalid floating point operations or rudely changes the FPU control settings.  We have found dozens of cases in Windows core DLLs, 3rd party DLLs, OpenGL drivers, VBScript, and the .NET JIT compiler where the FPU CTRL setting is changed or floating point exceptions are generated.  When these cases are discovered, we bracket the code that is abusing the FPU with:

```cpp
ON_FPU_BeforeSloppyCall();
// call that abuses the FPU
ON_FPU_AfterSloppyCall();
```

In doing this, we don't lose any information about exceptions in our own code and we don't get pestered about exceptions we can't do anything about.  (Note, if you are calling something that may run the .NET JIT, then use `ON_FPU_AfterDotNetJITUse` instead of `ON_FPU_AfterSloppyCall`).

Also, the following error occurs when a serious divide by zero, overflow, or invalid operation happened sometime before the call to `ON_FPU_BeforeSloppyCall`:

```
[[developer:opennurbs:home|opennurbs]] ERROR # 3 .\opennurbs_plus_fpu.cpp:289 ON_FPU_BeforeSloppyCall - fpu STAT is already dirty. See source comment for next steps.
```

These are easy to find.  Start Rhino, run `TestErrorCheck` and set `CrashOnFPUException=Yes`.  Then do whatever it is that made the FPU dirty.  You will crash on the line that is dividing by zero, overflowing, or performing the invalid operation.
