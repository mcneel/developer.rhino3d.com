---
title: 8 Geometry
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

## 8.1 The openNURBS™ kernel

Now that you are familiar with the basics of scripting, it is time to start with the actual geometry part of RhinoScript. To keep things interesting we've used plenty of Rhino methods in examples before now, but that was all peanuts. Now you will embark upon that great journey which, if you survive, will turn you into a real 3D geek.

As already mentioned in Chapter 3, Rhinoceros is built upon the openNURBS™ kernel which supplies the bulk of the geometry and file I/O functions. All plugins that deal with geometry tap into this rich resource and the RhinoScript plugin is no exception. Although Rhino is marketed as a "NURBS modeler", it does have a basic understanding of other types of geometry as well. Some of these are available to the general Rhino user, others are only available to programmers. When writting in Python you will not be dealing directly with any 
openNURBS™ code since RhinoScript wraps it all up into an easy-to-swallow package. However, programmers need to have a much higher level of comprehension than users which is why we'll dig fairly deep.

## 8.2 Objects in Rhino

All objects in Rhino are composed of a geometry part and an attribute part. There are quite a few different geometry types but the attributes always follow the same format. The attributes store information such as object name, color, layer, isocurve density, linetype and so on. Not all attributes make sense for all geometry types, points for example do not use linetypes or materials but they are capable of storing this information nevertheless. Most attributes and properties are fairly straightforward and can be read and assigned to objects at will. 

<img src="{{ site.baseurl }}/images/primer-rhinoobjects.svg" width="90%" float="right">

This table lists most of the attributes and properties which are available to plugin developers. Most of these have been wrapped in the RhinoScript plugin, others are missing at this point in time and the custom user data element is special. We'll get to user data after we're done with the basic geometry chapters.

The following procedure displays some attributes of a single object in a dialog box. There is nothing exciting going on here so I'll refrain from providing a step-by-step explanation.

```python
import rhinoscriptsyntax as rs

def displayobjectattributes(object_id):
    source = "By Layer", "By Object", "By Parent"
    data = []
    data.append( "Object attributes for :"+str(object_id) )
    data.append( "Description: " + rs.ObjectDescription(object_id))
    data.append( "Layer: " + rs.ObjectLayer(object_id))
    #data.append( "LineType: " + rs.ObjectLineType(object_id))
    #data.append( "LineTypeSource: " + rs.ObjectLineTypeSource(object_id))
    data.append( "MaterialSource: " + str(rs.ObjectMaterialSource(object_id)))
    
    name = rs.ObjectName(object_id)
    if not name: data.append("<Unnamed object>")
    else: data.append("Name: " + name)
    
    groups = rs.ObjectGroups(object_id)
    if groups:
        for i,group in enumerate(groups):
            data.append( "Group(%d): %s" % i+1, group )
    else:
        data.append("<Ungrouped object>")

    s = ""
    for line in data: s += line + "\n"
    rs.EditBox(s, "Object attributes", "RhinoPython")


if __name__=="__main__":
    id = rs.GetObject()
    displayobjectattributes(id)
```

<img src="{{ site.baseurl }}/images/primer-objectattributedialog.png" width="45%" float="right">

## 8.3 Points and Pointclouds

Everything begins with points. A point is nothing more than a list of values called a coordinate. The number of values in the list corresponds with the number of dimensions of the space it resides in. Space is usually denoted with an R and a superscript value indicating the number of dimensions. (The 'R' stems from the world 'real' which means the space is continuous. We should keep in mind that a digital representation always has gaps, even though we are rarely confronted with them.) 

Points in 3D space, or R3 thus have three coordinates, usually referred to as [x,y,z]. Points in R2 have only two coordinates which are either called [x,y] or [u,v] depending on what kind of two dimensional space we're talking about. Points in R1 are denoted with a single value. Although we tend not to think of one-dimensional points as 'points', there is no mathematical difference; the same rules apply. One-dimensional points are often referred to as 'parameters' and we denote them with [t] or [p].

<img src="{{ site.baseurl }}/images/primer-rhinospaces.svg" width="90%" float="right">

The image on the left shows the R3 world space, it is continuous and infinite. The x-coordinate of a point in this space is the projection (the red dotted line) of that point onto the x-axis (the red solid line). Points are always specified in world coordinates in Rhino.

