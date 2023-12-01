import random
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
card_names = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
card_list = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
deck = [(card, category) for category in card_names for card in card_list]
def card_value(card):
    if card[0] in ['Jack', 'Queen', 'King']:
        return 10
    elif card[0] == 'Ace':
        return 11
    else:
        return int(card[0])
def card_sum(card_deck):
    add = 0
    for card in card_deck:
        add += card_value(card)
    return add
random.shuffle(deck)
player_cards = [deck.pop(), deck.pop()]
dealer_cards = [deck.pop(), deck.pop()]
print(logo)
while True:
    player_score = card_sum(player_cards)
    dealer_score = card_sum(dealer_cards)
    print(f"Player cards: {player_cards}")
    print(f"Player score: {player_score}")
    print("\n-----------------------------")
    choice = input("Pick your poison, type 'hit' to request a card or 'hold' to hold\n").lower()
    if choice == 'hit':
        player_cards.append(deck.pop())
        player_score = card_sum(player_cards)
    elif choice == 'hold':
        break
    else:
        print("Invalid choice, please type either 'hold' or 'hit': ")
        continue

    if player_score > 21:
        print(f"Dealer has {dealer_cards}")
        print(f"Dealer score: {dealer_score}")
        print(f"Player has {player_cards}")
        print(f"Player score: {player_score}")
        print("Player's cards is exceeding 21, Dealer wins :(")
        exit()
while dealer_score < 17:
    dealer_cards.append(deck.pop())
    dealer_score = card_sum(dealer_cards)
print("\n-----------------------------")
if dealer_score > 21:
    print(f"Dealer has {dealer_cards}")
    print(f"Dealer score: {dealer_score}")
    print(f"Player has {player_cards}")
    print(f"Player score: {player_score}")
    print("Dealer's cards is exceeding 21, Player wins :)")
elif player_score > dealer_score:
    print(f"Dealer has {dealer_cards}")
    print(f"Dealer score: {dealer_score}")
    print(f"Player has {player_cards}")
    print(f"Player score: {player_score}")
    print("Player's score is higher than dealer's score, Player wins :)")
elif dealer_score > player_score:
    print(f"Dealer has {dealer_cards}")
    print(f"Dealer score: {dealer_score}")
    print(f"Player has {player_cards}")
    print(f"Player score: {player_score}")
    print("Dealer's score is higher than player's score, Dealer wins :(")
else:
    print(f"Dealer has {dealer_cards}")
    print(f"Dealer score: {dealer_score}")
    print(f"Player has {player_cards}")
    print(f"Player score: {player_score}")
    print("Player's score is equal to dealer's score, It's a tie!!!")
