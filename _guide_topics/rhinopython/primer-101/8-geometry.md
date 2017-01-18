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

The *ProjectPolyline()* function will be responsible for making sure all the vertices of a polyline point-array are in fact coincident with a certain surface. In order to do this it must project the R3 coordinates of the polyline onto the surface, and then again evaluate that projection back into R3 space. This is called 'pulling'.

The purpose of *SmoothPolyline()* will be to average all polyline vertices with their neighbours. This function will be very similar to our previous example, except it will be much simpler since we know for a fact we're not dealing with nurbs curves here. We do not need to worry about knots, weights, degrees and domains.

*GeodesicFit()* is the essential geodesic routine. We expect it to deform any given polyline into the best possible geodesic curve, no matter how coarse and wrong the input is. The algorithm in question is a very naive solution to the geodesic problem and it will run much slower than Rhinos native _ShortPath command. The upside is that our script, once finished, will be able to deal with self-intersecting surfaces.

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

<table rules="rows">
<tr>
<th>Line</th>	
<th>Description</th>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">1...3</td>
<td>Since this is a specialized def which we will only be using inside this script, we can skip projecting the first and last point. We can safely assume the polyline is open and that both endpoints will already be on the curve.</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">4</td>
<td>We ask Rhino for the closest point on the surface object given our polyline vertex coordinate. The reason why we do not use <i>rs.SurfaceClosestPoint()</i> is because <i>BRepClosestPoint()</i> takes trims into account. This is a nice bonus we can get for free. The native <i>_ShortPath</i> command does not deal with trims at all. We are of course not interested in aping something which already exists, we want to make something better.</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">5</td>
<td>If <i>BRepClosestPoint()</i> returned Null something went wrong after all. We cannot project the vertex in this case so we'll simply ignore it. We could of course short-circuit the whole operation after a failure like this, but I prefer to press on and see what comes out the other end. </td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">6</td>
<td>The <i>BRepClosestPoint()</i> method returns a lot of information, not just the R2 coordinate. In fact it returns a tuple of data, the first element of which is the R3 closest point. This means we do not have to translate the uv coordinate into xyz ourselves. Huzzah! Assign it to the vertex and move on.</td>
</tr>
</table>

```python
def smoothpolyline(vertices):
    smooth = []
    smooth.append(vertices[0])

    for i in range(1, len(vertices)-1):
        prev = vertices[i-1]
        this = vertices[i]
        next = vertices[i+1]
        pt = (prev+this+next) / 3.0
        smooth.append(pt)
    smooth.append(vertices[len(vertices)-1])
    return smooth
```


<table rules="rows">
<tr>
<th>Line</th>	
<th>Description</th>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">1...3 6...8</td>
<td>Since we need the original coordinates throughout the smoothing operation we cannot deform it 
directly. That is why we need to make a copy of each vertex point before we start messing about with coordinates.</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">9</td>
<td>What we do here is average the x, y and z coordinates of the current vertex ('current' as defined by i) using both itself and its neighbours.
<br><br>
We iterate through all the internal vertices and add the Point3d objects together, rather than explicitly adding their x, y and z components together. Writing smaller functions will not make the code go faster, but it does mean we just get to write less junk. Also, it means adjustments are easier to make afterwards since less code-rewriting is required.</td>
</tr>
</table>  

Time for the bit that sounded so difficult on the previous page, the actual geodesic curve fitter routine:

```python
def geodesicfit(vertices, surface_id, tolerance):
    length = polylinelength(vertices)
    while True:
        vertices = smoothpolyline(vertices)
        vertices = projectpolyline(vertices, surface_id)
        newlength = polylinelength(vertices)
        if abs(newlength-length)<tolerance: return vertices
        length = newlength
```

