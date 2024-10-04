+++
aliases = ["/en/5/guides/rhinopython/primer-101/2-python-essentials/", "/en/6/guides/rhinopython/primer-101/2-python-essentials/", "/en/7/guides/rhinopython/primer-101/2-python-essentials/", "/wip/guides/rhinopython/primer-101/2-python-essentials/"]
authors = [ "skylar-tibbits", "arthur-van-der-harten", "steve" ]
categories = [ "Rhino.Python 101" ]
category_page = "guides/rhinopython/primer-101/"
keywords = [ "python", "commands" ]
languages = [ "Python" ]
sdk = [ "RhinoPython" ]
title = "2 Python Essentials"
type = "guides"
weight = 4
draft = false

[admin]
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 7
until = ""

[page_options]
block_webcrawlers = false
byline = true
toc = true
toc_type = "single"

+++

## 2.1 Language Origin

Like conversational languages, programming languages group together in clusters. Python is a high level language, indicating that the language was designed to be easy for humans to understand.  On the opposite end of the spectrum are extremely low level languages, (often referred to as machine-code), that are most definitely not easy to understand.  In between are languages such as C or C++ which offer layers of abstraction above machine-code.  As I mentioned, Python is a step even higher, meaning that it is far easier to read (closer to the English language) and we don't need to manage difficult functionality like memory allocation, or declaring variables!

Lucky us.

