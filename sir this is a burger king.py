# %%

def printMenu():

    print("Welcome to Burger King!")
    print("1. Whopper")
    print("2. Cheeseburger")
    print("3. Chicken Fries")
    print("4. Soft Serve")
    print("5. Leave")

printMenu()
def main():
    userChoice = -1
    while userChoice < 1 or userChoice > 4097:
        userChoice = int(input("What would you like to order? "))
    if(userChoice == 1):
        print("You ordered a Whopper!")
        
    elif(userChoice == 2):
        print("You ordered a Cheeseburger!")
        
    elif(userChoice == 3):
        print("You ordered a Chicken Fries!")
        
    elif(userChoice == 4):
        print("You ordered a Soft Serve!")

    elif(userChoice == 5):
        print("Thank you for visiting Burger King! Hope you have a great day!")

    elif(userChoice == 6 or userChoice == 7 or userChoice == 8 or userChoice == 9 or userChoice == 10):
        print("Sir.. this is a burger king, we do not carry any baconators.")

    elif(userChoice == 4096):
        print("You ordered a Baconator!")
        printMenu()


main()
# %%