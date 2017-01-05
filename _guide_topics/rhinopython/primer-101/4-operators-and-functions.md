---
title: 4 Operators and functions
description:
authors: ['Skylar Tibbits', 'Arthur van der Harten', 'Steve Baer']
author_contacts: ['steve']
apis: ['RhinoPython']
languages: ['Python']
platforms: ['Windows', 'Mac']
categories: ['Python Primer']
origin:
order: 15
keywords: ['python', 'commands']
layout: toc-guide-page
---

## 4.1 What on earth are they and why should I care?

When we were discussing numeric variables in paragraph 2.3.1, there was an example about mathematical operations on numbers:

```python
x = 15 + 26 * 2.33
x = math.sin(15 + 26) + math.sqrt(2.33)
x = math.tan(15 + 26) / math.log(55)
```

The four lines of code above contain four kinds of code:

1. Numbers		`15, 26, 2.33 and 55`
2. Variables	`x` 
3. Operators	`=, +, * and /`
4. Functions    `math.sin(), math.sqrt(), math.tan() and math.log()`

Numbers and variables are well behind us now. Arithmetic operators should be familiar from everyday life, Python uses them in the same way as you used to during math classes. Python comes with a limited amount of arithmetic operators and they are always positioned between two variables or constants (a constant is a fixed number).  The function first signifies that we have imported math at the top of our code, using "import math", and then call a function that is within the math module called "sin()". Thus we write: math.sin(value). 

<img src="{{ site.baseurl }}/images/primer-operators.svg" width="95%" float="right">

<!--TODO: The font in the SVG above is not rendeirng correctly.  What Font to use -->

## 4.2 Careful…

One thing to watch out for is operator precedence. As you will remember from math classes, the addition and the multiplication operator have a different precedence. If you see an equation like this:

```python
x = 4 + 5 * 2

x = (4 + 5) * 2		# wrong precedence
x = 4 + (5 * 2)		# correct precedence
```

x doesn't equal 18, even though many cheap calculators seem to disagree. The precedence of the multiplication is higher which means you first have to multiply 5 by 2, and then add the result to 4. Thus, x equals 14. Python is not a cheap calculator and it has no problems whatsoever with operator precedence. It is us, human beings, who are the confused ones. The example above is fairly straightforward, but how would you code the following?

<img src="{{ site.baseurl }}/images/primer-formula.svg" width="35%" float="right">

<!--TODO: The font in the SVG above is not rendeirng correctly.  What Font to use -->

Without extensive use of parenthesis, this would be very nasty indeed. By using parenthesis in equations we can force precedence, and we can easily group different bits of mathematics. All the individual bits in the mathematical notation have been grouped inside parenthesis and extra spaces have been inserted to accentuate transitions from one top level group to the next:

```python
y = ( math.sqrt(x ** 2 + (x - 1)) / (x - 3) )   +   abs( (2 * x) / (x ** (0.5 * x)) )
```

It is still not anywhere near as neat as the original notation, but I guess that is why the original notation was invented in the first place. Usually, one of the best things to do when lines of code are getting out of hand, is to break them up into smaller pieces. The equation becomes far more readable when spread out over multiple lines of code:

```python
A = x**2 + (x-1)
B = x-3
C = 2*x
D = x**(0.5* x)
y = (math.sqrt(A) / B) + abs(C / D)
```
## 4.3 Logical operators

I realize the last thing you want right now is an in-depth tutorial on logical operators, but it is an absolute must if we want to start making smart code. I'll try to keep it as painless as possible. 

Logical operators mostly work on booleans and they are indeed very logical. As you will remember, booleans can only have two values. Boolean mathematics were developed by George Boole (1815-1864) and today they are at the very core of the entire digital industry. Boolean algebra provides us with tools to analyze, compare and describe sets of data. Although George originally defined six boolean operators we will only discuss three of them:

1. Not
2. And
3. Or

