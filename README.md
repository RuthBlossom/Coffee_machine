
# Coffee Machine

This is a simple coffee machine program implemented in Python. The program allows users to order different types of coffee, process payments, and check the machine's resource status.

## Features

- **Menu Options**: The coffee machine offers three types of coffee:
  - Espresso
  - Latte
  - Cappuccino
- **Resource Management**: The machine keeps track of its resources (water, milk, coffee) and ensures there are sufficient ingredients to make the selected coffee.
- **Payment Processing**: Users can insert coins (quarters, dimes, nickels, pennies) to pay for their order. The machine calculates the total amount inserted and checks if it's sufficient for the selected coffee.
- **Transaction Handling**: If the payment is successful, the machine provides change if needed, updates the profit, and deducts the used resources.
- **Reporting**: Users can request a report to see the current resource levels and total profit.
- **Machine Control**: The machine can be turned off by the user.

## How to Run

1. **Clone the Repository**:
   Clone the repository to your local machine using:
   ```bash
   git clone <repository-url>
   ```
   
2. **Navigate to the Project Directory**:
   ```bash
   cd coffee-machine
   ```
   
3. **Run the Program**:
   ```bash
   python coffee_machine.py
   ```

## Program Details

- **MENU**: A dictionary containing the coffee options, their ingredients, and costs.
- **resources**: A dictionary storing the initial amount of resources available in the machine.
- **profit**: A variable to keep track of the total profit.

### Functions

1. **is_resource_sufficient(order_ingredients)**:
   - Checks if there are enough resources to fulfill the order.
   - Returns `True` if resources are sufficient, otherwise `False`.

2. **process_coins()**:
   - Prompts the user to insert coins and calculates the total amount.
   - Returns the total amount of money inserted.

3. **is_transaction_successful(money_received, drink_cost)**:
   - Checks if the payment is sufficient for the selected coffee.
   - Returns `True` if the transaction is successful, otherwise `False`.

4. **make_coffee(drink_name, order_ingredients)**:
   - Deducts the required ingredients from the resources and prints a message indicating the coffee is ready.

### Main Loop

- The program runs in a loop, continuously asking the user for their choice of coffee.
- The user can:
  - Select a coffee (`espresso`, `latte`, `cappuccino`)
  - Request a resource report by typing `report`
  - Turn off the machine by typing `off`

## Example Usage

![Capture Coffee machine](https://github.com/user-attachments/assets/f11d1d73-c3d3-49f6-9691-6bdbacdcd869)


```bash
What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickels?: 0
How many pennies?: 0
Here is your change: $7.5
Here is your latte 🤎☕

What would you like? (espresso/latte/cappuccino): report
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
```

- Inspired by the Python bootcamp by Dr. Angela Yu on Udemy.
