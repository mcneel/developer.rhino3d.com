---
title: Python Looping
description: This guide is an overview of looping through Python code.
authors: ['Scott Davidson']
author_contacts: ['scottd']
sdk: ['RhinoPython']
languages: ['Python']
platforms: ['Mac', 'Windows']
categories: ['Fundamentals']
origin:
order: 7
keywords: ['script', 'Rhino', 'python']
layout: toc-guide-page
---


## Overview

Looping allows you to run a group of statements repeatedly.  Some loops repeat statements until a condition is *False*; others repeat statements until a condition is *True*.  There are also loops that repeat statements a specific number of times.

The following looping statements are available in Python:

* `for` - Uses a counter or loops through a each item in a list a specified number of times.
* `while` - Loops while a condition is True.
* Nested loops - Repeats a group of statements for each item in a collection or each element of an array.
* Existing loops - What can be done to exit a loop?

Unlike other languages, Python does not use an end statement for its loop syntax.  Instead, the initial Loop statement is followed by a colon `:` symbol.  Then the next line will be indented by 4 spaces.  Each subsequent line in the loop also needs to be indented by 4 or more spaces.  It is these spaces to the left of the line that are key.

```
for c in range(0, 3):
   This is the the loop
   This is a second line and the last line of the for loop
This line is not part of the loop. It is the first line in the rest of the script.
.....
```

If a line is not indented it is considered outside the loop and will also terminate any additional lines considered in the loop.  A common mistake is remove the spaces and therefore prematurely end the loop.

## For Loop

You can use *for* statements to run a block of statements a specific number of times. 

Using Python to loop through each item in a list based structure is very easy:

```
list1 = [10,25,33,42,59,64]

for i in list1:
    print i

print "This is the end of the function"
```

 The `for` loop will process each member individually.  This syntax will also work directly on any indexable structures like the coordinates of a Point3D, values of a Vector, points of a Line, etc... Other iterable objects can be lists or a string. You can also create you [own iterable objects](https://wiki.python.org/moin/ForLoop#line-110) if needed.

Sometimes it is useful to have a counter variable whose value increases or decreases with each repetition of the loop. The following example causes a procedure to execute 4 times. The `for` statement specifies the counter variable `x` and its start and end values. Python will automatically increments the counter (x) variable by 1 after coming to end of the `for` block.

```python
for x in range(0, 3):
    print "We're on loop " + str(x)
```

Python can use any iterable method as a the for loop counter. In the case above we are using `range()`. In the example below the `range(len())`function is used to coordinate the counter with the number of members in `list1`:   

```
list1 = [10,25,33,42,59,64]

for i in range(len(list1)):
    print list1[i]

print "This is the end of the function"
```

Sometimes it is required to increase or decrease the counter variable by the value you specify. In the following example, the counter variable `j` is incremented by 2 each time the loop repeats. When the loop is finished, the total is the sum of 0, 2, 4, 6 and 8.

```python
for j in range(0, 10, 2):
    print "We're on loop " + str(j)
```

To decrease the counter variable, use a negative `range` value. You must specify an end value that is less than the start value. In the following example, the counter variable `j` is decreased by 2 each time the loop repeats. When the loop is finished, total is the sum of 10, 8, 6, 4, and 2.

```python
 for j in range(10, 0, -2):
    print "We're on loop " + str(j)
```

 You can exit any *for* statement before the counter reaches its end value by using the `break` statement. Because you usually want to exit only in certain situations, such as when an error occurs, you could also use the `if` statement in the *True* statement block. If the condition is *False*, the loop runs as usual.

More information on the `for` loop can be found at the [Python.org For Loops article](https://wiki.python.org/moin/ForLoop).

## While Loop

Use the `while` loop to check a condition before each execution of the loop.

```while
var1 = 2
while var1 < 32:
    var1 = var1 * 2
    print var1
print "Exited while loop."
```

*while* loops are not used as much as *for* loops.  But *while* loops are used often in in cases the following way, polling for specific input or a loop that will execute forever until a condition is met:

```python
while True:
    n = raw_input("Please enter 'hello':")
    if n.strip() == 'hello':
        break
```

As you can see, this compacts the whole thing into a piece of code managed entirely by the while loop. Having True as a condition ensures that the code runs until it's broken by n.strip() equaling 'hello'. 

More information on the `while` loop can be found at the [Python.org While Loop article](https://wiki.python.org/moin/WhileLoop).

## Nested Loops

Python allows for loops to be nested inside one another.  Any type of loop can be nested within any other type of loop. Take note of the progressive spaces to the left of the lines in a nested loop.

```python
for x in range(0, 100):
   if x % 2 == 0:
      print str(x) + " is an even number."
```

Nested loops can also be used to look at each member in nested lists:

```
list_of_points = [ [10, -34, 6], [15, 25, 12], [34, 67, 2]]

for point in list_of_points:
    for c in point:
        print c
        
print "End of the nested list"
```

## Exiting Loops

Sometimes exiting a loop before it finishes its initial loop count.  The 3 statements that can be used are `break`, `continue`, and `pass`.

### Break

The `break` statement will immediately exit the loop after finding a point that has a x coordinate of 15.  The script then executes outside of the loop.  Many times a `break` is used within an `if` statement in the loop:

```
list_of_points = [ [10, -34, 6], [15, 25, 12], [34, 67, 2]]

for point in list_of_points:
        if point[0] == 15:
            break
        print point

print "End of the list"
```
The output here show that once the point with the x coordinate of 15 is hit, the loop is exited.

```
[10, -34, 6]
End of the list
```

### Continue

The `continue` statement is used to stop a single iteration of a loop, but continue to subsequent iterations of the loop.  For instance, using the same example above, but with a `continue statement:

```
list_of_points = [ [10, -34, 6], [15, 25, 12], [34, 67, 2]]

for point in list_of_points:
        if point[0] == 15:
            continue
        print point

print "End of the list"
```
The output will skip any iteration that the continue is triggered.  In this case the output looks like this:

```
[10, -34, 6]
[34, 67, 2]
End of the list
```
The second point was skipped due to the `continue` statement.

### Pass

The `pass` statement is more of a place holder inside a loop.  A `pass` will not affect the execution of a loop, but allows a statement to be placed in a loop syntax:

```
list_of_points = [ [10, -34, 6], [15, 25, 12], [34, 67, 2]]

for point in list_of_points:
        if point[0] == 15:
            pass
        print point

print "End of the list"
```

The output to this loop is identical to a loop without the if statement:

```
[10, -34, 6]
[15, 25, 12]
[34, 67, 2]
End of the list
```

The `pass` is simply there to hold a place in the if statement.  The `pass` statement is commonly used to create placeholders for loops when writing new code. 

---

## Related Topics

- [What are VBScript and RhinoScript?]({{ site.baseurl }}/guides/rhinoscript/what-are-vbscript-rhinoscript)
