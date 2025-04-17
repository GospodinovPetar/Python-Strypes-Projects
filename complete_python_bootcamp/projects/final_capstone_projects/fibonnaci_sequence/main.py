def numbers_update(first_num, second_num):
    """
    Calculates the next Fibonacci number and updates the Fibonacci sequence.

    This function computes the next number in the Fibonacci sequence as the sum of
    `first_num` and `second_num`. The computed number is then appended to the global list
    `fib_sequence` which stores the sequence. If the next number exceeds the maximum value
    specified by the global variable `m`, the function returns (0, 0) as a signal that the
    sequence should end (since 0 is not a valid Fibonacci number in this context). This termination
    condition is later checked in the while loop.

    Parameters:
        first_num (int): The first number of the current Fibonacci pair.
        second_num (int): The second number of the current Fibonacci pair.

    Returns:
        tuple[int, int]: A tuple containing the updated Fibonacci pair. If the next number exceeds `m`,
                          returns (0, 0) to indicate termination.

    Example:
        If first_num is 5 and second_num is 8, and the next number (13) is not greater than `m`,
        the function appends 13 to fib_sequence and returns (8, 13).
    """

    next_num = first_num + second_num
    if next_num > m:
        return 0, 0
    fib_sequence.append(next_num)

    return second_num, next_num


# Initial Fibonacci numbers
first_num: int = 0
second_num: int = 1

# List to store the Fibonacci sequence
fib_sequence = [first_num, second_num]

# Get the maximum value for the sequence
m: int = int(input("Input the number you want the Fibonacci sequence to go to: "))

# Generate the Fibonacci sequence until the value exceeds m
while True:
    first_num, second_num = numbers_update(first_num, second_num)
    if first_num == 0 and second_num == 0:
        break
# Print the Fibonacci sequence
print(fib_sequence)
