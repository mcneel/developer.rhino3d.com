+++
aliases = ["/5/guides/rhinopython/primer-101/6-tuples-lists-dictionaries/", "/6/guides/rhinopython/primer-101/6-tuples-lists-dictionaries/", "/7/guides/rhinopython/primer-101/6-tuples-lists-dictionaries/", "/wip/guides/rhinopython/primer-101/6-tuples-lists-dictionaries/"]
authors = [ "skylar-tibbits", "arthur-van-der-harten", "steve" ]
categories = [ "Rhino.Python 101" ]
category_page = "guides/rhinopython/primer-101/"
keywords = [ "python", "commands" ]
languages = [ "Python" ]
sdk = [ "RhinoPython" ]
title = "6 Tuples, Lists and Dictionaries"
type = "guides"
weight = 15
override_last_modified = "2018-12-05T14:59:06Z"

[admin]
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++

## 6.1 Tuples

We've already been using tuples and lists in examples and I've always told you not to worry about it. Those days are officially over. Now is the time to panic. Perhaps it's best if we just get the obvious stuff out of the way first:

**Tuples, Lists and Dictionaries are just a collection of things!**

That's really all there is to it. Sometimes -in fact quite often- you want to store a large or unknown amount of things. You could of course declare 15,000 different variables by hand but that is generally considered to be bad practice. Remember, Tuples, Lists and Dictionaries always start counting at zero, while us humans are normally used to start counting at one. Try it by counting the number of fingers on your right hand. Chances are you are someone who has just counted to five. Code would disagree with you, it would only have counted to four:

{{< image url="/images/primer-arraycountingfingers.png" alt="/images/primer-arraycountingfingers.png" class="image_center" width="25%" >}}

It helps to refer to numbers as 'indices' when you use the zero-based counting system just to avoid confusion. So when we talk about the 'first element' of a tuple we actually mean 'the element with index 0'. I know this all sounds strange, but zero-based counting systems habitually confuse even the most die-hard programmer.

A tuple consists of a number of values separated by commas, for instance:

```python
t = 12345, 5421, 'hello!' # Creating a Tuple with a variable name t
print(t[0]) # print the first value of the Tuple t
# This returns 12345 - the first value inside the Tuple
print(t)
# This returns (12345, 54321, 'hello!') - all of the values within the Tuple
```

Tuples can be used for coordinates (x,y) or any other time you need to store various elements.  Tuples may contain multiple variables, nested Tuples, Lists or other objects. If you remember from section 4.5, Tuples are immutable, meaning that they cannot be changed! (Refer to section 4.5 on Mutability) That means that we cannot create a Tuple then remove an element, instead we need to create an entirely new Tuple that contains the desired change.  A number of RhinoscriptSyntax methods return tuples rather than lists for their simplicity.  When utilizing the RhinoscriptSyntax methods make sure to be particularly careful with the input and return types (numbers, strings, tuples, lists etc) and understand how to pass or use each of them. This is a common source of errors in people's code, so pay special attention to read the methods found in the RhinoscriptSyntax help file!

## 6.2 Lists

Lists are just like Tuples, however they can be changed (mutable), they use brackets rather than parenthesis and  have far more powerful built-in functionality!  Lists can be added to, items can be removed, they can be sorted, sliced apart, nested with multiple levels of inner lists and packed with other objects.  Lists are very powerful!

```python
myList = [] #This creates an empty list with the variable name myList
myList.append(5)
myList.append(6)
print myList[0]
# This returns 5 - the first element (0th item) in the list
print(myList)
# This returns [5,6] - the entire contents of the list myList
```

Lists also can be sliced by using the following syntax:

```python
myList = [1,2,3,4] #This creates a list with elements 1,2,3,4
print (myList[1:3])
#This returns [2,3] - the 1st and 2nd elements of the list
```

Similar to the range() function, the syntax for slicing list[start:end] - begins with the index of "start" (from the 0th element) and finishes at 1 less than the index "end." To create a copy of a list we can also use a similar syntax:

```python
myList = [1,2,3,4] #This creates a list with elements 1,2,3,4
dupList = myList[:]
```
Some useful methods for lists:

