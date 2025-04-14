# Final Capstone Project: <br> Change Calculator: Breakdown of Payment

This Python script calculates the change to be returned to the customer based on the amount paid and the cost of a product. It breaks down the change into the fewest coins possible, including dollars, quarters, dimes, nickels, and pennies.

## Requirements

This script does not require any external libraries. It is written in plain Python and can be run directly in any Python environment.

## Script Functionality

### `compute_change(cost, paid)`
This function calculates the change that needs to be returned to the customer. It works as follows:
- It first calculates the total change in cents (difference between the amount paid and the cost).
- It then breaks down the change into the fewest number of coins, including dollars, quarters, dimes, nickels, and pennies.
- The function returns a string that lists the number of each coin denomination.

### Example Usage

1. The user inputs the cost of the product and the amount paid.
2. If the paid amount is less than the cost, the program asks the user to input a correct value until the paid amount is greater than the cost.
3. Once a valid paid amount is provided, the program calculates the change and prints out the breakdown in terms of coins.

### Example

```bash
Enter the cost of the product: 8.77
Enter the amount you paid: 10
Change breakdown: dollars: 1, quarters: 4, pennies: 23
