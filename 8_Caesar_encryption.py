def encrypt(text, shift):
    l= len(text)
    l_text=list(text)
    for letter in l_text:
        if not letter in alphabet:
            print(letter, end="")
            continue
            
        initial_pos= alphabet.index(letter)
        pos_shift= initial_pos+shift
        while(pos_shift>alphabet_len):
            pos_shift= pos_shift-alphabet_len #this while is equivalent to pos_shift= pos_shift%len(alphabet)
        
        print(alphabet[pos_shift], end="")
    print()

def decrypt(plain_text, d_shift):
    while d_shift>len(alphabet):
        d_shift-=len(alphabet)
    encrypt(plain_text, -d_shift)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_len= len(alphabet)
end=False
while(not end):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction== "encode":
        print("the encode text is:", end=' ')
        encrypt(text, shift)
    elif direction== "decode":
        print("the decoded text is:", end=' ')
        decrypt(text, shift)
    else: 
        print("no valide argument!")
    
    again= input("Do you want to go again? (type yes or no): ").lower()
    if again!="yes":
        end=True
        break
