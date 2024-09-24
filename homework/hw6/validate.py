"""
This module contains functions that validate different inputs better.

Author: Joshua Lucas
Date: 09/24/24
"""


def valid_with_range(prompt: str, min_value: int, max_value: int) -> int:
    """
    Prompts user for input until they provide a valid number in the given range.

    Args:
        prompt (str): Message to display to the user.
        min_value (int): Minimum acceptable input value.
        max_value (int): Maximum acceptable input value.

    Returns:
        int: A valid integer input by the user.
    """
    while True:
        try:
            user_input = int(input(prompt))
            if min_value <= user_input <= max_value:
                return user_input
            else:
                print(f'Enter a number between {min_value} and {max_value}.')
        except ValueError:
            print('Enter a valid number.')


def get_valid_int(prompt: str) -> int:
    """
    Prompts user for input until they provide a valid number.

    Args:
        prompt (str): Message to display to the user.

    Returns:
        int: A valid integer input by the user.
    """
    user_input = 0
    while True:
        try:
            user_input = int(input(prompt))
        except ValueError:
            print('Enter a valid number.')
        return user_input


def main():
    '''Nothing here'''


if __name__ == '__main__':
    main()