| Method           |      |      | Description                              |
| :--------------- | :--: | :--: | :--------------------------------------- |
| list.append(x)   |      |      | Adds an item to the end of  a list.      |
| list.insert(i,x) |      |      | Inserts item i at location x.</td>       |
| list.remove(x)   |      |      | Removes the first item from the list who's value is x. |
| list.count(s)    |      |      | Counts how many times an item x is found within the list. |
| list.append(x)   |      |      | Adds an item to the end of  a list.      |
| list.sort()      |      |      | Sorts the elements of the list.          |
| list.reverse()   |      |      | Reverses the elements of the list.       |

### 6.2.1 List Comprehension

List comprehensions are a way of utilizing the functionality of Lists and For...Loops with very concise syntax. The list comprehension begins with an expression then has a For...Loop - effectively executing the expression for the number of times specified in the For...Loop. This will create a List with the resultant values from the expression. For example:

```python
myList = [2,4,6] #This creates a list with elements 2,4,6
print ([3*x for x in myList]
# This returns [6,12,18] as the resultant calculation from the List Comprehension
```

List comprehensions can become far more complex and include more complicated expressions, loops and conditional statements.  One last example:

```python
myList = [2,4,6] #This creates a list with elements 2,4,6
print ([3*x for x in myList if x>3]
# This returns [12,18] as the resultant calculation from the expression, loop and conditional
```

The following example should teach you almost all there is to know about lists, except nesting:

{{< div class="line-numbers" >}}
```python
import rhinoscriptsyntax as rs

def myfavoritethings():
    things = []

    while True:
        count = len(things)
        prompt = "What is your {0}th most favorite thing?".format(count+1)
        if len(things)==0:
            prompt = "What is your most favorite thing?"
        elif count==1:
            prompt = "What is your second most favorite thing?"
        elif count==2:
            prompt = "What is your third most favourite thing?"

        answer = rs.GetString(prompt)
        if answer is None: break
        things.append(answer)
    if len(things)==0: return

    print "Your", len(things)+1, "favorite things are:"
    for i,thing in enumerate(things): print i+1, ".", thing
```
{{< /div >}}

<table class="multiline">
<tr>
<th>Line</th>
<th>Description</th>
</tr>
<tr>
<td>4</td>
<td>We do not know how many favourite things the user has, so there's no way we can set the list to a certain size in advance. Luckily, we do not have to. Items can be appended to a list on an as needed basis!</td>
</tr>
<tr>
<td>7</td>
<td>The function len() returns the length of a list object. The very first time this line is run, count will be 0.</td>
</tr>
<tr>
<td>17</td>
<td>If the user does not enter an answer to our question regarding his/her Nth favorite thing, we will exit the loop and move into the last task of the script on lines 21 and 22.</td>
</tr>
<tr>
<td>18</td>
<td>We've just asked the user what his/her Nth favourite thing was, and he/she answered truthfully. This means that it is time to store the answer in a safe place. A list is a convenient place to store an arbitrarily long collection of data. The append function shown will add the entry to the end of the list.</td>
</tr>
<tr>
<td>19</td>
<td>It is possible the user has not entered any String. If this is the case then the result of len(things) will still have a its initial value of zero. There is nothing for us to do in this case and we should abort the subroutine.</td>
</tr>
<tr>
<td>21</td>
<td>After the loop has completed and we've made certain the array contains some actual data, we print all the gathered information to the command history. First we will tell the user how many favourite things he/she entered.</td>
</tr>
<tr>
<td>22</td>
<td>Using a For...loop, we can iterate through the items in the list. Note that this For...loop has two iteration variables - one to keep track of the index of the list item, and one to get the actual list item. This is convenient, as it is not necessary to explicitly retrieve the item in the list using the index.
We then print the index of the user's nth favority thing, and the favorite thing.</td>
</tr>
</table>

## 6.3 Dictionaries

Dictionaries go one step further than lists because they store a "key" and an associated value.  Every dictionary contains a series of key : value associations.  This is very similar to actual word-based dictionaries that contain words and their associated definition.  Python Dictionaries can use any immutable type for the "key", such as; strings, numbers, Tuples (they can only contain strings, numbers or tuples and NOT lists). The value can be any mutable or immutable item that will become associated to the key (this includes, lists or other dictionaries). Lets see an example:

