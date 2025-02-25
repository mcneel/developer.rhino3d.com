+++
aliases = [ ]
authors = [ "callum"]
categories = [ "Eto" ]
description = "An overview of using async within a Rhino and Eto context."
keywords = [ "rhino", "developer", "eto", "ui", "ux" ]
languages = [ "C#" ]
sdk = "eto"
title = "Async in Eto and Rhino"
type = "guides"

[admin]
TODO = ""
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]

+++

{{< call-out info "No Python yet" >}}
  This guide does not cover async within the python context.
{{< /call-out >}}

## Fear not
Asynchronous programming can seem like a tricky and even dangerous part of desktop programming, but this page will steer you in a safe direction away from potential crashes or a frozen rhino.

# The Line
As Rhino is synchronous, our plugins and associated UIs must draw a clear line between sync and async. This is a very good line to understand clearly, and this page will go over it in detail.

There are 3 ways async and non async can mix, with mixed outcomes.

### 1. Events
Events are a quite seamless line between async and non-async. They allow us to use await async code, and run tasks nicely in the background as we'd like async to do. They can however crash if not created carefully.

``` cs
using Rhino;

// synchronous event invoker
RhinoApp.Idle += MyEvent;

// asynchronous event handler
async void MyEvent(object sender, System.EventArgs e)
{
  RhinoApp.Idle -= MyEvent;
}
```

### 2. Eto Invoke
Eto's [AsyncInvoke](http://pages.picoe.ca/docs/api/html/M_Eto_Forms_Application_AsyncInvoke.htm) provides an asynchronous context within synronous methods. This method also has the same crash potential as described below with `async void`.

``` cs
using Eto.Forms;

Eto.Forms.Application.Instance.AsyncInvoke(async () => { /* .. code .. */ });
```

### 3. Non-awaiting
Async code lets us perform tasks on a separate thread, often with tasks that are io-based, that is reading/writing files and creating HTTP calls, and awaiting results. But awaiting results, isn't mandatory.

Normally the HttpClient would use `await` to await the results of the post and act based on the result, if we do not, execution will carry on. There are limited circumstances where this is useful, and either of the two above scenarios are much better.

``` cs
var http = new System.Net.Http.HttpClient();
http.PostAsync("https://example.org", null);
```

# Scenarios to be aware of
{{< call-out warning "Crashing & Blocking" >}}
  Read this section carefully, using any of the examples below will result in unrecoverable scenarios such as rhino crashing or requiring a force quit.
  Please save any work you have _before_ running these samples.
{{< /call-out >}}

### async void
If an exception happens inside an async void, the exception will not be caught, and likely your plugin/rhino will crash. However, async void cannot be avoided when making normal events async.

This will not catch the exception, and therefore crash.
``` cs
using System;

using Rhino;

RhinoApp.Idle += MyEvent;

async void MyEvent(object sender, EventArgs e)
{
  throw new NullReferenceException("This will crash the program");
}
```

This will catch the exception, and not crash.
``` cs
using System;

using Rhino;

RhinoApp.Idle += MyEvent;

async void MyEvent(object sender, EventArgs e)
{
  RhinoApp.Idle -= MyEvent;
  try
  {
    throw new NullReferenceException("This will NOT crash the program");
  }
  catch(Exception ex)
  {
    RhinoApp.WriteLine("Thank gosh we caught that exception!");
  }
}
```

### Blocking with await
Async can never be awaited (safely) in synchronous contexts. There is no safe way to do this.

This will freeze your Rhino.
``` cs
using System;
using System.Threading.Tasks;

using Rhino;

async Task<bool> MyAsyncMethod()
{
  await Task.Delay(2000);
  return true;
}

var result = MyAsyncMethod().Result;

RhinoApp.WriteLine("Done!");
```

This will also freeze your Rhino.
``` cs
using System;
using System.Threading.Tasks;

using Rhino;

async Task<bool> MyAsyncMethod()
{
  await Task.Delay(2000);
  return true;
}

var result = MyAsyncMethod().GetAwaiter().GetResult();

Rhino.RhinoApp.WriteLine("Done!");
```

### Further Reading
- [Avoiding Async Deadlocks](https://medium.com/rubrikkgroup/understanding-async-avoiding-deadlocks-e41f8f2c6f5d)