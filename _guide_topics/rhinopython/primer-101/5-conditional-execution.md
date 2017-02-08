---
title: 5 Conditional Statements
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

## 5.1 What if?

What if I were to fling this rock at that bear? What if I were to alleviate that moose from its skin and wear it myself instead? It's questions like these that signify abstract thought, perhaps the most stunning of all human traits. As a programmer, you need to take abstract thought to the next level; the very-very-conscious level. 

A major part of programming is recovering from screw-ups. A piece of code does not always behave in a straightforward manner and we need to catch these aberrations before they propagate too far. Other times we design our code to deal with more than one situation. In any case, there's always a lot of conditional evaluation going on, a lot of 'what if' questions. Let's take a look at three conditionals of varying complexity:

1. If the object is a curve, delete it.
2. If the object is a short curve, delete it.
3. If the object is a short curve, delete it, otherwise move it to the "curves" layer.

The first conditional statement evaluates a single boolean value; an object is either is a curve or it is not. There's no middle ground. The second conditional must also evaluate the constraint 'short'. Curves don't become short all of a sudden any more than people grow tall all of a sudden. We need to come up with a boolean way of talking about 'short' before we can evaluate it. The third conditional is identical to the second one, except it defines more behavioral patterns depending on the outcome of the evaluation.

The translation from English into Python is not very difficult. We just need to learn how conditional syntax works.

Problem 1:

```python
if (rs.IsCurve(strObjectID)):
    rs.DeleteObject(strObjectID)
```

Problem 2:

```python
if (rs.IsCurve(strObjectID)):
    if (rs.CurveLength(strObjectID) < 0.01):
        rs.DeleteObject(strObjectID)
```

Problem 3:

```python
if (rs.IsCurve(strObjectID)):
    if (rs.CurveLength(strObjectID) < 0.01):
        rs.DeleteObject(strObjectID)
    else:
        rs.ObjectLayer(strObjectID, "Curves")
```

The most common conditional evaluation is the If…Then statement. If…Then allows you to bifurcate the flow of a program. The simplest If…Then structure can be used to shield certain lines of code. It always follows the same format:

```python
if (SomethingOrOther):
    DoSomething()
    DoSomethingElseAsWell()
```

The bit of code that is indented after the *if():* is evaluated and when it turns out to be True, the block of code between the first and last line will be executed. If *SomethingOrOther* turns out to be False, lines 2 and 3 are skipped and the script goes on with whatever comes after line 3.

In case of very simple If…Then structures, such as the first example, it is possible to use a shorthand notation which only takes up a single line instead of three. The shorthand for If…Then looks like:

```python
if (SomethingOrOther): DoSomething()
```

Whenever you need an If…Then…Else structure, you can use the following syntax:

```python
    if (SomethingOrOther):
    DoSomething()
else:
    DoSomethingElse()
```

If *SomethingOrOther* turns out to be True, then the bit of code between lines 1 and 3 are executed. This block can be as long as you like of course. However, if *SomethingOrOther* is False, then the code after else is executed. So in the case of If…Else, one -and only one- of the two blocks of code is put to work.

You can nest If…Then structures as deep as you like, though code readability will suffer from too much indenting.
The following example uses four nested If…Then structures to delete short, closed curves.

```python
    if (rs.IsCurve(strObjectID)):
    if (rs.CurveLength(strObjectID) < 1.0):
        if (rs.IsCurveClosed(strObjectID)):
            rs.DeleteObject(strObjectID)
```

When you feel you need to split up the code stream into more than two flows and you don't want to use nested structures, you can instead switch to something which goes by the name of the If…Elif…Else statement.

As you may or may not know, the Make2D command in Rhino has a habit of creating some very tiny curve segments. We could write a script which deletes these segments automatically, but where would we draw the line between 'short' and 'long'? We could be reasonably sure that anything which is shorter than the document absolute tolerance value can be removed safely, but what about curves which are slightly longer? Rule #1 in programming: When in doubt, make the user decide. That way you can blame them when things go wrong. 

A good way of solving this would be to iterate through a predefined set of curves, delete those which are definitely short, and select those which are ambiguous. The user can then decide for himself whether those segments deserve to be deleted or retained. We won't discuss the iteration part here. The conditional bit of the algorithm looks like this:

