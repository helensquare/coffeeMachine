MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "coffee": 100
}


def check_resources(drink_ingredients):
    """Returns True if there are enough ingredients to make the drink, False if not"""
    is_enough = True
    for item in drink_ingredients:
        if drink_ingredients[item] >= resources[item]:
            print(f"Sorry, {item} insufficient.")
            is_enough = False
            return is_enough
    return is_enough


def process_coins():
    """Returns total of the coins inserted"""
    print("Please insert coins.")
    quarters = float(input("How many quarters? ")) * 0.25
    dimes = float(input("How many dimes? ")) * 0.10
    nickles = float(input("How many nickles? ")) * 0.05
    pennies = float(input("How many pennies? ")) * 0.01
    total = quarters + dimes + nickles + pennies
    return total


def transaction_successful(cost, money_paid):
    """Returns True if money inserted is enough, False if not."""
    change = round(money_paid - cost, 2)
    is_successful = True
    if cost > money_paid:
        is_successful = False
    elif cost == money_paid:
        print("Exact amount inserted. No change required.")
    else:
        print(f"Your change is ${change}.")
    return is_successful


def make_coffee(resources, chosen_drink):
    """Deduct the used ingredients from the resources"""
    resources["water"] = resources["water"] - drink["ingredients"]["water"]
    resources["milk"] = resources["milk"] - drink["ingredients"]["milk"]
    resources["coffee"] = resources["coffee"] - drink["ingredients"]["coffee"]
    print(f"Here is your {chosen_drink}! ☕")


machine_on = True

while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        print("Turning machine off...")
        machine_on = False
    elif choice == "report":
        print(f'''
            Water: {resources["water"]}ml
            Milk: {resources["milk"]}ml
            Coffee: {resources["coffee"]}g
            Money: ${profit}
        ''')
    else:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            money_inserted = process_coins()
            cost_drink = drink["cost"]
            if transaction_successful(cost_drink, money_inserted):
                profit += cost_drink
                make_coffee(resources, choice)
            else:
                print("Sorry, money inserted is not enough. Money refunded.")

