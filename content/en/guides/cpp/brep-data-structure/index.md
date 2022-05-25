+++
authors = [ "dale" ]
categories = [ "Fundamentals" ]
description = "This guide discusses the Boundary Representation (B-rep) in the context of openNURBS."
keywords = [ "rhino", "brep", "openNURBS", "data" ]
languages = [ "C/C++" ]
sdk = [ "C/C++" ]
title = "Brep Data Structure"
type = "guides"
weight = 4

[admin]
TODO = "needs explanation, diagram style update"
origin = "http://wiki.mcneel.com/developer/brepstructure"
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++

 
## Conceptual diagram

![BRep Data Structure](/images/brep-data-structure-01.png)

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