R2 world space (not drawn) is the same as R3 world space, except that it lacks a z-component. It is still continuous
and infinite. R2 parameter space however is bound to a finite surface as shown in the center image. It is still continuous, I.e. hypothetically there is an infinite amount of points on the surface, but the maximum distance between any of these points is very much limited. R2 parameter coordinates are only valid if they do not exceed a certain range. In the example drawing the range has been set between 0.0 and 1.0 for both [u] and [v]directions, but it could be any finite domain. A point with coordinates [1.5, 0.6] would be somewhere outside the surface and thus invalid.

Since the surface which defines this particular parameter space resides in regular R3 world space, we can always translate a parametric coordinate into a 3d world coordinate. The point [0.2, 0.4] on the surface for example is the same as point [1.8, 2.0, 4.1] in world coordinates. Once we transform or deform the surface, the R3 coordinates which correspond with [0.2, 0.4] will change. Note that the opposite is not true, we can translate any R2 parameter coordinate into a 3D world coordinate, but there are many 3D world coordinates that are not on the surface and which can therefore not be written as an R2 parameter coordinate. However, we can always project a 3D world coordinate onto the surface using the closest-point relationship. We'll discuss this in more detail later on.

If the above is a hard concept to swallow, it might help you to think of yourself and your position in space. We usually tend to use local coordinate systems to describe our whereabouts; "I'm sitting in the third seat on the seventh row in the movie theatre", "I live in apartment 24 on the fifth floor", "I'm in the back seat". Some of these are variations to the global coordinate system (latitude, longitude, elevation), while others use a different anchor point. If the car you're in is on the road, your position in global coordinates is changing all the time, even though you remain in the same back seat 'coordinate'.

Let's start with conversion from R1 to R3 space. The following script will add 500 colored points to the 
document, all of which are sampled at regular intervals across the R1 parameter space of a curve object:

```python
import rhinoscriptsyntax as rs

def main():
    curve_id = rs.GetObject("Select a curve to sample", 4, True, True)
    if not curve_id: return
    
    rs.EnableRedraw(False)
    t = 0
    while t<=1.0:
        addpointat_r1_parameter(curve_id,t)
        t+=0.002
    rs.EnableRedraw(True)

def addpointat_r1_parameter(curve_id, parameter):
    domain = rs.CurveDomain(curve_id)
    
    
    r1_param = domain[0] + parameter*(domain[1]-domain[0])
    r3point = rs.EvaluateCurve(curve_id, r1_param)
    if r3point:
        point_id = rs.AddPoint(r3point)
        rs.ObjectColor(point_id, parametercolor(parameter))

def parametercolor(parameter):
    red = 255 * parameter
    if red<0: red=0
    if red>255: red=255
    return (red,0,255-red)

if __name__=="__main__":
    main()
```

<img src="{{ site.baseurl }}/images/primer-curveparameterspace.svg" width="45%" float="right">

For no good reason whatsoever, we'll start with the bottom most function:

<table rules="rows">
<tr>
<th>Line</th>	
<th>Description</th>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">24</td>
<td>Standard out-of-the-box function declaration which takes a single double value. This function is 
supposed to return a colour which changes gradually from blue to red as parameter changes from zero to one. Values outside of the range {0.0~1.0} will be clipped.</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">25</td>
<td>The red component of the colour we're going to return is declared here and assigned the naive value of 255 times the parameter. Colour components must have a value between and including 0 and 255. If we attempt to construct a colour with lower or higher values a run-time error will spoil the party.</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">26...27</td>
<td>Here's where we make sure the party can continue unimpeded.</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">28</td>
<td>Compute the colour gradient value. If parameter equals zero we want blue (0,0,255) and if it equals one we want red (255,0,0). So the green component is always zero while blue and red see-saw between 0 and 255.</td>
</tr>
</table>

Now, on to function *AddPointAtR1Parameter()*. As the name implies, this function will add a single point in 3D world space based on the parameter coordinate of a curve object. In order to work correctly this function must know what curve we're talking about and what parameter we want to sample. Instead of passing the actual parameter which is bound to the curve domain (and could be anything) we're passing a unitized one. 
I.e. we pretend the curve domain is between zero and one. This function will have to wrap the required math for translating unitized parameters into actual parameters.

Since we're calling this function a lot (once for every point we want to add), it is actually a bit odd to put all the heavy-duty stuff inside it. We only really need to perform the overhead costs of 'unitized parameter + actual parameter' calculation once, so it makes more sense to put it in a higher level function. Still, it will be very quick so there's no need to optimize it yet.