The Not operator is a bit of an oddity among operators. It is odd because it doesn't require two values. Instead, it simply inverts the one on the right. Imagine we have a script which checks for the existence of a bunch of Block definitions in Rhino. If a block definition does not exist, we want to inform the user and abort the script. The English version of this process might look something like:

```
Ask Rhino if a certain Block definition exists
If not, abort this sinking ship
```

The more observant among you will already have noticed that English version also requires a "not" in order to make this work. Of course you could circumvent it, but that means you need an extra line of code:

```
Ask Rhino if a certain Block definition exists
If it does, continue unimpeded
Otherwise, abort
```

When we translate this into Python code we get the following:

```python
if (not rs.IsBlock("SomeBlockName")):
	print ("Missing block definition: SomeBlockName")
```

And and Or at least behave like proper operators; they take two arguments on either side. The And operator requires both of them to be True in order for it to evaluate to True. The Or operator is more than happy with a single True value. Let's take a look at a typical 'one-beer-too-many' algorithm:

```python
person = GetPersonOverThere()
colHair = GetHairColour(person)

if((IsGirl(person)) and (colHair == Blond or colHair == Brunette) and (Age(person) >= 18)):
    neighbour = GetAdjacentPerson(person)
    if(not IsGuy(neighbour) or not LooksStrong(neighbour)):
        print("Hey baby, you like Heineken?")
    else:
        RotateAngleOfVision 5.0
```
As you can see the problem with Logical operators is not the theory, it's what happens when you need a lot of them to evaluate something. Stringing them together, quickly results in convoluted code not to mention operator precedence problems. 

A good way to exercise your own boolean logic is to use Venn-diagrams. A Venn diagram is a graphical representation of boolean sets, where every region contains a (sub)set of values that share a common property. The most famous one is the three-circle diagram:

<img src="{{ site.baseurl }}/images/primer-venn-1.svg" width="50%" float="right">

<!--TODO: The font in the SVG above is not rendeirng correctly.  What Font to use -->

Every circular region contains all values that belong to a set; the top circle for example marks off set {A}. Every value inside that circle evaluates True for {A} and every value not in that circle evaluates False for {A}. If you're uncomfortable with "A, B and C", you can substitute them with *"Employed"*, *"Single"* and *"HomeOwner"*. By coloring the regions we can mimic boolean evaluation in programming code:

<img src="{{ site.baseurl }}/images/primer-venn-2.svg" width="100%" float="right">

<!--TODO: The font in the SVG above is not rendeirng correctly.  What Font to use -->

Try to color the four diagrams below so they match the boolean logic:

<img src="{{ site.baseurl }}/images/venn-blank.svg" width="100%" float="right">

<!--TODO: The font in the SVG above is not rendeirng correctly.  What Font to use -->

Venn diagrams are useful for simple problems, but once you start dealing with more than three regions it becomes a bit opaque. The following image is an example of a 6-regional Venn diagram. Pretty, but not very practical:

<img src="{{ site.baseurl }}/images/venn-complex.svg" width="35%" float="right">

<!--TODO: The font in the SVG above is not rendeirng correctly.  What Font to use -->

## 4.4 Functions and Procedures

In the end, all that a computer is good at is shifting little bits of memory back and forth. When you are drawing a cube in Rhino, you are not really drawing a cube, you are just setting some bits to zero and others to one. 
At the level of Python there are so many wrappers around those bits that we can't even access them anymore. A group of 32 bits over there happens to behave as a number, even though it isn't really. When we multiply two numbers in Python, a very complicated operation is taking place in the memory of your PC and we may be very thankful that we are never confronted with the inner workings. As you can imagine, a lot of multiplications are taking place during any given second your computer is turned on and they are probably all calling the same low-level function that takes care of the nasty bits. That is what functions are about, they wrap up nasty bits of code so we don't have to bother with it. This is called encapsulation.

