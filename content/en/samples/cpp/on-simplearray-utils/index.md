+++
authors = [ "dale" ]
categories = [ "Other" ]
description = "Demonstrates how to sort and cull simple arrays."
keywords = [ "rhino" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "ON_SimpleArray Utilities"
type = "samples/cpp"
weight = 1

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/sdksamples/simplearray"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

+++

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
