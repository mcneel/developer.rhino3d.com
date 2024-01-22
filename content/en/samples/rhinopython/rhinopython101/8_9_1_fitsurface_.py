"""
NOTE:

- Reference to RhinoCommmon.dll is added by default

- You can specify your script requirements like:

    # r: <package-specifier> [, <package-specifier>]
    # requirements: <package-specifier> [, <package-specifier>]

    For example this line will ask the runtime to install
    the listed packages before running the script:

    # requirements: pytoml, keras

    You can install specific versions of a package
    using pip-like package specifiers:

    # r: pytoml==0.10.2, keras>=2.6.0

- Use env directive to add an environment path to sys.path automatically
    # env: /path/to/your/site-packages/
"""
#! python3

import rhinoscriptsyntax as rs
import scriptcontext as sc

import System
import System.Collections.Generic
import Rhino

import rhinoscriptsyntax as rs


def SurfaceFitter():
    srf_id = rs.GetObject("Surface to fit", 8, True, True)
    if not srf_id: return

    pts = rs.GetPointCoordinates("Points to fit to", False)
    if not pts: return

    for n in range(100):
        nSrf = FitSurface(srf_id, pts)
        rs.DeleteObject(srf_id)
        srf_id = nSrf


def FitSurface(srf_id, samples):
    ptSurface = rs.SurfacePoints(srf_id)
    grSurface = rs.SurfaceEditPoints(srf_id, True, True)
    nrSurface = GrevilleNormals(srf_id)

    uvSamples = XYZ_To_UVW(srf_id, samples)
    #Create null vectors for all control-point forces
    vecForce = [(0,0,0) for pt in ptSurface]

    for i in range(len(uvSamples)):
        LocalCP = NearestUV(uvSamples[i], grSurface)
        LocalForce = nrSurface[LocalCP]
        LocalForce = rs.VectorScale(LocalForce, uvSamples[i][2])
        vecForce[LocalCP] = rs.VectorAdd(vecForce[LocalCP], LocalForce)
	
    ptSurface = [rs.PointAdd(ptSurface[i], vecForce[i]) for i in range(len(ptSurface))]

    srf_CP_Count = rs.SurfacePointCount(srf_id)
    srf_Knots = rs.SurfaceKnots(srf_id)
    srf_Weights = rs.SurfaceWeights(srf_id)
    srf_Degree = (rs.SurfaceDegree(srf_id, 0), rs.SurfaceDegree(srf_id, 1))
    return rs.AddNurbsSurface(srf_CP_Count, ptSurface, srf_Knots[0], srf_Knots[1], srf_Degree, srf_Weights)


def XYZ_To_UVW(srf_id, pXYZ):
    pUVW = []
    for point in pXYZ:
        uvClosest = rs.SurfaceClosestPoint(srf_id, point)
        ptClosest = rs.EvaluateSurface(srf_id, uvClosest[0], uvClosest[1])
        srfNormal = rs.SurfaceNormal(srf_id, uvClosest)
        pPositive = rs.PointAdd(ptClosest, srfNormal)
        pNegative = rs.PointSubtract(ptClosest, srfNormal)
        fDistance = rs.Distance(ptClosest, point)
        if rs.Distance(point,pPositive) > rs.Distance(point, pNegative):
            fDistance = -fDistance
        pUVW.append( (uvClosest[0], uvClosest[1], fDistance) )
    return pUVW


def GrevilleNormals(srf_id):
    uvGreville = rs.SurfaceEditPoints(srf_id, True, True)
    return [rs.SurfaceNormal(srf_id, g) for g in uvGreville]


def NearestUV(uvPt, uvSet):
    minI = -1
    minD = 1e300

    for i in range(len(uvSet)):
        d = (uvPt[0] - uvSet[i][0])**2 + (uvPt[1] - uvSet[i][1])**2
        if d<minD:
            minI = i
            minD = d
    return minI


if __name__=="__main__":
    SurfaceFitter()