A good example is the *math.sin()* function, which takes a single numeric value and returns the sine of that value. If we want to know the sine of -say- 4.7, all we need to do is type in *x = math.sin(4.7)*. Internally the computer might calculate the sine by using a digital implementation of the Taylor series:

<img src="{{ site.baseurl }}/images/taylorseries2.png" width="30%" float="right">

In other words: you don't want to know. The good people who develop programming languages predicted you don't want to know, which is why they implemented a *math.sin()* function. Python comes with a long list of predefined functions all of which are available to RhinoScripters. Some deal with mathematical 
computations such as *math.sin()*, others perform String operations such as *abs()* which returns the absolute value. Python lists 75 native procedures plus many more in any of the modules that can be imported (i.e. the *math* module). I won't discuss them here, except when they are to be used in examples.

Apart from implementing the native Python functions, Rhino adds a number of extra ones for us to use. The current RhinoScript helpfile for Rhino5 claims a total number of about 800 additional functions, and new ones are added frequently. Rhino's built in functions are referred to as "methods". They behave exactly the same as Python procedures although you do need to look in a different helpfile to see what they do. [http://www.rhino3d.com/5/ironpython/index.html](http://www.rhino3d.com/5/ironpython/index.html)

So how do functions/procedures/methods behave? Since the point of having procedures is to encapsulate code for frequent use, we should expect them to blend seamlessly into written code. In order to do this they must be able to both receive and return variables. *math.sin()* is an example of a function which both requires and returns a single numeric variable. The *datetime.now()* function on the other hand only returns a single value which contains the current date and time. It does not need any additional information from you, it is more than capable of finding out what time it is all by itself. An even more extreme example is the *rs.Exit()* method which does not accept any argument and does not return any value. There are two scenarios for calling procedures. We either use them to assign a value or we call them out of the blue:

```python
strPointID = rs.AddPoint([0.0, 0.0, 1.0])	# Correct
rs.AddPoint([0.0, 0.0, 1.0])			    # Correct
rs.AddPoint [0.0, 0.0, 1.0]			        # Wrong
```

If you look in the RhinoScript helpfile and search for the *AddLayer()* method, you'll see the following text:

```python
rs.AddLayer (name=None, color=0, visible=True, locked=False, parent=None)
```

*rs.AddLayer()* is capable of taking five arguments, all of which are optional. We can tell they are optional because it says *"Optional"* next to each item under the *"Parameters"* section of the helpfile. The *"Parameters"* signify the Input values for the Function, while the *"Returns"* section tells us what the Function will return. Optional arguments have a default value which is used when we do not override it. If we omit to specify the `lngColor` argument for example the new layer will become black.

### 4.4.1 A simple function example

This concludes the boring portion of the primer. We now have enough information to actually start making useful scripts. I still haven't told you about loops or conditionals, so the really awesome stuff will have to wait until Chapter 5, though. We're going to write a script which uses some Python functions and a few RhinoScript methods. Our objective for today is to write a script that applies a custom name to selected objects. First, I'll show you the script, then we'll analyze it line by line:

<table>
<tr>
<td width="10%">
1
2
3
4
5
6
7
8
9
10
11	
</td>
<td>	
import rhinoscriptsyntax as rs
import time
#This script will rename an object using the current system time

strObjectID = rs.GetObject("Select an object to rename",0,False,True)

if strObjectID:

   strNewName = "Time: " + str(time.localtime())
    
   rs.ObjectName(strObjectID, strNewName)</td>
</tr>
</table>


|--:|:-------------------------------|
| 1 | ```import rhinoscriptsyntax as rs``` |
| 2 | ```import time``` |

#This script will rename an object using the current system time

strObjectID = rs.GetObject("Select an object to rename",0,False,True)

if strObjectID:

   strNewName = "Time: " + str(time.localtime())
    
   rs.ObjectName(strObjectID, strNewName)
	
<!-- TODO: The table code block with line number goes here. -->

This is a complete script file which can be run directly from the disk. It adheres to the basic script structure according to page 13.

