from time import sleep

starLine = "*************************"
startMsg = " STARTING MathPy " 

print(startMsg.center(50,"#"))

""" def sumar(data):
    print("Beginning data processing...")
    modified_data = data + " that has been modified"
    sleep(30)
    print("Data processing finished.")
    return modified_data
 """

def suma():

    print ("my name is: ", suma.__name__)
    return 0

def resta():

    print ("my name is: ", resta.__name__)
    return 0

def multi():

    print ("my name is: ", multi.__name__)
    return 0

def divi():

    print ("my name is: ", divi.__name__)
    return 0

def exponen():

    print ("my name is: ", exponen.__name__)
    return 0

def rCuadrada():

    print ("my name is: ", rCuadrada.__name__)
    return 0

def NOPE():

    print ("Somenthing went wrong, try again!")
    return -1
 
switcher = {
        0: suma,
        1: resta,
        2: multi,
        3: divi,
        4: exponen,
        5: rCuadrada
        # "NOPE": NOPE
    }

def main():

    intExe = 0 
    print ("¡WELCOME!")

    while intExe == 0:      
        print ("MathPy has the following operation: \n -[0] ADDITION \n -[1] SUBTRACTION \n -[2] MULTIPLICATION \n -[3] DIVISION \n -[4] EXPONENTIATION \n -[5] SQUARE ROOTING ")
        vOpera = input("Using numbers, specify the desired operation: ")

        func = switcher.get(int(vOpera), NOPE)
        func()
        pass
    

if __name__ == "__main__":
    main()