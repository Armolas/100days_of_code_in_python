import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
print("Rock Paper Scissors!\nCan you beat me?")
play = int(input("type '0' for rock, '1' for paper and '2' for scissors: "))
if play == 0:
    print(rock)
elif play == 1:
    print(paper)
elif play == 2:
    print(scissors)
computer = random.randint(0, 2)
print(f"Computer chose {computer}")
if computer == 0:
    print(rock)
elif computer == 1:
    print(paper)
elif computer == 2:
    print(scissors)
if play == computer:
    print("It's a draw! :|")
elif play == 0 and computer == 2:
    print("You Win! :)")
elif play == 1 and computer == 0:
    print("You Win! :)")
elif play == 2 and computer == 1:
    print("You Win! :)")
else:
    print("You Lose! :(")