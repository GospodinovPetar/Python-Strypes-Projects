# Checkout System

## Overview
This project consists of two Python classes: `Discount` and `Checkout`, which together form a simple checkout system that calculates the total price for a customer based on item prices, discounts, and quantities. 

### Features:
- Adds items and their prices.
- Calculates the total cost of the checkout based on item prices and quantities.
- Applies discount rules for specific items when a certain quantity is purchased.

## Class Descriptions

### `Discount`
The `Discount` class holds information about discounts applied to specific items. It requires:
- `number_of_items`: the number of items needed to trigger the discount.
- `price`: the discounted price for the specified quantity of items.

```python
class Discount:
    def __init__(self, number_of_items, price):
        self.number_of_items = number_of_items
        self.price = price
```

### `Checkout`
The `Checkout` class is responsible for managing the items, prices, and discounts. It contains methods to:

- Add item prices.
- Add items to the checkout.
- Calculate the total price of items.
- Apply discounts to items.

#### Key Methods:
- `addItemPrice(item, price)`: Adds an item and its price.
- `addItem(item)`: Adds an item to the cart, increasing its count.
- `calculateTotal()`: Calculates the total price of all items in the cart, considering any discounts.
- `addDiscount(item, number_of_items, price)`: Adds a discount to an item that applies when a certain number of items is purchased.
- `calculateItemTotal(item, count)`: Calculates the total price for a specific item, considering any discounts.
- `calculateItemDiscountedTotal(item, count, discount)`: Calculates the total price of an item when a discount is applied.
```python
class Checkout:
    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}

    def addItemPrice(self, item, price):
        self.prices[item] = price

    def addItem(self, item):
        if item not in self.prices:
            raise Exception('Bad Item')

        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def calculateTotal(self):
        total = 0
        for item, count in self.items.items():
            total += self.calculateItemTotal(item, count)
        return total

    def addDiscount(self, item, number_of_items, price):
        discount = Discount(number_of_items, price)
        self.discounts[item] = discount

    def calculateItemTotal(self, item, count):
        total = 0
        if item in self.discounts:
            discount = self.discounts[item]
            if count >= discount.number_of_items:
                total += self.calculateItemDiscountedTotal(item, count, discount)
            else:
                total += self.prices[item] * count
        else:
            total += self.prices[item] * count

        return total

    def calculateItemDiscountedTotal(self, item, count, discount):
        total = 0
        number_of_discounts = count // discount.number_of_items
        total += number_of_discounts * discount.price
        remaining = count % discount.number_of_items
        total += remaining * self.prices[item]
        return total
```

## Unit Tests
### Setup
The unit tests are written using pytest and ensure that the checkout system behaves as expected.

`checkout` Fixture

A fixture is used to create an instance of the `Checkout` class and add some initial item prices for testing.

```python
@pytest.fixture()
def checkout():
    checkout = Checkout()
    checkout.addItemPrice('a', 1)
    checkout.addItemPrice('b', 2)
    return checkout
```

### Tests
1. `test_CanCalculateTotal`: Verifies that the total calculation works with a single item.
```python
def test_CanCalculateTotal(checkout):
    checkout.addItem('a')
    assert checkout.calculateTotal() == 1
```
2. `test_GetCorrectTotalWithMultipleItems`: Verifies that the total calculation works with multiple items.
```python
def test_GetCorrectTotalWithMultipleItems(checkout):
    checkout.addItem('a')
    checkout.addItem('b')
    assert checkout.calculateTotal() == 3
```
3. `test_addDiscount`: Tests that a discount can be added to an item.
```python
def test_addDiscount(checkout):
    checkout.addDiscount('a', 3, 2)
```
4. `test_canApplyDiscountRule`: Tests that the discount rule is applied correctly when the item count meets the discount criteria.
```python
def test_canApplyDiscountRule(checkout):
    checkout.addDiscount('a', 3, 2)
    checkout.addItem('a')
    checkout.addItem('a')
    checkout.addItem('a')
    assert checkout.calculateTotal() == 2
```
5. `test_ExceptionWithBadItem`: Verifies that an exception is raised when attempting to add an item that is not listed.
```python
def test_ExceptionWithBadItem(checkout):
    with pytest.raises(Exception):
        checkout.addItem('c')
```
