import os

def clear():
    if os.name== "nt":
        os.system("cls") #cleans the console in Windows
    else:
        os.system("clear") #cleans the console in linux

clear() 
print("Welcome to secret auction program")
end=False
total={}
while(not end):
    name= input("What is your name?: ")
    bid= round(float(input("What is yout bid? (€): ")),2)
    new_name=name
    count=0
    while(new_name in total):
        count+=1
        new_name= name+str(count) #in case there are some with the same name.
    total[new_name]= bid
    while(1):
        menu= input("Are ther any other bidders? (type 'yes' or 'no'): ").lower()
        if (menu== 'yes'):
            clear()
            end= False
            break
        elif (menu == 'no'):
            end= True
            break
        else:
            print("No valid argument")
    
maxi=max(total, key= total.get) #gets the maximum of .get and returns the key of total
print(f"{maxi} is the winner with {total[maxi]:.2f}€")