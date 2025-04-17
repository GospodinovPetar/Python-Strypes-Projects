def compute_change(cost : float, paid : float) -> str:
    """
    Calculates the change and breaks it down into denominations (dollars, quarters, dimes, nickels, and pennies).

    Parameters:
        cost (float): The cost of the product.
        paid (float): The amount paid by the customer.

    Returns:
        str: A formatted string describing the number of coins for each denomination that should be returned,
             for example "dollars: 3, quarters: 1".

    Example:
         compute_change(2.35, 5.00)
        'dollars: 2, quarters: 2, dimes: 1, pennies: 5'
    """

    #calculating the change in cents
    change_in_cents : float = round((paid - cost) * 100)
    coin_breakdown : dict = {}
    dollars : float = change_in_cents // 100
    result : list = []

    if dollars > 0:
        coin_breakdown["dollars"] = dollars
    change_in_cents %= 100

    quarters = change_in_cents // 25
    if quarters > 0:
        coin_breakdown["quarters"] = quarters
    change_in_cents %= 25

    dimes = change_in_cents // 10
    if dimes > 0:
        coin_breakdown["dimes"] = dimes
    change_in_cents %= 10

    nickels = change_in_cents // 5
    if nickels > 0:
        coin_breakdown["nickels"] = nickels
    change_in_cents %= 5

    pennies = change_in_cents // 1
    if pennies > 0:
        coin_breakdown["pennies"] = pennies
    change_in_cents %= 1

    #Appending the values of each coin into a list
    for name, value in coin_breakdown.items():
        result.append(f'{name}: {value}')

    #Returning a joined list with each coin, if we have a 0 of a certain coin we don't print it
    return ', '.join(result)


#The amount that needs to be paid
cost : float = float(input("Enter the cost of the product: "))
#The amount that has been paid with
paid : float = float(input("Enter the amount you paid: "))

#If the cost is higher than the paid amount
if cost > paid:
    while True:
        print(f'Error! You need to pay more than the cost, which is {cost}')
        # The amount that has been paid with
        paid : float = float(input("Enter the amount you paid: "))
        if paid > cost:
            break
        else:
            continue

change_breakdown = compute_change(cost, paid)
print("Change breakdown:", change_breakdown)

