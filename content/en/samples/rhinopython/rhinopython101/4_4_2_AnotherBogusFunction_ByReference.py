import rhinoscriptsyntax as rs

def main():
    intA = 4
    intB = 7
    dblC = AnotherBogusFunction(intA, intB)
    print("A:", intA, ", B:", intB, ", C:", dblC)


def AnotherBogusFunction(number1, number2):
    number1 += 1
    number2 += 2
    return number1 * number2


if __name__=="__main__":
    main()