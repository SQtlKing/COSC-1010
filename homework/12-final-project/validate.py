"""
This module contains functions for validating integer and character inputs.

Author: Joshua Lucas
Date: 10/07/24
"""

from typing import Optional


def get_valid_int(prompt: str,
                  min_value: Optional[int] = None,
                  max_value: Optional[int] = None) -> int:
    """
    Continuously prompt for a valid integer, optionally within a specified range.

    Args:
        prompt (str): Message displayed to the user.
        min_value (int, optional): Minimum allowed value. Defaults to None.
        max_value (int, optional): Maximum allowed value. Defaults to None.

    Returns:
        int: A valid integer (within range if specified).
    """
    while True:
        try:
            user_input = int(input(prompt))
        except ValueError:
            print('Error: Please enter a valid number.')
            continue

        # Check min and max constraints together first, if both are set
        if (min_value is not None and max_value is not None
                and not (min_value <= user_input <= max_value)):
            print(
                f'Error: Enter a number between {min_value} and {max_value}.')
            continue

        # Check min_value constraint independently
        if min_value is not None and user_input < min_value:
            print(
                f'Error: Enter a number greater than or equal to {min_value}.')
            continue

        # Check max_value constraint independently
        if max_value is not None and user_input > max_value:
            print(f'Error: Enter a number less than or equal to {max_value}.')
            continue

        return user_input


def get_valid_char(prompt: str, valid_chars: str) -> str:
    """
    Continuously prompt for a valid character from a set of options.

    Args:
        prompt (str): Message displayed to the user.
        valid_chars (str): Valid characters (e.g., 'yn' for 'yes' or 'no').

    Returns:
        str: A valid character from the options.
    """
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_chars:
            return user_input
        else:
            print(
                f'Error: Enter one of the following: {", ".join(valid_chars)}.'
            )


def validate_int(number: int,
                 min_value: Optional[int] = None,
                 max_value: Optional[int] = None) -> int:
    """
    Validate an integer within a specified range.

    Args:
        number (int): The integer to validate.
        min_value (int, optional): Minimum allowed value. Defaults to None.
        max_value (int, optional): Maximum allowed value. Defaults to None.

    Returns:
        int: A valid integer (within range if specified).

    Raises:
        ValueError: If the number is not within the specified range.
    """
    # Check both min_value and max_value constraints
    if min_value is not None and max_value is not None:
        if not (min_value <= number <= max_value):
            raise ValueError(
                f'Error: Enter a number between {min_value} and {max_value}.')

    # Check only min_value constraint
    elif min_value is not None and number < min_value:
        raise ValueError(
            f'Error: Enter a number greater than or equal to {min_value}.')

    # Check only max_value constraint
    elif max_value is not None and number > max_value:
        raise ValueError(
            f'Error: Enter a number less than or equal to {max_value}.')

    return number


# Example Usage
if __name__ == '__main__':
    number = get_valid_int('Choose a number between 1 and 10: ', 1, 10)
    print(f'You entered: {number}')

    number = get_valid_int('Choose a number above 9: ', min_value=10)
    print(f'You entered: {number}')

    integer = get_valid_int('Enter any integer: ')
    print(f'You entered: {integer}')

    char = get_valid_char('Enter yes or no (y/n): ', 'yn')
    print(f'You entered: {char}')
