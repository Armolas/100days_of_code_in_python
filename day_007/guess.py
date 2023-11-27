import random
import hangman_art as art
words = ["ardvark", "baboon", "camel", "octopus", "narwhal", "porcupine"]
lives = 7
word = random.choice(words)
word_list = []
for let in word:
    word_list.append('_')
print(art.logo)
print("Welcome to Hangman!\nCan you save him?")
print(art.hangman[lives])
print(' '.join(word_list))
while '_' in word_list and lives > 0:
    guess = input("Guess a letter: ").lower()
    i = 0
    flag = False
    while i < len(word):
        if word[i] == guess:
            if word_list[i] == guess:
                print(f"You already guessed '{guess}', guess again!")
            word_list[i] = guess
            flag = True
        i += 1
    if flag == False:
        lives -= 1
        print(f"Oops, '{guess}' is a wrong guess, Sorry!")
        print(art.hangman[lives])
    print(' '.join(word_list))
print(f"The word is {word}")
if lives > 0:
    print("You Won!!!")
else:
    print("You Lose!!!")