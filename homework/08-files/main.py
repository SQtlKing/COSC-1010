"""
File: .\homework\hw8\main.py

Name: main.py

Requirements: Adds bands and singers to a list stored in a file.
              Users can choose what list to add to, with updated
              lists shown after every entry. Repeats until user quits.

Constants: 
    file_paths: Maps user choice (1 for bands, 2 for singers) to the file paths.

Variables:
        category_choice: User selects 1 (band) or 2 (singer).
        name_entry: The name of the band or singer entered by the user.
        user_action: Whether the user wants to continue ('c') or quit ('q').

Output: Confirmation of added names and the updated lists.

Key design considerations: 
    - Open file in append mode to keep existing data.
    - Combined band and singer logic into one function.
    - Make it as stylish as possible. or else...
"""

# Imports
from append_file import append_file
from display_content import display_content
from validate import get_valid_char, get_valid_int

# Definitions
file_paths = {1: 'band_list.txt', 2: 'singer_list.txt'}


def display_lists() -> None:
    """Helper function to display both the band and singer lists."""
    separator = '-' * 60

    print(f'\n{separator}')
    print('Displayed lists:')
    print(separator)

    display_content('band_list.txt')
    display_content('singer_list.txt')


def add_entry() -> None:
    """Prompts the user to add an entry to the corresponding file."""

    # Prompt for input choice (band or singer)
    category_choice = get_valid_int('Add to bands(1) or singers(2): ', 1, 2)
    name_entry = input('Enter the band or singer name: ')

    # Append the name to the appropriate file
    append_file(name_entry, file_paths[category_choice])


def main():
    """Adds bands and singers to a list in a selected file."""

    display_lists()

    while True:
        add_entry()

        # Check if the user wants to continue or quit
        user_action = get_valid_char('Continue? Repeat(c), quit(q): ', 'cq')
        if user_action == 'q':
            break

    # Display updated lists after user exits
    display_lists()


if __name__ == '__main__':
    main()