```python
emptyDict = {} #This creates an empty Dictionary
myDict = {'a':1,'b':2,'c':3} #This creates a Dictionary with its associated Key:Value pairs
myDict['d'] = 4 #This Adds a key:value to the Dictionary
myDict['a'] = 2 #This Changes the key "a"'s value to 2 rather than 1
print (myDict['a'])
#This returns 2 - the associated value to the key "a"
print (myDict)
#This returns {'a': 2, 'c': 3, 'b': 2, 'd': 4} - the entire Dictionary
print (myDict.keys())
#This returns ['a', 'c', 'b', 'd'] - a list containing all of the Keys
del myDict['b'] # This deletes the Key "b" and its associated value of 2
```

Because of the associated Key:Value relationship, Dictionaries are great for representing points and giving them an associated name based on the points relationship to their neighbors.  Let's say we have a surface and we want to extract points across the surface with rows and columns.  Each point has a 3D point coordinate [x,y,z] which is represented as a list who's first element 0 corresponds to x, element 1 corresponds to y and element 2 corresponds to z. If we wanted to store these points we have 2 options. We could create a list with internal lists that contain the point coordinates (one long linear organization of points) or we could use a Dictionary to add point coordinates as values and have a Key that is a name in relation to its Row/Column position.  The second option then allows us to take any point on the surface and know its 4, 8 or however many neighbors because they are named accordingly.  The first option would only allow us to know the neighbor direction in front or behind it in line.  We will get into this more later, but this should wet your appetite for the exciting potential of lists and dictionaries for geometric information!

## 6.4 Points and Vectors

As was just explained, points are represented by lists containing three values - [x,y,z]. This notation is used for both points and vectors. First, a point example:

{{< div class="line-numbers" >}}
```python
import rhinoscriptsyntax as rs
import math

#Call rs.EnableRedraw(False)
for t in rs.frange(-50,50,1.25):
    arrPoint = [t * math.sin(5*t), t * math.cos(5*t),t]

   print(arrPoint)
   rs.AddPoint(arrPoint)
#Call rs.EnableRedraw(True)
```
{{< /div >}}

{{< image url="/images/primer-pointspiral.svg" alt="/images/primer-pointspiral.svg" class="float_right" width="375" >}}

The variable arrPoint is declared as an empty list, the elements are assigned different values on lines 7 to 9 inside the body of the loop. On line 10 the list is printed and on line 11 it is used as the point coordinates to create a 3D point in space.

Vectors are a slightly new concept. Those of you who are familiar with the essentials of geometrical mathematics will have no problems with this concept... in fact you probably all are familiar with the essentials of geometrical mathematics or you wouldn't be learning how to program a 3D CAD platform.


Vectors are indistinguishable from points. That is, they are both lists of three numbers so there's absolutely no way of telling whether a certain list represents a point or a vector. There is a practical difference though; points are absolute, vectors are relative. When we treat a list of three doubles as a point it represents a certain coordinate in space, when we treat it as a vector it represents a certain direction. You see, a vector is an arrow in space which always starts at the world origin (0.0, 0.0, 0.0) and ends at the specified coordinate.

{{< image url="/images/primer-vectordefinition.svg" alt="/images/primer-vectordefinition.svg" class="float_right" width="375" >}}

The picture on the right shows two vector definitions; a purple and a blue one. The blue one happens to have all positive components while the purple one has only negative components. Both vectors have a different direction and a different length. When I say vectors are relative, I mean that they only indicate the difference between the start and end points of the arrow, i.e. vectors are not actual geometrical entities, they are only information! The blue vector could represent the tangent direction of the black curve at parameter {t}. If we also know the point value of the curve at parameter {t}, we know what the tangent of the curve looks like; we know where in space the tangent belongs. The vector itself does not contain this information; the orange and the blue vector are identical in every respect.

The addition of vector definitions in IronPython is accompanied by a whole group of point/vector related methods which perform the basic operations of 'vector mathematics'. Addition, subtraction, multiplication, dot and cross products, so on and so forth. The table on the following page is meant as a reference table, do not waste your time memorizing it.

I will be using standard mathematical notation:

