print("Tip calculator program")
cuenta=float(input("what was te total bill (€)?: "))

propina= float(input("introduce the the tip(%)?: "))
personas= int(input("introduce the number of people?: "))

total_per_person= (cuenta+ (propina*cuenta)/100)/personas


#print(f"eache person must pay {"{:.2f}".format(round(total_per_person,2))}")
#Equivalentemente
print("Each person musta pay "+ "{:.2f}".format(round(total_per_person,2)))

