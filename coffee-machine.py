MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def order_resources(order_ingredients):
    """compares items ingredients to those in stock"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True


def is_transaction_success(money_received, drink_cost):
    """returns true when payment is sucessful"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change:${change}.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry thats not enough. Money refunded.")
        return False


def process_coins():
    """calculates total amount povided by customer"""
    total = int(input("How many quarters?")) * .25
    total += int(input("How many dimes?")) * .1
    total += int(input("How many nickels?")) * .05
    total += int(input("How many pennies?")) * .01
    return total


def make_coffee(drink_name, order_ingredients):
    """deduct ingredients from resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}.")


is_on = True

while is_on:
    choice = input('What would you like?').lower()
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if order_resources(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_success(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

# TODO: 1. Print report of resources. X
# TODO: 2. Check resources are sufficient X
# TODO: 3. Process coins
# TODO: 4. check transaction successful?
# TODO: 5. Make coffee