- A lowercase letter represents a number
- A lowercase letter with a dot above it represents a point
- A lowercase letter with an arrow above it represents a vector
- Vertical bars are used to denote vector length



<table class="multiline-middle" width="100%">
<tr>
<th>Notation</th>
<th width="25%">Implementation</th>
<th>Description</th>
<th>Example</th>
</tr>
<tr>
<td>{{< mathjax >}}$$d =|\dot{p}-\dot{r}|$${{< /mathjax >}}</td>
<td>Distance(Pt1, Pt2)</td>
<td>Compute the distance between two points.</td>
<td><img src="/images/primer-distance.svg" width="100%"></td>
</tr>
<tr>
<td>{{< mathjax >}}$$\dot{r} = a \times \dot{p}$${{< /mathjax >}}</td>
<td>PointScale(Pt1, dblA)</td>
<td>Multiply the components of the point by the specified factor. This operation is the equivalent of a 3DScaling around the world origin.</td>
<td><img src="/images/primer-pointscale.svg" width="100%"></td>
</tr>
<tr>
<td>{{< mathjax >}}$$\dot{r} = \frac{\dot{p}}{a}$${{< /mathjax >}}</td>
<td>PointDivide(Pt1, dblA)</td>
<td>Divide the components of the point by the specified factor. This is the equivalent of <i>PointScale(Pt1, a-1)</i>.</td>
<td><img src="/images/primer-pointdivide.svg" width="100%"></td>
</tr>
<tr>
<td>{{< mathjax >}}$$? \dot{r} = \dot{p} \pm t$${{< /mathjax >}}</td>
<td>PointCompare(Pt1, Pt2, dblT)</td>
<td>Check to see if two points are more or less identical. Two points are identical if the length of the vector between them is less than the specified tolerance.</td>
<td><img src="/images/primer-pointcompare.svg" width="100%"></td>
</tr>
<tr>
<td>{{< mathjax >}}$$\dot{r} = \dot{p} \times \mathbb{M}$${{< /mathjax >}}</td>
<td>PointTransform(Pt1, arrM)</td>
<td>Transform the point using a linear transformation matrix. </td>
<td><img src="/images/primer-pointtransform.svg" width="100%"></td>
</tr>
<tr>
<td>{{< mathjax >}}$$\overrightarrow{w} = \left(\frac{1}{|\overrightarrow{v}|} \right) \times \overrightarrow{v}$${{< /mathjax >}}</td>
<td>VectorUnitize(Vec1)</td>
<td>Divide all components by the inverse of the length of the vector. The resulting vector has a length of 1.0 and is called the unit-vector. Unitizing is sometimes referred to as "normalizing".</td>
<td><img src="/images/primer-vectorunitize.svg" width="100%"></td>
</tr>
<tr>
<td>{{< mathjax >}}$$l = |\overrightarrow{v}|$${{< /mathjax >}}</td>
<td>VectorLength(Vec1)</td>
<td>Compute the square root of the sum of the squares of all the components. Standard Pythagorean distance equation.</td>
<td><img src="/images/primer-vectorlength.svg" width="100%"></td>
</tr>
<tr>
<td>{{< mathjax >}}$$\overrightarrow{w} = -\overrightarrow{v}$${{< /mathjax >}}</td>
<td>VectorReverse(Vec1)</td>
<td>Negate all the components of a vector to invert the direction. The length of the vector is maintained.</td>
<td><img src="/images/primer-vectorreverse.svg" width="100%"></td>
</tr>
<tr>
<td>{{< mathjax >}}$$? \overrightarrow{w} = \overrightarrow{v} \pm t$${{< /mathjax >}}</td>
<td>VectorCompare(Vec1, Vec2, dblT)</td>
<td>Check to see if two vectors are more or less identical. This is the equivalent of <i>PointCompare()</i>.</td>
<td><img src="/images/primer-vectorcompare.svg" width="100%"></td>
</tr>
<tr>
<td>{{< mathjax >}}$$\overrightarrow{w} =\frac{\overrightarrow{v}}{a}$${{< /mathjax >}}</td>
<td>VectorDivide(Vec1, dblA)</td>
<td>Divide the components of the vector by the specified
factor. This is the equivalent of *PointDivide()*.</td>
<td><img src="/images/primer-vectordivide.svg" width="100%"></td>
</tr>
<tr>
<td>{{< mathjax >}}$$\dot{r} = \dot{p} + \overrightarrow{v}$${{< /mathjax >}}</td>
<td>PointAdd(Pt1, Vec1)</td>
<td>Add the components of the vector to the components of the point. Point-Vector summation is the equivalent of moving the point along the vector.</td>
<td><img src="/images/primer-pointadd.svg" width="100%"></td>
</tr>
<tr>
<td>{{< mathjax >}}$$\dot{r} = \dot{p} - \overrightarrow{v}$${{< /mathjax >}}</td>
<td>PointSubtract(Pt1, Vec1)</td>
<td>Subtract the components of the vector from the components of the point. Point-Vector subtraction is the equivalent of moving the point along the reversed vector.</td>
<td><img src="/images/primer-pointsubtract.svg" width="100%"></td>
</tr>
<tr>
<td>{{< mathjax >}}$$\overrightarrow{v} = \dot{p} - \dot{r}$${{< /mathjax >}}</td>
<td>PointSubtract(Pt1, Vec1)</td>
<td>Subtract the components of the vector from the components of the point. Point-Vector subtraction is the equivalent of moving the point along the reversed vector.</td>
<td><img src="/images/primer-vectorcreate.svg" width="100%"></td>
</tr>
<tr>
<td>{{< mathjax >}}$$\overrightarrow{u} = \overrightarrow{v} + \overrightarrow{w}$${{< /mathjax >}}</td>
<td>VectorAdd(Vec1, Vec2)</td>
<td>Add the components of Vec1 to the components of Vec2. This is equivalent to standard vector summation.</td>
<td><img src="/images/primer-vectoradd.svg" width="100%"></td>
</tr>
<tr>
<td>{{< mathjax >}}$$\overrightarrow{u} = \overrightarrow{v} - \overrightarrow{w}$${{< /mathjax >}}</td>
<td>VectorSubtract(Vec1, Vec2)</td>
<td>Subtract the components of Vec1 from the components of Vec2. This is equivalent of *VectorAdd(Vec1, -Vec2)*.</td>
<td><img src="/images/primer-vectorsubtract.svg" width="100%"></td>
</tr>
<tr>
<td>{{< mathjax >}}$$\alpha = \overrightarrow{v} \times \overrightarrow{w}$${{< /mathjax >}}</td>
<td>VectorDotProduct(Vec1, Vec2)<br>-or-<br>VectorMultiply(Vec1, Vec2)</td>
<td>Calculate the sum of the products of the corresponding components. In practical, everyday-life the DotProduct can be used to compute the angle between vectors since the DotProduct of two vectors v and w equals: |v||w| cos(a)</td>
<td><img src="/images/primer-vectordotproduct.svg" width="100%"></td>
</tr>
<tr>
<td>{{< mathjax >}}$$\overrightarrow{u} = \overrightarrow{v} \times \overrightarrow{w}$${{< /mathjax >}}</td>
<td>VectorCrossProduct(Vec1, Vec2)</td>
<td>The cross-product of two vectors v and w, is a third vector which is perpendicular to both v and w.</td>
<td><img src="/images/primer-vectorcrossproduct.svg" width="100%"></td>
</tr>
<tr>
<td>{{< mathjax >}}$$\overrightarrow{u} = \overrightarrow{v} \times (\sphericalangle\alpha)\overrightarrow{w}$${{< /mathjax >}}</td>
<td>VectorRotate(Vec1, dblA, VecA)</td>
<td>Rotate a vector a specified number of degrees around an axis-vector.</td>
<td><img src="/images/primer-vectorrotate.svg" width="100%"></td>
</tr>
</table>

