print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
      ''')
print("Welcome to Treasue Island!")
print("Your mission is to find the treasure.")
crossroad = input("You are at a crossroad, where would you like to go? \
type 'left' or 'right'\n").lower()
if crossroad == "left":
      lake = input("You come across a lake, type 'wait' to wait for a boat or type 'swim' to swim across\n").lower()
      if lake == 'wait':
            print("You arrived safely on the Island.")
            print("You came across a house with 3 doors. Red, Yellow and Blue.")
            door = input("Which door would you like to go through?\n").lower()
            if door == 'yellow':
                  print("Congratulations!, you found the treasure.")
            elif door == "red":
                  print("You Entered a room full of snakes!\nGAME OVER!!!")
            elif door == "blue":
                  print("You Entered a room full of beasts!\nGAME OVER!!!")
      elif lake == 'swim':
          print("You got caught by a crocodile!\nGAME OVER!!!")
elif crossroad == 'right':
      print("You fell into a big hole!\nGAME OVER!!!")