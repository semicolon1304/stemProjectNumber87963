import sys
import time


# Standard Text
def print2(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)
    print()

# Editor Webb
def print3(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)
    print()

# Draws the current screen's menu
def drawMenu(numberOfOptions, options, turns):
  for i in range (numberOfOptions):
    print(f"{i+1}). {options[i]} ")
  out = input(f"\n What would you like to do? ({turns} turns remaining) ")
  return out
  
  
# Help menu (WIP)
def drawHelp():
  print("Select an option by typing the number and pressing enter.")