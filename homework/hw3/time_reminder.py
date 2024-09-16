# Takes input time (0-23) from user and responds.

# Takes input time (0-23).
time = int(input("What's the time 0-23? "))

# Responds based on input.
if time < 8:
  print("too early to get up")
elif time < 12:
  print("Good morning")
elif time < 14:
  print("Lunch time!")
elif time < 18:
  print("Good afternoon")
elif time == 18:
  print("Tea Time")
elif time <= 19:
  print("Good evening")
elif time <= 22:
  print("Nearly bedtime")
elif time == 23:
  print("Good night!")
else:
  print("Sorry, I don't recognize that")
