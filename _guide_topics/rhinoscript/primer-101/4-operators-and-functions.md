---
title: 4 Operators and functions
description:
authors: ['David Rutten']
author_contacts: ['DavidRutten']
sdk: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['RhinoScript 101']
origin:
order: 15
keywords: ['rhinoscript', 'vbscript', commands']
layout: toc-guide-page
guide_homepage: guides/rhinoscript/primer-101/
---

## 4.1 What on earth are they and why should I care?

When we were discussing numeric variables in paragraph 2.3.1, there was an example about mathematical operations on numbers:

```python
x = 15 + 26 * 2.33
x = math.sin(15 + 26) + math.sqrt(2.33)
x = math.tan(15 + 26) / math.log(55)
```

The four lines of code above contain four kinds of code:

1. Numbers        `15, 26, 2.33 and 55`
2. Variables    `x`
3. Operators    `=, +, * and /`
4. Functions    `math.sin(), math.sqrt(), math.tan() and math.log()`

Numbers and variables are well behind us now. Arithmetic operators should be familiar from everyday life, VBScript uses them in the same way as you used to during math classes. VBScript comes with a limited amount of arithmetic operators and they are always positioned between two variables or constants (a constant is a fixed number).

<img src="{{ site.baseurl }}/images/primer-operators.svg">{: .img-center  width="95%"}

Now, that looks really scary doesn't it? I am always amazed at how good people are in finding expensive words for simple things. There's nothing to be afraid about though, I'll talk you through the hardest bits and when were done with this chapter, you can impress the living daylights out of any non-programmer by throwing these terms into casual conversation.


## 4.2 Careful...

As you take a closer look at the tables on the opposite page, you'll notice that the + and the = operator occur twice. The way they behave depends on where you put them, which I can't help but feel was a silly choice to make, even in 1963. Especially the assignment/equals operator can be confusing. If you want to assign a value to a variable called x, you use the following code:

```
x = SomethingOrOther
```

But if you want to check if x equals SomethingOrOther you use very identical syntax:

```
If x = SomethingOrOther Then…
```

In the second line, the value of x will not change. Java and C programmers are always scornful when they see such careless treatment of the equals operator, and for once they may be right.

Another thing to watch out for is operator precedence. As you will remember from math classes, the addition and the multiplication operator have a different precedence. If you see an equation like this:

```
x = 4 + 5 * 2

x = (4 + 5) * 2		» wrong precedence
x = 4 + (5 * 2)		» correct precedence
```

x doesn't equal 18, even though many cheap calculators seem to disagree. The precedence of the multiplication is higher which means you first have to multiply 5 by 2, and then add the result to 4. Thus, x equals 14. VBScript is not a cheap calculator and it has no problems whatsoever with operator precedence. It is us, human beings, who are the confused ones. The example above is fairly straightforward, but how would you code the following?

$$y =\frac{\sqrt{x^2+(x+1)}}{x-3} + \left|{\frac{2x}{x^{0.5x}}}\right|$$

Without extensive use of parenthesis, this would be very nasty indeed. By using parenthesis in equations we can force precedence, and we can easily group different bits of mathematics. All the individual bits in the mathematical notation have been grouped inside parenthesis and extra spaces have been inserted to accentuate transitions from one top level group to the next:

```
y = ( Sqr(x ^ 2 + (x - 1)) / (x - 3) )   +   Abs( (2 * x) / (x ^ (0.5 * x)) )
```

It is still not anywhere near as neat as the original notation, but I guess that is why the original notation was invented in the first place. Usually, one of the best things to do when lines of code are getting out of hand, is to break them up into smaller pieces. The equation becomes far more readable when spread out over multiple lines of code:

```vb
Dim A, B, C, D
A = x^2 + (x-1)
B = x-3
C = 2*x
D = x^(0.5* x)
y = (Sqr(A) / B) + Abs(C / D)
```

## 4.3 Logical operators

I realize the last thing you want right now is an in-depth tutorial on logical operators, but it is an absolute must if we want to start making smart code. I'll try to keep it as painless as possible.

Logical operators mostly work on booleans and they are indeed very logical. As you will remember booleans can only have two values, so whatever logic deals with them cannot be too complicated. It isn't. The problem is, we are not used to booleans in every day life. This makes them a bit alien to our own logic systems and therefore perhaps somewhat hard to grasp.

Boolean mathematics were developed by George Boole (1815-1864) and today they are at the very core of the entire digital industry. Boolean algebra provides us with tools to analyze, compare and describe sets of data. Although George originally defined six boolean operators we will only discuss three of them:

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

When we translate this into VBScript code we get the following:

```vb
If Not Rhino.IsBlock("SomeBlockName") Then
	Rhino.Print "Missing block definition: SomeBlockName"
	Exit Sub
End If
```

And and Or at least behave like proper operators; they take two arguments on either side. The And operator requires both of them to be True in order for it to evaluate to True. The Or operator is more than happy with a single True value. Let's take a look at a typical 'one-beer-too-many' algorithm:

```vb
Dim person
person = GetPersonOverThere()
colHair = GetHairColour(person)

If IsGirl(person) And (colHair = Blond Or colHair = Brunette) And (Age(person) >= 18) Then
    Dim neighbour
    neighbour = GetAdjacentPerson(person)
    If Not IsGuy(neighbour) Or Not LooksStrong(neighbour) Then
        Rhino.Print "Hey baby, you like Heineken?"
    Else
        RotateAngleOfVision 5.0
    End If
End If
```

As you can see the problem with Logical operators is not the theory, it's what happens when you need a lot of them to evaluate something. Stringing them together, quickly results in convoluted code not to mention operator precedence problems.

A good way to exercise your own boolean logic is to use Venn-diagrams. A Venn diagram is a graphical representation of boolean sets, where every region contains a (sub)set of values that share a common property. The most famous one is the three-circle diagram:

<img src="{{ site.baseurl }}/images/primer-venn-1.svg">{: .img-center  width="50%"}

Every circular region contains all values that belong to a set; the top circle for example marks off set {A}. Every value inside that circle evaluates True for {A} and every value not in that circle evaluates False for {A}. If you're uncomfortable with "A, B and C", you can substitute them with "Employed", "Single" and "HomeOwner". By
colouring the regions we can mimic boolean evaluation in programming code:

<img src="{{ site.baseurl }}/images/primer-venn-2.svg">{: .img-center  width="100%"}

Try to color the four diagrams below so they match the boolean logic:

<img src="{{ site.baseurl }}/images/venn-blank.svg">{: .img-center  width="100%"}

Venn diagrams are useful for simple problems, but once you start dealing with more than three regions it becomes a bit opaque. The following image is an example of a 6-regional Venn diagram. Pretty, but not very practical:

<img src="{{ site.baseurl }}/images/venn-complex.svg">{: .img-center  width="35%"}

## 4.4 Functions and Procedures

In the end, all that a computer is good at is shifting little bits of memory back and forth. When you are drawing a cube in Rhino, you are not really drawing a cube, you are just setting some bits to zero and others to one. At the level of VBScript there are so many wrappers around those bits that we can't even access them anymore. A group of 32 bits over there happens to behave as a number, even though it isn't really. When we multiply two numbers in VBScript a very complicated operation is taking place in the memory of your PC and we may be very thankful that we are never confronted with the inner workings. As you can imagine, a lot of multiplications are taking place during any given second your computer is turned on and they are probably all calling the same low-level function that takes care of the nasty bits. That is what functions are about, they wrap up nasty bits of code so we don't have to bother with it. This is called encapsulation.

A good example is the `Sin()` function, which takes a single numeric value and returns the sine of that value. If we want to know the sine of -say- 4.7, all we need to do is type in *x = Sin(4.7)*. Internally the computer might calculate the sine by using a digital implementation of the Taylor series:

$$f(x) = \sum_{n=0}^\infty \frac{f^n(a)}{n!} {(x-a)^n}$$

In other words: you don't want to know. The good people who develop programming languages
predicted you don't want to know, which is why they implemented a *Sin()* function. VBScript comes with a long list of predefined functions all of which are available to RhinoScripters. Some deal with mathematical
computations such as *Sin()*, others perform String operations such as *Trim()* which removes all leading
and trailing spaces from a block of text. When a function does not return a value we call it a 'subroutine' instead for no good reason whatsoever. Both functions and subroutines can be referred to as procedures.
This is all just coding slang, in the end it all boils down to the same thing. My copy of the VBScript helpfile lists 89 native procedures. I won't discuss them here, unless when they are to be used in examples.

Apart from implementing the native VBScript functions, Rhino adds a few extra ones for us to use. The current RhinoScript helpfile for Rhino4 claims a total number of about 800 additional functions, and new ones are added frequently. For a special reason which I will not be going into anytime soon, the procedures you get to use through Rhino are referred to as "methods". They behave exactly the same as VBScript procedures although you do need to look in a different helpfile to see what they do.

So how do functions, subroutines and methods behave? Since the point of having procedures is to encapsulate code for frequent use, we should expect them to blend seamlessly into written code. In order to do this they must be able to both receive and return variables. *Sin()* is an example of a function which both requires and returns a single numeric variable. The *Now()* function on the other hand only returns a single value which contains the current date and time. It does not need any additional information from you, it is more than capable of finding out what time it is all by itself. An even more extreme example is the *Rhino.Exit()* method which does not accept any argument and does not return any value. There are two scenarios for calling procedures. We either use them to assign a value or we call them out of the blue:

```vb
1. strPointID = Rhino.AddPoint(Array(0.0, 0.0, 1.0))	» Correct
2. Call Rhino.AddPoint(Array(0.0, 0.0, 1.0))		» Correct
3. Rhino.AddPoint(Array(0.0, 0.0, 1.0))			» Wrong
```

Actually, this is not all there is to it but since the syntax rules for parenthesis and function calls are so exceptionally horrid, I will not discuss them here. All you need to know to be a successful VBScript programmer is that you always, always use parenthesis when calling functions and that you have to use the Call keyword if you're not assigning a value.

If you look in the RhinoScript helpfile and search for `Rhino.AddLayer`, you'll see the following text:

```vb
Rhino.AddLayer ([strLayer [, lngColor [, blnVisible [, blnLocked [, strParent]]]]])
```

The combined information of procedure name and arguments is called the 'signature'. `Rhino.AddLayer()` is capable of taking five arguments, all of which are optional. We can tell they are optional by the fact that they are encapsulated in square brackets. Optional arguments have a default value which is used when we do not override it. If we omit to specify the lngColor argument for example the new layer will become black.

### 4.4.1 A simple function example

This concludes the boring portion of the primer. We now have enough information to actually start making useful scripts. I still haven't told you about arrays and loops, so the really awesome stuff will have to wait till Chapter 5 though. We're going to write a script which uses some VBScript functions and a few RhinoScript methods. Our objective for today is to write a script that applies a custom name to selected objects. First, I'll show you the script, then we'll analyze it line by line:

```vb

Option Explicit
'This script will rename an object using the current system time

Call RenameObject()
Sub RenameObject()
    Dim strObjectID
    strObjectID = Rhino.GetObject("Select an object to rename", , , True)
    If IsNull(strObjectID) Then Exit Sub

    Dim strNewName
    strNewName = "Date tag: " & CStr(Now())

    Call Rhino.ObjectName(strObjectID, strNewName)
End Sub

```
{: .line-numbers}

This is a complete script file which can be run directly from the disk. It adheres to the basic script structure according to page 13, but it doesn't use any global variables or additional functions. There is a standard *Option Explicit* area which takes up the first two lines of the script.

The Main Function Call can be found on line 4. The main function in this case is not called *Main()*, since that is rather nondescript and I prefer to use names that tell me something extra. The main 'function' incidentally is in fact a main subroutine, it does not return a value since there is nothing to return a value to.

Line 5 contains a standard subroutine declaration. The *Sub* keyword is used to indicate that we are about to baptize a new subroutine. The word after *Sub* is always the name of the subroutine. Function and variable names have to adhere to VBScript naming conventions or the compiler will generate an error. Names cannot contain spaces or weird characters. The only non-alphanumeric character allowed is the underscore. Names cannot start with a number either.

We'll be using two variables in this script, one to hold the ID of the object we're going to rename and one containing the new name. On line 6 we declare a new variable. Although the "str" prefix indicates that we'll be storing Strings in this variable, that is by no means a guarantee. You can still put numbers into something that starts with str, just as you can put malt liquor into a Listerine™ bottle. You're just not supposed to.

The variable *strObjectID* has been initialized, but it does not contain any data yet. It is still set to vbEmpty. On line 7 we're assigning a different value to *strObjectID*. We're using the RhinoScript method *GetObject()* to ask the user to select an object. The help topic on *GetObject()* tells us the following:

```vb
Rhino.GetObject ([strMessage [, intType [, blnPreSelect [, blnSelect [, arrObjects ]]]]])

Returns:
String		» The identifier of the picked object if successful.
Null		» If not successful, or on error.
```

This method accepts five arguments, all of which happen to be optional. In our script we're only specifying the first and fourth argument. The strMessage refers to the String which will be visible in the command-line during the picking operation. We're overriding the default, which is "Select object", with something a bit more specific. The second argument is an integer which allows us to set the selection filter. The default behaviour is to apply no filter; all objects can be selected whether they be points, textdots, polysurfaces, lights or whatever. We want the default behaviour. The same applies to the third argument which allows us to override the default behaviour of accepting preselected objects. The fourth argument is False by default, meaning that the object we pick will not be actually selected. This is not desired behaviour in our case. The fifth argument takes a bit more explaining so we'll leave it for now.

Note that we can simply omit optional arguments and put a closing bracket after the last argument that we do specify.

When the user is asked to pick an object -any object- on line 7, there exists a possibility he changed his mind and pressed the escape button instead. If this was the case then *strObjectID* will not contain a valid Object ID, it will be *Null* instead. If we do not check for variable validity here but simply press on, we will get an error on line 13 where we are trying to pass that *Null* value as an argument into the *Rhino.ObjectName()* method. We must always check our return values and act accordingly. In the case of this script the proper reaction to an Escape is to abort the whole thing. The *If…Then* structure on Line 8 will abort the current script if *strObjectID* turns out to be *Null*. The *Exit Sub* statement can be used anywhere within a Subroutine and it will immediately cancel the subroutine and return control to the line of code which was responsible for calling the sub in the first place.

If *strObjectID* turns out to be an actual valid object identifier, our next job is to fabricate a new name and to assign it to the selected object. The first thing we need is a variable which contains this new name. We declare it on line 10 and assign it a value on line 11.

The name we are constructing always has the same prefix but the suffix depends on the current system time. In order to get the current system time we use the *Now()* function which is native to VBScript. *Now()* returns a Date variable type which contains information about both the date and the time. Since a Date and a String are not the same thing, we cannot concatenate them with the ampersand operator. We must first convert the Date into a valid String representation. The *CStr()* function is another VBScript native function which is used to convert non-string variables into Strings.* CStr* stands for Convert to String and you can use it to turn booleans, numbers, dates and a whole lot of other things into proper Strings. When I tested this script, the value assigned to *strNewName* at line 11 was:

```
Time: (2011, 3, 10, 22, 17, 53, 3, 69, 0)
```

Finally, at line 13, we reach the end of our quest. We tell Rhino to assign the new name to the old object:

<img src="{{ site.baseurl }}/images/primer-objectname.jpg">{: .img-center  width="35%"}

Instead of using *strNewName* to store the name String, we could have gotten away with the following:

```
Call Rhino.ObjectName(strObjectID, "Date tag: " & CStr(Now()))
```

This one line replaces lines 10 through 13 of the original script. Sometimes brevity is a good thing, sometimes not. Especially in the beginning it might be smart not to cluster your code too much; it makes debugging a lot easier.

On line 14 we tell the script interpreter that our subroutine has ended.

### 4.4.2 Advanced function syntax

The previous example showed a very simple subroutine which did not take any arguments and did not
return a value. In many cases you will need something a bit more advanced. For one, a complex function will
usually require some information and it will often have a return value, if only to indicate whether the function completed successfully.

Whenever you call a function it always returns a value, even if you do not specifically set it. By default, every function returns a vbEmpty value, since this is the default value for all variables and functions in VBScript. So if you want to write a function which returns you a String containing the alphabet, doing this is not enough:

```vb
Function Alphabet()
    Dim strSeries
    strSeries = "abcdefghijklmnopqrstuvwxyz"
End Function
```
{: .line-numbers}

Although the function actually assigns the alphabet to the variable called strSeries, this variable will go out of scope once the function ends on line #4 and its data will be lost. You have to assign the return value to the function
name, like so:

```vb
Function Alphabet()
    Alphabet = "abcdefghijklmnopqrstuvwxyz"
End Function
```
{: .line-numbers}

Every function has a specific variable which shares its name with the function. You can treat this variable like any other but the value of this variable is passed back to the caller when the function ends. This is usually called the "return value". If your function is designed-to-fail (this doesn't mean it is poorly designed), it will crash when confronted with invalid input. If your function however is designed-not-to-fail, it should return a value which tells the caller whether or not it was able to perform its duty.

Imagine you want to lock all curve objects in the document. Doing this by hand requires three steps and it will ruin your current selection set, so it pays to make a script for it. A function which performs this task might fail if there are no curve objects to be found. If the function is designed-not-to-fail you can always call it without thinking and it will sort itself out. If the function is designed-to-fail it will crash if you try to run it without making sure everything is set up correctly. The respective functions are:

```vb
Sub LockCurves_Fail()
    Call Rhino.LockObjects(Rhino.ObjectsByType(4))
End Sub
```
{: .line-numbers}

```vb
Function LockCurves_NoFail()
    LockCurves_NoFail = False               'Set a default return value

    Dim arrCurves
    arrCurves = Rhino.ObjectsByType(4)      'Get all curve object IDs
    If IsNull(arrCurves) Then Exit Function 'At this point the return value is False

    Call Rhino.LockObjects(arrCurves)       'Lock the curves
    LockCurves_NoFail = True                'Set a new return value indicating success
End Function
```
{: .line-numbers}

If you call the first subroutine when there are no curve objects in the document, the Rhino.ObjectsByType() method will return a Null variable. It returns null because it was designed-not-to-fail and the null
variable is just its way of telling you; "tough luck". However, if you pass a null variable as an argument to the  Rhino.LockObjects() method it will keel over and die, generating a fatal error:

<img src="{{ site.baseurl }}/images/NoFailFunctionCrash.png">{: .img-center  width="60%"}

The second function, which is designed-not-to-fail, will detect this problem on line 6 and abort the operation. As you can see, it takes a lot more lines of code to make sure things run smoothly...

A custom defined function can take any amount of arguments between nill and a gazillion. Unfortunately you cannot define optional arguments in your own functions, nor can you declare multiple functions with the same name but different signatures (what is called 'overloading' in languages that do support this). The VBScript helpfile provides the following syntax rules for functions:

```
[Public | Private] Function name [(arglist)]
    [statements]
    [Exit Function]
    [name = expression]    
End Function
```

To put it in regular English...
Functions can be declared with either Public or Private scope. If you use the Private keyword you will limit the function to your script only, meaning no one else can call it. If you use the Public keyword all the scripts which run in Rhino can access your function. This keyword is optional, meaning that when you omit it, Public is assumed. You also have to provide a unique name which adheres to VBScript naming conventions, this is not optional. Finally you can declare a set of arguments. Anyone who calls this function must provide a matching signature or an error will occur. More on the argument list in a bit.

The first line which contains the scope, name and the arguments is called the function declaration. The last line of a function is always, always an End Function statement, no two ways about it. Everything in between  is called the function body. The function body could technically be empty, though that won't do anybody any good. In the function body you can declare variables, assign values, call other functions or place a call to Exit Function, which will terminate the function prematurely and return execution to the line of code which was responsible for calling this function.

The argument list takes a bit more of explaining. Usually, you can simply comma separate a bunch of arguments and they will act as variables from there on end:

```vb
Public Function MyBogusFunction(intNumber1, intNumber2)
```

This function declaration already provides three variables to be used inside the function body:

```
MyBogusFunction		(the return value)
intNumber1			(the first argument)
intNumber2			(the second argument)
```

Let's assume this function determines whether intNumber1 plus 100 is larger than twice the value of intNumber2.
The function could look like this:

```vb
Function MyBogusFunction(intNumber1, intNumber2)
    intNumber1 = intNumber1 + 100
    intNumber2 = intNumber2 * 2
    MyBogusFunction = (intNumber1 > intNumber2)
End Function
```

Note that we do not need to declare any additional variables, we can get away with the ones that are implied by the function declaration. Since we cannot specify what kind of variable intNumber1 has to be, there is no guarantee that it is in fact a number. It might just as well be a boolean or a null or an array or something even more scary. This function is thus designed-to-fail; it will crash if we call it with improper arguments:

```vb
Sub Main()
    Dim blnResult
    blnResult = MyBogusFunction(45, "Fruitbat")
End Sub
```

<img src="{{ site.baseurl }}/images/FunctionTypeMismatchError.png">{: .img-center  width="50%"}

So what if we want our function to manipulate several variables? How do we get around the 'one return value only' limitation? There are essentially four solutions to this, two of which are far too difficult for you at this moment and one of which is just stupid... try to guess which is which:

1. Use global variables
2. Declare arguments by reference
3. Return an array
4. Return a class instance

We'll focus on number two for the time being. (#1 was the stupid option in case you were wondering.)

Arguments in the function declaration can be declared either by value or by reference. By value means that the variable data will be copied before it enters the function body. This means a function can do whatever it likes with an argument variable, it will not affect the caller in any way. If you declare an argument to be passed in by reference however, the function knows where the variable came from and it can change the original value. Observe what happens if we do this:

![{{ site.baseurl }}/images/ByValueResult.png]({{ site.baseurl }}/images/ByReferenceResult.png){: .float-img-right width="275"}

```vb
Call Main()
Sub Main()
    Dim intA, intB, dblC
    intA = 4
    intB = 7
    dblC = AnotherBogusFunction(intA, intB)
    Call Rhino.Print("A:" & intA & ", B:" & intB & ", C:" & dblC)
End Sub

Function AnotherBogusFunction(ByVal intNumber1, ByVal intNumber2)
    intNumber1 = intNumber1 + 1
    intNumber2 = intNumber2 + 2
    AnotherBogusFunction = intNumber1 * intNumber2
End Function  
```
{: .line-numbers}

Since the arguments are passed in by value, `intA` and `intB` are left intact when AnotherBogusFunction is called. Although the function received the values 4 and 7 respectively, it does not know where they came from and thus when it increments them on lines 11 and 12, the operation only applies to the local variable copies `intNumber1` and `intNumber2`. However, if we replace the `ByVal` keywords with `ByRef` we get the following result:

![{{ site.baseurl }}/images/ByReferenceResult.png]({{ site.baseurl }}/images/ByReferenceResult.png){: .float-img-right width="275"}

```vb
Function AnotherBogusFunction(ByRef intNumber1, ByRef intNumber2)
    intNumber1 = intNumber1 + 1
    intNumber2 = intNumber2 + 2
    AnotherBogusFunction = intNumber1 * intNumber2
End Function
```
{: .line-numbers}

`intNumber1` and `intA` now both point to the exact same section in the computer memory so when we change `intNumber1` we also change the value of `intA`.

Passing arguments by reference is quite a tricky thing to wrap your head around, so don't feel bad if you don't get it at first. You can rest assured that in almost all cases we'll be using the `ByVal` approach which means our data is simply copied out of harms way.

There is one other reason to use `ByRef` arguments which has to do with optimization. Whenever you pass an argument to a function it will be copied in the computer memory. With small stuff like integers, vectors and shorts strings this doesn't matter, but when you start copying huge arrays back and forth you're wasting memory and processor cycles. If it turns out your script is running slowly you could consider passing arguments by
reference in order to avoid casual copying. You have to be careful not to change them, or very unpredictable things will start happening.

It's a bit too early for optimizations though, more on this in Chapter 9.



---

## Next Steps

Ok, so now that you can get some functions to work. Next is [conditional execution]({{ site.baseurl }}/guides/rhinoscript/primer-101/5-conditional-execution/) to control how the script reacts to input.
