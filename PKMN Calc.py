# %%
basePower = int(input("Base power: "))
atk = int(input("Attacking stat: "))
defence = int(input("Defending stat: "))
hp = int(input("Opponent's total HP: "))
level = int(input("What level are you?: "))
additionalMultiplyers = int(input("Any additional multiplyers? (answer in numbered form, type 1 for no): "))

minRoll = ((((((((((2 * level) / 5) + 2) * basePower * atk / defence) / 50) + 2) * additionalMultiplyers) / hp) * .85) * 100) 
maxRoll = (((((((((2 * level) / 5) + 2) * basePower * atk / defence) / 50) + 2) * additionalMultiplyers) / hp) * 100)

print(minRoll)
print("to")
print(maxRoll)
print("Percent!")
print("Results may be off by a few percent.")


# %%