# Finds volume of a cylinder.

# Asks for radius and length inputs from user.
radius = float(input("Radius: "))
length = float(input("Length: "))
pi = 3.1416

# Calculates volume.
volume = pi * (radius**2) * length

# Prints volume.
print(f"Volume of cylinder: {volume:.2f}")
