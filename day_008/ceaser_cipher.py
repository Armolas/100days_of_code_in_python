letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def cipher(message, shift, direction):
    cipher = ""
    for let in message:
        if not let.isalpha():
            cipher += let
            continue
        index = letters.index(let)
        if direction == "encode":
            cipher += letters[index + shift]
        elif direction == "decode":
            cipher += letters[index + 26 - shift]
        else:
            print("Wrong direction. please type either 'encode' or 'decode'")
    print(f"Your {direction}d message is '{cipher}'")
flag = True
while flag:
    message = input("Enter your message:\n")
    shift = int(input("Enter the shift number: "))
    while shift > 25:
        print("Shift overflow, lease enter a value below 26")
        shift = int(input("Enter the shift number: "))
    direction = input("Type 'encode' to encrypt, or 'decode' to decrypt: ")
    cipher(message, shift, direction)
    again = input("Do you want to go again? Type 'yes' or 'no': ").lower()
    if again == 'no':
        flag = False