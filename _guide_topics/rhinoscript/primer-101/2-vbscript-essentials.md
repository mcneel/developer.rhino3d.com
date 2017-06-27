---
title: 2 RhinoScript Essentials
description:
authors: ['David Rutten']
author_contacts: ['DavidRutten']
sdk: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['RhinoScript Primer']
origin:
order: 4
keywords: ['rhinoscript', 'vbscript', commands']
layout: toc-guide-page
guide_homepage: /guides/rhinoscript/primer-101/rhinoscript101/
---

## 2.1 Language origin

Like conversational languages, programming languages group together in clusters. There are language families and language generations. VBScript is a member of the BASIC language family which in turn is a third generation group. ‘Third generation’ indicates that the language was designed to be easy for humans to understand.  First and second generation languages (often referred to as machine-code), are most definitely not easy to understand. Just so you know the difference between second and third generation code, here is an example of second generation assembly:

| mov | | | [ebx], ecx |
| add | | |	ebx, 4 |
| loop | | | init_loop |
| push	| | | dword FirstMsg |
| call | | | _puts | 
| pop | | | ecx | 
| push | | | dword 10 | 
| push | | | dword array |
| call | | | _print_array |
| add | | | esp, 8 | 

Lucky us.

Incidentally, BASIC stands for Beginner’s All-purpose Symbolic Instruction Code and was first developed in 1963 in order to drag non-science students into programming. As you can see above, even assembly already makes heavy use of English vocabulary but although we are familiar with the words, it is not possible for laymen to decipher the commands. Assuming that you might be reading these pages without any prior programming experience whatsoever, I still dare guess that the following example will not give you much problems:

```
somenumber = Rhino.GetReal("Line length")
line = Rhino.AddLine(Array(0,0,0), Array(somenumber,0,0))
If IsNull(line) Then
	Rhino.Print "Something went wrong"
Else
	Rhino.Print "Line curve inserted"
End If
```

Of course you might have no conception of what `Array(0,0,0)` actually means and you might be confused by `Rhino.GetNumber(0)` or `IsNull()`, but on the whole it is pretty much the same as the English you use at the grocers:

Ask Rhino to assign a number to something called 'somenumber'.
Tell Rhino to add a line from the world origin to the point on the x-axis indicated by 'somenumber'
If the result of the previous operation was not a curve object,
then print a failure message
otherwise print a success message

Translating VBScript code to and from regular English should not be very difficult, at least not at this featherweight level. It is possible to convolute the code so that it becomes unreadable, but this is not something you should take pride in. The syntax resembles English for a good reason, I suggest we stick to it.

As mentioned before, there are three things the syntax has to support, and the above script uses them all:

Flow control		» Depending on the outcome of the second line, some lines are not run  
Variable data		» somenumber is used to store a variable number  
Communication		» The user is asked to supply information and is informed about the result  

## 2.2 Flow control

We use flow-control in VBScript to skip certain lines of code or to execute others more than once. We can also use flow-control to jump to different lines in our script and back again. You can add conditional statements to your code which allow you to shield off certain portions. If…Then…Else and Select…Case structures are examples of conditional statements, but we'll discuss them later. A typical conditional statement is:

```
You have to be this tall (1.5m) to ride the roller coaster.
```

This line of ‘code’ uses a condition (taller than 1.5m) to evaluate whether or not you are allowed to ride the roller coaster. Conditional statements like this can be strung together indefinitely. We could add a maximum height as well, or a weight limitation, or a ban on spectacles or heart-conditions.

Instead of skipping lines we can also repeat lines. We can do this a fixed number of times:

```
Add 5 tea-spoons of cinnamon.
```

Or again use a conditional evaluation:

```
Keep adding milk until the dough is kneadable.
```

The repeating of lines is called ‘Looping’ in coding slang. There are several loop types available but they all work more or less the same. They will be covered in detail later on.

## 2.3 Variable data

Whenever we want our code to be dynamic we have to make sure it can handle all kinds of different situations. In order to do that we must have the ability to store variables. For instance we might want to store a selection of curves in our 3Dmodel so we can delete them at a later stage. Or perhaps our script needs to add a line from the mouse pointer to the origin of the 3D scene. Or we need to check the current date to see whether or not our software has expired. This is information which was not available at the time the script was written.

Whenever we need to store data or perform calculations or logic operations we need variables to remember the results. Since these operations are dynamic we cannot add them to the script prior to execution. We need placeholders.

In the example on the previous page the thing named "somenumber" is a placeholder for a number. It starts out by being just a name without any data attached to it, but it will be assigned a numeric value in the line:

```
somenumber = Rhino.GetNumber("Line length")
```

Then later on we retrieve that specific value when we add the line curve to Rhino:

```
curve = Rhino.AddLine(Array(0,0,0), Array(somenumber,0,0))
```

All the other coordinates that define the line object are hard-coded into the script. There is no limit to how often a variable can be read or re-assigned a new value, but it can never contain more than one value and there’s no undo system for retrieving past values. Apart from numbers we can also store other types of data in variables. For the time being, we’ll restrict ourselves to the four most essential ones, plus a special one which is used for error-trapping:

1. Integers
2. Doubles
3. Booleans
4. Strings
5. Null variable


### 2.3.1 Integers and Doubles

Integers and Doubles are both numeric variable types, meaning they can be used to store numbers. They cannot store the same kind of numbers, which is why we ended up with more than one type. Integers can only be used to store whole numbers. Their range extends from roughly minus two-
billion to roughly plus two-billion. Every whole number between these extremes can be represented using an integer. Integers are used almost exclusively for counting purposes (as opposed to calculations).

Doubles are numeric variables which can store numbers with decimals. Doubles can be used to represent 
numbers as large as 1.8×10308 and as small as 5.0×10-324, though in practise the range of numbers which can be accurately represented is much smaller. Those of you who are unfamiliar with scientific notation need not to worry, I shall not make a habit out of this. It is enough to know that the numeric range of doubles is truly enormous.

<img src="{{ site.baseurl }}/images/primer-integers.svg">{: .img-center  width="75%"}

<!--TODO: The font in the SVG above is not rendeirng correctly.  What Font to use -->

he set of all possible Double and Integer numbers is not continuous; it has gaps. There exists no Integer between zero and one and there exists no Double between zero and 5.0×10-324. The fact that the size of the gap is so much smaller with Doubles is only because we’ve picked a number close to zero. As we move towards bigger and 
bigger numbers, the gaps between two adjacent Double values will become bigger as well and as we approach the limits of the range, the gaps are big enough to fit the Milky Way. 2×10300 minus one billion is still 2×10300, so beware when using extremely large numbers. Normally, we never stray into the regions where 32-bit computing starts to break down, we tend to restrict ourselves to numbers we can actually cope with.

The VBScript syntax for working with numeric variables should be very familiar:


```vb
x = 15 + 26                # x equals 41
x = 15 + 26 * 2.33        #  x equals 75.58
x = math.sin(15 + 26) + math.sqrt(2.33)    # x equals 1.368
```
You can use the `Rhino.Print()` method to display the result of these computations. `Rhino.Print()` will display the value in the command-line:

```
x = 2 * Sin(15 + 26) + Log(55)
Rhino.Print x
```
Of course you can also use numeric variables on the right hand side of the equation:   

```
x = x + 1
x = Sin(y) + Sqr(0.5 * y)
```

The first line of code will increment the current value of x by one, the second line will assign a value to x which depends on the value of y. If *y* equals 34 for example, *x* will become *4.65218831173768+.


### 2.3.2 Booleans

umeric variables can store a whole range of different numbers. Boolean variables can only store two values mostly referred to as Yes or No, True or False. Obviously we never use booleans to perform calculations because of their limited range. We use booleans to evaluate conditions... remember?

```
You have to be taller than 1.5m to ride the roller coaster.
```

"taller than 1.5m" is the condition in this sentence. This condition is either True or False. You are either taller than 1.5m or you are not. Since most of the Flow-control code in a script is based on conditional statements, booleans play a very important role. Let’s take a look at the looping example:

```
Keep adding milk until the dough is kneadable.
```

The condition here is that the dough has to be kneadable. Let’s assume for the moment that we added something (an algorithm) to our script that could evaluate the current consistency of the dough. Then our first step would be to use this algorithm so we would know whether or not to add milk. If our algorithm returns False (I.e. "the dough isn’t kneadable") then we will have to add some milk. After we added the milk we will have to ask again and repeat these steps until the algorithm returns True (the dough is kneadable). Then we will know there is no more milk needed and that we can move on to the next step in making our Apfelstrudel.

The example on page 5 used a VBScript function which returns a boolean value:

```
IsNull(ObjectID)
```

This method requires us to pass in a variable -any variable- and it will return True if that variable contains no data. If `IsNull()` returns `True` it means that Rhino was unable to successfully complete the task we assigned it, which in turn indicates something somewhere went astray.

In VBScript we never write "0" or "1" or "Yes" or "No", we always use "True" or "False". Please note that there is no need to compare the result of IsNull() to True or False:

```
If IsNull(curve) = True Then…
```

This is unnecessary code. Something which is already True does not need to be compared to True in order to become really True.


### 2.3.3 Strings

Strings are used to store text. Whenever you add quotes around stuff in VBScript, it automatically becomes a String. So if we encapsulate a number in quotes, it will become text:

```
variable1 = 5
variable2 = "5"
```

You could print these variables to the Rhino command history and they would both look like 5, but the String variable behaves differently once we start using it in calculations:

```
Rhino.Print (variable1 + variable1)		» Results in 10
Rhino.Print (variable2 + variable2)		» Results in 55
```

In the first line, the plus-sign recognizes the variables on either side as numerical ones and it will perform a numeric addition (5 + 5 = 10). On the second line however, the variables on either side are Strings and the plus sign will concatenate them (I.e. append the one on the right to the one on the left). You must always pay attention to what type of variable you are using.


When you need to store text, you have no choice but to use Strings. Strings are not limited length-wise (well, they are, but my guess is you will not run into the two-billion characters limit anytime soon). The syntax for Strings is quite simple, but working with Strings can involve some very tricky code. For the time being we’ll only focus on simple operations such as assignment and concatenation:

```
a = "Apfelstrudel"				»  Apfelstrudel
a = "Apfel" & "strudel"				»  Apfelstrudel
a = "4" & " " & "Apfelstrudel"			»  4 Apfelstrudel
a = "The square root of 2.0 = " & Sqr(2.0)	»  The square root of 2.0 = 1.4142135623731 
```

Internally, a String is stored as a series of characters. Every character (or 'char') is taken from the Unicode table, which stores a grand total of ~100.000 different characters. The index into the unicode table for the question mark for example is 63, lowercase e is 101 and the blank space is 32:

<img src="{{ site.baseurl }}/images/primer-strings.svg">{: .img-center  width="75%"}

Further down the road we'll be dealing with some advanced String functions which will require a basic 
understanding of how Strings work, but while we are still just using the simple stuff, it's good enough to know it just works the way you expect it to. 

Note that in VBScript we can append numeric values to Strings, but not the other way around. The ampersand sign (&) is used to join several variables into a single String. You could also use the plus sign to do this, but I prefer to restrict the usage of + to numeric operations only. When using & you can treat numeric variables as Strings:

```
a = 5 + 7						» a equals 12
b = 5 & 7						» b equals 57
```

Strings are used heavily in RhinoScript since object IDs are always written as strings. Object IDs are those weird codes that show up in the Object Property Details: D7EFCF0A-DB47-427D-9B6B-44EC0670C573. IDs are designed to be absolutely unique for every object which will ever exist in this universe, which is why we can use them to safely and unambiguously identify objects in the document.

### 2.3.4 None variable

Whenever we ask Rhino a question which might not have an answer, we need a way for Rhino to say "I don't know". Using the example on page 5:

```VB
curve = Rhino.AddLine(Array(0,0,0), Array(somenumber,0,0))
```
It is not a certainty that a curve was created. If the user enters zero when he is asked to supply the value for somenumber, then the startpoint of the line would be coincident with the endpoint. Rhino does not like zero-length lines and will not add the object to the document. This in turn means that the return value of Rhino.AddLine() is not a valid object ID. Almost all methods in Rhino will return a Null variable if they fail, this way we can add error-checks to our script and take evasive action when something goes wrong. Every variable in a script can become a Null variable and we check them with the IsNull() function:

```VB
curve = Rhino.AddLine(Array(0,0,0), Array(somenumber,0,0))
If IsNull(curve) Then
	Rhino.Print "Something went terribly wrong!"
End If
```

IsNull() will pop up a lot in examples to come, and it is always to check whether or not something went according to plan.

### 2.3.5 Using variables

Whenever we intend to use variables in a script, we have to declare them first. When your boss asks you to deliver a package to Mr. Robertson, your first reaction is probably "who on earth is Mr. Robertson?". The VBScript interpreter is not that different from you or me. It likes to be told in advance what all those words mean you are about to fling at it. So when we write:

```
a = "Apfelstrudel"
```

We should not be surprised when we are asked "what on earth is a?". This line of code assigns a value to a variable which has not been declared. We normally declare a variable using the Dim keyword. The only  exception to this rule is if we want to declare global variables. But we don't yet.

Whenever a variable is declared, it receives a unique name, a scope and a default value. The name you get to pick yourself. In the example above we have used a, which is not the best of all possible choices. For one, it doesn't tell us anything about what the variable is used for or what kind of data it contains. A better name would be strFood. The str prefix indicates that we are dealing with a String variable here and the Food bit is hopefully fairly obvious. A widely used system for variable prefixes is as follows:

<img src="{{ site.baseurl }}/images/primer-variable-type.svg">{: .img-center  width="60%"}

Don't worry about all those weird variable types, some we will get to in later chapters, others you will probably never use. The scope (sometimes called "lifetime") of a variable refers to the region of the script where it is accessible. Whenever you declare a variable inside a function, only that one function can read and write to it. Variables go 'out of scope' whenever their containing function terminates. 'Lifetime' is not a very good description in my opinion, since some variables may be very much alive, yet unreachable due to being in another scope. But we'll worry about scopes once we get to function declarations. For now, let's just look at an example with proper variable declaration:

```vb
Dim strComplaint, strNag, strFood

strComplaint = "I don't like "
strFood = "Apfelstrudel. "
strNag = "Can I go now?"

Call Rhino.Print(strComplaint & strFood & strNag)
```

As you will have noticed, we can declare multiple variables using a single Dim keyword if we comma-separate them. Though technically you could jam all your variable declarations onto a single line, it is probably a good idea to only group comparable variables together. Incidentally, the default value of all variables is always a specially reserved value called vbEmpty. It means the variable contains no data and it cannot be used in 
operations. Before you can use any of your variables, you must first assign them a value.
Now, high time for an example. We'll be using the macro from page 2, but we'll replace some of the hard coded numbers with variables for added flexibility. This script looks rather intimidating, but keep in mind that the messy looking bits (line 10 and beyond) are caused by the script trying to mimic a macro, which is a bit like trying to drive an Aston-Martin down the sidewalk. Usually, we talk to Rhino directly without using the command-line and the code looks much friendlier:


```vb
Dim dblMajorRadius, dblMinorRadius
Dim intSides

dblMajorRadius = Rhino.GetReal("Major radius", 10.0, 1.0, 1000.0)
dblMinorRadius = Rhino.GetReal("Minor radius", 2.0, 0.1, 100.0)
intSides = Rhino.GetInteger("Number of sides", 6, 3, 20)

Dim strPoint1, strPoint2
strPoint1 = " w" & dblMajorRadius & ",0,0"
strPoint2 = " w" & (dblMajorRadius + dblMinorRadius) & ",0,0"

Rhino.Command "_SelNone"
Rhino.Command "_Polygon _NumSides=" & intSides & " w0,0,0" & strPoint1
Rhino.Command "_SelLast"
Rhino.Command "-_Properties _Object _Name Rail _Enter _Enter"
Rhino.Command "_SelNone"
Rhino.Command "_Polygon _NumSides=" & intSides & strPoint1 & strPoint2
Rhino.Command "_SelLast"
Rhino.Command "_Rotate3D w0,0,0 w1,0,0 90"
Rhino.Command "-_Properties _Object _Name Profile _Enter _Enter"
Rhino.Command "_SelNone"
Rhino.Command "-_Sweep1 _SelName Rail _SelName Profile _Enter _Closed=Yes Enter"
Rhino.Command "_SelName Rail"
Rhino.Command "_SelName Profile"
Rhino.Command "_Delete"
```
{: .line-numbers}

<table>
<tr>
<th>
Line
</th>
<th>
Description
</th>
</tr>
<tr>
<td>
1...2
</td>
<td>
Here we declare three variables. By the looks of it two doubles and one integer (prefixes, prefixes!).
</td>
</tr>
<tr>
<td>
4
</td>
<td>
This is where we ask the user to enter a number value ("Real" is another word for "Double"). We supply the Rhino.GetReal() method with four fixed values, one string and three doubles. The string will be displayed in the command-line and the first double (10.0) will be available as the default option:

<img src="{{ site.baseurl }}/images/primer-getrealexample.png" width="75%" margin="10px"><br>

We're also limiting the numeric domain to a value between one and a thousand. If the user attempts to enter a larger number, Rhino will claim it's too big:

<br><img src="{{ site.baseurl }}/images/primer-getrealexamplemaximumlimit.png" width="75%">

</td>
</tr>
<tr>
<td>5...6</td>
<td>These lines are fairly similar. On line 7 we ask the user for an integer instead of a double.</td>
</tr>
<tr>
<td>8</td>
<td>We're declaring two string variables, which will be used to store a text representation of a coordinate. Since we're going to use these coordinates more than once I thought it prudent to create them ahead of time so we don't have to concatenate the strings over and over again..</td>
</tr>
<tr>
<td>9...10</td>
<td>On these lines we're creating the strings, based on the values of `dblMajorRadius` and `dblMinorRadius`. If we assume the user has chosen the default values in all cases, `dblMajorRadius` will be 10.0 and `dblMinorRadius` will be 2.0, which means that `strPoint2` will look like " w12,0,0".</td>
</tr>
<tr>
<td>12...25</td>
<td>This is the same as the macro on page 3, except that we've replaced some bits with variables and there are three extra lines at the bottom which get rid of the construction geometry (so we can run the script more than once without it breaking down).</td>
</tr></table>
{: .multiline}

---

## Next Steps

There are the basics of the RhinoScript datastructures, next learn the  [script anatomy]({{ site.baseurl }}/guides/rhinoscript/primer-101/3-script-anatomy/).