```python
dblCurveLength = rs.CurveLength(strObjectID)

if (dblCurveLength != None):
    if (dblCurveLength < rs.UnitAbsoluteTolerance()):
        rs.DeleteObject(strObjectID)
    elif (dblCurveLength < (10 * rs.UnitAbsoluteTolerance())):
        rs.SelectObject(strObjectID)
    else:
        rs.UnselectObject(strObjectID)
```

In Python you can say the same thing in many different ways. The above snippet could have been written as a nested If…Then structure, but then it would not resemble the way we think about the problem.

## 5.2 Looping

Executing certain lines of code more than once is called looping in programming slang. There are two types of loops; conditional and incremental which can be described respectively as:

```
Keep adding milk until the dough is kneadable
Add five spoons of cinnamon
```

Conditional loops will keep repeating until some condition is met where as incremental loops will run a predefined number of times. Life isn't as simple as that though, and there are many different syntax specifications for loops in Python, we'll only discuss the two most important ones in depth.


## 5.3 Conditional loops

Sometimes we do not know how many iterations we will need in advance, so we need a loop which is potentially capable of running an infinite number of times. This type is called a Do…Loop. In the most basic form it looks like this:

```python
while (something is true):
    DoSomething()
    if (condition is met):
        break
```    

All the lines indented after the while keyword will be repeated until we abort the loop ourselves. If we do not abort the loop, I.e. if we omit the break statement or if our condition just never happens to be met, the loop will continue forever. This sounds like an easy problem to avoid but it is in fact a very common bug.

In Python it does not signify the end of the world to have a truly infinite loop. The following example script contains an endless While...Loop which can only be cancelled by shutting down the application.

```python
import rhinoscriptsyntax as rs
import datetime as dt

def viewportclock():
    now = dt.datetime.now()
    textobject_id = rs.AddText(str(now), (0,0,0), 20)
    if textobject_id is None: return
    rs.ZoomExtents(None, True)
    while True:
        rs.Sleep(1000)
        now = dt.datetime.now()
        rs.TextObjectText(textobject_id, str(now))

if __name__=="__main__":
    viewportclock()

	
```	
{: .line-numbers}


<img src="{{ site.baseurl }}/images/primer-viewportclock.svg">{: .img-center  width="40%"}


Here's how it works:


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
1 & 2
</td>
<td>
Import calls referencing external code - in this case, Rhinoscriptsyntax and datetime.
We assign each of them an alias using the 'as' keyword in order simplify function calls later.
</td>
</tr>
<tr>
<td>4</td>
<td>Main Function declaration</td>
</tr>
<tr>
<td>5</td>
<td>We create a time object which contains a record the date and time of the function call datetime.now().</td>
</tr>
<tr>
<td>6</td>
<td>
We create a new Rhino Text object to display the date and time from step 5.

<code class="language-python hljs">
rs.AddText (Text, point_or_plane , Height=1.0 , Font="Arial" ,font_style=0 )
</code>

Five arguments, the last three of which have default assignments, and so are optional. When adding a text object to Rhino we must specify the text string and the location for the object. There are no defaults for this. The height of the text, font name and style do have default values. However, since we're not happy with the default height, we will override it to be much bigger:

<code class="language-python hljs">
textobject_id = rs.AddText(str(now), (0,0,0), 20)
</code>

The Text argument must contain a String description of the current system time. We will simply nest casting function to get it. Since a cast operation for a datetime object is a well known and solid operation, we do not have to check for a Null variable and we can put it 'inline'. This will give us the date and the time. we could have pared this down to just the time by calling the *dt.datetime.time(now)* function. Neither of these return a String type variable, so before we pass it into Rhino we have to cast it to a proper String using the *str()* function. This is analogous with our code on page 20.

The *point_or_plane* argument requires a list of doubles. We haven't done lists yet, but it essentially means we have to supply the x, y and z coordinates of the text insertion point. *(0,0,0)* means the same as the world origin. 

