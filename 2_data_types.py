#STRINGS

string= "data" + " type"
print(string[0])

#INTEGER    

inter= 12+1
print(123_123_12)

#Float

floating=3_141.2131
print(floating)

#BOOL

print(True == 1)

#f-stings

print(f"el float es: {floating} el entero es {inter}")

#################################
print(str(float(int("2"))))

print(2**3) #exponential

# lists 

lista=["Hola", 3, "Hello"]

matriz= [[1,2],[3,4]] #list inside a list

print([1,2] in matriz)

print(matriz[0][1])

print(len(matriz))

#dictionaries dictionary={key: value}

programming_dictinary= {
"Bug": "An error in the program",
"Function": "A piece of code that can easily be calle",
}
print(programming_dictinary["Bug"])
    #Adding another element
programming_dictinary["Loop"]= "Doing something over and over again"
print(programming_dictinary)
for thing in programming_dictinary:
    print(thing) #thing= key