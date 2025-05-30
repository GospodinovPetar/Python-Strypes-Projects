import random


# Problem 1
def gensquares(N):
    for i in range(N):
        yield i**2


for x in gensquares(10):
    print(x)

# Problem 2

random.randint(1, 10)


def rand_num(low, high, n):
    for i in range(n):
        yield random.randint(low, high)


for num in rand_num(1, 10, 12):
    print(num)

# Problem 3

s = "hello"
s = iter(s)

print(next(s))

# Problem 4

numbers = [1, 2, 3, 4, 5]

filtered_gen = (element for element in numbers if element > 3)

for element in filtered_gen:
    print(element)
