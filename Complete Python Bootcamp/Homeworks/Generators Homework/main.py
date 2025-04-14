# Problem 1
def generate_squares(limit):
    return (i * i for i in range(limit))

for number in generate_squares(10):
    print(number)

# Problem 2
import random

def generate_random_numbers(min_value, max_value, count):
    for _ in range(count):
        yield random.randint(min_value, max_value)

for number in generate_random_numbers(1, 10, 12):
    print(number)

# Problem 3

s = 'hello'
s = iter(s)

print(next(s))

# Problem 4

numbers = [1, 2, 3, 4, 5]

filtered_gen = (element for element in numbers if element > 3)

for element in filtered_gen:
    print(element)