<table rules="rows">
<tr>
<th>Line</th>	
<th>Description</th>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">1</td>
<td>Hah... that doesn't look so bad after all, does it? You'll notice that it's often the stuff which is easy to explain that ends up taking a lot of lines of code. Rigid mathematical and logical structures can typically be coded very efficiently.</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">2</td>
<td>We'll be monitoring the progress of each iteration and once the curve no longer becomes noticeably shorter (where 'noticeable' is defined by the <i>tolerance</i> argument), we'll call the 'intermediate result' the 'final result' and return execution to the caller. In order to monitor this progress, we need to remember how long the curve was before we started; <i>length</i> is created for this purpose.</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">3</td>
<td>Whenever you see a while True: without any standard escape clause you should be on your toes. This is potentially an infinite loop. I have tested it rather thoroughly and have been unable to make it run more than 120 times. Experimental data is never watertight proof, the routine could theoretically fall into a stable state where it jumps between two solutions. If this happens, the loop will run forever.
<br><br>
You are of course welcome to add additional escape clauses if you deem that necessary.</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">4...5</td>
<td>Place the calls to the functions on page 56. These are the bones of the algorithm.</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">6</td>
<td>Compute the new length of the polyline.</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">7</td>
<td>Check to see whether or not it is worth carrying on.</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">8</td>
<td>Apparently it was, we need now to remember this new length as our frame of reference.</td>
</tr>
</table>

The main subroutine takes some explaining. It performs a lot of different tasks which always makes a block of code harder to read. It would have been better to split it up into more discrete chunks, but we're already using seven different functions for this script and I feel we are nearing the ceiling. Remember that splitting problems into smaller parts is a good way to organize your thoughts, but it doesn't actually solve anything. You'll need to find a good balance between splitting and lumping.

```python
def geodesiccurve():
    surface_id = rs.GetObject("Select surface for geodesic curve solution", 8, True, True)
    if not surface_id: return

    vertices = getr2pathonsurface(surface_id, 10, "Start of geodes curve", "End of geodes curve")
    if not vertices: return

    tolerance = rs.UnitAbsoluteTolerance() / 10
    length = 1e300
    newlength = 0.0

    while True:
        print("Solving geodesic fit for %d samples" % len(vertices))
        vertices = geodesicfit(vertices, surface_id, tolerance)

        newlength = polylinelength(vertices)
        if abs(newlength-length)<tolerance: break
        if len(vertices)>1000: break
        vertices = subdividepolyline(vertices)
        length = newlength

    rs.AddPolyline(vertices)
    print "Geodesic curve added with length: ", newlength
```


<table rules="rows">
<tr>
<th>Line</th>	
<th>Description</th>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">2...3</td>
<td>Get the surface to be used in the geodesic routine.</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">5...6</td>
<td>Declare a variable which will store the polyline vertices. Since the return value of <i>getr2pathonsurface()</i> is already a list, we do not need to declare it with empty brackets - '[ ]' - as we have done elsewhere.</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">8</td>
<td>The tolerance used in our script will be 10% of the absolute tolerance of the document.</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">9...12</td>
<td>This loop also uses a length comparison in order to determine whether or not to continue. But instead of evaluating the length of a polyline before and after a smooth/project iteration, it measures the difference before and after a subdivide/geodesicfit iteration. The goal of this evaluation is to decide whether or not further elaboration will pay off. The variables <i>length</i> and <i>newlength</i> are used in the same context as on the previous page.</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">13</td>
<td>Display a message in the command-line informing the user about the progress we're making. This script may run for quite some time so it's important not to let the user think the damn thing has crashed.</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">14</td>
<td>Place a call to the <i>GeodesicFit()</i> subroutine.</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">16...17</td>
<td>Compare the improvement in length, exit the loop when there's no progress of any value.</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">18</td>
<td>A safety-switch. We don't want our curve to become too dense.</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">19</td>
<td>A call to <i>subdividepolyline()</i> will double the amount of vertices in the polyline. The newly added vertices will not be on the surface, so we must make sure to call <i>geodesicfit()</i> at least once before we add this new polyline to the document.</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">22...23</td>
<td>Add the curve and print a message about the length.</td>
</tr>
</table>