{{< image url="/images/primer-addvector.svg" alt="/images/primer-addvector.svg" class="float_right" width="325" >}}

IronPython has no method for displaying vectors, which is a pity since this would be very useful for visual feedback. I shall define a function here called *AddVector()* which we will use in examples to come. The function must be able to take two arguments; one vector definition and a point definition. If the point array is not defined the vector will be drawn starting at the world origin.


{{< div class="line-numbers" >}}
```python
def AddVector(vecdir, base_point=[0,0,0]):
       tip_point = rs.PointAdd(base_point, vecdir)
       line = rs.AddLine(base_point, tip_point)
       if line: return rs.CurveArrows(line, 2)
```
{{< /div >}}

<table class="multiline">
<tr>
<th>Line</th>
<th>Description</th>
</tr>
<tr>
<td>1</td>
<td>Standard function declaration. The function takes two arguments, if the first one does not represent a proper vector array the function will not do anything, if the second one does not represent a proper point array the function will draw the vector from the world origin.</td>
</tr>
<tr>
<td>2</td>
<td>Declare and compute the coordinate of the arrow tip. This will potentially fail if ptBase or vecDir are not proper arrays. However, the script will continue instead of crash due to the exception handling.</td>
</tr>
<tr>
<td>3</td>
<td>Here we are calling the RhinoScriptSyntax method rs.AddLine() and we're storing the return value
directly into the line variable. There are three possible scenarios at this point:

