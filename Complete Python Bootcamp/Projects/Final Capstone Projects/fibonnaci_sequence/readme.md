# Final Capstone Project: <br> Fibonacci Sequence Generator

This Python script generates the Fibonacci sequence up to a specified maximum value provided by the user. It continues to generate and append numbers to the sequence until the next number exceeds the user's input. If the next Fibonacci number exceeds the maximum value, the program stops.

## Requirements

This script does not require any external libraries or installations. It is written in plain Python and can be run directly in any Python environment.

## Script Functionality

### `numbers_update(first_num, second_num)`
This function generates the next Fibonacci number by adding the two previous numbers in the sequence. If the next number exceeds the user-defined maximum value, the function returns `(0, 0)` to indicate an invalid sequence, which causes the program to stop. Otherwise, it appends the next Fibonacci number to the sequence and returns the updated numbers for the next iteration.

### Example Usage

1. The program prompts the user to input a maximum value for the Fibonacci sequence.
2. It starts generating Fibonacci numbers, appending them to the sequence until the next number exceeds the specified maximum.
3. If the next Fibonacci number is greater than the input value, the program terminates.
4. The program prints the final Fibonacci sequence.

### Example

```bash
Input the number you want the Fibonacci sequence to go to: 50
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
