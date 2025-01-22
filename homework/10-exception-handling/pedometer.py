"""
File: ~/Python/homeworks/10-exception-handling/pedometer.py

Purpose:
    - Prompt for step count, convert to miles, and handle exceptions.

Constants:
    - CONVERSION_RATE (int): Steps per mile (2000 by default).

Variables:
    - step_count (int): User input for steps.
    - mile_count (float): Calculated miles from steps.

Output:
    - Prints miles walked, formatted to two decimals.

Calculations:
    - mile_count = step_count / CONVERSION_RATE

Design:
    - Uses get_valid_int for input validation.
    - Raises ValueError for negative steps in steps_to_miles.

Test Data:
    - step_count: 5345  --> "You walked 2.67 miles!"
    - step_count: 0     --> "You walked 0.00 miles!"
    - step_count: -3850 --> "Error: Negative step count entered."
"""

from validate import get_valid_int


def steps_to_miles(steps: float, conversion_rate: float = 2000) -> float:
    """Convert steps to miles."""
    if steps < 0:
        raise ValueError("Error: Negative step count entered.")
    return steps / conversion_rate


def main() -> None:
    """Prompt for steps, convert to miles, and print."""
    try:
        step_count = get_valid_int("How many steps did you take? ")
        mile_count = steps_to_miles(step_count)
        print(f"You walked {mile_count:.2f} miles!")
    except ValueError:
        print("Error: Negative step count entered.")


if __name__ == "__main__":
    main()
