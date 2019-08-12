---
title: Task Capable Components
description: A guide to programming multi-threaded components in Grasshopper
authors: ['steve_baer', 'scott_davidson']
sdk: ['Grasshopper']
languages: ['C#']
platforms: ['Windows', 'Mac']
categories: ['Advanced']
origin:
order: 2
keywords: ['developer', 'grasshopper', 'components']
layout: toc-guide-page
---

## Overview

Grasshopper for Rhino 6 allows you to develop multi-threaded components by way of the new `IGH_TaskCapableComponent` interface. Benchmarks have shown that Grasshopper can run significantly faster when using multi-threaded components.  Results may vary, as not all solutions can be computed in parallel.

## The Interface

When a component implements the `IGH_TaskCapableComponent` interface, Grasshopper will notice and potentially call a full enumeration of `SolveInstance` for the component twice in consecutive passes:

1. The first pass is for collecting data and starting tasks to compute results
1. The second pass is for using the results from the tasks to set outputs.

## Example

In this guide, we will convert a standard component into a task capable component.  In our example, the initial component code looks like this:

```cs
public class FibonacciComponent : GH_Component
{
  ...
  protected override void SolveInstance(IGH_DataAccess data)
  {
    const int max_steps = 46;

    int steps = 0;
    data.GetData(0, ref steps);
    if (steps < 0)
    {
      AddRuntimeMessage(GH_RuntimeMessageLevel.Error, "Steps must be >= 0.");
      return;
    }
    if (steps > max_steps) // Prevent overflow...
    {
      AddRuntimeMessage(GH_RuntimeMessageLevel.Error, $"Steps must be <= {max_steps}.");
      return;
    }

    int result;
    if (steps == 0)
      result = 0;
    else if (steps == 1)
      result = 1;
    else
    {
      int x = 0, y = 1, rc = 0;
      for (int i = 2; i <= steps; i++)
      {
        rc = x + y;
        x = y;
        y = rc;
      }
      result = rc;
    }

    data.SetData(0, result);
  }
  ...  
}
```

## Separate Methods

Now you need to separate calculations into separate methods.  Independent tasks should not be directly accessing `IGH_DataAccess`, as that interface is not thread safe. Thus, the we will want to break the current flow of a component’s `SolveInstance` method into three distinct steps:

1. Collect input data
1. Compute results on given data
1. Set output data

To implement *Step 2*, we will break out the computation code into its own method.

To start, create a public `SolveResults` class to hold the data for each `SolveInstance` iteration. For this computation, our definition of `SolveInstance` is very simple:

```cs
public class SolveResults
{
  public int Value { get; set; }
}
```

Create a *Compute* function that takes the input retrieved from `IGH_DataAccess` and returns an instance of `SolveResults`.

```cs
private static SolveResults ComputeFibonacci(int n)
{
  SolveResults result = new SolveResults();
  if (n == 0)
    result.Value = 0;
  else if (n == 1)
    result.Value = 1;
  else
  {
    int x = 0, y = 1, rc = 0;
    for (int i = 2; i <= n; i++)
    {
      rc = x + y;
      x = y;
      y = rc;
    }
    result.Value = rc;
  }
  return result;
}
```

## Implement the Interface

Now, we are ready to launch multiple tasks in the component.

Change the component's inheritance from `GH_Component` to `GH_TaskCapableComponent<T>`. In this example, modify the component from this:

`public class FibonacciComponent : GH_Component`

to this:

`public class FibonacciComponent : GH_TaskCapableComponent<FibonacciComponent.SolveResults>`

Finally, modify `SolveInstance` to use tasks:

```cs
protected override void SolveInstance(IGH_DataAccess data)
{
  const int max_steps = 46;

  if (InPreSolve)
  {
    // First pass; collect input data
    int steps = 0;
    data.GetData(0, ref steps);
    if (steps < 0)
    {
      AddRuntimeMessage(GH_RuntimeMessageLevel.Error, "Steps must be >= 0.");
      return;
    }
    if (steps > max_steps) // Prevent overflow...
    {
      AddRuntimeMessage(GH_RuntimeMessageLevel.Error, $"Steps must be <= {max_steps}.");
      return;
    }

    // Queue up the task
    Task<SolveResults> task = Task.Run(() => ComputeFibonacci(steps), CancelToken);
    TaskList.Add(task);
    return;
  }

  if (!GetSolveResults(data, out SolveResults result))
  {
    // Compute right here; collect input data
    int steps = 0;
    data.GetData(0, ref steps);
    if (steps < 0)
    {
      AddRuntimeMessage(GH_RuntimeMessageLevel.Error, "Steps must be >= 0.");
      return;
    }
    if (steps > max_steps) // Prevent overflow...
    {
      AddRuntimeMessage(GH_RuntimeMessageLevel.Error, $"Steps must be <= {max_steps}.");
      return;
    }

    // Compute results on given data
    result = ComputeFibonacci(steps);
  }

  // Set output data
  if (result != null)
  {
    data.SetData(0, result.Value);
  }
}
```

The full source code for this revision [can be seen here](https://github.com/mcneel/rhino-developer-samples/tree/6/grasshopper/cs/SampleGhTaskCapable).