We'll be using two variables in this script, one to hold the ID of the object we're going to rename and one containing the new name. On line 5 we declare a new variable. Although the "str" prefix indicates that we'll be storing Strings in this variable, that is by no means a guarantee. You can still put numbers into something that starts with str.  It is simply the convention to name a variable with strSomething if it is storing a string, similarly you can use intSomething for integers etc.

On line 5, we're assigning a value to *strObjectID* by using the RhinoScript method *GetObject()* to ask the user to select an object. The help topic on *GetObject()* tells us the following:

```python
Rhino.GetObject (message=None,filter=0,preselect=False,Select=False,custom_filter=None,subobjects=False)
```

```
Returns:
String		» The identifier of the picked object if successful.
None		» If not successful, or on error.
```

This method accepts six arguments, all of which happen to be optional. In our script we're only specifying the first and fourth argument. The *strMessage* refers to the String which will be visible in the command-line during the picking operation. We're overriding the default, which is "Select object", with something a bit more specific. The second argument is an integer which allows us to set the selection filter. The default behavior is to apply no filter; all objects can be selected whether they are points, textdots, polysurfaces, lights or whatever. We want the default behavior. The same applies to the third argument which allows us to override the default behavior of accepting preselected objects. The fourth argument is False by default, meaning that the object we pick will not be actually selected. This is not desired behavior in our case. The fifth argument takes a bit more explaining so we'll leave it for now.

Note that we can simply omit optional arguments and put a closing bracket after the last argument that we do specify.

When the user is asked to pick an object -any object- on line 5, there exists a possibility they changed their mind and pressed the escape button instead. If this was the case then *strObjectID* will not contain a valid Object ID, it will be None instead. If we do not check for variable validity (line 7) but simply press on, we will get an error on line 11 where we are trying to pass that None value as an argument into the *rs.ObjectName()* method. We must always check our return values and act accordingly. In the case of this script the proper reaction to an Escape is to abort the whole thing. The If: structure on Line 7 will abort the current script if *strObjectID* turns out to be None. 

If *strObjectID* turns out to be an actual valid object identifier, our next job is to fabricate a new name and to assign it to the selected object. The first thing we need is a variable which contains this new name. We declare it and assign it a value on line 9.

The name we are constructing always has the same prefix but the suffix depends on the current system time. In order to get the current system time we use the *time.localtime()* function which is a function built into the time module (which we have imported at the top of our script). Since a Time and a String are not the same thing, we cannot concatenate them with the ampersand operator. We must first convert the Time into a valid String representation. The *str()* function is another Python native function which is used to convert non-string variables into Strings. When I tested this script, the value assigned to *strNewName* at line 11 was:

```
Time: (2011, 3, 10, 22, 17, 53, 3, 69, 0)
```

Finally, at line 11, we reach the end of our quest. We tell Rhino to assign the new name to the old object:

<img src="{{ site.baseurl }}/images/primer-objectname.jpg" width="40%" float="right">

Instead of using *strNewName* to store the name String, we could have gotten away with the following:

```python
rs.ObjectName(strObjectID, "Time: " & str(time.localtime()))
```

This one line replaces lines 9 through 11 of the original script. Sometimes brevity is a good thing, sometimes not. Especially in the beginning it might be smart to be explicit and take up multiple lines; it makes debugging a lot easier (until you feel comfortable making your code shorter and possibly harder to decipher).

### 4.4.2 Advanced function syntax

Whenever you call a function it always returns a value, even if you do not specifically set it. By default, every function returns a *None* value, since this is the default value for all variables and functions in Python. So if you want to write a function which returns you a String containing the alphabet, doing this is not enough:

```python
def Alphabet():
    strSeries = "abcdefghijklmnopqrstuvwxyz"
```

The word "def" signifies the start of a function.  "Alphabet" is a name we have made-up for our function.  Again, the indentation indicates that line 2 is within the function and should only be run after the function is called.  

