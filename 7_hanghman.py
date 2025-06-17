import random
from hanghman_art import stages
print("Welcome to hanghman!")
word_list = ["aardvark", "baboon", "camel"]
word= random.choice(word_list)
n= len(word)
user_word= ["_"]*n
lives=6

while(1):
    print(stages[lives])   
    print(" ".join(user_word))      #join transforms a list in a str putting a "whaterver" spaces between them
    guess= input("\nSelect a letter to guess: ").lower()

    if (guess in word) and (guess in user_word):
        print("you have already guessed that letter")
        continue
    elif guess in word:
        for j in range(0, n):
            #print(f"{j+1} is {guess==word[j]}")
            if guess==word[j]:
                user_word[j]=guess
        print("\n" * 100) #For ""cleaning"" the console
    else:
        print("You fail, you loose 1 life")
        lives-=1

    if "_" not in user_word:
        print("congratulations you WON!")
        print("the worde was: "+"".join(user_word))
        break

    if lives<=0:
        print(stages[0]+ "\nYOU LOOSE!")
        print("The word was "+word+".")
        break

