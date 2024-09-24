"""
This script allows the user to select and display a range of names from a list.

Author: Joshua Lucas
Date: 09/18/24
"""


def get_valid_input(prompt: str, min_value: int, max_value: int) -> int:
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


def main() -> None:
    """
    Main function to prompt user for name range selection and display selected names.
    """
    names = [
        'Joshua', 'Macy', 'William', 'Lee', 'Michael', 'Lucas', 'Todd',
        'Charlie', 'Robert', 'Scott'
    ]

    # Ask user for output range type.
    range_type = get_valid_input(
        'Select range: (1) point-point, (2) point-end, (3) begin-point: ', 1, 3)

    # User inputs start/end points as a 1-based index, adjusted to 0-based for Python.
    start = None
    end = None

    if range_type == 1:  # Point to point.
        while True:
            start = get_valid_input('Starting point (1-10): ', 1, 10) - 1
            end = get_valid_input('Ending point (1-10): ', 1, 10)
            if start < end:
                break
            else:
                print(
                    'Invalid range: Start must be less than or equal to end.')
    elif range_type == 2:  # Point to end.
        start = get_valid_input('Starting point (1-10): ', 1, 10) - 1
    else:  # Begin to point.
        end = get_valid_input('Ending point(1-10): ', 1, 10)

    # Store names in range.
    if range_type == 1:
        output_names = names[start:end]
    elif range_type == 2:
        output_names = names[start:]
    else:
        output_names = names[:end]

    # Print names.
    if not output_names:
        print('No names selected.')
    else:
        print('Selected names: ', ', '.join(output_names))


if __name__ == '__main__':
    main()
