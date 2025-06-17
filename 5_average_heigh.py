heigh_list=(input("inroduce the a list with heihgs\n").split(" "))
print(heigh_list)
l=0
total= 0

for heigh in heigh_list:
    total+=int(heigh)
    l+=1
total/=l
print(f"the average heigh is {total}")
