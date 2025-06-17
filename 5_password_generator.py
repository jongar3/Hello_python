import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

size= nr_letters+nr_symbols+nr_numbers

password= list(range(0, size))
positions= random.sample(password, nr_numbers+ nr_symbols) #eligo las posiciones a cambiar
#print(positions)
for j in range(0, size):
    password[j]=random.choice(letters) 

for j in range(0, nr_numbers+nr_symbols):
    if j<nr_symbols:
        password[positions[j]]= random.choice(symbols)
    else:
        password[positions[j]]= random.choice(numbers)

print(f"The generated password is:")
password_char=""
for j in password: 
    password_char+= j
print(password_char)

 #NOTE: maybe it is easier to do it with shuffle(password) function