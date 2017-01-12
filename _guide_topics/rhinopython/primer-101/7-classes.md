---
title: 7 Classes
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

## 7.1 Class Syntax

Classes are useful mechanism for organization above what we have already mentioned: variables, flow control and functions.  Classes give us another level of functionality and actually define a specific type of programming called Object-Oriented Programming.  This means that we can create objects, rather than simply procedures or variables.  Object-Oriented Programming gives us the ability to create a class with internal attributes, functions and any number of other characteristics and then create multiple instances.  Classes offer you a possibility to organize your code based on objects, these objects can relate to one another with inheritance, add or remove information/characteristics through functions and actually exhibit "polymorphism"! (Sounds fancy!) 

Polymorphism, another exciting feature of Object-Orient Programming, is the ability to create one object or class that can exhibit multiple characteristics and commonly respond to similar functions. For example, if we have a function that asks for a "Person's" age and returns their birth year, we could pass in a "Professor" or we could pass in a "Person" although they are actually different objects they can respond to the same question (this is like acting as different people at different times, depending on the question)!  

Classes can be used describe geometry - i.e. a surface is an object that has multiple characteristics, curvature, centroid, number of U & V points etc. We can also ask for information about a surface based on functions embedded within the class; like returning the surface area or the bounding box etc! We can also create our own types of objects like "Connections" or "Apertures" etc - with functionality and specific attributes, while each one being slightly unique! Classes are very powerful, but at first glance are often difficult to wrap your head around!!

Ok, enough talking - lets see some code (because that's much easier to understand...)! To create a class the syntax is:

```python
class MyClass:
    """A simple example""" 
    x = 10
    def test(self):
        return 'hello'

obj = MyClass()
print obj.x
print obj.test()
```	


<table rules="rows">
<tr>
<th style="vertical-align:top;text-align:right;padding:0px 10px;">
Line
</th>
<th>
Description
</th>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">
1
</td>
<td>
Standard class declaration, this class is called "MyClass"
</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">2</td>
<td>Standard class declaration, this class is called "MyClass"</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">3</td>
<td>Declare a variable x = 10.</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">4</td>
<td>Create a function within the class that returns 'hello'</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">7</td>
<td>Create an instance of MyClass() called obj</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">8</td>
<td>This print statement will return >> 10</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">9</td>
<td>This print statement will return >> 'hello'</td>
</tr></table>


Now, if we change the value of x and print the result:

```python
obj.x = 5
print obj.x
```
```
>> 5 
```

The result is 5, showing that we can change the attributes of an object and call functions outside of the class! Regarding the strange use of "self", the Python documentation explains, *" Often, the first argument of a method is called self. This is nothing more than a convention: the name self has absolutely no special meaning to Python. Note, however, that by not following the convention your code may be less readable to other Python programmers, and it is also conceivable that a class browser program might be written that relies upon such a convention."*

Often, a class will have a function called __init__ - this forces the class to give certain attributes whenever it is created (rather than adding them later). For example:

```python
class Harder:
    def __init__(self,m,n):
        self.i = m
        self.j = n
newObj = Harder(10,20)
print newObj.i
print newObj.j
```	

<table rules="rows">
<tr>
<th style="vertical-align:top;text-align:right;padding:0px 10px;">
Line
</th>
<th>
Description
</th>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">
1
</td>
<td>
Standard class declaration, this class is called "Harder"
</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">2</td>
<td>This line initializes a number of variables that must be described when creating an instance of the class</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">3-4</td>
<td>Sets internal variables i & j to the input variables m & n</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">5</td>
<td>Creates an instance of the class Harder() called newObj</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">6</td>
<td>The print call returns the value of i (which was initially m) = 10</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">7</td>
<td>The print call returns the value of j (which was initially n) = 20</td>
</tr>
</table>


Now for an example of inheritance, or the ability for a class to take on the qualities of another class, yet have its own differences (Polymorphism!):

```python
class Weird(MyClass):
    k = 17

newerObj = Weird()
print newerObj.test()
```	


<table rules="rows">
<tr>
<th style="vertical-align:top;text-align:right;padding:0px 10px;">
Line
</th>
<th>
Description
</th>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">
1
</td>
<td>
Standard class declaration, this class is called "Weird." However, this time we put another class in parenthesis - this means that it inherits all of the properties of the class, MyClass()!
</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">2</td>
<td>Standard variable k = 17</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">4</td>
<td>Creates an instance of the class Weird() called newerObj</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">5</td>
<td>The print call returns 'hello'! (Weird...right!?) This means that it referenced the previous class and returned 'hello', because Weird is an child of MyClass()</td>
</tr>
</table>

You can use isinstance(newerObj,MyClass) to check if one object is an instance of another object. 

Classes can be nested, they can have multiple functions, create powerful systems with polymorphism, privacy and modularity of your code! Like I said, classes are very powerful and sometimes difficult to wrap your head around at first (don't get hung up on them....work your way into it)! We are certainly not doing them justice here by explaining them in just 2 short pages! However, their complete depths are certainly out of the scope of this primer and you can find more information on Python classes from the resources at the beginning of this primer or at: [http://docs.python.org/tutorial/classes.html](http://docs.python.org/tutorial/classes.html) 


---

#### Related Topics

- [Where to find help - Next Topic >>]({{ site.baseurl }}/guides/rhinopython/primer-101/1-2-where-to-find-help/)
- [Rhino.Python Primer 101]({{ site.baseurl }}/guides/rhinopython/primer-101/rhinopython101)
- [Running Scripts]({{ site.baseurl }}/guides/rhinopython/python-running-scripts)
- [Canceling Scripts]({{ site.baseurl }}/guides/rhinopython/python-canceling-scripts)
- [Editing Scripts]({{ site.baseurl }}/guides/rhinopython/python-editing-scripts)
- [Scripting Options]({{ site.baseurl }}/guides/rhinopython/python-scripting-options)
- [Reinitializing Python]({{ site.baseurl }}/guides/rhinopython/python-scripting-reinitialize)
