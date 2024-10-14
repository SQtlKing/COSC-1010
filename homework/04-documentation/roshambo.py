# Assignment: code commenting.
# I made rock, paper, scissors to comment on.

# Import modules.
import random

# Start.
print("Game Start!")

# Get valid user input rock, paper, or scissors as player.
player = 0
while player != 1 and player != 2 and player != 3:
  try:
    player = int(input("Rock(1), Paper(2), or Scissors(3) "))
    if 1 < player > 3:
      print("Invalid number. Enter 1, 2, or 3.")
  except ValueError:
    print("Invalid input. Enter 1, 2, or 3.")
  
# Computer picks rock, paper, or scissors.
computer = random.randint(1, 3)

# Print winner.
if (player > computer) or (player == 1 and computer == 3):
  print("You win!")
elif player == computer:
  print("It's a tie!")
else:
  print("You lose!")

# End.
