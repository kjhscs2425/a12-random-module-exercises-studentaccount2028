import random
# Make a random pet.

# Choose:
# Type of animal (at least 3 choices, string)
animal = random.choice(["dawg","zebra", "cat", "monkey"])
# Age (integer)
age = random.randint(1,100)
# Color (at least 3 choices, string)
color = random.choice(["Blue","Red","Purple"])
# Weight (float)
weight = random.uniform(1,100)

# Print a summary of your pet using an f-string
print(f"Your pet is a {animal} that is {age} years old. {color} is the color and your animal weighs {weight} pounds precisely")#REPLACE THIS WITH YOUR CODE