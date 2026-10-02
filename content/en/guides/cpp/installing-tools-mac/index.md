+++
aliases = []
authors = [ "andy" ]
categories = [ "Getting Started" ]
description = "This guide covers the tools you need to write Rhino plugins in C/C++ on macOS."
keywords = [ "c", "C/C++", "plugin" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Installing Tools (Mac)"
type = "guides"
weight = 1

[included_in]
platforms = [ "Mac" ]
since = 9

[page_options]
byline = true
toc = true
toc_type = "single"
+++

By the end of this guide you will have everything you need to write, build and debug a C/C++ plugin for Rhino for Mac.

## Rhino 9 for Mac

The C/C++ SDK for Mac is new in Rhino 9. There is no Mac C/C++ SDK for Rhino 8 or earlier.

Download [Rhino 9 for Mac](https://www.rhino3d.com/download/rhino-for-mac/9/latest/) and install it.

Rhino 9 for Mac runs only on Apple silicon - an M-series Mac. Your plugin is built for that processor too, so an Intel Mac cannot be used.

## Xcode

Install [Xcode](https://developer.apple.com/xcode/) from the Mac App Store. It is free.

Xcode brings the compiler and the debugger. You do not have to write your plugin in Xcode if you would rather use another editor, but the compiler it installs is the one that builds your plugin.

After installing it, open Xcode once and let it finish setting itself up. Then install the Command Line Tools:

```
xcode-select --install
```

If the tools are already there, that command tells you so, which is also a good check.

## Homebrew

Homebrew is our preferred package manager on macOS.

Install [Homebrew](https://brew.sh/) from the one-liner on their homepage.

## CMake

You build and debug in Xcode. CMake only generates the Xcode project. You run it once, when you set up a project.

Install [CMake](https://cmake.org/download/) and forget about it until then.

The easiest way to install it is with [Homebrew](https://brew.sh):

```
brew install cmake
```

## Git and Git LFS

The SDK and the samples are on GitHub, so you need Git:

```
brew install git
```

A Mac build does not need Git LFS. Only the SDK's four Windows libraries are kept in Git LFS - the Mac links against small `.tbd` files that Git fetches normally. If you will also build for Windows from the same checkout, install it now:

```
brew install git-lfs
git lfs install
```

You need to run the last line only once on each computer.

## The SDK

You do not install the C/C++ SDK. It lives in a repository:

<https://github.com/mcneel/rhino_sdk_cpp>

You normally add it to your own plugin's repository as a *submodule*, so that the SDK sits in a folder inside your project and everyone who clones your project gets it.

The SDK's own [README](https://github.com/mcneel/rhino_sdk_cpp/blob/main/README.md) is the reference for building against it, and covers both platforms.

## Next Steps

You now have the tools. Go on to [Creating your first C/C++ plugin (Cross-Platform)](/guides/cpp/your-first-plugin-crossplatform/), which builds a working plugin for Rhino for Mac and Rhino for Windows from the same code.
