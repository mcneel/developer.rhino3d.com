---
title: Operators and Functions in Python
description: This guide provides an overview of a RhinoScriptSytntax in Python.
authors: ['Skylar Tibbits', 'Arthur van der Harten', 'Steve Baer']
author_contacts: ['sjet@sjet.us', 'aharten', 'stevebaer']
sdk: ['RhinoPython']
languages: ['Python']
platforms: ['Mac', 'Windows']
categories: ['python-primer']
origin:
order: 4
keywords: ['script', 'Rhino', 'python']
layout: toc-guide-page
---

+-----------------------------------+-----------------------------------+
| [4]{.chapter-white}               | [Operators and                    |
|                                   | functions]{.chapter}              |
+-----------------------------------+-----------------------------------+

[4.1 What on earth are they and why should I care?]{.paragraph}

[When we were discussing numeric variables in paragraph 2.3.1, there was
an example about mathematical operations on numbers:]{.content}

[x = 15 + 26 \* 2.33]{.code}

[x = ]{.code}[math.sin]{.code-keyword}[(15 + 26) +
]{.code}[math.sqrt]{.code-keyword}[(2.33)]{.code}

[x = ]{.code}[math.tan]{.code-keyword}[(15 + 26) /
]{.code}[math.log]{.code-keyword}[(55)]{.code}

[The four lines of code above contain four kinds of code:]{.content}

1.  [Numbers » ]{.content}[15, 26, 2.33 ]{.code-10pt}[and]{.content}[
    55]{.code-10pt}
2.  [Variables » ]{.content}[x]{.code-10pt}[ ]{.content}
3.  [Operators » ]{.content}[=, +, \* ]{.code-10pt}[and]{.content}[
    /]{.code-10pt}
4.  [Functions » ]{.content}[math.sin(), math.sqrt(), math.tan()
    ]{.code-10pt}[and]{.content}[ math.log()]{.code-10pt}

[Numbers and variables are well behind us now. Arithmetic operators
should be familiar from everyday life, Python uses them in the same way
as you used to during math classes. Python comes with a limited amount
of arithmetic operators and they are always positioned between two
variables or constants (a constant is a fixed number). The function
first signifies that we have imported math at the top of our code, using
"import math", and then call a function that is within the math module
called "sin()". Thus we write: math.sin(value). ]{.content}

<div class="story">

<table>
<tbody>
<tr>
<td>
[Operator]{.content-emphasis}

</td>
<td>
</td>
<td>
[Example]{.content-emphasis}

</td>
</tr>
<tr>
<td colspan="3">
[Arithmetic operators:]{.content}

</td>
</tr>
<tr>
<td>
[=]{.code-10pt}

</td>
<td>
[Assign a value to a variable]{.code-10pt}

</td>
<td>
[x = 5]{.code-10pt}

</td>
</tr>
<tr>
<td>
[+]{.code-10pt}

</td>
<td>
[Add two numeric values]{.code-10pt}

</td>
<td>
[x = x + 1]{.code-10pt}

</td>
</tr>
<tr>
<td>
[-]{.code-10pt}

</td>
<td>
[Subtract two values]{.code-10pt}

</td>
<td>
[x = 1 - x]{.code-10pt}

</td>
</tr>
<tr>
<td>
[\*]{.code-10pt}

</td>
<td>
[Multiply two values]{.code-10pt}

</td>
<td>
[x = x \* (x-1)]{.code-10pt}

</td>
</tr>
<tr>
<td>
[/]{.code-10pt}

</td>
<td>
[Divide two values]{.code-10pt}

</td>
<td>
[x = (x+1) / (2\*x + 1)]{.code-10pt}

