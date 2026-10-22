# %%
width = 2.544
height = 3.55
area = (width * height)
par = (width * 2 + height * 2)

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

        print("The Area is ", 2.544 * 3.55)
        print("The paramiter is ", 2.544 * 2 + 3.55 *2)        

        a()

        width = 2
        height = 5

        a()

        width = 10
        height = 10

        a()

            
        if(userChoice == 2):
            print("You ordered a Cheeseburger!")
            
        if(userChoice == 3):
            print("You ordered a Chicken Fries!")
            
        if(userChoice == 4):
            print("You ordered a Soft Serve!")

        if(userChoice == 5):
            print("Thank you for visiting Burger King! Hope you have a great day!")

        if(userChoice == 6 or userChoice == 7 or userChoice == 8 or userChoice == 9 or userChoice == 10):
            print("Sir.. this is a burger king, we do not carry any baconators.")

        if(userChoice == 4096):
            print("You ordered a Baconator!")
            printMenu()


main()
# %%