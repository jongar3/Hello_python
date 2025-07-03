from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu= Menu()
coffe_machine = CoffeeMaker()
coin_machine = MoneyMachine()
while True:
    option= input(f"What would you like to order? ({menu.get_items()}): ").lower()
    if option == "report":
        coffe_machine.report()
        coin_machine.report()
    elif option== "off":
        break
    elif menu.find_drink(option) is not None:
        drink = menu.find_drink(option)
        if coffe_machine.is_resource_sufficient(drink):
            if coin_machine.make_payment(drink.cost):
                coffe_machine.make_coffee(drink)
            else:
                print("Sorry not enough money!")
        else:
            print("Resources insufficient, please refill.")
    else:
        print("Sorry that item is not available.")