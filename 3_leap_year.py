print("Leap year checker")

#print("Angela".lower().count("a")) .lower() the capital a lower letters, count cuenta el numero de "a"s

year= int(input("introduce the year you want to check: "))

if (year%4==0):
    if (year%100==0 and year%400==0 ):
        print("Leap year!")
    elif(year%100==0):
        print("No leap year!")
    else: 
        print("Leap year!")

else: 
    print("No leap year!")    