## 8.5 Planes

Planes are not genuine objects in Rhino, they are used to define a coordinate system in 3D world space. In fact, it's best to think of planes as vectors, they are merely mathematical constructs. Although planes are internally defined by a parametric equation, I find it easiest to think of them as a set of axes:

<img src="{{ site.baseurl }}/images/primer-planedefinition.svg" width="45%" float="right">  

A plane definition is an array of one point and three vectors, the point marks the origin of the plane and the vectors represent the three axes. There are some rules to plane definitions, I.e. not every combination of points and vectors is a valid plane. If you create a plane using one of the RhinoScript plane methods you don't have to worry about this, since all the bookkeeping will be done for you. The rules are as follows:

- The axis vectors must be unitized (have a length of 1.0).
- All axis vectors must be perpendicular to each other.
- The x and y axis are ordered anti-clockwise.

The illustration shows how rules #2 and #3 work in practice.

```python
ptOrigin = rs.GetPoint("Plane origin")

ptX = rs.GetPoint("Plane X-axis", ptOrigin)

ptY = rs.GetPoint("Plane Y-axis", ptOrigin)

dX = rs.Distance(ptOrigin, ptX)
dY = rs.Distance(ptOrigin, ptY)
arrPlane = rs.PlaneFromPoints(ptOrigin, ptX, ptY)

rs.AddPlaneSurface(arrPlane, 1.0, 1.0)
rs.AddPlaneSurface(arrPlane, dX, dY)
```

<table>
<tr>
<td>
You will notice that all RhinoScript methods that require plane definitions make sure these demands are met, no matter how poorly you defined the input. 
<br><br>
The adjacent illustration shows how the rs.AddPlaneSurface() call on line 11 results in the red plane, while the rs.AddPlaneSurface() call on line 12 creates the yellow surface which has dimensions equal to the distance between the picked origin and axis points.
</td>
<td width="40%"><img src="{{ site.baseurl }}/images/primer-planecreation.svg" width="100%" height="300" float="right"></td>
</tr>
</table>

We'll only pause briefly at plane definitions since planes, like vectors, are usually only constructive elements. In examples to come they will be used extensively so don't worry about getting the hours in. A more interesting script which uses the *rs.AddPlaneSurface()* method is the one below which populates a surface with so-called surface frames:

```primer
idSurface = rs.GetObject("Surface to frame", 8, True, True)
	
intCount = rs.GetInteger("Number of iterations per direction", 20, 2)

uDomain = rs.SurfaceDomain(idSurface, 0)
vDomain = rs.SurfaceDomain(idSurface, 1)
uStep = (uDomain[1] - uDomain[0]) / intCount
vStep = (vDomain[1] - vDomain[0]) / intCount
	
rs.EnableRedraw(False)
for u in range(uDomain[0],uDomain[1], uStep):
    For v in range(vdomain[0],vDomain[1],vStep):
        pt = rs.EvaluateSurface(idSurface, [u, v]) 
        if rs.Distance(pt, rs.BrepClosestPoint(idSurface, pt)[0]) < 0.1:
            srfFrame = rs.SurfaceFrame(idSurface, [u, v])
            rs.AddPlaneSurface(srfFrame, 1.0, 1.0) 

rs.EnableRedraw(True)
```
Frames are planes which are used to indicate geometrical directions. Both curves, surfaces and textured meshes have frames which identify tangency and curvature in the case of curves and [u] and [v] directions in the case of surfaces and meshes. The script above simply iterates over the [u] and [v] directions of any given surface and adds surface frame objects at all uv coordinates it passes.

