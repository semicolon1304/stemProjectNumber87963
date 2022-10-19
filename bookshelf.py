import sys
import time

class Location:
  def __init__(self, name, menuOptions, description, adjacentLocations, people):
    self.name = name
    self.menuOptions = menuOptions
    self.description = description
    self.adjacentLocations = adjacentLocations
    self.people = people

class Person:
  def __init__(self, name, object):
    self.name = name
    self.object = object
    self.dialogue = ""
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
    out = ""
  while type(out) != int:
    out = int(input(f"\n What would you like to do? ({turns} turns remaining) "))
  return out
  
  
# Help menu (WIP)
def drawHelp():
  print("Select an option by typing the number and pressing enter.")

# Move be like :|
def move(currentArea):
  print()
  locationDict = {}
  for i, location in enumerate(currentArea.adjacentLocations):
    locationDict.update([(i+1, location)])
    print(f"{i+1}.) {location.name}")
  num = int(input("\nWhere do you want to move to? "))
  moveTo = locationDict[num]
  return moveTo