<ol>
<li>The method completed successfully</li>
<li>The method failed, but it didn't crash</li>
<li>The method crashed</li>
</ol>

In the case of scenario 1, the line variable now contains the object ID for a newly added line object. This is exactly what we want the function to return on success.
In case of scenario #2, the line variable will be set to None. The last option means that there was no return value for AddLine() and hence line will also be None. </td>
</tr>
<tr>
<td>4</td>
<td>Check for scenario 2 and 3, and if they did not occur, go ahead and and add an arrow head using the CurveArrows method. If they did, this method will not be exectuted, and the script simply does not returns *None*.</td>
</tr>
</table>


## 6.5 An AddVector() example

{{< image url="/images/primeraddvectorexample.svg" alt="/images/primeraddvectorexample.svg" class="float_right" width="325" >}}

{{< div class="line-numbers" >}}
```python
import rhinoscriptsyntax as rs
# This script will compute a bunch of cross-product vector based on a pointcloud

def vectorfield():
    cloud_id = rs.GetObject("Input pointcloud", 2, True, True)
    if cloud_id is None: return

    listpoints = rs.PointCloudPoints(cloud_id)
    base_point = rs.GetPoint("Vector field base point")
    if base_point is None: return

    for point in listpoints:
        vecbase = rs.VectorCreate(point, base_point)
        vecdir = rs.VectorCrossProduct(vecbase, (0,0,1))
        if vecdir:
            vecdir = rs.VectorUnitize(vecdir)
            vecdir = rs.VectorScale(vecdir, 2.0)
            AddVector(vecdir, point)
```
{{< /div >}}

<table class="multiline">
<tr>
<th>Line</th>
<th>Description</th>
</tr>
<tr>
<td>8</td>
<td>The <i>listpoints</i> variable is a list which contains all the coordinates of a pointcloud object. This is an example of a nested list (see paragraph 6.6).</td>
</tr>
<tr>
<td>12</td>
<td>The variable <i>point</i>, which is taken from the <i>listpoints</i> variable, contains an array of three doubles; a standard Rhino point definition. We use that point to construct a new vector definition which points from the Base point to <i>arrPoints(i)</i>.</td>
</tr>
<tr>
<td>14</td>
<td>The *rs.VectorCrossProduct()* method will return a vector which is perpendicular to vecBase and the world z-axis. If you feel like doing some homework, you can try to replace the hard-coded direction ([0,0,1]) with a second variable point a la *base_point*.</td>
</tr>
<tr>
<td>15</td>
<td><i>rs.VectorCrossProduct()</i> will fail if one of the input vectors is zero-length or if both input vectors are parallel. In those cases we will not add a vector to the document.</td>
</tr>
<tr>
<td>16 & 17</td>
<td>Here we make sure the <i>vecdir</i> vector is two units long. First we unitize the vector, making it one unit long, then we double the length.</td>
</tr>
<tr>
<td>25</td>
<td>Finally, place a call to the <i>AddVector()</i> function we defined on page 40. If you intend to run this script, you must also include the <i>AddVector()</i> function in the same script.</td>
</tr>
</table>

## 6.6 Nested lists

> I wonder why, I wonder why.  
> I wonder why I wonder.  
> I wonder why I wonder why.  
> I wonder why I wonder.  