Although the function actually assigns the alphabet to the variable called strSeries, this variable will go out of scope once the function ends on line #2 and its data will be lost. You have to assign the return value to the function 
name, like so:

```python
def Alphabet():
    strSeries = "abcdefghijklmnopqrstuvwxyz"
    return strSeries

print Alphabet()
```	

The "return value" identifies what will be returned once the method is called and the code within its scope is executed.  When this code is run, it will call the function *Alphabet()*, the code within the function's scope will be run and the function will return the value of strSeries.  This returned value will then be printed to the command line.  It should be noted that at first glance, the return and print functions appear to be very similar.  However, they are not! *print()* will print anything to the command line and console.  return(), on the other hand, will only return a value from a function - basically assigning a value to a variable whenever the function was called. Return is used for the output of a function (in this case the function "Alphabet"), print is used for debugging code or whenever the user wants to see a value printed to the screen.

Imagine you want to lock all curve objects in the document. Doing this by hand requires three steps and it will ruin your current selection set, so it pays to make a script for it. A function which performs this task might fail if there are no curve objects to be found. If the function is designed-not-to-fail you can always call it without thinking and it will sort itself out. If the function is designed-to-fail it will crash if you try to run it without making sure everything is set up correctly. The respective functions are:

```python
def lockcurves_fail():
    rs.LockObjects(rs.ObjectsByType(rs.filter.curve))
```

```python
def lockcurves_nofail():
    curves = rs.ObjectsByType(rs.filter.curve)
    if not curves: return False
    rs.LockObjects(curves)
    return True
```

If you call the first function when there are no curve objects in the document, the *rs.ObjectsByType()* method will return a None variable. It returns None because it was designed-not-to-fail and the *None* variable is just its way of telling you; "tough luck". However, if you pass a None variable as an argument to the *rs.LockObjects()* method it will keel over and die, generating a fatal error!

```
Error Message: iteration over non-sequence of type NoneType
```

This means that the *rs.LockObjects()* method requires a list to iterate through and we have provided None variable - thus the error!

The second function, which is designed-not-to-fail, will detect this problem on line 6 and abort the operation. As you can see, it takes a lot more lines of code to make sure things run smoothly...

A custom defined function can take any amount of arguments between nill and a gazillion. Anyone who calls this function must provide a matching signature or an error will occur. More on the argument list in a bit.

The first line which contains the name and the arguments is called the function declaration. Everything in between  is called the function body, and is noted by the indentation. In the function body you can declare variables, assign values, call other functions and return variables.

The argument list takes a bit more of explaining. Usually, you can simply comma separate a bunch of arguments and they will act as variables from there on end:

```python
def MyBogusFunction(intNumber1, intNumber2):
```

This function declaration already provides three variables to be used inside the function body:

1. MyBogusFunction - (when a user calls this function - it will provide the return value)
2. intNumber1 - (the first argument)
3. intNumber2 - (the second argument)

Let's assume this function determines whether *intNumber1* plus 100 is larger than twice the value of *intNumber2*. 
The function could look like this:

```python
	def MyBogusFunction(intNumber1, intNumber2):
    intNumber1 = intNumber1 + 100
    intNumber2 = intNumber2 * 2
    return (intNumber1 > intNumber2)
```

In this function, we can see that we have used "def" to indicate that we are creating a new function, we have called it "MyBogusFunction" and have given it two input variables (intNumber1, intNumber2). Within the indentation (the guts of the function), we have done a few calculations and we have used the "return" statement to output an evaluation of our calculations. Now, when we call the function somewhere else in our code, the variable will be set to the return value of our function.:

```python
print MyBogusFunction(5, 6)
```

The result will be True (105 is indeed greater than 36)!

Previously, we mentioned something called variable scope - this refers to where a variable has been defined and where it can be used.  Functions and Classes are very specific when it comes to variable scope.  Variables that are defined within a function cannot be referenced outside of the function unless they are passed through the input or return statements!! For example:

