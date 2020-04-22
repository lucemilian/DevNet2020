import sys
import random
from time import sleep
from functools import reduce


#El texto se ha puesto en ingles con el objetivo de practicar el idioma

#Mensaje de bienvenida
# starLine = "*************************"
startMsg = " STARTING MathPy " 
print(startMsg.center(50,"#"))

# Funcion externa para pasar las entradas del usuario a float, ya que se usa en mas de un sitio
def laLita():

    exeLita=True
    litaN =[]

    while  (exeLita):
        valor = input("Give number, or press ENTER: ")
        print
        if valor == "":
            exeLita=False

        else: 
            try:
                number = float(valor) 
                litaN.append(number)
                print (litaN)

            except ValueError:
                print ("Error...numbers only!")

    if not litaN:
        litaN = [random.randint(1,99),random.randint(1,99)]
        print ("The list is empty...so...EXAMPLE LIST! => ", litaN)


    return litaN

# Funcion suma
def suma():

    sumaMsg = " I am operation: " + suma.__name__+" "
    print(sumaMsg.center(40,"*"))
    # print ("\nI am operation: ", suma.__name__)

    lNums = laLita()                  
    sValor = sum(lNums)

    print("\nSum of", lNums," es :",sValor,"\n")

    sleep(5)
    return

# Funcion resta
def resta():

    restaMsg = " I am operation: " + resta.__name__+" "
    print(restaMsg.center(40,"*"))
    # print ("My name is: ", resta.__name__)
    
    lNums = laLita()
    rValor = reduce(lambda x,y: x - y, lNums)
    
    print("\nReduction of", lNums," es :",rValor,"\n")

    sleep(5)
    return

# Funcion multiplicación
def multi():

    multiMsg = " I am operation: " + multi.__name__+" "
    print(multiMsg.center(40,"*"))
    # print ("\nI am operation: ", multi.__name__)

    lNums = laLita()
    mValor = reduce(lambda x,y: x * y, lNums)
    print("\nProduct of ", lNums," es :",mValor,"\n")

    sleep(5)    
    return

# Funcion división
def divi():

    diviMsg = " I am operation: " + divi.__name__+" "
    print(diviMsg.center(40,"*"))
    # print ("\nI am operation: ", divi.__name__)

    lNums = laLita()
    try:
        dValor = reduce(lambda x,y: x / y, lNums)
        print("\nProduct of ", lNums," es :",dValor,"\n")
    except ZeroDivisionError:
        print ("There was an attempt to divide by zero, what would you like to do? \n-[0] Remove all zeros and try again \n-[1] Go back to square 1 \n-[2] Give up")
        vZDE = input("Using numbers, specify the desired operation: ")
        if vZDE == "0":
            lNumsZeroless= [i for i in lNums if i != 0]
            dValorZeroless = reduce(lambda x,y: x / y, lNums)
            print("\nProduct of ", lNumsZeroless," es :",dValorZeroless,"\n")
        if vZDE == "1":
            pass
        if vZDE == "2":
            bye()
        else:
            print("\nNow i give up...")
            bye()
    
    sleep(5)
    return

def exponen():

    exponenMsg = " I am operation: " + exponen.__name__+" "
    print(exponenMsg.center(40,"*"))
    # print ("\nI am operation: ", exponen.__name__)

    print("\nREMINDER: \nThe first number given will be taken as the base. \nThe second will be used as the power \nThe following will be used as the power to the last product \nEssentially: [2,3,4,5] => ((2^3)^4)^5  => 1152921504606846976")

    lNums = laLita()
    eValor = reduce(lambda x,y: x ** y, lNums)  
    
    print("\nProduct of ", lNums," es :",eValor)
    print("\nHOT TIP: If you see a ""+ij"", then it means the product is imaginary. \n")

    sleep(5)
    return

def rCuadrada():

    rCuadradaMsg = " I am operation: " + rCuadrada.__name__+" "
    print(rCuadradaMsg.center(40,"*"))
    # print ("\nI am operation: ", rCuadrada.__name__)

    print("\nREMINDER: \nAll numbers given will be square rooted.")

    lNums = laLita()
    sqrtValor = [number ** 0.5 for number in lNums]
    
    print("\nProduct of ", lNums," es :",sqrtValor)

    sleep(5)
    return

def NOPE():
    print ("Didn't understand you, try again! \n")
    return

def bye():
    sys.exit("GOODBYE!")

switcher = {
        0: suma,
        1: resta,
        2: multi,
        3: divi,
        4: exponen,
        5: rCuadrada,
        6: bye
    }

# El buen main...menú
def main():

    mainMsg=" MAIN MENU "

    while True:         
        print(mainMsg.center(40,"*"))
        
        print ("\nMathPy is capable of the following operations: \n-[0] ADDITION \n-[1] SUBTRACTION \n-[2] MULTIPLICATION \n-[3] DIVISION \n-[4] EXPONENTIATION \n-[5] SQUARE ROOTING \n-[6] SAY ""GOODBYE!""")
        vOpera = input("Using numbers, specify the desired operation: ")
        
        print ("\nProcessing...\n")
        
        try:
            func = switcher.get(int(vOpera), NOPE)
            print(func)
            func()

        except ValueError as e:
            print(e)
            NOPE()
        
        pass
    

if __name__ == "__main__":
    main()