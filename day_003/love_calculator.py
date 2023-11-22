print("Welcome to the Love Calculator!")
name_1 = input("Enter your name: ").lower()
name_2 = input("Enter their name: ").lower()
true = 0
love = 0
name = name_1 + name_2
for letter in "true":
    true += name.count(letter)
for letter in "love":
    love += name.count(letter)
match = int(str(true) + str(love))
if match < 10 or match > 90:
    print(f"Your love score is {match}, you go together like coke an mentos!")
elif match >= 40 and match <= 50:
    print(f"Your love score is {match}, you are alright together!")
else:
    print(f"Your love score is {match}")