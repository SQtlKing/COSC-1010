"""
File: ~Python/homeworks/09-modules/dice_stats.py

Name: dice_stats.py

Requirements:
    Calculate stats for dice rolls based on user input (number of rolls and sides).
    Display results in a formatted table.

Constants: N/A

Variables:
    Input:
        num_rolls: Number of rolls to perform.
        num_sides: Number of sides on the die.

    Calculated:
        roll_counts: Dictionary counting each side's occurrences.
        results: List of all rolls made.
        probability: Percentage chance of each side appearing.

Output:
    Formatted table showing each side, its count, and the probability.

Key calculations:
    Probability of each side appearing.

Key design considerations:
    Keep it clean and simple. Prioritize readability.

Test data:
    Tested with up to 100,000,000 rolls successfully. Handled various inputs well.
"""

# Imports
from dice_roller import roll_die
from validate import get_valid_int


def main() -> None:
    """Rolls a die with a specified number of sides for a given number of times and
    displays the results in a formatted table showing side count and probabilities."""
    # Get user input
    num_rolls = get_valid_int('How many rolls? ', min_value=1)
    num_sides = get_valid_int('How many sides? ', min_value=4)

    # Initialize roll count dictionary
    roll_counts = {side: 0 for side in range(1, num_sides + 1)}

    # Perform rolls and record results
    for _ in range(num_rolls):
        roll_counts[roll_die(num_sides)] += 1

    # Display results in a formatted table
    print(f'\nStatistics for {num_rolls:,} rolls of a D{num_sides}:')
    print(f'{"Side":<10}{"Count":<10}{"Probability (%)":<15}')
    print('-' * 35)

    for side, count in roll_counts.items():
        probability = (count / num_rolls) * 100
        print(f'{side:<10}{count:<10}{probability:<15.2f}')


if __name__ == '__main__':
    main()
