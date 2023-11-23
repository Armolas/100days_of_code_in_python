import random

print("Welcome to Banker Roulette!\nLet's find out who's paying today.")
names = input("Give me everybody's name, separated by a comma and a space.\n").split(", ")

payer = random.randint(0, len(names) - 1)
print(f"{names[payer]} is going to buy the meal today!\nThank you {names[payer]}! :)")