<table>
<tr>
<td>
On lines 5 and 6 we determine the domain of the surface in u and v directions and we derive the required stepsize from those limits.
<br><br>
Line 11 and 12 form the main structure of the two-dimensional iteration. You can read such nested For loops as "Iterate through all columns and inside every column iterate through all rows".
<br><br>
Line 14 does something interesting which is not apparent in the adjacent illustration. When we are dealing with trimmed surfaces, those two lines prevent the script from adding planes in cut-away areas. By comparing the point on the (untrimmed) surface to it's projection onto the trimmed surface, we know whether or not the [uv] coordinate in question represents an actual point on the trimmed surface.
</td>
<td width="40%"><img src="{{ site.baseurl }}/images/primersurfaceframes.svg" width="100%" height="300" float="right"></td>
</tr>
</table>

The *rs.SurfaceFrame()* method returns a unitized frame whose axes point in the [u] and [v] directions of the surface. Note that the [u] and [v] directions are not necessarily perpendicular to each other, but we only add valid planes whose x and y axis are always at 90º, thus we ignore the direction of the v-component.

## 8.6 Circles, Ellipses and Arcs

Although the user is never confronted with parametric objects in Rhino, the openNURBS™ kernel has a certain set of mathematical primitives which are stored parametrically. Examples of these are cylinders, spheres, circles, revolutions and sum-surfaces. To highlight the difference between explicit (parametric) and implicit circles:

<img src="{{ site.baseurl }}/images/primer-circleschart.svg" width="100%" float="right">

When adding circles to Rhino through scripting, we can either use the Plane+Radius approach or we can use a 3-Point approach (which is internally translated into Plane+Radius). You may remember that circles are tightly linked with sines and cosines; those lovable, undulating waves. We're going to create a script which packs circles with a predefined radius onto a sphere with another predefined radius. Now, before we start and I give away the answer, I'd like you to take a minute and think about this problem.

The most obvious solution is to start stacking circles in horizontal bands and simply to ignore any vertical nesting which might take place. If you reached a similar solution and you want to keep feeling good about yourself I recommend you skip the following two sentences. This very solution has been found over and over again but for some reason Dave Rusin is usually given as the inventor. Even though Rusin's algorithm isn't exactly rocket science, it is worth discussing the mathematics in advance to prevent -or at least reduce- any confusion when I finally confront you with the code.

Rusin's algorithm works as follows:

- Solve how many circles you can evenly stack from north pole to south pole on the sphere.
- For each of those bands, solve how many circles you can stack evenly around the sphere.
- Do it.

No wait, back up. The first thing to realize is how a sphere actually works. Only once we master spheres can we start packing them with circles. In Rhino, a sphere is a surface of revolution, which has two singularities and a single seam:

<img src="{{ site.baseurl }}/images/primer-uv-map.svg" width="80%" float="right">

The north pole (the black dot in the left most image) and the south pole (the white dot in the same image) are both on the main axis of the sphere and the seam (the thick edge) connects the two. In essence, a sphere is a rectangular plane bent in two directions, where the left and right side meet up to form the seam and the top and bottom edge are compressed into a single point each (a singularity). This coordinate system should be familiar since we use the same one for our own planet. However, our planet is divided into latitude and longitude degrees, whereas spheres are defined by latitude and longitude radians. The numeric domain of the latitude of the sphere starts in the south pole with -½π, reaches 0.0 at the equator and finally terminates with ½π at the north pole. The longitudinal domain starts and stops at the seam and travels around the sphere from 0.0 to 2π. Now you also know why it is called a 'seam' in the first place; it's where the domain suddenly jumps from one value to another, distant one.

We cannot pack circles in the same way as we pack squares in the image above since that would deform them heavily near the poles, as indeed the squares are deformed. We want our circles to remain perfectly circular which means we have to fight the converging nature of the sphere

<table>
<tr>
<td width="30%"><img src="{{ site.baseurl }}/images/primer-sphereuv.svg" width="100%" float="right"></td>
<td>
Assuming the radius of the circles we are about to stack is sufficiently smaller than the radius of the sphere, we can at least place two circles without thinking; one on the north- and one on the south pole. The additional benefit is that these two circles now handsomely cover up the singularities so we are only left with the annoying seam. The next order of business then, is to determine how many circles we need in order to cover up the seam in a straightforward fashion. The length of the seam is half of the circumference of the sphere (see yellow arrow in adjacent illustration).  
<br><br>
Home stretch time, we've collected all the information we need in order to populate this sphere. The last step of the algorithm is to stack circles around the sphere, starting at every seam-circle. We need to calculate the circumference of the sphere at that particular latitude, divide that number by the diameter of the circles and once again find the largest integer value which is smaller than or equal to that result. The equivalent mathematical notation for this is:
<br><br>