<table rules="rows">
<tr>
<th>Line</th>	
<th>Description</th>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">14</td>
<td>Function declaration.</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">15...16</td>
<td>Get the curve domain and check for <i>Null</i>. It will be <i>Null</i> if the ID does not represent a proper curve object. The <i>Rhino.CurveDomain()</i> method will return an array of two doubles which indicate the minimum and maximum t-parameters which lie on the curve.</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">18</td>
<td>Translate the unitized R1 coordinate into actual domain coordinates.</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">19</td>
<td>Evaluate the curve at the specified parameter. Rhino.EvaluateCurve() takes an R1 coordinate and returns an R3 coordinate.</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">21</td>
<td>Add the point, it will have default attributes.</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">22</td>
<td>Set the custom colour. This will automatically change the color-source attribute to By Object.</td>
</tr>
</table>

The distribution of R1 points on a spiral is not very enticing since it approximates a division by equal length segments in R3 space. When we run the same script on less regular curves it becomes easier to grasp what parameter space is all about:

<img src="{{ site.baseurl }}/images/primer-curvestructure.svg" width="100%" float="right">

Let's take a look at an example which uses all parameter spaces we've discussed so far:

```python
import rhinoscriptsyntax as rs

def main():
    surface_id = rs.GetObject("Select a surface to sample", 8, True)
    if not surface_id: return

    curve_id = rs.GetObject("Select a curve to measure", 4, True, True)
    if not curve_id: return

    points = rs.DivideCurve(curve_id, 500)
    rs.EnableRedraw(False)
    for point in points: evaluatedeviation(surface_id, 1.0, point)
    rs.EnableRedraw(True)

def evaluatedeviation( surface_id, threshold, sample ):
    r2point = rs.SurfaceClosestPoint(surface_id, sample)
    if not r2point: return

    r3point = rs.EvaluateSurface(surface_id, r2point[0], r2point[1])
    if not r3point: return

    deviation = rs.Distance(r3point, sample)
    if deviation<=threshold: return

    rs.AddPoint(sample)
    rs.AddLine(sample, r3point)

if __name__=="__main__":
    main()
```

<table>
<tr>
<td>
This script will compare a bunch of points on a curve to their projection on a surface. If the distance exceeds one unit, a line and a point will be added.
<br><br>
First, the R1 points are translated into R3 coordinates so we can 
project them onto the surface, getting the R2 coordinate [u,v] in return. This R2 point has to be translated into R3 space as well, since we need to know the distance between the R1 point on the curve and the R2 point on the surface. Distances can only be measured if both points reside in the same number of dimensions, so we need to translate them into R3 as well.
<br>
Told you it was a piece of cake...
</td>
<td width="30%"><img src="{{ site.baseurl }}/images/primer-surfaceparameterspace.svg" width="100%" height="300" float="right"></td>
</tr>
</table>

<table rules="rows">
<tr>
<th>Line</th>	
<th>Description</th>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">10</td>
<td>We're using the <i>Rhino.DivideCurve()</i> method to get all the R3 coordinates on the curve in one go. This saves us a lot of looping and evaluating.</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">24</td>
<td><i>Rhino.SurfaceClosestPoint()</i> returns an array of two doubles representing the R2 point on the surface (in {u,v} coordinates) which is closest to the sample point.</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">27</td>
<td>Rhino.EvaluateSurface() in turn translates the R2 parameter coordinate into R3 world coordinates</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">30...38</td>
<td>Compute the distance between the two points and add geometry if necessary. This function returns True if the deviation is less than one unit, False if it is more than one unit and Null if something went wrong.</td>
</tr>
</table>

One more time just for kicks. We project the R1 parameter coordinate on the curve into 3D space (Step A), then we project that R3 coordinate onto the surface getting the R2 coordinate of the closest point (Step B). We evaluate the surface at R2, getting the R3 coordinate in 3D world space (Step C), and we finally measure the distance between the two R3 points to determine the deviation:


<img src="{{ site.baseurl }}/images/primer-surfaceparameterspacediagram.svg" width="60%" float="right">

## 8.4 Lines and Polylines

You'll be glad to learn that (poly)lines are essentially the same as point-lists. The only difference is that we treat the points as a series rather than an anonymous collection, which enables us to draw lines between them. There is some nasty stuff going on which might cause problems down the road so perhaps it's best to get it over with quick.

