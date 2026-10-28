# %%

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

    return double

def roll():
    global dieOne, dieTwo
    for i in range(count):
        dieOne = random.randint(1, 6)
        dieTwo = random.randint(1, 6)
        eval()

double = eval()
two = eval()
three = eval()
four = eval()
five = eval()
six = eval()
seven = eval()
eight = eval()
nine = eval()
ten = eval()
eleven = eval()
twelve = eval()

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


# %%