$$N_{count} = \left[\frac{2 \cdot R_{sphere} \cdot \cos{\phi}}{2 \cdot R_{circle}} \right]$$  

in case you need to impress anyone…
</td>
</tr>
</table>

```python
def DistributeCirclesOnSphere():
    sphere_radius = rs.GetReal("Radius of sphere", 10.0, 0.01)
    if not sphere_radius: return

    circle_radius = rs.GetReal("Radius of circles", 0.05*sphere_radius, 0.001, 0.5*sphere_radius)
    if not circle_radius: return

    vertical_count = int( (math.pi*sphere_radius)/(2*circle_radius) )

    rs.EnableRedraw(False)
    phi = -0.5*math.pi
    phi_step = math.pi/vertical_count
    while phi<0.5*math.pi:
        horizontal_count = int( (2*math.pi*math.cos(phi)*sphere_radius)/(2*circle_radius) )
        if horizontal_count==0: horizontal_count=1
        theta = 0
        theta_step = 2*math.pi/horizontal_count
        while theta<2*math.pi-1e-8:
            circle_center = (sphere_radius*math.cos(theta)*math.cos(phi), 
                sphere_radius*math.sin(theta)*math.cos(phi), sphere_radius*math.sin(phi))
            circle_normal = rs.PointSubtract(circle_center, (0,0,0))
            circle_plane = rs.PlaneFromNormal(circle_center, circle_normal)
            rs.AddCircle(circle_plane, circle_radius)
            theta += theta_step
        phi += phi_step
    rs.EnableRedraw(True)
```
<img src="{{ site.baseurl }}/images/primer-spherepack.svg" width="45%" float="right">

