
from data import coffe_emoji, initial_resources, drinks
resources = initial_resources
option=None
coins= [5, 10, 20, 50, 100, 200]

def print_report():
    for resource in resources:
        print(f"{resource}: {resources[resource]}", end= " ")
    print()
def check_resources(option):
        ingredients = drinks[option]["ingredients"]
        for ingredient in ingredients:
            if ingredients[ingredient]> resources[ingredient]:
                print(f"Sorry there is not enough {ingredient}, please refill the machine.")
                return False
        return True
def serve_drink(option, resources):
    ingredients = drinks[option]["ingredients"]
    for ingredient in ingredients:
        resources[ingredient]-= ingredients[ingredient]
    print(f"Enjoy you {option}! {coffe_emoji}")

while option!= "off":
    introduced_value=0
    option= input("What would you like to order (espresso/latte/cappuccino)?").lower()

    if option== "report":
        print_report()
    elif option== "off":
        break
    elif drinks.get(option) is None:
        print("No valid drink.")
    else:
        if check_resources(option):
            print(f"You choose {option} it costs {drinks[option]["cost"]} \n Please introduce the coins:")
            for coin_value in coins:
                introduced_value += int(input(f"How many {coin_value/100 if coin_value%100==0 else coin_value}{"€" if coin_value%100==0 else "cents"} would you like to introduce?"))*coin_value

            if introduced_value >= drinks[option]["cost"]*100:
                refund=-(drinks[option]["cost"]*100 - introduced_value)
                serve_drink(option, resources)
                print(f"Your refund: {refund/100}€")
            else:
                print("Not enough money! Refund")
