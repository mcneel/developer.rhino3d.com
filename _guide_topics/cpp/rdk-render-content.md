---
title: Renderer Development Kit
description: This document describes how to use the RDK render content classes in C/C++.
authors: ['john_croudy']
sdk: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['RDK']
origin: http://wiki.mcneel.com/labs/rendererdevelopmentkit10
order: 1
keywords: ['RDK', 'Rhino', 'Renderer', 'Development', 'Plugin']
layout: toc-guide-page
---
# Render Contents
## What they are and how to use them

![Material Environment and Texture]({{ site.baseurl }}/images/rdk-met.png)

### Introduction
Probably the most important object in the Rhino RDK is the Render Content (AKA ‘Content’) object. This object is an abstraction that represents one of three possible ways of describing something that is going to be drawn (rendered) on the screen. There are three kinds of contents: _Materials_, _Environments_ and _Textures_. A material describes how a surface will be rendered. It has properties such as color, glossiness, etc. An environment describes how the surroundings of a model affect its appearance. A texture describes the texture of a surface. In addition to color and glossiness, all real-world surfaces have a detailed appearance such as a wood grain. This appearance is described by RDK textures.

### Classes
The base class for contents is _CRhRdkContent_. This is an abstraction that controls the features common to all contents. For example, all contents have a unique identifier called the instance id which identifies each instance of CRhRdkContent. They also have a unique type id which defines their type and an instance name which is the user-defined name that appears on the screen. They can also have any number of children which means that a content is usually considered as a hierarchy -- a kind of family tree, because these children can also have children to any depth. This flexibility allows the user to create very complex materials if so desired. All these properties and more are stored in and managed by the base class called CRhRdkContent. This base class has a single immediate subclass called _CRhRdkCoreContent_ which provides default implementations of some of the more complicated functions, mostly to do with the user interface. Derived from this are the three main kinds; _CRhRdkMaterial_, _CRhRdkEnvironment_ and _CRhRdkTexture_. It is from these latter three objects that a plug-in should derive its own specialized materials, environments and textures. To do this, it is necessary to choose a base class from one of those three and write a subclass that overrides or implements all the necessary virtual functions, implement a factory class that knows how to create an instance of the class, and register the factory with the RDK. Once this is done, your content will start to appear in the Rhino user interface, specifically in the Material Editor if the content is a material (or the Environment Editor or Texture Palette if it is an environment or texture). You can choose to use the default user interface provided by CRhRdkCoreContent or you can create a custom user interface of your own design.

### Lifetime and ownership
There are two flavors of content in the RDK -- temporary and persistent. It is very important to understand the distinction between a temporary content instance and a persistent content instance, and the fact that a temporary instance (and all its children) can become persistent.

Temporary contents get created and deleted very often during the normal operation of the RDK. In fact, just about anything the user clicks on might result in a temporary content being created and deleted again. They are created by the content browser, the preview rendering, and so on. They are 'free floating' and are owned by whomever created them. They do not appear in the modeless UI, they do not get saved in the 3dm file, and they can freely be deleted again after use.

Contrast this with persistent contents which are attached to a document. They are always owned by the RDK, appear in the modeless UI and get saved in the 3dm file. You should never store pointers to persistent contents; you should only store their instance ids and look them up again using  CRhRdkDocument::FindContentInstance(). They can be deleted only after detaching them from the document.

This is an example code sequence showing the main stages in the lifetime of a content.

```cpp
  // Create a new content owned by you.
  auto* pContent = new CMyContent;

  // Initialize the content.
  pContent->Initialize();

  // Attach the content to a document. The content is now owned by
  // the document and it will appear in the various user interfaces.
  rdkDoc.AttachContent(pContent);

  // Detach the content from the document. The content will disappear
  // from any user interfaces and it is once again owned by you.
  rdkDoc.DetachContent(pContent);

  // Uninitialize the content to prepare it for deletion.
  pContent->Uninitialize();

  // Delete the content. This is possible because the content is owned by you.
  delete pContent;
```

You can also create a free-floating content that is not attached to a document. This content will not appear in any modeless UIs, but it is possible to edit it in a modal UI by calling the `Edit()` method.

```cpp

  auto* pContent = new CMyMaterial;

  // Initialize the content.
  pContent->Initialize();

  // Edit the content in the Modal Editor. If the user clicks OK, this returns an edited version
  // of the content (the original is unaltered) and you own this object as well as the original one.
  auto* pEdited = pContent->Edit();
  if (nullptr != pEdited) // Returns null if the editor is canceled.
  {
    // Uninitialize the edited content to prepare it for deletion.
    pEdited->Uninitialize();

    // Delete the edited content. This is possible because the content is owned by you.
    delete pEdited;
  }

  // Uninitialize the original content to prepare it for deletion.
  pContent->Uninitialize();

  // Delete the original content. This is possible because the content is owned by you.
  delete pContent;
```

In an ideal world, the call to `delete` would both uninitialize and delete the content. But since `Uninitialize()` is a virtual function, this is not possible. So every call to `delete` must be preceded by a call to `Uninitialize()`. Remember that you can only do this if you own the object. Contents that are owned by a document (attached) cannot be deleted by the client without first being detached.

The most important thing to understand is that if you want to delete a content, you must know who owns it and act accordingly. The RDK tries to enforce good practice by using constness. For example, the function `CRhRdkDocument::FindContentInstance()` returns a const pointer to the content. This has two implications:
1. This content is not owned by you and you can’t delete it.
2. This content can’t be modified; it’s read-only. See below under Modifying Contents for information on how a const content can be modified.

{:class="table table-bordered"}
| Who owns it?            | Procedure for deletion |
|-------------------------|------------------------|
| You                     | Uninitialize it.<br>Delete it. |
| A document              | Detach it from the document.<br>Uninitialize it.<br>Delete it. |
| Unknown                 | You have no right to delete it. Don’t even try. |

### Modifying Contents
If a content is owned by you, for example immediately after you create it, then it is generally non-const and you can modify it by calling any non-const method such as `SetParameter()`. But if the content is const, for example after being found in a document, then you have to open it for modification. This is done by calling `BeginChange()` which begins a change bracket. BeginChange() takes a parameter called the change context. This is one of the values of the enum `RhRdkChangeContext`. The most common one used by plug-ins is `RhRdkChangeContext::UI` which means the change is being done by the user inside some user interface. BeginChange() also returns a non-const reference to the same content, allowing you to call any non-const method such as `SetParameter()`. It is important to call the `Changed()` method on the content if you detect that a change to the parameter has occurred. If this is not done, the user interface will not update. More than one parameter can be changed inside the change bracket. When all the desired changes have been made, you must call `EndChange()`. Calls to BeginChange() and EndChange() can be nested but there must always be exactly one call to EndChange() for every call to BeginChange(). The final call to EndChange() closes the content and sends the events necessary to update the user interface.