<table rules="rows">
<tr>
<th>Line</th>	
<th>Description</th>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">1...6</td>
<td>Collect all custom variables and make sure they make sense. We don't want spheres smaller than 0.01 units and we don't want circle radii larger than half the sphere radius.</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">8</td>
<td>Compute the number of circles from pole to pole. The <i>int()</i> function in VBScript takes a double and returns only the integer part of that number. Hence it always rounds downwards.</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">11...12<br>16...17</td>
<td>phi and theta (Φ and Θ) are typically used to denote angles in spherical space and it's not hard to see why. I could have called them latitude and longitude respectively as well.</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">13</td>
<td>The phi loop runs from -½π to ½π and we need to run it <i>VerticalCount</i> times.</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">14</td>
<td>This is where we calculate how many circles we can fit around the sphere on the current latitude. The math is the same as before, except we also need to calculate the length of the path around the sphere: 2π·R·Cos(Φ)</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">15</td>
<td>If it turns out that we can fit no circles at all at a certain latitude, we're going to get into trouble since we use the HorizontalCount variable as a denominator in the stepsize calculation on line 24. And even my mother knows you cannot divide by zero. However, we know we can always fit at least one circle.</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">18</td>
<td>This loop is essentially the same as the one on line 20, except it uses a different stepsize and a different numeric range ({0.0 <= theta < 2π} instead of {-½π <= phi <= +½π}). The more observant among you will have noticed that the domain of theta reaches from nought up to but not including two pi. If <i>theta</i> would go all the way up to 2π then there would be a duplicate circle on the seam. The best way of preventing a loop to reach a certain value is to subtract a fraction of the stepsize from that value, in this case I have simply subtracted a ludicrously small number (1e-8 = 0.00000001).</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">19...21</td>
<td><i>circle_center</i> will be used to store the center point of the circles we're going to add.  
<i>circle_normal</i> will be used to store the normal of the plane in which these circles reside.  
<i>circle_plane</i> will be used to store the resulting plane definition.</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">19</td>
<td>This is mathematically the most demanding line, and I'm not going to provide a full proof of why and how it works. This is the standard way of translating the spherical coordinates Φ and Θ into Cartesian coordinates x, y and z. 
<br><br>
Further information can be found on [MathWorld.com](http://mathworld.wolfram.com/)</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">20</td>
<td>Once we found the point on the sphere which corresponds to the current values of phi and theta, it's a piece of proverbial cake to find the normal of the sphere at that location. The normal of a sphere at any point on its surface is the inverted vector from that point to the center of the sphere. And that's what we do on line 29, we subtract the sphere origin (always (0,0,0) in this script) from the newly found {x,y,z} coordinate.</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">21...22</td>
<td>We can construct a plane definition from a single point on that plane and a normal vector and we can construct a circle from a plane definition and a radius value. Voila.</td>
</tr>
</table>

### 8.6.1 Ellipses

Ellipses essentially work the same as circles, with the difference that you have to supply two radii instead of just one. Because ellipses only have two mirror symmetry planes and circles possess rotational symmetry (I.e. an infinite number of mirror symmetry planes), it actually does matter a great deal how the base-plane is oriented in the case of ellipses. A plane specified merely by origin and normal vector is free to rotate around that vector without breaking any of the initial constraints.

The following example script demonstrates very clearly how the orientation of the base plane and the ellipse correspond. Consider the standard curvature analysis graph as shown on the left:

<img src="{{ site.baseurl }}/images/primer-curvaturespline.svg" width="80%" float="right">

It gives a clear impression of the range of different curvatures in the spline, but it doesn't communicate the helical twisting of the curvature very well. Parts of the spline that are near-linear tend to have a garbled curvature since they are the transition from one well defined bend to another. The arrows in the left image indicate these areas of twisting but it is hard to deduce this from the curvature graph alone. The upcoming script will use the curvature information to loft a surface through a set of ellipses which have been oriented into the curvature plane of the local spline geometry. The ellipses have a small radius in the bending plane of the curve and a large one perpendicular to the bending plane. Since we will not be using the strength of the curvature but only its orientation, small details will become very apparent. 

```python
def FlatWorm():
    curve_object = rs.GetObject("Pick a backbone curve", 4, True, False)
    if not curve_object: return

    samples = rs.GetInteger("Number of cross sections", 100, 5)
    if not samples: return

    bend_radius = rs.GetReal("Bend plane radius", 0.5, 0.001)
    if not bend_radius: return

    perp_radius = rs.GetReal("Ribbon plane radius", 2.0, 0.001)
    if not perp_radius: return

    crvdomain = rs.CurveDomain(curve_object)

    crosssections = []
    t_step = (crvdomain[1]-crvdomain[0])/samples
    t = crvdomain[0]
    for t in rs.frange(crvdomain[0], crvdomain[1], t_step):
        crvcurvature = rs.CurveCurvature(curve_object, t)
        crosssectionplane = None
        if not crvcurvature:
            crvPoint = rs.EvaluateCurve(curve_object, t)
            crvTangent = rs.CurveTangent(curve_object, t)
            crvPerp = (0,0,1)
            crvNormal = rs.VectorCrossProduct(crvTangent, crvPerp)
            crosssectionplane = rs.PlaneFromFrame(crvPoint, crvPerp, crvNormal)
        else:
            crvPoint = crvcurvature[0]
            crvTangent = crvcurvature[1]
            crvPerp = rs.VectorUnitize(crvcurvature[4])
            crvNormal = rs.VectorCrossProduct(crvTangent, crvPerp)
            crosssectionplane = rs.PlaneFromFrame(crvPoint, crvPerp, crvNormal)

        if crosssectionplane:
            csec = rs.AddEllipse(crosssectionplane, bend_radius, perp_radius)
            crosssections.append(csec)
        t += t_step

    if not crosssections: return
    rs.AddLoftSrf(crosssections)
    rs.DeleteObjects(crosssections)
```


<table rules="rows">
<tr>
<th>Line</th>	
<th>Description</th>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">16</td>
<td><i>crosssections</i> is a list where we will store all our ellipse IDs. We need to remember all the ellipses we add since they have to be fed to the <i>rs.AddLoftSrf()</i> method. <i>crosssectionplane</i> will contain the base plane data for every individual ellipse, we do not need to remember these planes so we can afford to overwrite the old value with any new one.
You'll notice I'm violating a lot of naming conventions from paragraph [2.3.5 Using Variables]. If you want to make something of it we can take it outside. </td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">19</td>
<td>We'll be walking along the curve with equal parameter steps. This is arguably not the best way, since we might be dealing with a polycurve which has wildly different parameterizations among its subcurves. This is only an example script though so I wanted to keep the code to a minimum. We're using the same trick as before in the header of the loop to ensure that the final value in the domain is included in the calculation. By extending the range of the loop by one billionth of a parameter we circumvent the 'double noise problem' which might result from multiple additions of doubles.<td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">20</td>
<td>The <i>rs.CurveCurvature()</i> method returns a whole set of data to do with curvature analysis. However, it will fail on any linear segment (the radius of curvature is infinite on linear segments).</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">22...27</td>
<td>Hence, if it fails we have to collect the standard information in the old fashioned way. We also have to pick a <i>crvPerp</i> vector since none is available. We could perhaps use the last known one, or look at the local plane of the curve beyond the current -unsolvable- segment, but I've chosen to simply use a z-axis vector by default.</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">28...32</td>
<td>If the curve does have curvature at t, then we extract the required information directly from the curvature data.</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">33</td>
<td>Construct the plane for the ellipse.</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">35...37</td>
<td>Add the ellipse to the file and append the new ellipse curve ID csec to the list <i>crosssections</i>.</td>
</tr>
<tr>
<td style="vertical-align:top;text-align:right;padding:0px 10px;">40...42</td>
<td>Create a lofted surface through all ellipses and delete the curves afterwards.</td>
</tr>
</table>

### 8.6.2 Arcs

Since the topic of Arcs isn't much different from the topic of Circles, I thought it would be a nice idea to drag in something extra. This something extra is what we programmers call "recursion" and it is without doubt the most exciting thing in our lives (we don't get out much). Recursion is the process of self-repetition. Like loops which are iterative and execute the same code over and over again, recursive functions call themselves and thus also execute the same code over and over again, but this process is hierarchical. It actually sounds harder than it is. One of the success stories of recursive functions is their implementation in binary trees which are the foundation for many search and classification algorithms in the world today. I'll allow myself a small detour on the subject of recursion because I would very much like you to appreciate the power that flows from the simplicity of the technique. Recursion is unfortunately one of those things which only become horribly obvious once you understand how it works. 

