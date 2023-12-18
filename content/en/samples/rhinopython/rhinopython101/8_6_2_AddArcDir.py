#This script features an implementation of the ArcStartEndDir algorithm
#The script is different from the version in the primer in that it adds 
#linesegments when the Direction vector is parallel to A-B
import rhinoscriptsyntax as rs


def DrawArcSED():
    ptA = rs.GetPoint("Start of arc")
    if not ptA: return
    
    ptB = rs.GetPoint("End of arc")
    if not ptB: return
    
    ptD = rs.GetPoint("Direction of arc at start", ptA)
    if not ptD: return
    
    vecD = rs.PointSubtract(ptD, ptA)
    if rs.VectorLength(vecD)==0.0: return
    AddArcDir(ptA, ptB, vecD)


def AddArcDir(ptStart, ptEnd, vecDir):
    vecBase = rs.PointSubtract(ptEnd, ptStart)
    if rs.VectorLength(vecBase)==0.0: return
    
    if rs.IsVectorParallelTo(vecBase, vecDir):
        return rs.AddLine(ptStart, ptEnd)

    vecBase = rs.VectorUnitize(vecBase)
    vecDir = rs.VectorUnitize(vecDir)

    vecBisector = rs.VectorAdd(vecDir, vecBase)
    vecBisector = rs.VectorUnitize(vecBisector)
    
    dotProd = rs.VectorDotProduct(vecBisector, vecDir)
    midLength = (0.5*rs.Distance(ptStart, ptEnd))/dotProd
    
    vecBisector = rs.VectorScale(vecBisector, midLength)
    return rs.AddArc3Pt(ptStart, rs.PointAdd(ptStart, vecBisector), ptEnd)


if __name__=="__main__":
    DrawArcSED()