#!/usr/bin/env python3

def print_fibonacci(length):
    # Initialization
    num1 = 0
    num2 = 1

    # Empty list to store the sequence
    fibonacci_sequence = []


    if length == 0:
        print(fibonacci_sequence)
        return

    # Checking for valid lengths
    if length < 0:
        print("Invalid length. Length should be a non-negative integer.")
        return

    # Adding the first two numbers to the sequence list
    fibonacci_sequence.append(num1)
    if length >= 2:
        fibonacci_sequence.append(num2)

    # Generating the remaining numbers of the sequence
    for i in range(2, length):
        # Calculating the next number in the sequence
        next_num = num1 + num2

        # Adding the next number to the  sequence list
        fibonacci_sequence.append(next_num)

        # Updating num1 and num2 for the next iteration
        num1 = num2
        num2 = next_num

    
    print(fibonacci_sequence)