```python
def testFunction():
    y=20
    return y
print y*testFunction()
```

This code will return an error, "'y' is not defined" because the variable named "y" has only been defined within a function. That means that we cannot use that variable outside of the function unless we pass it through the input or return statements. The code literally does not understand what "y" means because it was created inside of the function. Otherwise, we could have defined y outside of the function which would make it have global scope and we could use it anywhere within the code.

```python
y = 20
def testFunction():
    return y
print testFunction()
```

## 4.5 Mutability

Python includes a fairly confusing, although sometimes useful, quality pertaining to variables, tuples, lists and dictionaries (the last three we will dive into deeper a bit later).  When we create a variable it points to a specific place in memory and if we create a second variable that is equal to the first - Does y point to the same space in memory as x, or does it now have its own referenced space? For example:

```python
#VARIABLE EXAMPLE:
x = 10
y = x
x = 5
print(y)
```

What will be printed? It turns out, the result is 10!  That means that y is referencing the initial value of x, it is NOT referencing the variable (and thus it does not change when x changes). Although we haven't gone through them, Tuples will act the same as this variable example, while Lists and Dictionaries will be changed based on the referenced variable. For example:

```python
#TUPLE EXAMPLE:
x = (1,2)
y = x
x = (3,4)
print y # The result = (1,2)
```


Tuples act very similar to variables with regard to referencing other items.  In this example, the tuple called "y" is NOT changed once we change the value of "x".

```python
#LIST EXAMPLE - BAD:
x = [1,2]
y = x
x.append(3)
print y The result = (1,2,3)
```

In this example, the List "y" DOES change once we change the value of "x". Thus, the result is (1,2,3), not (1,2) as was the case in the previous examples.  This demonstrates that Lists are referencing the variable not the value of "x".  In order to make "y" act as its own, independent variable and value, we must create a copy of the first variable:

```python
#LIST EXAMPLE - GOOD:
x = [1,2]
y = x[:] #This creates a copy of the list "x"
x.append(3)
print y The result = (1,2)
```

The variable[:] symbol creates a copy of the variable.  This means that "y" will now be an independent list and will not change when "x" changes!  One more example:

```python
#DICTIONARY EXAMPLE - BAD:
x = {1:'a',2:'b'}
y = x
x[3] = 'c'
print y The result = {1:'a',2:'b',3:'c'}
```

In this example the dictionary "y" will be changed with the dictionary "x", unless we use *x.copy()*.

```python
#DICTIONARY EXAMPLE - GOOD:
x = {1:'a',2:'b'}
y = x.copy()
x[3] = 'c'
print y The result = {1: 'a', 2: 'b'}
```

This gets into the topic of mutability.  An element is considered mutable if it can be changed/modified once they are created.  Variables and Tuples are considered Immutable, meaning that they cannot be changed unless you create a new variable with the newly desired value (or copy over top of the old variable).  Lists and Dictionaries are considered mutable, because they can be modified once they have been created. This means that we can freely add, remove, slice the values within a List or Dictionary.  This is an exciting and powerful tool, that was previously not available with VBscript Arrays!  More on this later when we get into Tuples, Lists and Dictionaries...

---

#### Related Topics

- [Where to find help - Next Topic >>]({{ site.baseurl }}/guides/rhinopython/primer-101/1-2-where-to-find-help/)
- [Rhino.Python Primer 101]({{ site.baseurl }}/guides/rhinopython/primer-101/rhinopython101)
- [Running Scripts]({{ site.baseurl }}/guides/rhinopython/python-running-scripts)
- [Canceling Scripts]({{ site.baseurl }}/guides/rhinopython/python-canceling-scripts)
- [Editing Scripts]({{ site.baseurl }}/guides/rhinopython/python-editing-scripts)
- [Scripting Options]({{ site.baseurl }}/guides/rhinopython/python-scripting-options)
- [Reinitializing Python]({{ site.baseurl }}/guides/rhinopython/python-scripting-reinitialize)