> -Richard P. Feynman-  


{{< image url="/images/primer-nestedarrays.svg" alt="/images/primer-nestedarrays.svg" class="float_right" width="300" >}}


There's nothing to it. A list (or tuple or dictionary for that matter) becomes nested when it is stored inside another list The VectorField example on the previous page deals with a list of points (a list of lists, each with three doubles). The image on the right is a visualization of such a structure. The left most column represents the base list, the one containing all coordinates. It can be any size you like, there's no limit to the amount of points you can store in a single list. Every element of this base list is a standard Rhino point. In the case of point-lists all the nested lists are three elements long, but this is not a requisite, you can store anything you want in a list.

Nesting can be done with tuples, lists or dictionaries. It simply means that you can put lists in lists, or tuples in tuples, dictionaries in dictionaries or even lists inside of dictionaries and so on.  Nesting can be done infinitely, you can have a list that contains a list with a list inside of it, another list inside of that list and so on. Nesting can easily be done by utilizing a Loop that allows you to iterate and either extract or place other items inside of the lists.

Accessing nested lists follows the same rules as accessing regular lists. Using the VectorField example:

```python
    arrSeventhPoint = arrPoints[6] #arrSeventhPoint now equals the 7th (starting from 0th) element
    arrLastPoint = arrPoints[len(arrPoints)] #arrLastPoint now equals the last point in the list
```

Len() can be used to get the length of a list. In this case we are saying that arrLastPoint equals the last element in the list called arrPoints because we have given it the numeric value that is the length of the list. This shows how to extract entire nested lists. Assuming the illustration on this page represents <i>arrPoints</i>, <i>arrSeventhPoint</i> will be identical to <i>[0.3, -1.5, 4.9]</i>. If we want to access individual coordinates directly we can use another bracket to explode out the z value:

```pyton
dblSeventhPointHeight = arrPoints[6][2]
#2 corresponds to the 3rd element (the Z coordinate) within that nested list.
```

The above code will store the third element of the nested list stored in the seventh element of the base list in *dblSeventhPointHeight*. This corresponds with the orange block.

Nested lists can be parsed using nested loops like so:

```python
for i in range(0,len(arrPoints)):
    for j in range(0,2):
        print("Coordinate(" + i + ", " + j + ") = " + arrPoints[i][j])
```

{{< image url="/images/primer-nestedarrayparsehistory.png" alt="/images/primer-nestedarrayparsehistory.png" class="image_center" width="45%" >}}

Remember the scaling script from before? We're now going to take curve-length adjustment to the next level
using nested lists. The logic of this script will be the same, but the algorithm for shortening a curve will be replaced with the following one (the illustration shows the first eight iterations of the algorithm):

{{< image url="/images/primer-curvesmoothing.svg" alt="/images/primer-curvesmoothing.svg" class="image_center" width="100%" >}}

Every control-point or 'vertex' of the original curve (except the ones at the end) will be averaged with its neighbors in order to smooth the curve. With every iteration the curve will become shorter and we will abort as soon a certain threshold length has been reached. The curve can never become shorter than the distance between the first and last control-point, so we need to make sure our goals are actually feasible before we start a potentially endless loop. Note that the algorithm is approximating, it may not be endless but it could still take a long time to complete. We will not support closed or periodic curves.

We're going to put the vector math bit in a separate function. This function will compute the {vM} vector given the control points {pN-1; p; pN+1} and a smoothing factor {s}. Since this function is not designed to fail, we will not be adding any error checking, if the thing crashes we'll have to fix the bug. Instead of using variable naming conventions, I'll use the same codes as in the diagram:

{{< div class="line-numbers" >}}
```python
def smoothingvector(point, prev_point, next_point, s):
    pm = (prev_point+next_point)/2.0
    va = rs.VectorCreate(pm, point)
    vm = rs.VectorScale(va, s)
    return vm
```
{{< /div >}}

