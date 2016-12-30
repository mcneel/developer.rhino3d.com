---
title: Garden Path Sample
description: Demonstrates Basic syntax for writing python scripts.
authors: ['Dale Fugier']
author_contacts: ['dale']
apis: ['RhinoPython']
languages: ['Python']
platforms: ['Windows', 'Mac']
categories: ['Adding Objects']
origin:
order: 9
keywords: ['script', 'Rhino', 'python']
layout: code-sample-python
---

The goal of the garden path tutorial is to develop a script that draws a garden path and fills it with circular concrete tiles. For those familiar with AutoLISP®, the programming language of Autodesk's AutoCAD®, you are probably also familiar with the garden path tutorial. 

```python
import rhinoscriptsyntax as rs
import math #Use this to get sine, cosine and radians.
import scriptcontext as sc

def test():
    
        #Assign variables to the sin and cos functions for use later.
    Sin = math.sin
    Cos = math.cos
    
    
    	# Acquire information for the garden path
    	
    	# set default values for the distances
    default_hwidth = 1
    default_trad = 1
    default_tspace = 1
    	
    	
    	# look for any previously used values stored in sticky and use those if available.
    if sc.sticky.has_key("GP_WIDTH"):
        default_hwidth = sc.sticky["GP_WIDTH"]
        
    if sc.sticky.has_key("GP_RAD"):
        default_trad = sc.sticky["GP_RAD"]
        
    if sc.sticky.has_key("GP_Space"):
        default_tspace = sc.sticky["GP_SPACE"]	
    	    
        #get the path direction, length and location from two points entered by the user
    sp = rs.GetPoint("Start point of path centerline")
    if sp is None: return
    
    ep = rs.GetPoint("End point of path centerline", sp)
    if ep is None: return
    
        #now ask the user what the distances should be, offering the defaults arrived at above
        
    hwidth = rs.GetDistance(sp, default_hwidth,  second_pt_msg = "Half width of path")
    if hwidth is None: return
    
        #Store the new value in sticky for use next time
    sc.sticky["GP_WIDTH"] = hwidth
    
    trad = rs.GetDistance(sp, default_trad, second_pt_msg = "Radius of tiles")
    if trad is None: return
    
        #Store  the new value in sticky for use next time
    sc.sticky["GP_RAD"] = trad
    
    tspace = rs .GetDistance(sp, default_tspace, second_pt_msg = "Distance between tiles")
    if tspace is None: return
    
        #Store  the new value in sticky for use next time
    sc.sticky["GP_SPACE"] = tspace
    
    	# Calculate angles
    
    temp = rs.Angle(sp, ep)
    
    pangle = temp[0]
    
    plength = rs.Distance(sp, ep)
    
    width = hwidth * 2
    
    angp90 = pangle + 90.0
    
    angm90 = pangle - 90.0
    
    
	# To increase speed, disable redrawing

    rs.EnableRedraw (False)
    
	# Draw the outline of the path
    #make an empty list
    pline = []
    
    #add points to the list
    pline.append(rs.Polar(sp, angm90, hwidth))
    
    pline.append(rs.Polar(pline[0], pangle, plength))
    
    pline.append(rs.Polar(pline[1], angp90, width))
    
    pline.append(rs.Polar(pline[2], pangle + 180.0, plength))
    
    #add the first point back on to the end of the list to close the pline
    pline.append (pline[0])
    
    #create the polyline from the lst of points.
    rs.AddPolyline (pline)
    
    

    # Draw the rows of tiles
    
    #define a plane - 
    #using the WorldXY plane the reults will always be added parallel to that plane, 
    #regardless of the active plane where the points are picked.
    
    plane = rs.WorldXYPlane()
    
    pdist = trad + tspace
    
    off = 0.0
    
    while (pdist <= plength - trad):
    
        #Place one row of tiles given distance along path
        
        # and possibly offset it
        
        pfirst = rs.Polar(sp, pangle, pdist)
        
        pctile = rs.Polar(pfirst, angp90, off)
        
        pltile = pctile
        
        while (rs.Distance(pfirst, pltile) < hwidth - trad):
        
            plane = rs.MovePlane(plane, pltile)
            
            rs.AddCircle (plane, trad)
            
            pltile = rs.Polar(pltile, angp90, tspace + trad + trad)
        
        
        pltile = rs.Polar(pctile, angm90, tspace + trad + trad)
        
        while (rs.Distance(pfirst, pltile) < hwidth - trad):
        
            plane = rs.MovePlane(plane, pltile)
            
            rs.AddCircle (plane, trad)
            
            pltile = rs.Polar(pltile, angm90, tspace + trad + trad)

        pdist = pdist + ((tspace + trad + trad) * Sin(math.radians(60)))
        
        if off == 0.0:
        
            off = (tspace + trad + trad) * Cos(math.radians(60))
        
        else:
        
            off = 0.0
    
   

	

    
if __name__ == "__main__":
    
    test()

```