</td>
</tr>
<tr>
<td>
[//]{.code-10pt}

</td>
<td>
[Floored Quotient ]{.code-10pt}

</td>
<td>
[x = x // 10]{.code-10pt}

</td>
</tr>
<tr>
<td>
[\*\*]{.content}

</td>
<td>
[Raise a number to the power of an exponent]{.code-10pt}

</td>
<td>
[x = x ]{.code-10pt}[\*\*]{.content}[ 2.3 ]{.code-10pt}[means:
]{.content}[x2.3]{.code-10pt}

</td>
</tr>
<tr>
<td>
[%]{.content}

</td>
<td>
[Divide two numbers and return only the remainder]{.code-10pt}

</td>
<td>
[x = x ]{.code-10pt}[%]{.content}[ 5]{.code-10pt}

</td>
</tr>
<tr>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td colspan="3">
[Concatenation operators:]{.content}

</td>
</tr>
<tr>
<td>
[+]{.code-10pt}

</td>
<td>
[Concatenate two String variables]{.code-10pt}

</td>
<td>
[x = x + ]{.code-10pt}[" \_Enter"]{.code-string}

</td>
</tr>
<tr>
<td>
<table>
<tbody>
<tr>
<td colspan="3">
[Comparison operators:]{.content}

</td>
</tr>
<tr>
<td>
[&lt;]{.code-10pt}

</td>
<td>
[Less than]{.code-10pt}

</td>
<td>
[if]{.code-keyword}[(x &lt; 5):]{.code-10pt}

</td>
</tr>
<tr>
<td>
[&lt;=]{.code-10pt}

</td>
<td>
[Less than or equal to]{.code-10pt}

</td>
<td>
[if]{.code-keyword}[(x &lt;= 4):]{.code-10pt}

</td>
</tr>
<tr>
<td>
[&gt;]{.code-10pt}

</td>
<td>
[Greater than]{.code-10pt}

</td>
<td>
[if]{.code-keyword}[(x &gt; -1):]{.code-10pt}

</td>
</tr>
<tr>
<td>
[&gt;=]{.code-10pt}

</td>
<td>
[Greater than or equal to]{.code-10pt}

</td>
<td>
[if]{.code-keyword}[(x &gt;= 0):]{.code-10pt}

</td>
</tr>
<tr>
<td>
[==]{.code-10pt}

</td>
<td>
[Equal to]{.code-10pt}

</td>
<td>
[if]{.code-keyword}[(x == 10.0):]{.code-10pt}

</td>
</tr>
<tr>
<td>
[!=]{.code-10pt}

</td>
<td>
[Not equal to]{.code-10pt}

</td>
<td>
[if]{.code-keyword}[(x != 10.0):]{.code-10pt}

</td>
</tr>
<tr>
<td>
[Is]{.code-10pt}

</td>
<td>
[Compare object variables for equality]{.code-10pt}

</td>
<td>
</td>
</tr>
<tr>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td colspan="3">
[Logical and bitwise operators:]{.content}

</td>
</tr>
<tr>
<td>
[And]{.code-10pt}

</td>
<td>
[Logical conjunction]{.code-10pt}

</td>
<td>
[if]{.code-keyword}[(A ]{.code-10pt}[and]{.code-keyword}[
B):]{.code-10pt}

</td>
</tr>
<tr>
<td>
[Or]{.code-10pt}

</td>
<td>
[Logical disjunction]{.code-10pt}

</td>
<td>
[if]{.code-keyword}[(A ]{.code-10pt}[or]{.code-keyword}[
B):]{.code-10pt}

</td>
</tr>
<tr>
<td>
[Not]{.code-10pt}

</td>
<td>
[Logical negation]{.code-10pt}

</td>
<td>
[if]{.code-keyword}[(A ]{.code-10pt}[not]{.code-keyword}[
B):]{.code-10pt}

</td>
</tr>
<tr>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
</tbody>
</table>
</td>
<td>
</td>
<td>
</td>
</tr>
<tr>
<td>
</td>
<td>
</td>
<td>
</td>
</tr>
</tbody>
</table>

</div>

[4.2 Careful…]{.paragraph}

[One thing to watch out for is operator precedence. As you will remember
from math classes, the addition and the multiplication operator have a
different precedence. If you see an equation like this:]{.content}

[x = 4 + 5 \* 2]{.code}

[x = (4 + 5) \* 2 » wrong precedence]{.code}

[x = 4 + (5 \* 2) » correct precedence]{.code}

[x]{.code-10pt}[ doesn't equal 18, even though many cheap calculators
seem to disagree. The precedence of the multiplication is higher which
means you first have to multiply 5 by 2, and then add the result to 4.
Thus, ]{.content}[x]{.code-10pt}[ equals 14. Python is not a cheap
calculator and it has no problems whatsoever with operator precedence.
It is us, human beings, who are the confused ones. The example above is
fairly straightforward, but how would you code the following?]{.content}

![ComplicatedEquation.ai](images/ComplicatedEquation_fmt.jpeg)

[Without extensive use of parenthesis, this would be very nasty indeed.
By using parenthesis in equations we can force precedence, and we can
easily group different bits of mathematics. All the individual bits in
the mathematical notation have been grouped inside parenthesis and extra
spaces have been inserted to accentuate transitions from one top level
group to the next:]{.content}

[y = ( ]{.code}[math.sqrt]{.code-keyword}[(x \*\* 2 + (x - 1)) / (x - 3)
) + ]{.code}[abs]{.code-keyword}[( (2 \* x) / (x \*\* (0.5 \* x))
)]{.code}

[It is still not anywhere near as neat as the original notation, but I
guess that is why the original notation was invented in the first place.
Usually, one of the best things to do when lines of code are getting out
of hand, is to break them up into smaller pieces. The equation becomes
far more readable when spread out over multiple lines of
code:]{.content}

[A = x\*\*2 + (x-1)]{.code}

[B = x-3]{.code}

[C = 2\*x]{.code}

[D = x\*\*(0.5\* x)]{.code}

[y = (]{.code}[math.sqrt]{.code-keyword}[(A) / B) +
]{.code}[abs]{.code-keyword}[(C / D)]{.code}

[4.3 Logical operators]{.paragraph}

[I realize the last thing you want right now is an in-depth tutorial on
logical operators, but it is an absolute must if we want to start making
smart code. I'll try to keep it as painless as possible. ]{.content}

[Logical operators mostly work on booleans and they are indeed very
logical. As you will remember, booleans can only have two values.
Boolean mathematics were developed by George Boole (1815-1864) and today
they are at the very core of the entire digital industry. Boolean
algebra provides us with tools to analyze, compare and describe sets of
data. Although George originally defined six boolean operators we will
only discuss three of them:]{.content}

1.  [Not]{.content}
2.  [And]{.content}
3.  [Or]{.content}

[The Not operator is a bit of an oddity among operators. It is odd
because it doesn't require two values. Instead, it simply inverts the
one on the right. Imagine we have a script which checks for the
existence of a bunch of Block definitions in Rhino. If a block
definition does not exist, we want to inform the user and abort the
script. The English version of this process might look something
like:]{.content}

[Ask Rhino if a certain Block definition exists]{.code}

[If not, abort this sinking ship]{.code}

[The more observant among you will already have noticed that English
version also requires a "not" in order to make this work. Of course you
could circumvent it, but that means you need an extra line of
code:]{.content}

[Ask Rhino if a certain Block definition exists]{.code}

[If it does, continue unimpeded]{.code}

[Otherwise, abort]{.code}

[When we translate this into Python code we get the
following:]{.content}

[if (not
rs.IsBlock]{.code-keyword}[(]{.code}["SomeBlockName"]{.code-string}[)):]{.code}

[print]{.code-keyword}[ (]{.code}["Missing block definition:
SomeBlockName")]{.code-string}

[And and Or at least behave like proper operators; they take two
arguments on either side. The ]{.content}[And]{.code-10pt}[ operator
requires both of them to be True in order for it to evaluate to True.
The ]{.content}[Or]{.code-10pt}[ operator is more than happy with a
single True value. Let's take a look at a typical 'one-beer-too-many'
algorithm:]{.content}

[person = GetPersonOverThere()]{.code}

[colHair = GetHairColour(person)]{.code}

[if]{.code-keyword}[((IsGirl(person)) ]{.code}[and]{.code-keyword}[
(colHair == Blond ]{.code}[or]{.code-keyword}[ colHair == Brunette)
]{.code}[and]{.code-keyword}[ (Age(person) &gt;= 18)):]{.code}

[ neighbour = GetAdjacentPerson(person)]{.code}

[if(not]{.code-keyword}[ IsGuy(neighbour) ]{.code}[or
not]{.code-keyword}[ LooksStrong(neighbour)):]{.code}

[print]{.code-keyword}[(]{.code}["Hey baby, you like
Heineken?")]{.code-string}

[else:]{.code-keyword}

[ RotateAngleOfVision 5.0]{.code}

[As you can see the problem with Logical operators is not the theory,
it's what happens when you need a lot of them to evaluate something.
Stringing them together, quickly results in convoluted code not to
mention operator precedence problems. ]{.content}

[A good way to exercise your own boolean logic is to use Venn-diagrams.
A Venn diagram is a graphical representation of boolean sets, where
every region contains a (sub)set of values that share a common property.
The most famous one is the three-circle diagram:]{.content}

![VennExample.ai](images/VennExample_fmt.jpeg)

[Every circular region contains all values that belong to a set; the top
circle for example marks off set {A}. Every value inside that circle
evaluates True for {A} and every value not in that circle evaluates
False for {A}. If you're uncomfortable with "A, B and C", you can
substitute them with "]{.content}[Employed]{.content-emphasis}[",
"]{.content}[Single]{.content-emphasis}[" and
"]{.content}[HomeOwner]{.content-emphasis}[". By\
coloring the regions we can mimic boolean evaluation in programming
code:]{.content}

<table>
<tbody>
<tr>
<td>
![Venn1.ai](images/Venn1_fmt.jpeg)

</td>
<td>
![Venn2.ai](images/Venn2_fmt.jpeg)

</td>
<td>
![Venn3.ai](images/Venn3_fmt.jpeg)

</td>
<td>
![Venn4.ai](images/Venn4_fmt.jpeg)

</td>
</tr>
<tr>
<td>
[A]{.code}

</td>
<td>
[Not A]{.code}

</td>
<td>
[A And B]{.code}

</td>
<td>
[A Or B]{.code}

</td>
</tr>
<tr>
<td>
![Venn5.ai](images/Venn5_fmt.jpeg)

</td>
<td>
![Venn6.ai](images/Venn6_fmt.jpeg)

</td>
<td>
![Venn7.ai](images/Venn7_fmt.jpeg)

</td>
<td>
![Venn8.ai](images/Venn8_fmt.jpeg)

</td>
</tr>
<tr>
<td>
[A Or B Or C]{.code}

</td>
<td>
[(A Or B) And Not C ]{.code}

</td>
<td>
[C And Not A And Not B]{.code}

</td>
<td>
[B Or (C And A)]{.code}

</td>
</tr>
<tr>
<td colspan="4">
[Try to color the four diagrams below so they match the boolean
logic:]{.content}

</td>
</tr>
<tr>
<td>
![VennBlank.ai](images/VennBlank_fmt.jpeg)

</td>
<td>
![VennBlank.ai](images/VennBlank_fmt1.jpeg)

</td>
<td>
![VennBlank.ai](images/VennBlank_fmt2.jpeg)

</td>
<td>
![VennBlank.ai](images/VennBlank_fmt3.jpeg)

</td>
</tr>
<tr>
<td>
[(A And B) Or ]{.code}

[(B And C) Or (A And C)]{.code}

</td>
<td>
[((B And C) And Not A) Or (A And Not B And Not C)]{.code}

</td>
<td>
[(B And Not C) Or (C And Not B)]{.code}

</td>
<td>
[A And B And C]{.code}

</td>
</tr>
</tbody>
</table>
[Venn diagrams are useful for simple problems, but once you start
dealing with more than three regions it becomes a bit opaque. The
following image is an example of a 6-regional Venn diagram. Pretty, but
not very practical:\
]{.content}

![VennComplex.ai](images/VennComplex_fmt.jpeg)

[4.4 Functions and Procedures]{.paragraph}

[In the end, all that a computer is good at is shifting little bits of
memory back and forth. When you are drawing a cube in Rhino, you are not
really drawing a cube, you are just setting some bits to zero and others
to one.\
At the level of Python there are so many wrappers around those bits that
we can't even access them anymore. A group of 32 bits over there happens
to behave as a number, even though it isn't really. When we multiply two
numbers in Python, a very complicated operation is taking place in the
memory of your PC and we may be very thankful that we are never
confronted with the inner workings. As you can imagine, a lot of
multiplications are taking place during any given second your computer
is turned on and they are probably all calling the same low-level
function that takes care of the nasty bits. That is what functions are
about, they wrap up nasty bits of code so we don't have to bother with
it. This is called encapsulation.]{.content}

[A good example is the ]{.content}[math.sin()]{.code-10pt}[ function,
which takes a single numeric value and returns the sine of that value.
If we want to know the sine of -say- 4.7, all we need to do is type
in]{.content}[ ]{.code}[x = math.sin(4.7)]{.code-10pt}[. Internally the
computer might calculate the sine by using a digital implementation of
the Taylor series:]{.content}

![TaylorSeries2.png](images/TaylorSeries2_fmt.jpeg)

[In other words: you don't want to know. The good people who develop
programming languages\
predicted you don't want to know, which is why they implemented a
]{.content}[math.sin()]{.code-10pt}[ function. Python comes with a long
list of predefined functions all of which are available to
RhinoScripters. Some deal with mathematical\
computations such as ]{.content}[math.sin()]{.code-10pt}[, others
perform String operations such as ]{.content}[abs()]{.code-10pt}[ which
returns the absolute value. Python lists 75 native procedures plus many
more in any of the modules that can be imported (i.e. the math module).
I won't discuss them here, except when they are to be used in
examples.]{.content}

[Apart from implementing the native Python functions, Rhino adds a
number of extra ones for us to use. The current RhinoScriptSyntax helpfile for
Rhino5 claims a total number of about 800 additional functions, and new
ones are added frequently. Rhino's built in functions are referred to as
"methods". They behave exactly the same as Python procedures although
you do need to look in a different helpfile to see what they do.
]{.content}

[(http://www.rhino3d.com/5/ironpython/index.html)]{.content}

[So how do functions/procedures/methods behave? Since the point of
having procedures is to encapsulate code for frequent use, we should
expect them to blend seamlessly into written code. In order to do this
they must be able to both receive and return variables.
]{.content}[math.sin()]{.code-10pt}[ is an example of a function which
both requires and returns a single numeric variable. The
]{.content}[datetime.now()]{.code-10pt}[ function on the other hand only
returns a single value which contains the current date and time. It does
not need any additional information from you, it is more than capable of
finding out what time it is all by itself. An even more extreme example
is the ]{.content}[rs.Exit()]{.code-10pt}[ method which does not accept
any argument and does not return any value. There are two scenarios for
calling procedures. We either use them to assign a value or we call them
out of the blue:]{.content}

[1. strPointID =
]{.code}[rs.AddPoint]{.code-keyword}[(]{.code}[\[]{.code-keyword}[0.0,
0.0, 1.0\]) » Correct]{.code}

[2.
]{.code}[rs.AddPoint]{.code-keyword}[(]{.code}[\[]{.code-keyword}[0.0,
0.0, 1.0\]) » Correct]{.code}

[2.]{.code}[ rs.AddPoint]{.code-keyword}[
]{.code}[\[]{.code-keyword}[0.0, 0.0, 1.0\] » Wrong]{.code}

[If you look in the RhinoScriptSyntax helpfile and search for the
]{.content}[AddLayer() ]{.code-10pt}[method, you'll see the following
text:]{.content}

[rs.AddLayer (name=None, color=0, visible=True, locked=False,
parent=None)]{.code}

[rs.AddLayer() ]{.code-10pt}[is capable of taking five arguments, all of
which are optional. We can tell they are optional because it says
"Optional" next to each item under the "Parameters" section of the
helpfile. The "Parameters" signify the Input values for the Function,
while the "Returns" section tells us what the Function will return.
Optional arguments have a default value which is used when we do not\
override it. If we omit to specify the
]{.content}[lngColor]{.code-10pt}[ argument for example the new layer
will become black.]{.content}

[4.4.1 A simple function example]{.paragraph}

[This concludes the boring portion of the primer. We now have enough
information to actually start making useful scripts. I still haven't
told you about loops or conditionals, so the really awesome stuff will
have to wait until Chapter 5, though. We're going to write a script
which uses some Python functions and a few RhinoScriptSyntax methods. Our
objective for today is to write a script that applies a custom name to
selected objects. First, I'll show you the script, then we'll analyze it
line by line:]{.content}

+-----------------------------------+-----------------------------------+
| [1]{.code}                        | [import rhinoscriptsyntax as      |
|                                   | rs]{.code-keyword}                |
| [2]{.code}                        |                                   |
|                                   | [import time]{.code-keyword}      |
| [3]{.code}                        |                                   |
|                                   | [\#This script will rename an     |
| [4]{.code}                        | object using the current system   |
|                                   | time]{.code-comment}              |
| [5]{.code}                        |                                   |
|                                   | [strObjectID =                    |
| [6]{.code}                        | ]{.code}[rs.GetObject]{.code-keyw |
|                                   | ord}[(]{.code}["Select            |
| [7]{.code}                        | an object to                      |
|                                   | rename"]{.code-string}[,0,]{.code |
| [8]{.code}                        | }[False]{.code-keyword}[,]{.code} |
|                                   | [True]{.code-keyword}[)]{.code}   |
| [9]{.code}                        |                                   |
|                                   | [if strObjectID:]{.code}          |
| [10]{.code}                       |                                   |
|                                   | [ strNewName = ]{.code}["Time:    |
| [11]{.code}                       | "]{.code-string}[ +               |
|                                   | ]{.code}[str]{.code-keyword}[(]{. |
|                                   | code}[time.localtime()]{.code-10p |
|                                   | t}[)]{.code}                      |
|                                   |                                   |
|                                   | [                                 |
|                                   | rs]{.code}[.ObjectName]{.code-key |
|                                   | word}[(strObjectID,               |
|                                   | strNewName)]{.code}               |
+-----------------------------------+-----------------------------------+
|                                   |                                   |
+-----------------------------------+-----------------------------------+

[This is a complete script file which can be run directly from the disk.
It adheres to the basic script structure according to page
13.]{.content}

[We'll be using two variables in this script, one to hold the ID of the
object we're going to rename and one containing the new name. On line 5
we declare a new variable. Although the "str" prefix indicates that
we'll be storing Strings in this variable, that is by no means a
guarantee. You can still put numbers into something that starts with
str. It is simply the convention to name a variable with strSomething if
it is storing a string, similarly you can use intSomething for integers
etc.]{.content}

[On line 5, we're assigning a value to
]{.content}[strObjectID]{.code-10pt}[ by using the RhinoScriptSyntax method
]{.content}[GetObject()]{.code-10pt}[ to ask the user to select an
object. The help topic on ]{.content}[GetObject()]{.code-10pt}[ tells us
the following:]{.content}

[Rhino.GetObject
(message=None,filter=0,preselect=False,Select=False,custom\_filter=None,subobjects=False)]{.code}

[Returns:]{.code}

[String » The identifier of the picked object if successful.]{.code}

[None » If not successful, or on error.]{.code}

[This method accepts six arguments, all of which happen to be optional.
In our script we're only specifying the first and fourth argument. The
]{.content}[strMessage]{.code-10pt}[ refers to the String which will be
visible in the command-line during the picking operation. We're
overriding the default, which is "Select object", with something a bit
more specific. The second argument is an integer which allows us to set
the selection filter. The default behavior is to apply no filter; all
objects can be selected whether they are points, textdots, polysurfaces,
lights or whatever. We want the default behavior. The same applies to
the third argument which allows us to override the default behavior of
accepting preselected objects. The fourth argument is False by default,
meaning that the object we pick will not be actually selected. This is
not desired behavior in our case. The fifth argument takes a bit more
explaining so we'll leave it for now.]{.content}

[Note that we can simply omit optional arguments and put a closing
bracket after the last argument that we
]{.content}[do]{.content-emphasis}[ specify.]{.content}

[When the user is asked to pick an object -any object- on line 5, there
exists a possibility they changed their mind and pressed the escape
button instead. If this was the case then
]{.content}[strObjectID]{.code-10pt}[ will not contain a valid Object
ID, it will be None instead. If we do not check for variable validity
(line 7) but simply press on, we will get an error on line 11 where we
are trying to pass that None value as an argument into the\
]{.content}[rs.ObjectName()]{.code-10pt}[ method. We must always check
our return values and act accordingly. In the case of this script the
proper reaction to an Escape is to abort the whole thing. The If:
structure on Line 7 will abort the current script if
]{.content}[strObjectID]{.code-10pt}[ turns out to be None. ]{.content}

[If ]{.content}[strObjectID]{.code-10pt}[ turns out to be an actual
valid object identifier, our next job is to fabricate a new name and to
assign it to the selected object. The first thing we need is a variable
which contains this new name. We declare it and assign it a value on
line 9.]{.content}

[The name we are constructing always has the same prefix but the suffix
depends on the current system time. In order to get the current system
time we use the ]{.content}[time.localtime()]{.code-10pt}[ function
which is a function built into the time module (which we have imported
at the top of our script). Since a Time and a String are not the same
thing, we cannot concatenate them with the ampersand operator. We must
first convert the Time into a valid String representation. The
]{.content}[str()]{.code-10pt}[ function is another Python native
function which is used to convert non-string variables into Strings.
When I tested this script, the value assigned to
]{.content}[strNewName]{.code-10pt}[ at line 11 was:]{.content}

[Time: (2011, 3, 10, 22, 17, 53, 3, 69, 0)]{.code-string}

[Finally, at line 11, we reach the end of our quest. We tell Rhino to
assign the new name to the old object:]{.content}

![ObjectName.jpg](images/ObjectName_fmt.jpeg)

[Instead of using ]{.content}[strNewName]{.code-10pt}[ to store the name
String, we could have gotten away with the following:]{.content}

[rs.ObjectName]{.code-keyword}[(strObjectID, ]{.code}["Time:
"]{.code-string}[ &
]{.code}[str]{.code-keyword}[(]{.code}[time.localtime()]{.code-10pt}[))]{.code}

[This one line replaces lines 9 through 11 of the original script.
Sometimes brevity is a good thing, sometimes not. Especially in the
beginning it might be smart to be explicit and take up multiple lines;
it makes debugging a lot easier (until you feel comfortable making your
code shorter and possibly harder to decipher).]{.content}

[4.4.2 Advanced function syntax]{.paragraph}

[Whenever you call a function it always returns a value, even if you do
not specifically set it. By default, every function returns a
]{.content}[None]{.code-10pt}[ value, since this is the default value
for all variables and functions in Python. So if you want to write a
function which returns you a String containing the alphabet, doing this
is not enough:]{.content}

+-----------------------------------+-----------------------------------+
| [1]{.code}                        | [def                              |
|                                   | ]{.code-keyword}[Alphabet():]{.co |
| [2]{.code}                        | de}                               |
|                                   |                                   |
|                                   | [ strSeries =                     |
|                                   | ]{.code}["abcdefghijklmnopqrstuvw |
|                                   | xyz"]{.code-string}               |
+-----------------------------------+-----------------------------------+

[The word "def" signifies the start of a function. "Alphabet" is a name
we have made-up for our function. Again, the indentation indicates that
line 2 is within the function and should only be run after the function
is called. ]{.content}

[Although the function actually assigns the alphabet to the variable
called ]{.content}[strSeries]{.code-10pt}[, this variable will go out of
scope once the function ends on line \#2 and its data will be lost. You
have to assign the return value to the function\
name, like so:]{.content}

+-----------------------------------+-----------------------------------+
| [1]{.code}                        | [def                              |
|                                   | ]{.code-keyword}[Alphabet():]{.co |
| [2]{.code}                        | de}                               |
|                                   |                                   |
| [3]{.code}                        | [ strSeries =                     |
|                                   | ]{.code}["abcdefghijklmnopqrstuvw |
| [4]{.code}                        | xyz"]{.code-string}               |
|                                   |                                   |
| [5]{.code}                        | [ return                          |
|                                   | ]{.code-keyword}[strSeries]{.code |
|                                   | }                                 |
|                                   |                                   |
|                                   | [print]{.code-keyword}[           |
|                                   | Alphabet()]{.code}                |
+-----------------------------------+-----------------------------------+
|                                   |                                   |
+-----------------------------------+-----------------------------------+

[The "return value" identifies what will be returned once the method is
called and the code within its scope is executed. When this code is run,
it will call the function Alphabet(), the code within the function's
scope will be run and the function will return the value of strSeries.
This returned value will then be printed to the command line. It should
be noted that at first glance, the return and print functions appear to
be very similar. However, they are not! print() will print anything to
the command line and console. return(), on the other hand, will only
return a value from a function - basically assigning a value to a
variable whenever the function was called. Return is used for the output
of a function (in this case the function "Alphabet"), print is used for
debugging code or whenever the user wants to see a value printed to the
screen.]{.content}

[Imagine you want to lock all curve objects in the document. Doing this
by hand requires three steps and it will ruin your current selection
set, so it pays to make a script for it. A function which performs this
task might fail if there are no curve objects to be found. If the
function is designed-not-to-fail you can always call it without thinking
and it will sort itself out. If the function is designed-to-fail it will
crash if you try to run it without making sure everything is set up
correctly. The respective functions are:]{.content}

+-----------------------------------+-----------------------------------+
| [1]{.code}                        | [def]{.code-keyword}[             |
|                                   | lockcurves\_fail():]{.code}[\     |
| [2]{.code}                        | ]{.code-keyword}[rs.LockObjects(r |
|                                   | s.ObjectsByType(rs.filter.curve)) |
|                                   | ]{.code}                          |
+-----------------------------------+-----------------------------------+

+-----------------------------------+-----------------------------------+
| [1]{.code}                        | [def]{.code-keyword}[             |
|                                   | lockcurves\_nofail():]{.code}[\   |
| [2]{.code}                        | ]{.code-keyword}[ curves =        |
|                                   | rs.ObjectsByType(rs.filter.curve) |
| [3]{.code}                        | \                                 |
|                                   | ]{.code}[ if not]{.code-keyword}[ |
| [4]{.code}                        | curves: ]{.code}[return False\    |
|                                   | ]{.code-keyword}[rs.LockObjects(c |
| [5]{.code}                        | urves)\                           |
|                                   | ]{.code}[return                   |
|                                   | True]{.code-keyword}              |
+-----------------------------------+-----------------------------------+

[If you call the first function when there are no curve objects in the
document, the ]{.content}[rs.ObjectsByType()]{.code-10pt}[ method will
return a ]{.content}[None]{.code-10pt}[ variable. It returns
]{.content}[None]{.code-10pt}[ because it was designed-not-to-fail and
the ]{.content}[None]{.code-10pt}[\
variable is just its way of telling you; "tough luck". However, if you
pass a ]{.content}[None]{.code-10pt}[ variable as an argument to the
]{.content}[rs.LockObjects()]{.code-10pt}[ method it will keel over and
die, generating a fatal error!]{.content}

[Error Message: iteration over non-sequence of type NoneType]{.content}

[This means that the ]{.content}[rs.LockObjects()]{.code-10pt}[ method
requires a list to iterate through and we have provided ]{.content}[None
]{.code-10pt}[variable - thus the error!]{.content}

[The second function, which is designed-not-to-fail, will detect this
problem on line 6 and abort the operation. As you can see, it takes a
lot more lines of code to make sure things run smoothly...]{.content}

[A custom defined function can take any amount of arguments between nill
and a gazillion. Anyone who calls this function must provide a matching
signature or an error will occur. More on the argument list in a
bit.]{.content}

[The first line which contains the name and the arguments is called the
function declaration. Everything in between is called the function body,
and is noted by the indentation. In the function body you can declare
variables, assign values, call other functions and return
variables.]{.content}

[The argument list takes a bit more of explaining. Usually, you can
simply comma separate a bunch of arguments and they will act as
variables from there on end:]{.content}

[def ]{.code-keyword}[MyBogusFunction(intNumber1, intNumber2):]{.code}

[This function declaration already provides three variables to be used
inside the function body:]{.content}

1.  [MyBogusFunction (when a user calls this function - it will provide
    the return value)]{.content}
2.  [intNumber1 (the first argument)]{.content}
3.  [intNumber2 (the second argument)]{.content}

[Let's assume this function determines whether
]{.content}[intNumber1]{.code-10pt}[ plus 100 is larger than twice the
value of ]{.content}[intNumber2]{.code-10pt}[.\
The function could look like this:]{.content}

+-----------------------------------+-----------------------------------+
| [1]{.code}                        | [def]{.code-keyword}[             |
|                                   | MyBogusFunction(intNumber1,       |
| [2]{.code}                        | intNumber2):]{.code}              |
|                                   |                                   |
| [3]{.code}                        | [ intNumber1 = intNumber1 +       |
|                                   | 100]{.code}                       |
| [4]{.code}                        |                                   |
|                                   | [ intNumber2 = intNumber2 \*      |
|                                   | 2]{.code}                         |
|                                   |                                   |
|                                   | [return]{.code-keyword}[          |
|                                   | (intNumber1 &gt;                  |
|                                   | intNumber2)]{.code}               |
+-----------------------------------+-----------------------------------+

[In this function, we can see that we have used "def" to indicate that
we are creating a new function, we have called it "MyBogusFunction" and
have given it two input variables (intNumber1, intNumber2). Within the
indentation (the guts of the function), we have done a few calculations
and we have used the "return" statement to output an evaluation of our
calculations. Now, when we call the function somewhere else in our code,
the variable will be set to the return value of our
function.:]{.content}

+-----------------------------------+-----------------------------------+
| [1]{.code}                        | [print MyBogusFunction(5,         |
|                                   | 6)]{.code}                        |
+-----------------------------------+-----------------------------------+

[The result will be True (105 is indeed greater than 36)!]{.content}

[Previously, we mentioned something called variable scope - this refers
to where a variable has been defined and where it can be used. Functions
and Classes are very specific when it comes to variable scope. Variables
that are defined within a function cannot be referenced outside of the
function unless they are passed through the input or return statements!!
For example:]{.content}

+-----------------------------------+-----------------------------------+
| [1]{.code}                        | [def]{.code-keyword}[             |
|                                   | testFunction():]{.code}           |
| [2]{.code}                        |                                   |
|                                   | [ y=20]{.code}                    |
| [3]{.code}                        |                                   |
|                                   | [ return y]{.code}                |
| [4]{.code}                        |                                   |
|                                   | [print y\*testFunction()]{.code}  |
+-----------------------------------+-----------------------------------+
|                                   |                                   |
+-----------------------------------+-----------------------------------+

[This code will return an error, "'y' is not defined" because the
variable named "y" has only been defined within a function. That means
that we cannot use that variable outside of the function unless we pass
it through the input or return statements. The code literally does not
understand what "y" means because it was created inside of the function.
Otherwise, we could have defined y outside of the function which would
make it have global scope and we could use it anywhere within the
code.]{.content}

+-----------------------------------+-----------------------------------+
| [1]{.code}                        | [y = 20]{.code-keyword}           |
|                                   |                                   |
| [2]{.code}                        | [def]{.code-keyword}[             |
|                                   | testFunction():]{.code}           |
| [3]{.code}                        |                                   |
|                                   | [ return y]{.code}                |
| [4]{.code}                        |                                   |
|                                   | [print testFunction()]{.code}     |
+-----------------------------------+-----------------------------------+
|                                   |                                   |
+-----------------------------------+-----------------------------------+

[4.5 Mutability]{.paragraph}

[Python includes a fairly confusing, although sometimes useful, quality
pertaining to variables, tuples, lists and dictionaries (the last three
we will dive into deeper a bit later). When we create a variable it
points to a specific place in memory and if we create a second variable
that is equal to the first - Does y point to the same space in memory as
x, or does it now have its own referenced space? For example:]{.content}

+-----------------------------------+-----------------------------------+
| [1]{.code}                        | [\#VARIABLE EXAMPLE:]{.code}      |
|                                   |                                   |
| [2]{.code}                        | [x = 10]{.code}                   |
|                                   |                                   |
| [3]{.code}                        | [y = x]{.code}                    |
|                                   |                                   |
| [4]{.code}                        | [x = 5]{.code}                    |
|                                   |                                   |
| [5]{.code}                        | [print(y)]{.code}                 |
+-----------------------------------+-----------------------------------+

[What will be printed? It turns out, the result is 10! That means that y
is referencing the initial value of x, it is NOT referencing the
variable (and thus it does not change when x changes). Although we
haven't gone through them, Tuples will act the same as this variable
example, while Lists and Dictionaries will be changed based on the
referenced variable. For example:]{.content}

+-----------------------------------+-----------------------------------+
| [1]{.code}                        | [\#TUPLE EXAMPLE:]{.code}         |
|                                   |                                   |
| [2]{.code}                        | [x = (1,2)]{.code}                |
|                                   |                                   |
| [3]{.code}                        | [y = x]{.code}                    |
|                                   |                                   |
| [4]{.code}                        | [x = (3,4)]{.code}                |
|                                   |                                   |
| [5]{.code}                        | [print y \# The result =          |
|                                   | (1,2)]{.code}                     |
+-----------------------------------+-----------------------------------+

[Tuples act very similar to variables with regard to referencing other
items. In this example, the tuple called "y" is NOT changed once we
change the value of "x".]{.content}

+-----------------------------------+-----------------------------------+
| [1]{.code}                        | [\#LIST EXAMPLE - BAD:]{.code}    |
|                                   |                                   |
| [2]{.code}                        | [x = \[1,2\]]{.code}              |
|                                   |                                   |
| [3]{.code}                        | [y = x]{.code}                    |
|                                   |                                   |
| [4]{.code}                        | [x.append(3)]{.code}              |
|                                   |                                   |
| [5]{.code}                        | [print y The result =             |
|                                   | (1,2,3)]{.code}                   |
+-----------------------------------+-----------------------------------+

[In this example, the List "y" DOES change once we change the value of
"x". Thus, the result is (1,2,3), not (1,2) as was the case in the
previous examples. This demonstrates that Lists are referencing the
variable not the value of "x". In order to make "y" act as its own,
independent variable and value, we must create a copy of the first
variable:]{.content}

+-----------------------------------+-----------------------------------+
| [1]{.code}                        | [\#LIST EXAMPLE - GOOD:]{.code}   |
|                                   |                                   |
| [2]{.code}                        | [x = \[1,2\]]{.code}              |
|                                   |                                   |
| [3]{.code}                        | [y = x\[:\] \#This creates a copy |
|                                   | of the list "x"]{.code}           |
| [4]{.code}                        |                                   |
|                                   | [x.append(3)]{.code}              |
| [5]{.code}                        |                                   |
|                                   | [print y The result =             |
|                                   | (1,2)]{.code}                     |
+-----------------------------------+-----------------------------------+

[The variable\[:\] symbol creates a copy of the variable. This means
that "y" will now be an independent list and will not change when "x"
changes! One more example:]{.content}

+-----------------------------------+-----------------------------------+
| [1]{.code}                        | [\#DICTIONARY EXAMPLE -           |
|                                   | BAD:]{.code}                      |
| [2]{.code}                        |                                   |
|                                   | [x = {1:'a',2:'b'}]{.code}        |
| [3]{.code}                        |                                   |
|                                   | [y = x]{.code}                    |
| [4]{.code}                        |                                   |
|                                   | [x\[3\] = 'c']{.code}             |
| [5]{.code}                        |                                   |
|                                   | [print y The result =             |
|                                   | {1:'a',2:'b',3:'c'}]{.code}       |
+-----------------------------------+-----------------------------------+

[In this example the dictionary "y" will be changed with the dictionary
"x", unless we use x.copy().]{.content}

+-----------------------------------+-----------------------------------+
| [1]{.code}                        | [\#DICTIONARY EXAMPLE -           |
|                                   | GOOD:]{.code}                     |
| [2]{.code}                        |                                   |
|                                   | [x = {1:'a',2:'b'}]{.code}        |
| [3]{.code}                        |                                   |
|                                   | [y = x.copy()]{.code}             |
| [4]{.code}                        |                                   |
|                                   | [x\[3\] = 'c']{.code}             |
| [5]{.code}                        |                                   |
|                                   | [print y The result = {1: 'a', 2: |
|                                   | 'b'}]{.code}                      |
+-----------------------------------+-----------------------------------+

[This gets into the topic of mutability. An element is considered
mutable if it can be changed/modified once they are created. Variables
and Tuples are considered Immutable, meaning that they cannot be changed
unless you create a new variable with the newly desired value (or copy
over top of the old variable). Lists and Dictionaries are considered
mutable, because they can be modified once they have been created. This
means that we can freely add, remove, slice the values within a List or
Dictionary. This is an exciting and powerful tool, that was previously
not available with VBscript Arrays! More on this later when we get into
Tuples, Lists and Dictionaries...]{.content}

---

## Related Topics

- [What is Python and RhinoScript?]({{ site.baseurl }}/guides/rhinopython/what-are-python-rhinoscript)
- [Python Points]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-points)
- [Python Vectors]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-vectors)
- [Python Lines]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-lines)
- [Python Planes]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-planes)
- [Python Objects]({{ site.baseurl }}/guides/rhinopython/python-rhinoscriptsyntax-objects)
