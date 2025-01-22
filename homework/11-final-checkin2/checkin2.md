# Final Check-In 2 - COSC-1010  

This week, I refined the **3-point strategy** simulation, focusing on the **logic for both teams** in the final 30 seconds of a basketball game.

### Team Logic:
- **Home Team:**  
  Starts with possession and attempts **3-point shots** to tie or win. Missed shots may result in offensive rebounds:  

```python
def simulate_home_turn():
    if attempt_three_pointer():
        return 3, False  # Score and lose possession
    return 0, attempt_rebound()  # Miss and rebound check
```
- **Away Team:**  
  Simulates responses, ensuring the home team trails. Missed shots can also trigger rebound logic:

```python
def simulate_away_turn(home_score, away_score):
if home_score == away_score - 3:  # Home team within 3
    if attempt_three_pointer():
        return 3, True  # Home ties the game
    return 0, not attempt_rebound()  # Miss and lose possession
if attempt_two_pointer():  # Extending lead
    return 2, True  # Score and retain possession
return 0, not attempt_rebound()  # Miss and lose possession
```
### Results:
- Simulated thousands of trials to evaluate the **3-point strategy's performance:**
```
Win percentage for 3-point strategy: 14.65%
Average score for 3-point strategy: 1.41
```
With this version, the end is in sight. All that I need to implement now is the 2-pointer strategy!