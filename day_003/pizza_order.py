print("Welcome to Armolas Pizza Deliveries")
size = input("What size if pizza do you want? \
Type S for small, M for Medium or L for large? ")
bill = 0
if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
elif size == 'L':
    bill += 25
else:
    print("Please Enter 'S' for small, 'M' for medium or 'L' for large")
    exit()
pepperoni = input("Do you want pepperoni? Y for yes, N for no? ")
extra_cheese = input("Do you want extra cheese? Y for yes, N for no? ")
if pepperoni == 'Y':
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == 'Y':
    bill += 1
print(f"Your final bill is ${bill}.\nThank you and come back soon :)")