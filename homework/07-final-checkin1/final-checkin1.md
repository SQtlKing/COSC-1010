# Final Check-In 1 - COSC-1010

This week, I started laying the groundwork for my final project: a **Monte Carlo simulation** focused on the last 30 seconds of a basketball game, down by 3 points.

The simulation compares two strategies:

1. **Shoot a 3-pointer**
2. **Shoot a 2-pointer and foul**

### Key parameters include:

- **3-point percentage:** `0.35`
- **2-point percentage:** `0.50`
- **Opponent free-throw percentage:** `0.75`
- **Offensive rebound chance:** `0.52`

Here's a rough idea of how I'm handling shots:

```python
def three_pointer():
    return random.random() < three_point_percentage

def two_pointer():
    return random.random() < two_point_percentage
```
### The Monte Carlo logic involves:

- Running thousands of trials
- Tracking time, rebounds, and possessions
- Printing out win percentages and average scores for each strategy

```Python
for _ in range(number_of_trials):
    possession = True
    if possession:
        time_remaining -= time_to_shoot
        if three_pointer():
            # Score logic
        else:
            possession = False
    # Continue simulation logic for other team
```

This is just the start, but it’s all about simulating **decision-making under pressure** with probabilities guiding the outcomes.