Imagine a box in 3D space which contains a number of points within its volume. This box exhibits a single behavioral pattern which is recursive. The recursive function evaluates a single conditional statement: {when the number of contained points exceeds a certain threshold value then subdivide into 8 smaller boxes, otherwise add yourself to the document}. It would be hard to come up with an easier If…Else statement. Yet, because this behavior is also exhibited by all newly created boxes, it bursts into a chain of recursion, resulting in the voxel spaces in the images below:

<img src="{{ site.baseurl }}/images/primer-threshold.svg" width="80%" float="right">

The input in these cases was a large pointcloud shaped like the upper half of a sphere. There was also a dense spot with a higher than average concentration of points. Because of the approximating pattern of the subdivision, the recursive cascade results in these beautiful stacks. Trying to achieve this result without the use of recursion would entail a humongous amount of bookkeeping and many, many lines of code.
Before we can get to the cool bit we have to write some of the supporting functions, which -I hate to say it- once again involve goniometry (the mathematics of angles).

The problem: adding an arc using the start point, end point and start direction. As you will be aware there is a way to do this directly in Rhino using the mouse. In fact a brief inspection yields 14 different ways in which arcs can be drawn in Rhino manually and yet there are only two ways to add arcs through scripting:

- rs.AddArc(Plane, Radius, Angle)
- rs.AddArc3Pt(Point, Point, Point)

