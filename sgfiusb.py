# %%
width = 2.544
height = 3.55
area = (width * height)
par = (width * 2 + height * 2)

import random

dieOne = 0
dieTwo = 0
double = 0
two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0
eight = 0
nine = 0
ten = 0
eleven = 0
twelve = 0

def a():
        width = int(input("Width: "))
        height = int(input("Height: "))
        area = (width * height)
        par = (width * 2 + height * 2)
        print("The Area is ",area)
        print("The paramiter is ",par)

def printMenu():

    print("Welcome to Burger King!")
    print("1. Math stuff like area :/")
    print("2. Golf Nerd")
    print("3. More meth stuff")
    print("4. Soft Serve")
    print("5. Leave")

printMenu()
def main():
    userChoice = -1
    while userChoice < 1 or userChoice > 4097:
        userChoice = int(input("What would you like to order? "))
    if(userChoice == 1):
        def math():
            print("The Area is ", 2.544 * 3.55)
            print("The paramiter is ", 2.544 * 2 + 3.55 *2)        

        math()

        width = 2
        height = 5

        math()

        width = 10
        height = 10

        math()

            
    if(userChoice == 2):
            hole = int(input("What hole are you on? "))
            par = int(input("Par on the hole? "))
            stroke = int(input("How many strokes did it take you? "))

            sOne = ''

            def a():
                if par == stroke:
                    sOne = "Even Par"
                elif par - 1 == stroke:
                    sOne = "Birdie"
                elif par - 2 == stroke:
                    sOne = "Eagle"
                elif par - 3 == stroke:
                    sOne = "Albatross"
                elif par - 4 == stroke:
                    sOne = "Condor"
                elif par - 5 == stroke:
                    sOne = "Ostrich"
                elif par - 5 > stroke:
                    sOne = "The Goat" 
                elif par + 1 == stroke:
                    sOne = "Bogey"
                elif par + 2 == stroke:
                    sOne = "Double Bogey"
                elif par + 3 == stroke:
                    sOne = "Triple Bogey"
                elif par + 4 == stroke:
                    sOne = "4 Over Par"
                elif par + 5 == stroke:
                    sOne = "5 Over Par"
                else:
                    sOne = "How ;-;" 
                return sOne

            aNumber = ''

            def b():
                if stroke == 1:
                    aNumber = "Hole in One"
                elif stroke == 4:
                    aNumber = "Sailboat"
                elif stroke == 8:
                    aNumber = "Frosty"
                elif stroke == 10:
                    aNumber = "Bo Derek"
                else:
                    aNumber = ''
                return aNumber

            beagle = ''
            def c():
                if stroke == par * 2:
                    beagle = "a Beagle!"
                else:
                    beagle = ''
                return beagle 

            a()
            b()
            c()

            sOne = a()
            aNumber = b()
            beagle = c()

            print("On hole #", hole, "A par", par, "hole, you shot a ", sOne, "With a ", aNumber,  beagle)

    if(userChoice == 3):
            intOne = int(input("Enter Starting Number: "))
            intTwo = int(input("Enter Ending Number: "))

            def meth():
                total = 0
                for i in range (intOne, intTwo + 1):
                    if i % 3 != 0 and i % 4 != 0 and i % 5 != 0:
                        total += i


                return total

            total = meth()

            print("Starting Number:", intOne)
            print("Ending Number:", intTwo)
            print("Total:", total)   

    if(userChoice == 4):
        count = int(input("How many die rolls? "))

        def eval():
            global double, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve
            if dieOne == dieTwo:
                double += 1

            if dieOne + dieTwo == 2:
                two += 1

            if dieOne + dieTwo == 3:
                three += 1

            if dieOne + dieTwo == 4:
                four += 1

            if dieOne + dieTwo == 5:
                five += 1

            if dieOne + dieTwo == 6:
                six += 1

            if dieOne + dieTwo == 7:
                seven += 1

            if dieOne + dieTwo == 8:
                eight += 1

            if dieOne + dieTwo == 9:
                nine += 1

            if dieOne + dieTwo == 10:
                ten += 1

            if dieOne + dieTwo == 11:
                eleven += 1

            if dieOne + dieTwo == 12:
                twelve += 1


        def roll():
            global dieOne, dieTwo
            for i in range(count):
                dieOne = random.randint(1, 6)
                dieTwo = random.randint(1, 6)
                eval()

        roll()

        print("2 -", two, ((two / count) * 100),"%")
        print("3 -", three, ((three / count) * 100),"%")
        print("4 -", four, ((four / count) * 100),"%")
        print("5 -", five, ((five / count) * 100),"%")
        print("6 -", six, ((six / count) * 100),"%")
        print("7 -", seven, ((seven / count) * 100),"%")
        print("8 -", eight, ((eight / count) * 100),"%")
        print("9 -", nine, ((nine / count) * 100),"%")
        print("10 -", ten, ((ten / count) * 100),"%")
        print("11 -", eleven, ((eleven / count) * 100),"%")
        print("12 -", twelve, ((twelve / count) * 100),"%")
        print("Doubles -", double, ((double / count) * 100),"%") 
        
main()
# %%