There are several ways in which polylines can be manifested in openNURBS™ and thus in Rhino. There is a special polyline class which is simply a list of ordered points. It has no overhead data so this is the simplest case. It's also possible for regular nurbs curves to behave as polylines when they have their degree set to 1. In 
addition, a polyline could also be a polycurve made up of line segments, polyline segments, degree=1 nurbs curves or a combination of the above. If you create a polyline using the _Polyline command, you will get a proper polyline object as the Object Properties Details dialog on the left shows:

The dialog claims an "Open polyline with 8 points". However, when we drag a control-point Rhino will 
automatically convert any curve to a Nurbs curve, as the image on the right shows. It is now an open nurbs curve of degree=1. From a geometric point of view, these two curves are identical. From a programmatic point of view, they are anything but. For the time being we will only deal with 'proper' polylines though; lists of sequential coordinates. For purposes of clarification I've added two example functions which perform basic operations on polyline point-lists.

Compute the length of a polyline point-array:

```python
def PolylineLength(arrVertices):
    PolylineLength = 0.0
    for i in range(0,len(arrVertices)-1):
        PolylineLength = PolylineLength + rs.Distance(arrVertices[i], arrVertices[i+1])
```

Subdivide a polyline by adding extra vertices halfway between all existing vertices:

```python
def SubDividePolyline(arrV)
    arrSubD = []

    for i in range(0, len(arrV)-1):
        'copy the original vertex location
        arrSubD.append(arrV[i])
        'compute the average of the current vertex and the next one
        arrSubD.append([arrV[i][0] + arrV[i+1][0]] / 2.0, _
                                    [arrV(i][1] + arrV[i+1][1]] / 2.0, _
                                    [arrV[i][2] + arrV[i+1][2]] / 2.0])

    'copy the last vertex (this is skipped by the loop)
    arrSubD.append(arrV[len(arrV)])
    return arrSubD
```

<img src="{{ site.baseurl }}/images/primer-polylinetonurbsdragchange.png" width="90%" float="right">

