"""
File: ~/COSC-1010-Final-Project/Final-Project

Name: finalproject.py

Requirements:
    Simulate and compare two basketball strategies:
        1. 3-point strategy.
        2. 2-point strategy with fouling.

Constants:
    THREE_PT_PROB = 0.35  # 3-point success rate
    TWO_PT_PROB = 0.50    # 2-point success rate
    REBOUND_PROB = 0.28   # Offensive rebound probability
    OPP_FT_PROB = 0.78    # Opponent free-throw success rate
    OT_WIN_PROB = 0.52    # Overtime win probability
    SHOT_TIME = 8.0       # Time per shot
    FOUL_TIME = 5.0       # Time per foul

Variables:
     input:
        num_trials: Number of trials (user input).

     calculated:
        home_score: Home team’s score.
        away_score: Away team’s score.
        home_wins: Total home wins.
        total_home_score: Total home points.

Output:
    Win percentage and average score for both strategies.


Key calculations:
    - 3-point strategy: Waste time, shoot, check win/overtime.
    - 2-point strategy: Alternate shots and fouls, check win.

Test data:
    Input:
        Enter the number of trials: 1,000,000

    Output:
        Simulating 3-point strategy...
        Simulating 2-point strategy...
        
        --- Simulation Results ---
        3-Point Strategy: Win Percentage = 18.24%
        3-Point Strategy: Average Score = 1.05
        2-Point Strategy: Win Percentage = 1.59%
        2-Point Strategy: Average Score = 2.12
"""

import random
from validate import get_valid_int

# Probabilities (% of 1)
THREE_PT_PROB = 0.35  # 3-point shot success rate
TWO_PT_PROB = 0.50  # 2-point shot success rate
REBOUND_PROB = 0.28  # Offensive rebound probability
OPP_FT_PROB = 0.78  # Opponent free-throw success rate
OT_WIN_PROB = 0.52  # Probability of winning in overtime

# Time settings (seconds)
SHOT_TIME = 8.0
FOUL_TIME = 5.0


def attempt_three_pointer():
    """Returns True if a 3-point shot is successful."""
    return random.random() < THREE_PT_PROB


def attempt_two_pointer():
    """Returns True if a 2-point shot is successful."""
    return random.random() < TWO_PT_PROB


def attempt_rebound():
    """Returns True if a rebound is successful."""
    return random.random() < REBOUND_PROB


def attempt_free_throw():
    """Returns True if a free throw is successful."""
    return random.random() < OPP_FT_PROB


def attempt_overtime():
    """Returns True if the home team wins in overtime."""
    return random.random() < OT_WIN_PROB


def simulate_three_point_strategy(num_trials):
    """
    Simulates a game using the 3-point strategy.
    Returns:
        tuple: Total wins and total score for the home team.
    """
    home_wins, total_home_score = 0, 0

    for _ in range(num_trials):
        home_score, away_score = 0, 3

        # Attempt the final 3-pointer
        if attempt_three_pointer():
            home_score += 3

        # Check if the game goes to overtime or if the home team wins
        if home_score == away_score and attempt_overtime():
            home_wins += 1
        elif home_score > away_score:
            home_wins += 1

        total_home_score += home_score

    return home_wins, total_home_score


def simulate_two_point_strategy(num_trials):
    """
    Simulates a game using the 2-point strategy.
    Returns:
        tuple: Total wins and total score for the home team.
    """
    home_wins, total_home_score = 0, 0

    for _ in range(num_trials):
        home_score, away_score, possession = 0, 3, True
        remaining_time = 30.0

        while remaining_time > 0:
            if possession:
                remaining_time -= SHOT_TIME
                if remaining_time >= 0:
                    if attempt_two_pointer():
                        home_score += 2
                        possession = False
                    else:
                        possession = attempt_rebound()
            else:
                remaining_time -= FOUL_TIME
                if remaining_time >= 0:
                    for _ in range(2):  # Opponent free throws
                        if attempt_free_throw():
                            away_score += 1
                    possession = not attempt_rebound()

        if home_score == away_score and attempt_overtime():
            home_wins += 1
        elif home_score > away_score:
            home_wins += 1

        total_home_score += home_score

    return home_wins, total_home_score


def main():
    """
    Simulates basketball games using both strategies and compares the results.
    """
    num_trials = get_valid_int(
        "Enter the number of trials: ", min_value=1)

    print("Simulating 3-point strategy...")
    three_pt_wins, three_pt_score = simulate_three_point_strategy(num_trials)

    print("Simulating 2-point strategy...")
    two_pt_wins, two_pt_score = simulate_two_point_strategy(num_trials)

    print("\n--- Simulation Results ---")
    print(
        f"3-Point Strategy: Win Percentage = {three_pt_wins / num_trials * 100:.2f}%"
    )
    print(
        f"3-Point Strategy: Average Score = {three_pt_score / num_trials:.2f}")
    print(
        f"2-Point Strategy: Win Percentage = {two_pt_wins / num_trials * 100:.2f}%"
    )
    print(f"2-Point Strategy: Average Score = {two_pt_score / num_trials:.2f}")


if __name__ == "__main__":
    main()
