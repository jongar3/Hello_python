import random
print('Welcome to "guess the number: "')

difficulty= ""
while(not (difficulty=="easy" or difficulty=="hard" )):
    difficulty= input("Type 'easy' or 'hard' to choose difficulty: ").lower()

if difficulty=="easy":
    attemps=10
else:
    attemps=5

print("Guess the number from 0 to 100")
number= random.randint(0,100)
while attemps>0:
    print(f"You have {attemps} attemps left.")
    guess= int(input("Introduce a number: "))
    if guess<number:
        print("To low")
        attemps-=1
    elif guess>number:
        print("To high")
        attemps-=1
    else:
        print("You win!", end=" ")
        break

if attemps<=0:
    print("You loose!", end=" ")
print(f"The number was {number}")