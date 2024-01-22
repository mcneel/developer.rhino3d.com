import rhinoscriptsyntax as rs
somenumber = rs.GetReal("Line length")
line = rs.AddLine( (0,0,0), (somenumber,0,0) )
if line is None:
    print("Something went wrong")
else:
    print("Line curve inserted with id", line)