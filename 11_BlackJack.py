import random
import os
print("Welcome to blackjack")
#c =clubs; h= hearts; s= spades; d= diamonds
def clear():
    os.system("cls" if os.name=="nt" else "clear")
def define_cards():
    cards= {}
    clubs= ["c", "h", "s", "d"]
    names= ['A', '2','3','4','5','6','7','8','9','10', "J", "Q", "K"]
    values= [11, 2, 3, 4, 5, 6, 7, 8, 9] + [10]*4
    for c in clubs:
        for pos in range(0, len(names)):
            cards[names[pos]+c]= values[pos]
    #print(cards)
    return(cards)

def return_card(cards):
    k= random.choice(list(cards.keys()))
    card= {k: cards.pop(k)} #the dictionaries are mutables
    #print(card)
    return(card)
def value(hand):
    return(sum(list(hand.values())))
def add_card(hand, cards):
    card= return_card(cards)
    hand[list(card.keys())[0]]= list(card.values())[0]
def print_hand(hand):
    for card in hand:
        print(card, end=' ')
    print()
def correct_ace(hand):
    for card in hand:
        if hand[card]==11 and value(hand)>21:
            hand[card]=1

def compare(player_hand, computer_hand):
    correct_ace(computer_hand)
    if value(player_hand)>21:
        print("You loose")
    elif value(computer_hand)>21:
        print("You Win!")
    elif value(player_hand)> value(computer_hand):
        print("You Win!")
    elif value(player_hand)< value(computer_hand):
        print("You loose!")
    else:
        print("You draw")

play_again='y'
while(play_again== "y"):
    clear()
    cards= define_cards() #We define the deck

    #We get the first hand
    computer_hand= return_card(cards)
    add_card(computer_hand, cards)
    player_hand= return_card(cards)
    add_card(player_hand, cards)

    print(f"Computer hand: {list(computer_hand.keys())[0]} ?")
    print("Your hand is: ", end='')
    print_hand(player_hand)
    player_values= value(player_hand)
    print(f"Your total values is {player_values}")

    option=input("Type 'y' to add a card Type 'n' to stand: ").lower()
    while(option== 'y'):
        add_card(player_hand, cards)
        correct_ace(player_hand) #as player_hand is mutable is not necessary to return anything in the function
        print("Your hand is: ", end='')
        print_hand(player_hand)
        print(f"Your total values is {value(player_hand)}")
        if value(player_hand)>21:
            break #you loose!
        option= input("Type 'y' to add a card Type 'n' to stand: ").lower()
    clear()
    print("computer hand is: "); print_hand(computer_hand)

    while(value(computer_hand)<17):
        print("Computer adds a card")
        add_card(computer_hand, cards=cards)
        correct_ace(computer_hand) #we supose that for example with an Ace and a seven the computer would get 18 so it can't take a card (18>17)

    print("Your hand is: ", end=''); print_hand(player_hand); print(f"A total value of {value(player_hand)}")
    print("Computers hand is: ", end=''); print_hand(computer_hand); print(f"A total value of {value(computer_hand)}")
    compare(player_hand, computer_hand)
    play_again=input("Do you want to play again? ('y'/'n'): ").lower()

print("Bye!")