The first way is very similar to adding circles using plane and radius values, with the added argument for sweep angle. The second way is also similar to adding circles using a 3-point system, with the difference that the arc terminates at the first and second point. There is no direct way to add arcs from point A to point B while constrained to a start tangent vector. We're going to have to write a function which translates the desired Start-End-Direction approach into a 3-Point approach. Before we tackle the math, let's review how it works:

<table>
<tr>
<td width="30%"><img src="{{ site.baseurl }}/images/primer-arcs.svg" width="100%" float="right"></td>
<td>
We start with two points {A} & {B} and a vector definition {D}. The arc we're after is the red curve, but at this point we don't know how to get there yet. Note that this problem might not have a solution if {D} is parallel or anti-parallel to the line from {A} to {B}. If you try to draw an arc like that in Rhino it will not work. Thus, we need to add some code to our function that aborts when we're confronted with unsolvable input.  
<br><br>
We're going to find the coordinates of the point in the middle of the desired arc {M}, so we can use the 3Point approach with {A}, {B} and {M}. As the illustration on the left indicates, the point in the middle of the arc is also on the line perpendicular from the middle {C} of the baseline.
<br><br>
The halfway point on the arc also happens to lie on the bisector between {D} and the baseline vector. We can easily construct the bisector of two vectors in 3D space by process of unitizing and adding both vectors. In the illustration on the left the bisector is already pointing in the right direction, but it still hasn't got the correct length.
<br><br>
We can compute the correct length using the standard "Sin-Cos-Tan right triangle rules": 

The triangle we have to solve has a 90º angle in the lower right corner, a is the angle between the baseline and the bisector, the length of the bottom edge of the triangle is half the distance between {A} and {B} and we need to compute the length of the slant edge (between {A} and {M}).
</td>
</tr>
</table>

The relationship between a and the lengths of the sides of the triangle is: 

$$\cos({\alpha})=\frac{0.5D}{?} \gg \frac{1}{\cos({\alpha})}=\frac{?}{0.5D} \gg \frac{0.5D}{\cos({\alpha})} = ?$$  

We now have the equation we need in order to solve the length of the slant edge. The only remaining problem is cos(a). In the paragraph on vector mathematics (6.2 Points and Vectors) the vector dotproduct is briefly introduced as a way to compute the angle between two vectors. When we use unitized vectors, the arccosine of the dotproduct gives us the angle between them. This means the dotproduct returns the cosine of the angle between these vectors. This is a very fortunate turn of events since the cosine of the angle is exactly the thing we're looking for. In other words, the dotproduct saves us from having to use the cosine and arccosine functions altogether. Thus, the distance between {A} and {M} is the result of:


```python
(0.5 * rs.Distance(A, B)) / rs.VectorDotProduct(D, Bisector)
```

```python
def AddArcDir(ptStart, ptEnd, vecDir):
    vecBase = rs.PointSubtract(ptEnd, ptStart)
    if rs.VectorLength(vecBase)==0.0: return
    
    if rs.IsVectorParallelTo(vecBase, vecDir): return

    vecBase = rs.VectorUnitize(vecBase)
    vecDir = rs.VectorUnitize(vecDir)

    vecBisector = rs.VectorAdd(vecDir, vecBase)
    vecBisector = rs.VectorUnitize(vecBisector)
    
    dotProd = rs.VectorDotProduct(vecBisector, vecDir)
    midLength = (0.5*rs.Distance(ptStart, ptEnd))/dotProd
    
    vecBisector = rs.VectorScale(vecBisector, midLength)
    return rs.AddArc3Pt(ptStart, rs.PointAdd(ptStart, vecBisector), ptEnd)
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
