import random
from game_data import logo, vs, data
import os 
def clear():
    os.system("cls" if os.name=="nt" else "clear")

def print_d(d):
    print(f"{d["name"]}, a {d["description"]} from {d["country"]}")

def define_second_d(d1):
    d2= random.choice(data)
    while(d2==d1):
        d2= random.choice(data)
    return d2

def ask_win(option, d1, d2):
    if option=='A':
        if d1["follower_count"]>= d2["follower_count"]:
            return True
        else:
            return False
    elif option =='B':
        if d1["follower_count"]> d2["follower_count"]:
            return False
        else:
            return True
    return None
score=0
def main(d1): 
    global score
    print(logo)
    if d1 is None:
        score=0
        d1= random.choice(data)
    d2= define_second_d(d1)
    print("option A",end=': ')    
    print_d(d1)
    print(vs)
    print("Option B", end= ': ')
    print_d(d2)
    option= input("Introduce A or B: ").upper()
    if ask_win(option, d1, d2):
        score+=1
        clear()
        print(f"Good job! your actual score is {score}")
        main(d2)

    else:
        clear()
        print(f"you loose! with a score of {score}")
        if ('y' == input("Play again 'y' or 'n': ").lower()):
            clear()
            main(None)
        else:
            return


main(None)