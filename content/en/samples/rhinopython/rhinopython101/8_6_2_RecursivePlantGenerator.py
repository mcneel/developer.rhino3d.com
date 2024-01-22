"""
This script features an implementation of the recursive growth algorithm.
A main subroutine was added (this one is missing from the primer, because
it is very boring) to cater for the frontend.
Comments have been added to this subroutine to explain the more exotic calls

---------------------------------------------------------------------------------------
-------------------------the code below does not appear in the primer------------------
---------------------------------------------------------------------------------------

We use the 'sticky' dictionary to hold growth properties that will
remain active after the script completes. This means the settings are remembered
between script runs but they will be erased whenever Rhino exits.
They all start out being uninitialized (not assigned any value)
"""
import rhinoscriptsyntax as rs
import scriptcontext
import random

prop_MinTwigCount = 0
prop_MaxTwigCount = 0
prop_MaxGenerations = 0
prop_MaxTwigLength = 0
prop_LengthMutation = 0
prop_MaxTwigAngle = 0
prop_AngleMutation = 0

def getsticky(name, default_value):
    name = "PlaneGenerator_"+name
    if scriptcontext.sticky.has_key(name):
        return scriptcontext.sticky[name]
    return default_value
def setsticky(name, value):
    name = "PlaneGenerator_"+name
    scriptcontext.sticky[name] = value


def PlantGenerator():
    #Ask for a start point of the plant.
    ptRoot = rs.GetPoint("Root point for plant")
    if not ptRoot: return

    #Check all sticky variables for initialization and assign default
    #values if they have not yet been set.
    prop_MinTwigCount = getsticky("MinTwigCount",0)
    prop_MaxTwigCount = getsticky("MaxTwigCount",8)
    prop_MaxGenerations = getsticky("MaxGenerations",5)
    prop_MaxTwigLength = getsticky("MaxTwigLength",10.0)
    prop_LengthMutation = getsticky("LengthMutation",0.75)
    prop_MaxTwigAngle = getsticky("MaxTwigAngle",30.0)
    prop_AngleMutation = getsticky("AngleMutation",0.85)

    #Collect all growth properties using a series of GetInteger and GetReal methods
    #This could be done a lot cleaner using an iterated Option getter, but that's a lot
    #more code. See chapter 8 on UI methods.
    
    #Some of these values have limits on their value. See the RhinoScript help
    #for information about the arguments.
    prop_MinTwigCount = rs.GetInteger("Minimum twig count", prop_MinTwigCount)
    if prop_MinTwigCount is None: return
	
    prop_MaxTwigCount = rs.GetInteger("Maximum twig count", prop_MaxTwigCount, 1)
    if prop_MaxTwigCount is None: return

    prop_MaxGenerations = rs.GetInteger("Maximum branch generations", prop_MaxGenerations, 1, 1000)
    if prop_MaxGenerations is None: return

    prop_MaxTwigLength = rs.GetReal("Maximum twig length", prop_MaxTwigLength, 0.01)
    if prop_MaxTwigLength is None: return

    prop_LengthMutation = rs.GetReal("Twig length mutation", prop_LengthMutation, 0.01)
    if prop_LengthMutation is None: return

    prop_MaxTwigAngle = rs.GetReal("Maximum twig angle", prop_MaxTwigAngle, 0.0, 90.0)
    if prop_MaxTwigAngle is None: return

    prop_AngleMutation = rs.GetReal("Twig angle mutation", prop_AngleMutation, 0.01)
    if prop_MaxTwigAngle is None: return

    setsticky("MinTwigCount",prop_MinTwigCount)
    setsticky("MaxTwigCount",prop_MaxTwigCount)
    setsticky("MaxGenerations",prop_MaxGenerations)
    setsticky("MaxTwigLength",prop_MaxTwigLength)
    setsticky("LengthMutation",prop_LengthMutation)
    setsticky("MaxTwigAngle",prop_MaxTwigAngle)
    setsticky("AngleMutation",prop_AngleMutation)

    #Turning of redraw will drastically speed up the tree generation. However, it's quite fun to watch
    #so you might consider switching it off.
    rs.EnableRedraw(False)

    #Collect all tree-growth variables into a single array.
    growthprops = (prop_MinTwigCount, prop_MaxTwigCount, prop_MaxGenerations, 
                   prop_MaxTwigLength, prop_LengthMutation, prop_MaxTwigAngle, prop_AngleMutation)

    #Call the recursive function the first time. It will call itself from now on.
    #We also need to tell this first function that is has generation 1
    #We're assuming the growth direction at the root is vertical, 
    #so we have to supply a (0,0,1) direction vector.
    RecursiveGrowth(ptRoot, (0,0,1), growthprops, 1)

    #After all recursion has completed, be sure to enable the redraw again.
    rs.EnableRedraw(True)


#---------------------------------------------------------------------------------------
#-------------------------the code below appears in the primer--------------------------
#---------------------------------------------------------------------------------------

def RecursiveGrowth( ptStart, vecDir, props, generation):
    minTwigCount, maxTwigCount, maxGenerations, maxTwigLength, lengthMutation, maxTwigAngle, angleMutation = props
    if generation>maxGenerations: return

    #Copy and mutate the growth-properties
    newProps = props
    maxTwigLength *= lengthMutation
    maxTwigAngle *= angleMutation
    if maxTwigAngle>90: maxTwigAngle=90

    #Determine the number of twigs (could be less than zero)
    newprops = minTwigCount, maxTwigCount, maxGenerations, maxTwigLength, lengthMutation, maxTwigAngle, angleMutation
    maxN = int( minTwigCount+random.random()*(maxTwigCount-minTwigCount) )
    for n in range(1,maxN):
        ptGrow = RandomPointInCone(ptStart, vecDir, 0.25*maxTwigLength, maxTwigLength, maxTwigAngle)
        newTwig = AddArcDir(ptStart, ptGrow, vecDir)
        if newTwig:
            vecGrow = rs.CurveTangent(newTwig, rs.CurveDomain(newTwig)[1])
            RecursiveGrowth(ptGrow, vecGrow, newProps, generation+1)


def RandomPointInCone( origin, direction, minDistance, maxDistance, maxAngle):
    vecTwig = rs.VectorUnitize(direction)
    vecTwig = rs.VectorScale(vecTwig, minDistance + random.random()*(maxDistance-minDistance))
    MutationPlane = rs.PlaneFromNormal((0,0,0), vecTwig)
    vecTwig = rs.VectorRotate(vecTwig, random.random()*maxAngle, MutationPlane.XAxis)
    vecTwig = rs.VectorRotate(vecTwig, random.random()*360, direction)
    return rs.PointAdd(origin, vecTwig)


def AddArcDir( ptStart, ptEnd, vecDir):
    vecBase = rs.PointSubtract(ptEnd, ptStart)
    if rs.VectorLength(vecBase)==0.0: return
    
    if rs.IsVectorParallelTo(vecBase, vecDir): return rs.AddLine(ptStart, ptEnd)

    vecBase = rs.VectorUnitize(vecBase)
    vecDir = rs.VectorUnitize(vecDir)

    vecBisector = rs.VectorAdd(vecDir, vecBase)
    vecBisector = rs.VectorUnitize(vecBisector)
    
    dotProd = rs.VectorDotProduct(vecBisector, vecDir)
    midLength = (0.5 * rs.Distance(ptStart, ptEnd)) / dotProd
    
    vecBisector = rs.VectorScale(vecBisector, midLength)
    return rs.AddArc3Pt(ptStart, ptEnd, rs.PointAdd(ptStart, vecBisector))


if __name__=="__main__":
    PlantGenerator()