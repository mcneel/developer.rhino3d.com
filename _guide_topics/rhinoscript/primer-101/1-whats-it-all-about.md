---
title: 1 What's it all about?
description:
authors: ['David Rutten']
author_contacts: ['DavidRutten']
sdk: ['RhinoScript']
languages: ['VBScript']
platforms: ['Windows']
categories: ['RhinoScript 101']
origin:
order: 1
keywords: ['rhinoscript', 'vbscript', commands']
layout: toc-guide-page
guide_homepage: guides/rhinoscript/primer-101/
---

## 1.1 Macros

Rhinoceros is based on a command-line interface. This means you can control it by using only the keyboard. You type in the commands and the program will execute them. Ever since the advent of the mouse, a user interface which is purely command-line based is considered to be primitive, and rightly so. Instead of typing:

```
Line 0,0,0 10,0,0
```

you can equally well click on the Line button and then twice in the viewport to define the starting and ending points of a line-curve. Because of this second (graphical) interface some people have done away with the
command-line entirely. Emotions run high on the subject; some users are command-line fanatics, others use only toolbars and menus. Programmers have no emotions in this respect, they are all wedded to the command-line. It’s no use programming the mouse to go to a certain coordinate and then simulate a mouse click, that is just plain silly. Programmers pump text into Rhino and they expect to get text in return.

The lowest form of programming in Rhino is using macros. I do not wish to offend those of you who write macros for a living, but it cannot be denied that it is a very primitive way to automate processes. I shall only briefly pause at the subject of macros, partly so we know which is which and partly because we might at some point simulate macros using RhinoScript.

A macro is a prerecorded list of orders for Rhino to execute. The _Line command at the top of this page is an example of a very simple macro. If your job is to open Rhino files, add a line from 0,0,0 to 10,0,0 to each one and save the file again, you would probably get very tired very quickly from typing "_Line w0,0,0 w10,0,0" six times a minute. Enter macros. Macros allow you to automate tasks you would normally do by hand but not by brain. Macros cannot be made smart, nor do they react to the things they help create. They’re a bit like traffic wardens in that respect. An example of a more sophisticated macro would be:

```
 _SelNone
 _Polygon _NumSides=6 w0,0,0 w10,0,0
 _SelLast
 -_Properties _Object _Name RailPolygon _Enter _Enter
 _SelNone
 _Polygon _NumSides=6 w10,0,0 w12,0,0
 _SelLast
 _Rotate3D w0,0,0 w10,0,0 90
 -_Properties _Object _Name ProfilePolygon _Enter _Enter
 _SelNone
 -_Sweep1 _SelName RailPolygon _SelName ProfilePolygon _Enter   _Simplify=None Enter
```

![{{ site.baseurl }}/images/hexagonaltorus.svg]({{ site.baseurl }}/images/hexagonaltorus.svg){: .float-img-right width="325"}

The above code will create the same hexagonal torus over and over again. It might be useful, but it's not flexible. You can type the above text into the command-line by hand, or you can put it into a button. You can even copy-paste the text directly into Rhino.

Incidentally, the underscores before all the command names are due to Rhino localization. Using underscores will force Rhino to use English command names instead of -say- Italian or Japanese or whatever the custom setting is. You should always force English command names since that is the only guarantee that your code will work on all copies of Rhino worldwide.

The hyphen in front of the _Properties and _Sweep1 command is used to suppress dialog boxes. If you take the hyphens out you will no longer be able to change the way a command works through the command-line.

There’s no limit to how complex a macro can become, you can keep adding commands without restrictions, but you’ll never be able to get around the limitations that lie at the heart of macros.

## 1.2 Scripts

The limitations of macros have led to the development of scripting languages. Scripts are something halfway between macros and true (compiled) programs and plug-ins. Unlike macros they can perform
mathematical operations, evaluate variable conditions, respond to their environment and communicate with the user. Unlike programs they do not need to be compiled prior to running. Rhinoceros implements the standard
‘Microsoft® Visual Basic® Scripting Edition’ language (more commonly known as VBScript) which means that everything that is true of VBScript is also true of RhinoScript.

Scripts, then, are text files which are interpreted one line at a time. But here’s the interesting part; unlike macros, scripts have control over which line is executed next. This flow control enables the script to skip certain instructions or to repeat others. Flow control is achieved by what is called "conditional evaluation" and we must familiarize ourselves with the language rules of VBScript before we can take advantage of flow control.

VBScript is a very forgiving programming language. ‘Forgiving’ in this sense indicates that the language rules are fairly loose. The language rules are usually referred to as the syntax and they indicate what is and isn’t valid:

```
"There is no apple cake here."		» valid
"There is here no apple cake"		» invalid
"Here, there is no apple cake."		» valid
"There is no Apfelstrudel here."        » invalid
```

The above list is a validity check for English syntax rules. The first and third lines are proper English and the others are not. However, there are certain degrees of wrong. Nobody will misunderstand the second line just because the word order is wrong. The forth line is already a bit harder since it features a word from a different language.

Although most of us are smart enough to understand all four lines, a computer is not. I mentioned before that VBScript is a forgiving language. That means that it can intercept small errors in the syntax. Before we can start doing anything with Rhino, we must have a good understanding of VBScript syntax.


## 1.3 Scripts

There are several ways to run scripts in Rhino, each has its own (dis)advantages. You could store scripts as external text files and have Rhino load them for you whenever you want to run them. You could also use Rhino's in-build script editor which means you can run the Scripts directly from the editor. The last option is to embed scripts in toolbar buttons, which makes it very hard to edit them, but much easier to distribute them.

Throughout this book, I will use the in-build editor method. I find this to be the best way to work on simple scripts. (Once a script becomes fairly complex and long, it's probably better to switch to an external editor.) In order to run a script via the in-build editor,  Use the _EditScript command to activate it, then type in your script and press the Run button:

<img src="{{ site.baseurl }}/images/EditScriptDialog.png">{: .img-center  width="75%"}

All the example code in this primer can be copy-pasted directly into the EditScript dialog.

---

## Next Steps

Now that you know what a scripting language is, check out the [Scripting Essentials]({{ site.baseurl }}/guides/rhinoscript/primer-101/2-vbscript-essentials/) guide to learn more about the RhinoScript language.
