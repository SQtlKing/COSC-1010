"""
This module contains a function to append an entry to a file.

Author: Joshua Lucas
Date: 10/10/24
"""


def append_file(entry: str, file_name: str) -> None:
    """
    Append an entry to the specified file.

    Args:
        entry (str): Text that will be appended to the file.
        file_name (str): The file where the entry will be stored.
    """
    try:
        with open(file_name, 'a') as file:
            file.write(entry + '\n')
    except FileNotFoundError:
        print(f'Error: Unable to locate "{file_name}".')
    except PermissionError:
        print(f'Error: Permission denied for writing to "{file_name}".')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
