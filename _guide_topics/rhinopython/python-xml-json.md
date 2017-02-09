---
title: How to use JSON with Python 
description: How to format in JSON or XML.
authors: ['Scott Davidson']
author_contacts: ['scottd']
apis: ['RhinoPython']
languages: ['Python']
platforms: ['Mac', 'Windows']
categories: ['intermediate']
origin:
order: 75
keywords: ['script', 'Rhino', 'python']
layout: toc-guide-page
---

Here are some threads that show what people are asking about:

https://discourse.mcneel.com/t/python-scripts-for-adding-pictureframes-and-writing-a-json-file/41103/2

https://discourse.mcneel.com/t/python-methodology-for-saving-data-between-sessions/5013/3


https://discourse.mcneel.com/t/storing-of-the-data-files-processed-by-plugin/20375



## Overview

https://www.safaribooksonline.com/library/view/python-cookbook-3rd/9781449357337/ch06s02.html

http://stackoverflow.com/questions/12309269/how-do-i-write-json-data-to-a-file-in-python

https://docs.python.org/2/tutorial/inputoutput.html#saving-structured-data-with-json


<!--

A few things, I typically use this to generate json from classes

[10:43]  
http://www.newtonsoft.com/json
newtonsoft.com
Json.NET - Newtonsoft
Json.NET is a popular high-performance JSON framework for .NET
 

scottdavidson [10:43 AM] 
Or just sudo code is fine

[10:43]  
with explaination.

luisfraguada [10:43 AM] 
so does everyone else

[10:43]  
using .net

[10:44]  
not sure if it works in IronPythin

[10:44]  
but let me show you an example

scottdavidson [10:45 AM] 
It is interesting, because there is a JSON endcoder and decoder in Python

luisfraguada [10:45 AM] 
great

[10:45]  
https://github.com/mcneel/Iris/blob/master/Iris/Objects/IrisObjectPointLight.cs

[10:45]  
here is the Iris Point Light class

[10:45]  
takes a Rhino Point Light

[10:46]  
Notice how there are things like:
`[JsonProperty("name")]
public string Name { get; private set; }`` (edited)

scottdavidson [10:46 AM] 
Yes

luisfraguada [10:46 AM] 
each of those c# class properties are 'decorated'

[10:47]  
`JsonProperty("name")`` (edited)

scottdavidson [10:47 AM] 
That is interesting.

[10:47]  
Without this library, in Python you are stuck using the Dictionary object.

luisfraguada [10:48 AM] 
https://github.com/mcneel/Iris/blob/master/Iris/Objects/IrisObjectCurve.cs

[10:48]  
this is a bit more complex...the curve class

[10:48]  
but it should take any user strings on the curve if they have them

scottdavidson [10:49 AM] 
Ok, here is a structural question.

luisfraguada [10:49 AM] 
added this C# snippet
public IrisObjectCurve(Guid geometry, Guid material, string layer) : this()
        {
            Geometry = geometry;
            Material = material;
​
Add Comment Click to expand inline 13 lines

scottdavidson [10:49 AM] 
Do you use this only to encode the string to get it out to somewhere else.

luisfraguada [10:50 AM] 
notice how in that snippet I create user data to bring layer info along

[10:50]  
anyways

[10:50]  
then

scottdavidson [10:50 AM] 
Yes

[10:50]  
So you are using JSON as a string format to write out.

luisfraguada [10:50 AM] 
https://github.com/mcneel/Iris/blob/master/Iris/IrisMain.cs#L311

scottdavidson [10:50 AM] 
Iris has there own format.

luisfraguada [10:51 AM] 
yes

scottdavidson [10:51 AM] 
OK

luisfraguada [10:51 AM] 
I go through all of the objects, convert them to all of these objects

luisfraguada [10:51 AM] 
added this C# snippet
var scene = new IrisSceneFile
            {
                Metadata = metadata,
                Geometries = m_geometry,
                Materials = m_materials,
Add Comment Click to expand inline 9 lines

luisfraguada [10:51 AM] 
pack it all in there

scottdavidson [10:52 AM] 
You grab certain properties off the objects and then use these tools to write out.

luisfraguada [10:52 AM] 
https://github.com/mcneel/Iris/blob/master/Iris/IrisMain.cs#L435

scottdavidson [10:52 AM] 
Perfect.

luisfraguada [10:52 AM] 
yes

-->