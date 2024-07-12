# Define a menu with different coffee options, each with ingredients and cost.
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

# Initialize the profit and available resources (water, milk, and coffee).
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Define a function to check if there are enough resources for a given order.
def is_resource_sufficient(order_ingredients):
    """Returns True when the order can be made, False if ingredients are insufficient."""
    is_sufficient = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}.")
            is_sufficient = False
    return is_sufficient

# Define a function to process coins and return the total amount.
def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

# Define a function to check if a transaction was successful based on the payment and cost.
def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment was successful, False if insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change: ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

# Define a function to make a coffee by deducting required ingredients from resources.
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from resources and make a coffee."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} 🤎☕")

# Set a flag to control the main loop.
is_on = True

# Main loop for processing user input.
while is_on:
    # Ask the user for their coffee choice.
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    # Check user input and perform corresponding actions.
    if choice == "off":
        # Turn off the coffee machine.
        is_on = False
    elif choice == "report":
        # Print a report showing available resources and profit.
        print(resources)
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        # Process the user's coffee order.
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

#Uppercase Letters: Variables in all uppercase letters are considered constants, indicating that their values should not be modified during the program's execution.

#Lowercase Letters: Variables in lowercase letters are typically used for regular variables whose values can be modified during the program's execution.

