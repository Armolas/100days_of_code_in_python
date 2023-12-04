import random
import os
import art
from data import data as data

player_A = data[random.randint(0, len(data) - 1)]
player_B = data[random.randint(0, len(data) - 1)]
score = 0
def compare(A, B):
    if A['follower_count'] >= B['follower_count']:
        return 'a'
    else:
        return 'b'
def prompt(player_A, player_B):
    print(f"Compare A: {player_A['name']}, a {player_A['description']}, from {player_A['country']}.")
    print(art.vs)
    print(f"Against B: {player_B['name']}, a {player_B['description']}, from {player_B['country']}.")
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    return choice
print(art.logo)
while prompt(player_A, player_B) == compare(player_A, player_B):
    os.system('clear')
    score += 1
    player_A = player_B
    player_B = data[random.randint(0, len(data) - 1)]
    print(art.logo)
    print(f"Your present score is {score}.")
os.system('clear')
print(art.logo)
print(f"Sorry wrong answer, your final score is {score}")
