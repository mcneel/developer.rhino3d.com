---
title: 2.3.1 Integers and Doubles
description:
authors: ['Scott Davidson']
author_contacts: ['scottd']
apis: ['RhinoPython']
languages: ['Python']
platforms: ['Windows', 'Mac']
categories: ['Python Primer']
origin:
order: 8
keywords: ['python', 'commands']
layout: toc-guide-page
---

Integers and Doubles are both numeric variable types, meaning they can be used to store numbers. They cannot store the same kind of numbers, which is why we ended up with more than one type. Integers can only be used to store whole numbers. Their range extends from roughly minus two-
billion to roughly plus two-billion. Every whole number between these extremes can be represented using an integer. Integers are used almost exclusively for counting purposes (as opposed to calculations).

Doubles are numeric variables which can store numbers with decimals. Doubles can be used to represent 
numbers as large as 1.8×10308 and as small as 5.0×10-324, though in practise the range of numbers which can be accurately represented is much smaller. Those of you who are unfamiliar with scientific notation need not to worry, I shall not make a habit out of this. It is enough to know that the numeric range of doubles is truly enormous.
		
<img src="{{ site.baseurl }}/images/primer-integers.svg" width="75%" float="right">

<!--TODO: The font in the SVG above is not rendeirng correctly.  What Font to use -->

The set of all possible Double and Integer numbers is not continuous; it has gaps. There exists no Integer between zero and one and there exists no Double between zero and 5.0×10-324. The fact that the size of the gap is so much smaller with Doubles is only because we’ve picked a number close to zero. As we move towards bigger and 
bigger numbers, the gaps between two adjacent Double values will become bigger as well and as we approach the limits of the range, the gaps are big enough to fit the Milky Way. 2×10300 minus one billion is still 2×10300, so beware when using extremely large numbers. Normally, we never stray into the regions where 32-bit computing starts to break down, we tend to restrict ourselves to numbers we can actually cope with.

The Python syntax for working with numeric variables should be very familiar:

```python
x = 15 + 26				# x equals 41
x = 15 + 26 * 2.33	    #  x equals 75.58
x = math.sin(15 + 26) + math.sqrt(2.33)	# x equals 1.368
```
You can use the `print()` method to display the result of these computations. The `print()` method will display the value in the command-line:

```python
x = 2 * math.sin(15 + 26) + math.log(55)
print(x)
```

Of course you can also use numeric variables on the right hand side of the equation:   

```python
x = x + 1
x = math.sin(y) + math.sqrt(0.5 * y)
```

The first line of code will increment the current value of x by one, the second line will assign a value to x which depends on the value of y. If y equals 34 for example, x will become 4.65218831173768.

Note, there is a special shortcut in Python that allows you to define multiple variables in a single line of code:

```python
x, y, z = [1,2,3]
print x  # returns 1
print y  # returns 2
print z  # returns 3
```

---

#### Related Topics

- [Where to find help - Next Topic >>]({{ site.baseurl }}/guides/rhinopython/primer-101/1-2-where-to-find-help/)
- [Rhino.Python Primer 101]({{ site.baseurl }}/guides/rhinopython/primer-101/rhinopython101)
- [Running Scripts]({{ site.baseurl }}/guides/rhinopython/python-running-scripts)
- [Canceling Scripts]({{ site.baseurl }}/guides/rhinopython/python-canceling-scripts)
- [Editing Scripts]({{ site.baseurl }}/guides/rhinopython/python-editing-scripts)
- [Scripting Options]({{ site.baseurl }}/guides/rhinopython/python-scripting-options)
- [Reinitializing Python]({{ site.baseurl }}/guides/rhinopython/python-scripting-reinitialize)
