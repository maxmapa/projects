# Dice Game

def rollDice():
  import random
  dice = random.randint(1, 6)
  print("You rolled", dice)

for i in range(7):
  rollDice()

# Login game  

def login():
  while True:
    username = input("What is your username?: ")
    password = input("What is your password? ")
    if username == "David" and password == "Replit4ev#r":
      print("Welcome David!")
      break
    else:
      print("That is not the correct username or password. Try again!")
      continue

print("REPLIT LOGIN SYSTEM")
login()

# Dice Game

import random
print("Infinity Dice 🎲")

sides = int(input("How many sides?: "))
playGame = "yes"

def rollDice(sides):
  print("You rolled ", random.randint(1,sides))
while playGame == "yes":
    rollDice(sides)
    playGame = input("Roll again?")