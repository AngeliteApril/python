# %%

def printMenu():

    print("Statistics!")
    print("1. Add value to List")
    print("2. Delete Value From List (by value)")
    print("3. Delete Value From List (by location in list)")
    print("4. Display List")
    print("5. Compute Mean")
    print("6. Compute Median")
    print("7. Compute Midpoint")
    print("8. Compute Mode(s)")
    print("9. Compute Standerd Deviation")

printMenu()
def main():
    userChoice = -1
    while userChoice < 1 or userChoice > 4097:
        userChoice = int(input("What would you like to do? "))
    if(userChoice == 1):
        print("Add value to list")
        
    elif(userChoice == 2):
        print("You ordered a Cheeseburger!")
        
    elif(userChoice == 3):
        print("You ordered a Chicken Fries!")
        
    elif(userChoice == 4):
        print("You ordered a Soft Serve!")

    if(userChoice == 5):
        print("You ordered a Whopper!")
        
    elif(userChoice == 6):
        print("You ordered a Cheeseburger!")
        
    elif(userChoice == 7):
        print("You ordered a Chicken Fries!")
        
    elif(userChoice == 8):
        print("You ordered a Soft Serve!")

    if(userChoice == 9):
        print("You ordered a Whopper!")
        
    elif(userChoice == 0):
        print("Byeee~")

main()

# %%