<table>
<tr>
<td>
No rocket science yet, but brace yourself for the next bit...
<br><br>
As you know, the shortest path between two points is a straight line. This is true for all our space definitions, from R1 to RN. However, the shortest path in R2 space is not necessarily the same shortest path in R3 space. If we want to connect two points on a surface with a straight line in R2, all we need to do is plot a linear course through the surface [u,v] space. (Since we can only add curves to Rhino which use 3D world coordinates, we'll need a fair amount of samples to give the impression of smoothness.) The thick red curve in the 
adjacent illustration is the shortest path in R2 parameter 
space connecting [A] and [B]. We can clearly see that this is definitely not the shortest path in R3 space.
</td>
<td width="30%"><img src="{{ site.baseurl }}/images/primer-r2shortpath.svg" width="100%" height="300" float="right"></td>
</tr>
</table>

We can clearly see this because we're used to things happening in R3 space, which is why this whole R2/R3 thing is so thoroughly counter intuitive to begin with. The green, dotted curve is the actual shortest path in R3 space which still respects the limitation of the surface (I.e. it can be projected onto the surface without any loss of information). The following function was used to create the red curve; it creates a polyline which represents the shortest path from [A] to [B] in surface parameter space:

```python
def getr2pathonsurface(surface_id, segments, prompt1, prompt2):
    start_point = rs.GetPointOnSurface(surface_id, prompt1)
    if not start_point: return

    end_point = rs.GetPointOnSurface(surface_id, prompt2)
    if not end_point: return

    if rs.Distance(start_point, end_point)==0.0: return

    uva = rs.SurfaceClosestPoint(surface_id, start_point)
    uvb = rs.SurfaceClosestPoint(surface_id, end_point)

    path = []
    for i in range(segments):
        t = i / segments
        u = uva[0] + t*(uvb[0] - uva[0])
        v = uva[1] + t*(uvb[1] - uva[1])
        pt = rs.EvaluateSurface(surface_id, u, v)
        path.append(pt)
    return path
```
<table rules="rows">
<tr>
<th>Line</th>	
<th>Description</th>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">1</td>
<td>This function takes four arguments; the ID of the surface onto which to plot the shortest route, the number of segments for the path polyline and the prompts to use for picking the A and B point.</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">1...3</td>
<td>Prompt the user for the {A} point on the surface. Return if the user does not enter a point.</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">5...6</td>
<td>Prompt the user for the {B} point on the surface. Return if the user does not enter a point.</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">10...11</td>
<td>Project {A} and {B} onto the surface to get the respective R2 coordinates <i>uva</i> and <i>uvb</i>.</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">13</td>
<td>Declare the list which is going to store all the polyline vertices.</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">14</td>
<td>Since this algorithm is segment-based, we know in advance how many vertices the polyline will have and thus how often we will have to sample the surface.</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">15</td>
<td><i>t</i> is a value which ranges from 0.0 to 1.0 over the course of our loop</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">16...17</td>
<td>Use the current value of <i>t</i> to sample the surface somewhere in between <i>uvA</i> and <i>uvB</i>.</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">18</td>
<td><i>rs.EvaluateSurface()</i> takes a {u} and a {v} value and spits out a 3D-world coordinate. This is just a friendly way of saying that it converts from R2 to R3.</td>
</tr>
</table>

We're going to combine the previous examples in order to make a real geodesic path routine in Rhino. This is a fairly complex algorithm and I'll do my best to explain to you how it works before we get into any actual code.

First we'll create a polyline which describes the shortest path between [A] and [B] in R2 space. This is our base curve. It will be a very coarse approximation, only ten segments in total. We'll create it using the function on page 54. Unfortunately that function does not take closed surfaces into account. In the paragraph on nurbs surfaces we'll elaborate on this.

Once we've got our base shape we'll enter the iterative part. The iteration consists of two nested loops, which we will put in two different functions in order to avoid too much nesting and indenting. We're going to write four functions in addition to the ones already discussed in this paragraph:

- The main geodesic routine
- ProjectPolyline()
- SmoothPolyline()
- GeodesicFit()

The purpose of the main routine is the same as always; to collect the initial data and make sure the script completes as successfully as possible. Since we're going to calculate the geodesic curve between two points on a surface, the initial data consists only of a surface ID and two points in surface parameter space. The algorithm for finding the geodesic curve is a relatively slow one and it is not very good at making major changes to dense polylines. That is why we will be feeding it the problem in bite-size chunks. It is because of this reason that our initial base curve (the first bite) will only have ten segments. We'll compute the geodesic path for these ten segments, then subdivide the curve into twenty segments and recompute the geodesic, then subdivide into 40 and so on and so forth until further subdivision no longer results in a shorter overall curve.

The ProjectPolyline() function will be responsible for making sure all the vertices of a polyline point-array are in fact coincident with a certain surface. In order to do this it must project the R3 coordinates of the polyline onto the surface, and then again evaluate that projection back into R3 space. This is called 'pulling'.

The purpose of SmoothPolyline() will be to average all polyline vertices with their neighbours. This function will be very similar to our previous example, except it will be much simpler since we know for a fact we're not dealing with nurbs curves here. We do not need to worry about knots, weights, degrees and domains.

GeodesicFit() is the essential geodesic routine. We expect it to deform any given polyline into the best possible geodesic curve, no matter how coarse and wrong the input is. The algorithm in question is a very naive solution to the geodesic problem and it will run much slower than Rhinos native _ShortPath command. The upside is that our script, once finished, will be able to deal with self-intersecting surfaces.

The underlying theory of this algorithm is synonymous with the simulation of a contracting rubber band, with the one difference that our rubber band is not allowed to leave the surface. The process is iterative and though we expect every iteration to yield a certain improvement over the last one, the amount of improvement will diminish as we near the ideal solution. Once we feel the improvement has become negligible we'll abort the function.

In order to simulate a rubber band we require two steps; smoothing and projecting. First we allow the rubber band to contract (it always wants to contract into a straight line between [A] and [B]). This contraction happens in R3 space which means the vertices of the polyline will probably end up away from the surface. We must then re-impose these surface constraints. These two operations have been hoisted into functions #2 and #3.


<img src="{{ site.baseurl }}/images/primer-geodesiccurvediagram.svg" width="65%" float="right">

The illustration depicts the two steps which compose a single iteration of the geodesic routine. The black polyline is projected onto the surface giving the red polyline. The red curve in turn is smoothed into the green  curve. Note that the actual algorithm performs these two steps in the reverse order; smoothing first, projection second.

We'll start with the simplest function:

```python
def projectpolyline(vertices, surface_id):
    polyline = []
    for vertex in vertices:
        pt = rs.BrepClosestPoint(surface_id, vertex)
        if pt: polyline.append(pt[0])
    return polyline
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
