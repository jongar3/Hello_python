print("Welcome to FizzBuzz game")

for j in range(1,101):
    if (j%3==0 and j%5==0): #equal to j%15
        print("FizzBuzz")
    elif j%5==0:
        print("Buzz")
    elif j%3==0:
        print("Fizz")
    else:
        print(j)

