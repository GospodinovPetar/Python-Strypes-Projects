def numbers_update(first_num, second_num):
    """"
    This function is used to create the next num for the fibonacci sequence and append it,
    if the next number is higher than the number inputted by the user we return 0,0 which is invalid for any fib sequence,
    later in the while loop we check if both numbers are 0 and stop the program.
    """
    next_num = first_num + second_num
    if next_num > m:
        return 0, 0
    fib_sequence.append(next_num)

    return second_num, next_num

# Initial Fibonacci numbers
first_num : int = 0
second_num : int = 1

# List to store the Fibonacci sequence
fib_sequence = [first_num, second_num]

# Get the maximum value for the sequence
m : int = int(input('Input the number you want the Fibonacci sequence to go to: '))

# Generate the Fibonacci sequence until the value exceeds m
while True:
    first_num, second_num = numbers_update(first_num, second_num)
    if first_num == 0 and second_num == 0:
        break
# Print the Fibonacci sequence
print(fib_sequence)
