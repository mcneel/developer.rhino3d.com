---
title: Parentheses
description: This guide discusses the Cannot use parentheses when calling a Sub error that occurs in RhinoScript.
author: ['Dale Fugier', '@dale']
apis: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['Miscellaneous', 'Intermediate']
origin: http://wiki.mcneel.com/developer/scriptsamples/parentheses
order: 1
keywords: ['script', 'Rhino', 'vbscript']
layout: toc-guide-page
---

# {{ page.title }}

{{ page.description }}

## Problem

Every now and then, you may get the error message "Cannot use parentheses when calling a Sub" when calling a function or method.  This does not happen all the time.  For example, the following code appears to work:

```vbnet
Result = MyFunc(MyArg)
MySub(MyArg)
```

...but this code does not work:

```vbnet
Result = MyOtherFunc(MyArg1, MyArg2)
MyOtherSub(MyArg1, MyArg2)
```

## Solution

In VBScript, parentheses mean several different things:

Evaluate a subexpression before the rest of the expression.  For example:

```vbnet
Average = (First + Last) / 2)`
```

or...

Dereference the index of an array.  For example:

```vbnet
Item = MyArray(Index)
```

or...

Call a function or subroutine.  For example:

```vbnet
Limit = UBound(MyArray)
```

or...

Pass an argument which would normally be `ByRef` as `ByVal`.  For example...

```vbnet
'Arg1 is passed ByRef, Arg2 is passed ByVal.
Result = MyFunction(Arg1, (Arg2))
```

And, there are additional rules that apply when calling a function or subroutine...

An argument list for a function call with an assignment to the returned value must be surrounded by parentheses.  For example:

```vbnet
Result = MyFunc(MyArg)
```

An argument list for a subroutine call, or a function call with no assignment, that uses the `Call` keyword must be surrounded by parentheses.  For example:

```vbnet
Call MySub(MyArg)
```

If the above two rules do not apply, then the list must not be surrounded by parentheses.

Finally, there is the `ByRef` rule: arguments are passed `ByRef` when possible.  But, if there are extra parentheses around a variable, then the variable is passed `ByVal`, not `ByRef`.

From these rules, it should be clear why the statement `MySub(MyArg)` is legal but `MyOtherSub(MyArg1, MyArg2)` is not. The first case appears to be a subroutine call with parentheses around the argument list, but that would violate the rules. Then why does this work?  In fact, it is a subroutine call with no parentheses around the argument list, but parentheses around the first argument.  This passes the argument by value. The second case is a clear violation of rules, and there is no way to make it legal, so an error is given.

## Examples

Here are some examples to what is legal and what is not in VBScript. Suppose `X` and `Y` are variables, `Func1` is a one argument procedure, and `Func2` is a two argument procedure.

To pass `X` `ByRef` and `Y` `ByRef`:

```vbnet
Func1 X
Call Func1(X)
Z = Func1(X)
Func2 X, Y
Call Func2(X, Y)
Z = Func2(X, Y)
```

To pass `X` `ByVal` and `Y` `ByRef`:

```vbnet
Func1(X)
Call Func1((X))
Z = Func1((X))
Func2 (X), Y
Func2 ((X)), Y
Call Func2((X), Y)
Z = Func2((X), Y)
```

The following will give syntax errors:

```vbnet
Call Func1 X
Z = Func1 X
Func2(X, Y)
Call Func2 X, Y
Z = Func2 X, Y
```
