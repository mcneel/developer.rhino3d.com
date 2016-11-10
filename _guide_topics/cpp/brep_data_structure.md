---
title: Brep Data Structure
description: This guide discusses the Boundary Representation (B-rep) in the context of openNURBS.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['C/C++']
languages: ['C/C++']
platforms: ['Windows']
categories: ['Fundamentals']
origin: http://wiki.mcneel.com/developer/brepstructure
order: 4
keywords: ['rhino', 'brep', 'openNURBS', 'data']
layout: toc-guide-page
TODO: 'needs explanation, diagram style update'
---

# {{ page.title }}

{{ page.description }}

## Conceptual diagram

![BRep Data Structure]({{ site.baseurl }}/images/brep_data_structure_01.png)

## Sample

```cpp
//Given a brep and a face index
const ON_Brep* brep;
const int face_index = 0;
ON_SimpleArray<int> face_ti_list; //trims indeces list
ON_SimpleArray<int> face_ei_list; //edges indeces list

//Get the BrepFace of the given index
const ON_BrepFace* face = brep->Face(face_index);
if( 0 == face )
  return false;

//Get the loop of the face
for( int fli = 0; fli < face->LoopCount(); fli++ )
{
  const ON_BrepLoop* loop = face->Loop( fli );
  if( 0 == loop )
    continue;

  for( int lti = 0; lti < loop->TrimCount(); lti++ )
  {
    //Find the trim
    const ON_BrepTrim* trim = loop->Trim( lti );
    if( 0 == trim )
      continue;
    face_ti_list.Append( trim->m_trim_index );

    //Find the edge of that trim
    //Each trim has exactly one edge attached to it
    const ON_BrepEdge* edge = trim->Edge();
    if( 0 == edge )
      continue;
    face_ei_list.Append( edge->m_edge_index );
  }
}
```
