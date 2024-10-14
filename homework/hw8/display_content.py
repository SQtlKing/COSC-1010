"""
This module contains a function to display the content of a file.

Author: Joshua Lucas
Date: 10/09/24
"""


def display_content(file_name: str) -> None:
    """
    Reads and displays the content of a specified file.

    Args:
        file_name (str): The name of the file to read and display.
    """
    separator = '-' * 60
    try:
        # Display file name and its content within separators.
        with open(file_name, 'r') as file:
            content = file.read().strip()
            print(
                f'\nDisplaying Contents of: {file_name}\n'
                f'{separator}\n{content}\n{separator}'
            )
    except FileNotFoundError:
        print(f'Error: "{file_name}" not found.')
    except PermissionError:
        print(f'Error: No permission to read "{file_name}".')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
