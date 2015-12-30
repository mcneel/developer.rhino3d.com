---
layout: code-sample-cpp
title: ON_SimpleArray Utilities
author: dale@mcneel.com
platforms: ['Windows']
apis: ['C/C++']
languages: ['C/C++']
keywords: ['rhino']
categories: ['Unsorted']
origin: http://wiki.mcneel.com/developer/sdksamples/simplearray
description: Demonstrates how to sort and cull simple arrays.
order: 1
---

```cpp
void SortDoubles( ON_SimpleArray<double>& arr, bool bIncreasing = true )
{
  if( arr.Count() > 1 )
  {
    if( bIncreasing )
      arr.QuickSort( &ON_CompareIncreasing<double> );
    else
      arr.QuickSort( &ON_CompareDecreasing<double> );
  }
}

void CullDoubles( ON_SimpleArray<double>& arr, double tolerance = ON_ZERO_TOLERANCE )
{
  const int count = arr.Count();
  if( count > 1 )
  {
    arr.QuickSort( &ON_CompareIncreasing<double> );

    if( tolerance < ON_ZERO_TOLERANCE )
      tolerance = ON_ZERO_TOLERANCE;

    double d = *arr.Last();
    int i;
    for( i = count - 2; i >= 0; i-- )
    {
      if( fabs(d - arr[i]) <= tolerance )
        arr.Remove(i);
      else
        d = arr[i];
    }

    arr.Shrink();
  }
}
```
