+++
aliases = ["/en/5/guides/rhinoscript/vbscript-logic/", "/en/6/guides/rhinoscript/vbscript-logic/", "/en/7/guides/rhinoscript/vbscript-logic/", "/en/wip/guides/rhinoscript/vbscript-logic/"]
authors = [ "dale" ]
categories = [ "Fundamentals" ]
description = "This guide discusses the logic, or lack of, in VBScript."
keywords = [ "script", "Rhino", "vbscript" ]
languages = [ "VBScript" ]
sdk = [ "RhinoScript" ]
title = "VBScript Logic"
type = "guides"
weight = 6
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
TODO = ""
origin = "http://wiki.mcneel.com/developer/scriptsamples/vbslogic"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"
+++

 
## Logic?

Consider the following statements:

```vbnet
If blnResult = True Then Print "True!" Else Print "False!"
```

and

```vbnet
If blnResult Then Print "True!" Else Print "False!"
```

Is there a difference?

## What Logic?

Yes, there is a big difference.  If `blnResult` is True or False, then both statements do what you would expect – the same thing.  But, the first statement is asking "Is `blnResult` equal to True?" whereas the second question is asking "Is `blnResult` not equal to False?"

In a strictly Boolean world, those are equal statements.  But the VBScript type system is richer than just Booleans.

## Details

For example, what if - in the above example - `blnResult` is the string True?  The string True is not equal to the Boolean True, so the first statement is false.  But the string is also not equal to False, so the second statement is true, and the statements have different semantics.

The same goes for numbers. When converted to a number, True converts to -1 (for reasons which will become clear in a moment) and False converts to 0. So, if `blnResult` is 1, again the first statement is false because 1 <> -1, and the second statement is true because 1 <> 0.

What's going on is that VBScript is not logical.  VBScript is bitwise.  All the so-called logical operators work on numbers, not on Boolean values.  `Not`, `And`, `Or`, `XOr`, `Eqv` and `Imp` all convert their arguments to four-byte integers, do the logical operation on each pair of bits in the integers, and return the result.  If True is -1 and False is 0 then everything works out, because -1 has all its bits turned on and 0 has all its bits turned off.  But if other numbers get in there, all bets are off.

This can lead to some strange situations if you're not careful.  In VBScript, it is certainly possible for...

```vbnet
If blnResult Then
```

and

```vbnet
If blnAnswer Then
```

to be both true, but

```vbnet
If Blah And Foo Then
```

to be false, if `blnResult` is 1 and `blnAnswer` is 2, for example.

## Best Practices

Conditional statements should always take Booleans.  Or, in other words, use Booleans as Booleans.  Use nothing else as Booleans.

Suppose you've got a method that returns a number and you want to do something if it doesn't return zero.  Don't do this, even though it does exactly what you want:

```vbnet
If intResult Then
```

it's clearer to call it out and make the conditional take a Boolean:

```vbnet
If intResult <> 0 Then
```

Conversely, if a value is a Boolean and you know that, there's no need to compare it.  When you see:

```vbnet
If blnResult = True Then
```

If blnResult can only contain True or False, then you can just say

```vbnet
If Blah Then
```

Use the same practice with logical operators.  Do not mix-and-match.  Either every argument should explicitly be a number and you're doing bitwise comparisons, or every argument is a Boolean.  Mixing the two makes the code harder to read and more bug-prone.
