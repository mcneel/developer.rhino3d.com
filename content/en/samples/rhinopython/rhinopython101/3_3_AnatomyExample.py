import rhinoscriptsyntax as rs                        # Import Statement
#Script written by Skylar Tibbits on 03-09-2011        # Default comments

strInfo = "This is just a test"                        # Global Variable

def simpleFunction(text):                # Function Declaration
    print(text)                            # Code to Execute Within the Function
                                        # (Note the Indentation)
simpleFunction(strInfo)                    # Calling the Function (After it's created)