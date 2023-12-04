import random

def guess(number, lives):
    print(f"You have {lives} attempts.")
    guess = int(input("Make a guess: "))
    lives -= 1
    while guess != number and lives > 0:
        print("-------------------------------\n")
        print(f"You have {lives} attempt(s) remaining.")
        if guess > number:
            guess = int(input("Too high, try again: "))
        else:
            guess = int(input("Too low, try again: "))
        lives -= 1
    print("-------------------------------\n")
    if lives == 0:
        print(f"Oops!, you ran out of attempts. Game Over!!!\nThe number was {number}")
    else:
        print(f"You rock!!!\nThe number was {number}")

number = random.randint(1, 101)
print("Welcome to Number Guessing Game!!!")
print("I'm thinking of a number between 1 and 100, can you guess the number?")
diff = input("Choose your difficulty, type 'easy' or 'hard': ").lower()
if diff == 'easy':
    guess(number, 10)
elif diff == 'hard':
    guess(number, 5)
