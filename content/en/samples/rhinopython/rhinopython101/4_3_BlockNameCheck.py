import rhinoscriptsyntax as rs

def main():
    if not rs.IsBlock("SomeBlockName"):
        print("Missing block definition: SomeBlockName")


if __name__=="__main__":
    main()