Python was first released in 1991, since then it has grown to become freely available with a user-group exceeding tens of thousands.  The Python documentation claims, " Python plays well with others," " Python runs everywhere," " Python is friendly... and easy to learn" and " Python is Open!"  For more information about the Python programming language and its development see: [http://www.python.org](http://www.python.org).

Assuming that you might be reading these pages without any prior programming experience whatsoever, I still dare guess that the following example will not give you much trouble:

```python
import rhinoscriptsyntax as rs

somenumber = rs.GetReal("Line length")
line = rs.AddLine( (0,0,0), (somenumber,0,0) )
if line is None:
    print("Something went wrong")
else:
    print("Line curve inserted with id", line)
```
Of course you might have no conception of what [0,0,0] actually means and you might be confused by rs.GetReal() but on the whole it is pretty much the same as the English you use at the grocers:

```
Ask Rhino to assign a number to something called 'somenumber'.
Tell Rhino to add a line from the world origin to the point on the x-axis indicated by 'somenumber'
print a success message
```

Translating Python code to and from regular English should not be very difficult, at least not at this featherweight level. It is possible to convolute the code so that it becomes unreadable, but this is not something you should take pride in. The syntax resembles English for a good reason, I suggest we stick to it.

As mentioned before, there are three things the syntax has to support, and the above script uses them all:

1. Flow control        » Depending on the outcome of the second line, some lines are not run
2. Variable data        » somenumber is used to store a variable number
3. Communication        » The user is asked to supply information and is informed about the result

## 2.2 Flow Control

We use flow-control in Python to skip certain lines of code or to execute others more than once. We can also use flow-control to jump to different lines in our script and back again. You can add conditional statements to your code which allow you to shield off certain portions. If…Else…Else If structures are examples of conditional statements, but we'll discuss them later. A typical conditional statement is:

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

## 2.3 Variable Data

Whenever we want our code to be dynamic we have to make sure it can handle all kinds of different situations. In order to do that we must have the ability to store variables. For instance we might want to store a selection of curves in our 3D model so we can delete them at a later stage. Or perhaps our script needs to add a line from the mouse pointer to the origin of the 3D scene. Or we need to check the current date to see whether or not our software has expired. This is information which was not available at the time the script was written.

Whenever we need to store data or perform calculations or logic operations we need variables to remember the results. Since these operations are dynamic we cannot add them to the script prior to execution. We need placeholders.

In the example on the previous page the thing named *"somenumber"* is a placeholder for a number. It starts out by being just a name without any data attached to it, but it will be assigned a numeric value in the line:

```python
somenumber = rs.GetNumber("Line length")
```

Then later on we retrieve that specific value when we add the line curve to Rhino:

```python
curve = rs.AddLine([0,0,0], [somenumber,0,0])
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

{{< image url="/images/primer-integers.svg" alt="/images/primer-integers.svg" class="image_center" width="75%" >}}

<!--TODO: The font in the SVG above is not rendeirng correctly.  What Font to use -->

The set of all possible Double and Integer numbers is not continuous; it has gaps. There exists no Integer between zero and one and there exists no Double between zero and 5.0×10-324. The fact that the size of the gap is so much smaller with Doubles is only because we’ve picked a number close to zero. As we move towards bigger and
bigger numbers, the gaps between two adjacent Double values will become bigger as well and as we approach the limits of the range, the gaps are big enough to fit the Milky Way. 2×10300 minus one billion is still 2×10300, so beware when using extremely large numbers. Normally, we never stray into the regions where 32-bit computing starts to break down, we tend to restrict ourselves to numbers we can actually cope with.

The Python syntax for working with numeric variables should be very familiar:

{{< download-script "rhinopython/rhinopython101/2_3_1_MathematicalNotation.py" "2_3_1_MathematicalNotation.py">}}

```python
x = 15 + 26                # x equals 41
x = 15 + 26 * 2.33        #  x equals 75.58
x = math.sin(15 + 26) + math.sqrt(2.33)    # x equals 1.368
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
print(x) # returns 1
print(y)  # returns 2
print(z)  # returns 3
```

### 2.3.2 Booleans

Numeric variables can store a whole range of different numbers. Boolean variables can only store two values mostly referred to as Yes or No, True or False. Obviously we never use booleans to perform calculations because of their limited range. We use booleans to evaluate conditions... remember?

```
You have to be taller than 1.5m to ride the roller coaster.
```

"Taller than 1.5m" is the condition in this sentence. This condition is either True or False. You are either taller than 1.5m or you are not. Since most of the Flow-control code in a script is based on conditional statements, booleans play a very important role. Let’s take a look at the looping example:

```
Keep adding milk until the dough is kneadable.
```

The condition here is that the dough has to be kneadable. Let’s assume for the moment that we added something (an algorithm) to our script that could evaluate the current consistency of the dough. Then our first step would be to use this algorithm so we would know whether or not to add milk. If our algorithm returns False (I.e. "the dough isn’t kneadable") then we will have to add some milk. After we added the milk we will have to ask again and repeat these steps until the algorithm returns True (the dough is kneadable). Then we will know there is no more milk needed and that we can move on to the next step in making our Apfelstrudel.

In Python we never write "0" or "1" or "Yes" or "No", for boolean values we always use "True" or "False".

```python
if curve is None:
    print("Something went terribly wrong!")
```

This will return either True or False, only if the result is True (the curve is None) will the code pass into the conditional statement and print "Something went terribly wrong!."

### 2.3.3 Strings

Strings are used to store text. Whenever you add quotes around stuff in Python, it automatically becomes a String. So if we encapsulate a number in quotes, it will become text:

```python
variable1 = 5
variable2 = "5"
```

You could print these variables to the command line and they would both look like 5, but the String variable behaves differently once we start using it in calculations:

```python
print(variable1 + variable2)        # Results in an "Unsupported Operand Type" Error
```

Python throws an error when we try to add a String variable to an Integer Variable.  We must first convert the string to an integer, then we can add them together.

```python
print(variable1 + int(variable2))        # Results in 10
```

When you need to store text, you have no choice but to use Strings. The syntax for Strings is quite simple, but working with Strings can involve some very tricky code. For the time being we’ll only focus on simple operations such as assignment and concatenation:

{{< download-script "rhinopython/rhinopython101/2_3_3_StringConcatenation.py" "2_3_3_StringConcatenation.py">}}

```python
import math
a = "Apfelstrudel"
print(a)

a = "Apfel" + "strudel"
print(a)

a = "4" + " " + "Apfelstrudel"
print(a)

a = "The square root of 2.0 = " + str(math.sqrt(2.0))
print(a)
```

Internally, a String is stored as a series of characters. Every character (or 'char') is taken from the Unicode table, which stores a grand total of ~100.000 different characters. The index into the unicode table for the question mark for example is 63, lowercase e is 101 and the blank space is 32:

{{< image url="/images/primer-strings.svg" alt="/images/primer-strings.svg" class="image_center" width="75%" >}}

<!--TODO: The font in the SVG above is not rendeirng correctly.  What Font to use -->

Further down the road we'll be dealing with some advanced String functions which will require a basic
understanding of how Strings work, but while we are still just using the simple stuff, it's good enough to know it just works the way you expect it to.

Strings are used heavily in Python since object IDs are always written as strings. Object IDs are those weird codes that show up in the Object Property Details: *D7EFCF0A-DB47-427D-9B6B-44EC0670C573*. IDs are designed to be absolutely unique for every object which will ever exist in this universe, which is why we can use them to safely and unambiguously identify objects in the document.

### 2.3.4 None Variable

Whenever we ask Rhino a question which might not have an answer, we need a way for Rhino to say "I don't know". Using the example on page 5:

```python
curve = rs.AddLine([0,0,0], [somenumber,0,0])
```

It is not a certainty that a curve was created. If the user enters zero when he is asked to supply the value for somenumber, then the startpoint of the line would be coincident with the endpoint. Rhino does not like zero-length lines and will not add the object to the document. This means that the return value of `rs.AddLine()` is not a valid object ID. Almost all methods in Rhino will return a None variable if they fail, this way we can add error-checks to our script and take evasive action when something goes wrong.

{{< download-script "rhinopython/rhinopython101/2_1_SomeNumber.py" "2_1_SomeNumber.py">}}

```python
curve = rs.AddLine([0,0,0], [somenumber,0,0])
if not curve:
   print "Something went terribly wrong!"
```

The statement, `if not x` in Python will return a value True if the variable "curve" is *None*, 0 or an empty list.

### 2.3.5 Using Variables

Conventionally, whenever we intend to use variables in a script, we would have to declare them first.  However, with Python, we are relieved of this duty and we can simply create and use variables without initially declaring them. Python also does not require that we declare the type of variable we are using, as in other programming languages.  Both of these qualities emphasize why Python is such a quick and easy to learn language. So, to declare a variable we simply write:

```python
a = "Apfelstrudel"
```

When using a variable, you choose the name and then set it equal to a value (Number, String, Boolean etc).The name you get to pick yourself. In the example above we have used a, which is not the best of all possible choices. For one, it doesn't tell us anything about what the variable is used for or what kind of data it contains. A better name would be `strFood`. The str prefix indicates that we are dealing with a String variable here and the Food bit is hopefully fairly obvious. A widely used system for variable prefixes is as follows:

{{< image url="/images/primer-variable-type.svg" alt="/images/primer-variable-type.svg" class="image_center" width="60%" >}}

Don't worry about all those weird variable types, some we will get to in later chapters, others you will probably never use. The scope (sometimes called "lifetime") of a variable refers to the region of the script where it is accessible. Whenever you declare a variable inside a function, only that one function can read and write to it. Variables go 'out of scope' whenever their containing function terminates. 'Lifetime' is not a very good description in my opinion, since some variables may be very much alive, yet unreachable due to being in another scope. But we'll worry about scopes once we get to function declarations. For now, let's just look at an example with proper variable usage:

{{< download-script "rhinopython/rhinopython101/2_3_5_VariableDeclaration.py" "2_3_5_VariableDeclaration.py">}}

```python
complaint = "I don't like "
food = "Apfelstrudel. "
nag = "Can I go now?"

print(complaint, food, nag)
```

An important note to reiterate is Python's case sensitivity.  Unlike other languages, in Python "Apfelstrudel", "apfelstrudel" and "ApfelStrudel" are not equivalent, this is also true for all variable names, functions, classes and any other part of the code. Just remember to be very careful with upper and lower case letters!

Now, high time for an example. We'll be using the macro from page 2, but we'll replace some of the hard coded numbers with variables for added flexibility. This script looks rather intimidating, but keep in mind that the messy looking bits (line 10 and beyond) are caused by the script trying to mimic a macro, which is a bit like trying to drive an Aston-Martin down the sidewalk. Usually, we talk to Rhino directly without using the command-line and the code looks much friendlier:

{{< download-script "rhinopython/rhinopython101/2_3_5_TorusScript.py" "2_3_5_TorusScript.py">}}

{{< div class="line-numbers" >}}
```python
import rhinoscriptsyntax as rs

major_radius = rs.GetReal("Major radius", 10.0, 1.0, 1000.0)
minor_radius = rs.GetReal("Minor radius", 2.0, 0.1, 100.0)
sides = rs.GetInteger("Number of sides", 6, 3, 20)

point1 = " w" + str(major_radius) + ",0,0"
point2 = " w" + str(major_radius + minor_radius) + ",0,0"

rs.Command("_SelNone")
rs.Command("_Polygon _NumSides=" + str(sides) + " w0,0,0" + point1)
rs.Command("_SelLast")
rs.Command("-_Properties _Object _Name Rail _Enter _Enter")
rs.Command("_SelNone")
rs.Command("_Polygon _NumSides=" + str(sides) + point1 + point2)
rs.Command("_SelLast")
rs.Command("_Rotate3D w0,0,0 w1,0,0 90")
rs.Command("-_Properties _Object _Name Profile _Enter _Enter")
rs.Command("_SelNone")
rs.Command(" _-Sweep1 _-SelName Rail _-SelName Profile _Enter _Enter _Closed=Yes _Enter")
rs.Command("_-SelName Rail")
rs.Command("_-SelName Profile")
rs.Command("_Delete")
```
{{< /div >}}

<table class="multiline">
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
2.5
</td>
<td>
This is where we ask the user to enter a number value ("Real" is another word for "Double"). We supply the *rs.GetReal()* method with four fixed values, one string and three doubles. The string will be displayed in the command-line and the first double (10.0) will be available as the default option:

<img src="/images/primer-getrealexample.png" width="75%" margin="10px"><br>

We're also limiting the numeric domain to a value between one and a thousand. If the user attempts to enter a larger number, Rhino will claim it's too big:

<br><img src="/images/primer-getrealexamplemaximumlimit.png" width="75%">

</td>
</tr>
<tr>
<td>7...8</td>
<td>On these lines we're creating the strings, based on the values of `dblMajorRadius` and `dblMinorRadius`. If we assume the user has chosen the default values in all cases, `dblMajorRadius` will be 10.0 and `dblMinorRadius` will be 2.0, which means that `strPoint2` will look like " w12,0,0".</td>
</tr>
<tr>
<td>10...23</td>
<td>This is the same as the macro on page 3, except that we've replaced some bits with variables and there are three extra lines at the bottom which get rid of the construction geometry (so we can run the script more than once without it breaking down).</td>
</tr></table>

## Next Steps

There are the basics of the Python datastructures, next learn the Python's [script anatomy](/guides/rhinopython/primer-101/3-script-anatomy/).
