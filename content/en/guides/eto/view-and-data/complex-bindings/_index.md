+++
aliases = []
authors = [ "callum" ]
categories = [ "Eto"]
description = "Complex Bindings in Eto"
keywords = [ "Eto", "UI", "Plugin", "DataContext", "Data", "View", "Model", "Binding" ]
languages = [ "C#" ]
sdk = [ "Eto" ]
title = "Complex Bindings"
type = "guides"

[admin]
TODO = ""
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ ]

[page_options]
byline = true
toc = true
toc_type = "single"
+++

{{< call-out note "View Models" >}}
  This section is not for Python, python cannot use View Models and bindings in the same way as C#.
{{< /call-out >}}

## Introduction
If you haven't read [the introductory page](../binding) on bindings, start there.

Bindings in Eto are very powerful, very easy to chain together and as such can get complex. This page attempts to break all the exciting things that can be done with bindings and then use those knowledge chunks to build some of those complex bindings.

## Conversions
### Convert\<T>


``` cs

```


### OfType\<T>


``` cs

```


### ToBool
ToBool offers an easy way to convert `bool?` and `bool`.

``` cs

```

### EnumToString


``` cs

```

### Child


``` cs

```


### Inverse


``` cs

```


### DefaultIfNull


``` cs

```


## Timings
### After Delay
<!-- This needs a good example -->


``` cs

```


## Misc
### Catch Exception


``` cs

```


### GetValue & SetValue <-- No idea what these do mate


``` cs

```


## More Reading
- [Eto Wiki Binding](https://github.com/picoe/Eto/wiki/Data-Binding)