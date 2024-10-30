"""
This module lets you roll a die with as many sides as you want (at least 4).

Author: Joshua Lucas
Date: 10/25/24
"""

from random import randint


def roll_die(sides: int) -> int:
    """
    Rolls a die with the specified amount of sides.

    Args:
        sides (int): The number of sides. Minumum of 4.

    Returns:
        int: The roll's result.
    """
    if sides < 4:
        raise ValueError("A die has a minimum of 4 sides.")
    return randint(1, sides)


def test_dice_roller():
    """Runs unit tests for the dice_roller function."""

    results = [roll_die(6) for _ in range(100)]
    assert all(1 <= result <= 6
               for result in results), "D6 roll results invalid"

    results = [roll_die(10) for _ in range(100)]
    assert all(1 <= result <= 10
               for result in results), "D10 roll results invalid"

    print("Dice roller tests passed successfully!")


if __name__ == "__main__":
    test_dice_roller()  # Run the unit tests when executed directly