The default height of text objects is 1.0 units, but we want our clock to look big since big things look expensive. Therefore we're overriding it to be 20 units instead.
</td>
</tr>
<tr>
<td>7</td>
<td>I don't think there's anything here that could possibly go wrong, but it never hurts to be sure. Just in case the text object hasn't been created we need to abort the subroutine in order to prevent an error later on.</td>
</tr>
<tr>
<td>9</td>
<td>We start an infinite While... loop, lines 10, 11 and 12 will be repeated for all eternity.</td>
</tr>
<tr>
<td>10</td>
<td>There's no need to update our clock if the text remains the same, so we really only need to change the text once every second. The *Rhino.Sleep()* method will pause Rhino for the specified amount of milliseconds. We're forcing the loop to take it easy, by telling it to take some time off on every iteration. We could remove this line and the script will simply update the clock many times per second. This kind of reckless behaviour will quickly flood the undo buffer.</td>
</tr>
<tr>
<td>11</td>
<td>Here we update our now object. This will give us an updated datetime object.</td>
</tr>
<tr>
<td>12</td>
<td>This is the cool bit. Here we replace the text in the object with a new String representing the current system time.</td>
</tr>
<tr>
<td>14 & 15</td>
<td>This is where the viewport clock function is called. In IronPython, the main function call must be executed after the definition of the function. The if __name__ == "__main__": ... trick exists in Python so that our Python files can act as either reusable modules, or as standalone programs. </td>
</tr>
</table>
{: .multiline}


 
![{{ site.baseurl }}/images/primer-iterativecurvescaler.svg]({{ site.baseurl }}/images/primer-iterativecurvescaler.svg){: .float-img-right width="325"}

A simple example of a non-endless loop which will terminate itself would be an iterative scaling script. Imagine we need a tool which makes sure a curve does not exceed a certain length {L}. Whenever a curve does exceed this predefined value it must be  scaled down by a factor {F} until it no longer exceeds {L}. 

This approach means that curves that turn out to be longer than {L} will probably end up being shorter than {L}, since we always scale with a fixed amount. There is no mechanism to prevent undershooting. Curves that start out by being shorter than {L} should remain untouched.


A possible solution to this problem might look like this:

```python
import rhinoscriptsyntax as rs
# Iteratively scale down a curve until it becomes shorter than a certain length

def fitcurvetolength():
    curve_id = rs.GetObject("Select a curve to fit to length", rs.filter.curve, True, True)
    if curve_id is None: return
    
    length = rs.CurveLength(curve_id)

    length_limit = rs.GetReal("Length limit", 0.5 * length, 0.01 * length, length)
    if length_limit is None: return

    while True:
        if rs.CurveLength(curve_id)<=length_limit: break
        curve_id = rs.ScaleObject(curve_id, (0,0,0), (0.95, 0.95, 0.95))
        if curve_id is None:
            print "Something went wrong..."
            return

    print "New curve length: ", rs.CurveLength(curve_id)

if __name__=="__main__":
    fitcurvetolength()
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
1...4
</td>
<td>
This should be familiar by now
</td>
</tr>
<tr>
<td>5</td>
<td>Prompt the user to pick a single curve object, we're allowing preselection.</td>
</tr>
<tr>
<td>6</td>
<td>Check that the user picked an object, and that its id was written to our curve_id variable. Exit if not.</td>
</tr>
<tr>
<td>8</td>
<td>Retrieve the current curve length. This function should not fail, no need to check for Null.</td>
</tr>
<tr>
<td>10</td>
<td>Prompt the user for a length limit value. The value must be chosen between the current curve length and 1% of the current curve length. We're setting the default to half the current curve length.</td>
</tr>
<tr>
<td>13</td>
<td>Start a While... loop</td>
</tr>
<tr>
<td>14</td>
<td>This is the break-away conditional. If the curve length no longer exceeds the preset limit, the break statement will take us directly to line 20.</td>
</tr>
<tr>
<td>15</td>
<td>If the length of the curve did exceed the preset limit, this line will be executed. The <i>rs.ScaleObject()</i> 
method takes four arguments, the last one of which is optional. We do not override it. We do need to specify which object we want rescaled <i>(curve_id)</i>, what the center of the scaling operation will be (<i>(0,0,0)</i>; the world origin) and the scaling factors along x, y and z (95% in all directions).</td>
</tr>
<tr>
<td>19</td>
<td>This line ends all indented code, which instructs the interpreter to go back to line 13</td>
</tr>
<tr>
<td>6</td>
<td>Eventually all curves will become shorter than the limit length and the While... loop will abort. We print out a message to the command line informing the user of the new curve length.</td>
</tr>
</table>
{: .multiline}

## 5.4 Incremental loops

When the number of iterations is known in advance, we could still use a While…Loop statement, but we'll have to do the bookkeeping ourselves. This is rather cumbersome since it involves us declaring, incrementing and evaluating variables. The For...statement is a loop which takes care of all this hassle. The underlying idea behind For... loops is to have a value incremented by a fixed amount every iteration until it exceeds a preset threshold: 

```python
group = 10
for item in group:
    AddSpoonOfCinnamon()
