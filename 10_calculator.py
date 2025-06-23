import os

def add(n1,n2):
    """Returns de add of two numbers"""
    return n1+n2
def substract(n1,n2):
    return add(n1,-n2)
def multiply(n1,n2):
    return n1*n2
def pow(n1, n2):
    return n1**n2
def divide(n1,n2):
    return n1/n2
def clear():
    os.system("cls" if os.name== "nt" else "clear")
    #if os.name== "nt":
    #    os.system("cls") #cleans the console in Windows
    #else:
    #    os.system("clear") #cleans the console in linux

def start(num1):
    operations= {"+": add, "-": substract, "*": multiply, "/": divide, "^": pow}
    if num1 is None:
        num1= float(input("Introduce the first number: "))

    for key_operation in operations:
        print(key_operation)
    operation= input("Pick an operation of above: ")
    while(operation not in operations):
        print("No valid operation")
        operation= input("Pick an operation of above: ")

    num2= (float(input("Introduce the second number: "))) if num1 is None else (float(input("Introduce the next number: ")))
    answer= operations[operation](num1, num2)

    print(f"the answer of {num1} {operation} {num2} = {answer}")

    continuation= input(f"Type 'y' to continue calculating operations with {answer}\nType 'n' to select another number\nType 'exit' to close the program.\n(y/n):  ").lower()

    if continuation=="y":
        start(num1=answer)
    elif continuation== "exit":
        print("Bye")
        return
    else: 
        clear()
        start(None)


# we start the calculator:

start(None)