<table class="multiline">
<tr>
<th>Line</th>
<th>Description</th>
</tr>
<tr>
<td>2</td>
<td>The smoothingvector function definition takes input of Rhino.Point3d. This object type allows for explicit point addition. The act of adding two Point3d objects together results in vector addition of the two points. The act of dividing the resulting point by 2.0 simply divides the three components (x,y and z) by 2.</td>
</tr>
<tr>
<td>3</td>
<td>The VectorCreate() function is called in order to obtain a Rhino.Vector3d with information about the directional components of a vector between points Pm, and point, P  being the origin. The math is effectively the same as Pm - Point = Va, but this operation would not have yielded a Rhion.Vector3d object. The VectorCreate() function creates this object efficiently.</td>
</tr>
<tr>
<td>4</td>
<td>Finally, we call the <i>Rhino.VectorScale()</i> function, which takes a Rhino.Vector3d object, and scales it according to a predetermined scaling factor 's'.
When we use this algorithm, we must make sure to set 's' to be something sensible, or the loop might become endless: 0.0 1 {s} # 1.0</td>
</tr>
<tr>
<td>5</td>
<td>We return the vector vm.</td>
</tr>
</table>

We'll also put the entire curve-smoothing algorithm in a separate function. Since it's fairly hard to adjust existing objects in Rhino, we'll be adding a new curve and deleting the existing one:

{{< div class="line-numbers" >}}
```python
def smoothcurve(curve_id, s):
    curve_points = rs.CurvePoints(curve_id)
    new_curve_points = []

    for i in range(1, len(curve_points)-1):
        vm = smoothingvector(curve_points[i], curve_points[i-1], curve_points[i+1], s)
        new_curve_points.append( rs.PointAdd(curve_points[i], vm) )

    knots = rs.CurveKnots(curve_id)
    degree = rs.CurveDegree(curve_id)
    weights = rs.CurveWeights(curve_id,0)
    newcurve_id = rs.AddNurbsCurve(new_curve_points, knots, degree, weights)
    if newcurve_id: rs.DeleteObject(curve_id)
    return newcurve_id
```
{{< /div >}}

<table class="multiline">
<tr>
<th>Line</th>
<th>Description</th>
</tr>
<tr>
<td>2</td>
<td>Retrieve the nested list of curve control points, and store it in curve_points.</td>
</tr>
<tr>
<td>3</td>
<td>We need a second list to contain the new points, while leaving the initial curve_points list intact.</td>
</tr>
<tr>
<td>5</td>
<td>This loop will start at one and stop one short of the length of the curve_points list. In other words, we're skipping the first and last items in the array.</td>
</tr>
<tr>
<td>6</td>
<td>Compute the smoothing vector using the current control point, the previous one (<i>i-1</i>) and the next one (<i>i+1</i>). Since we're omitting the first and last point in the array, every point we're dealing with has two neighbors.</td>
</tr>
<tr>
<td>7</td>
<td>Set the new control point position. The new coordinate equals the old coordinate plus the smoothing vector.</td>
</tr>
<tr>
<td>9...11</td>
<td>We'll be adding a new curve to the document which is identical to the existing one, but with different control point positions. A nurbs curve is defined by four different blocks of data: control points, knots, weights and degree (see paragraph 7.7 Nurbs Curves). We just need to copy the other bits from the old curve.</td>
</tr>
<tr>
<td>12</td>
<td>Create a new nurbs curve and store the object ID in the variable newcurve_id.</td>
</tr>
<tr>
<td>13</td>
<td>Delete the original curve.</td>
</tr>
</table>

The top-level subroutine doesn't contain anything you're not already familiar with:

```python
def iterativeshortencurve():
    curve_id = rs.GetObject("Open curve to smooth", 4, True)
    if curve_id is None or rs.IsCurveClosed(curve_id): return

    min = rs.Distance(rs.CurveStartPoint(curve_id), rs.CurveEndPoint(curve_id))
    max = rs.CurveLength(curve_id)
    goal = rs.GetReal("Goal length", 0.5*(min+max) , min, max)
    if goal is None: return

    while rs.CurveLength(curve_id)>goal:
        rs.EnableRedraw(False)
        curve_id = smoothcurve(curve_id, 0.1)
        rs.EnableRedraw(True)
        if curve_id is None: break
```

## Next Steps

Tuples, Lists and Dictionaries are very powerful in Python. Let's make a quick stop to learn about [class syntax](/guides/rhinopython/primer-101/7-classes/#class-syntax).