```

This loop will operate for each item in the group, adding a spoon of cinnamon and will exit when we come to the last item of the group.

We can also use the range() function for more control:

```python
for i in range(A,B,N):
    AddSpoonOfCinnamon()
```

The variable i starts out by being equal to A and it is incremented by N until it becomes 1 less than B. In other words, B is the total amount that you want to increment up to. Remember, that in programming, we always start with 0, therefore the total increment amount will be 1 more than we actually want! N signifies the "Step" value which is optional and if we do not override it the default stepsize of 1.0 will be used. If we have a stepsize of 2, it will increment every-other time. In the example above the variable i is not used in the loop itself, we're using it for counting purposes only.

If we want to abort a For... loop ahead of time, we can use break in order to short-circuit the process.
Creating mathematical graphs is a typical example of the usage of For…Loops:


```python
import math
import rhinoscriptsyntax as rs
#Draw a sine wave using points

dblA = -8.0
dblB = 8.0
dblStep = 0.25

for x in rs.frange(dblA, dblB, dblStep):
    y = 2*math.sin(x)
    rs.AddPoint([x, y, 0])    
```

![{{ site.baseurl }}/images/primer-sinewave.svg]({{ site.baseurl }}/images/primer-sinewave.svg){: .float-img-right width="375"}

The above example draws a sine wave graph in a certain numeric domain with a certain accuracy. There is no user input since that is not the focus of this paragraph, but you can change the values in the script. The numeric domain we're interested in ranges from -8.0 to +8.0 and with the current stepsize of 0.25 that means we'll be running this loop 64 times. 64 = dblStep-1 × (dblB - dblA)) 

The For…loop will increment the value of x automatically with the specified stepsize, so we don't have to worry about it when we use x on line 10. We should be careful not to change x inside the loop since that will play havoc with the logic of the iterations.

Loop structures can be nested at will, there are no limitations, but you'll rarely encounter more than three. The following example shows how nested For…Loops can be used to compute distributions:

```primer
import math
import rhinoscriptsyntax as rs

pi = math.Pi()
dblTwistAngle = 0.0

rs.EnableRedraw(False)
for z in rs.frange(0.0, 5.0, 0.5):
   dblTwistAngle = dblTwistAngle + (pi/30)
      
   for a in rs.frange(0.0, 2*pi, (pi/15)):
       x = 5 * math.sin(a + dblTwistAngle)
       y = 5 * math.cos(a + dblTwistAngle)
       rs.AddSphere([x,y,z], 0.5)

rs.EnableRedraw(True)
```    
![{{ site.baseurl }}/images/primer-twistandshout.svg]({{ site.baseurl }}/images/primer-twistandshout.svg){: .float-img-right width="375"}

The master loop increments the z variable from 0.0 to 5.0 with a default step size of 0.5. The z variable is used directly as the z-coordinate for all the sphere centers. For every iteration of the master loop, we also want to increment the twist angle with a fixed amount. We can only use the For…Loop to automatically increment a single variable, so we have to do this one ourselves on line 8.

The master loop will run a total of ten times and the nested loop is designed to run 30 times. But because the nested loop is started every time the master loop performs another iteration, the code between lines 11 and 14 will be executed 10×30 = 300 times. Whenever you start nesting loops, the total number of operations your script performs will grow exponentially.


The *rs.EnableRedraw()* calls before and after the master loop are there to prevent the viewport from updating 
while the spheres are inserted. The script completes much faster if it doesn't have to redraw 330 times. If you comment out the *rs.EnableRedraw()* call you can see the order in which spheres are added, it may help you understand how the nested loops work together.

---

## Next Steps

Now it should be coming together on how Python works.  Just a few more details. Leanr more about Python's advanced variables in [Tuples, Lists and Dictionaries]({{ site.baseurl }}/guides/rhinopython/primer-101/6-tuples-lists-dictionaries/).
