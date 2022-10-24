import sys
import time

class Location:
  def __init__(self, name, menuOptions, description):
    self.name = name
    self.menuOptions = menuOptions
    self.description = description
    self.adjacentLocations = []
    self.people = []

class Person:
  def __init__(self, name, likedObject, giveObject):
    self.name = name
    self.likedObject = likedObject
    self.giveObject = giveObject
    self.dialogue = "This string is for testing purposes, be sure to remove it when the game is finished."
    self.objectDialogue = "[!] This is yet another string made for testing purposes. Unlike the other string, this one doesn't need to be removed when the game is finished. "
    
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
  
# Wally's Room's Sign 
def print4(text):
  for c in text:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.5)

# Draws the current screen's menu
def drawMenu(numberOfOptions, options, turns):
  for i in range (numberOfOptions):
    print(f"{i+1}). {options[i]} ")
    out = None
  while type(out) != int or out > numberOfOptions:
    out = int(input(f"\n What would you like to do? ({turns} turns remaining) "))
  return out

# Move be like :|
def move(currentArea):
  print()
  locationDict = {}
  for i, location in enumerate(currentArea.adjacentLocations):
    locationDict.update([(i+1, location)])
    print(f"{i+1}.) {location.name}")
  num = int(input("\nWhere do you want to move to? "))
  return locationDict[num]
  
# Talk be like :]
def talk(currentLocation, item):
  print()
  personDict = {}
  for i, person in enumerate(currentLocation.people):
    personDict.update([(i+1, person)])
    print(f"{i+1}). {person.name}")
  num = int(input("\nWho do you want to talk to? "))
  if personDict[num].name == "Sign":
    print4("YOU CANNOT WIN.")
  elif personDict[num].name != "Mr. Webb":
    print2(personDict[num].dialogue) 
  else:
    print3(personDict[num].dialogue)
  if item == personDict[num].likedObject:
    if personDict[num].name != "Mr. Webb":
      print2(personDict[num].objectDialogue)
    else:
      print3(personDict[num].objectDialogue)
    return personDict[num].giveObject
  return item
