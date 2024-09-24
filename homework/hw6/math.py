"""
This script performs basic arithmetic operations (add, subtract, multiply, divide)
on two user-provided integers.

Author: Joshua Lucas
Date: 09/24/24
"""


import validate


def add(n1: int, n2: int) -> int:
    """Adds two integers."""
    return n1 + n2


def subtract(n1: int, n2: int) -> int:
    """Subtracts two integers."""
    return n1 - n2


def multiply(n1: int, n2: int) -> int:
    """Multiplies two integers."""
    return n1 * n2


def divide(n1: int, n2: int) -> float | str:
    """Divides two integers, returns 'undefined' if dividing by zero."""
    if n2 == 0:
        return 'undefined'
    return n1 / n2


def main() -> None:
    """
    Main function to process two integers through selected math type.
    
    Prints the processed result.
    """
    # Mapping operation types to functions for cleaner operation handling
    operations = {1: add, 2: subtract, 3: multiply, 4: divide}

    # Ask user for operation type.
    operation_choice = validate.valid_with_range(
        'Enter: (1) add, (2) subtract, (3) multiply, (4) divide: ', 1, 4)

    # Ask user for two integers.
    num_1 = validate.get_valid_int('Enter the first number: ')
    num_2 = validate.get_valid_int('Enter the second number: ')

    # Get the operation and execute.
    result = operations[operation_choice](num_1, num_2)

    # Print result as part of a sentence.
    if result == 'undefined':
        print(f'The result of {num_1} and {num_2} is {result}.')
    else:
        print(f'The result of {num_1} and {num_2} is {result:.2f}')


if __name__ == '__main__':
    main()
