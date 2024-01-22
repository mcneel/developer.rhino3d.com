import rhinoscriptsyntax as rs


def main():
    object_id = rs.GetObject("Select an object to sort")
    if object_id is None: return

    object_type = rs.ObjectType(object_id)
    if object_type is None: return
    
    layer_name = "Unsorted"
    if object_type==1 or object_type==2:
        layer_name="Points"
    elif object_type==4:
        layer_name="Curves"
    elif object_type==8 or object_type==16:
        layer_name="PolySurfaces"
    elif object_type==32:
        layer_name="Meshes"
    elif object_type==256:
        layer_name="Lights"
    elif object_type==512 or object_type==8192:
        layer_name="Annotations"
    elif object_type==2048 or object_type==4096:
        layer_name="Blocks"

    if not rs.IsLayer(layer_name):
        rs.AddLayer(layer_name)
    rs.ObjectLayer(object_id, layer_name)


if __name__=="__main__":
    main()