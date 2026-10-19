print("hello world")

# there are 4 data types that we need to know

print(type(7))
print(type(.0))
print(type("april"))
print(type(True))

# variable = a named spot in ram

varOne = 5
varTwo = 5.0
varThree = "Five"
varFour = "True"

print(varOne + varTwo)
# changing a data type
print(varThree + str(varTwo))

#def stars a function. a function is something that you can run over and over

#paramiters are things you can "pass" into a function

def addTwo(numOne, numTwo):
    print(numOne + numTwo)

def multiplyTwo(numThree, numFour):
    print(numFour * numFour)

def divideTwo(numFive, numSix):
    print(numFive / numSix)
    
def subtractTwo(numSeven, numEight):
    print(numSeven - numEight)
    
addTwo(4, 5)
addTwo(750, 13)
multiplyTwo(217, 8)
multiplyTwo(16, 3)
divideTwo(200, 4)
divideTwo(80, 8)
subtractTwo(8176, 187)
subtractTwo(6187, 1524)


def mpg(miles, gallons):
    print(miles/gallons)

mpg(50, 2.4)

def tax(money, tax):
    print(money * tax)

tax(5.99, 1.10)

    


