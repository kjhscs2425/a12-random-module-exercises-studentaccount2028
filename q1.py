import random
def spin_twister_spinner():
  info = []
  color = random.choice(["red", "green", "yellow", "blue"])
  sides = random.choice(["left","right"])
  appendage = random.choice(["hand", "foot"])
  info.append(color)
  info.append(sides)
  info.append(appendage)
  #YOUR CODE HERE
  return info

# Here's the function call. This should print a random assortment of twister commands
for i in range(10):
  print(spin_twister_spinner())