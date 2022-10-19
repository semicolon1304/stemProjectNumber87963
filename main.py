# Note to self: try separating the adjacentLocations assignment from the rest of the object

# Add functions from bookshelf.py
import bookshelf as b

# Declaring locations and people so the program doesn't flip out
school = ballField = gibbHouse = webbHouse = wallyRoom = mainStreet = wallyWebb = howieNewsome = mzGibbs = mrGibbs = mzWebb = mrWebb = georgeGibbs = rebeccaGibbs = emilyWebb = None
listOLocations = [school, ballField, gibbHouse, webbHouse, wallyRoom, mainStreet]

# Locations

school = b.Location("School", ["Move", "Talk", "Check"], "The town school. Kids are walking out as the school day ends. Standing nearby is Rebbecca Gibbs.", [ballField, mainStreet], [])

ballField = b.Location("Baseball Field", ["Move", "Talk", "Check"], "The baseball field. Nearby, George Gibbs is practicing his swing.", [school, mainStreet], [])

gibbHouse = b.Location("Gibbs House", ["Move", "Talk", "Check"], "The home of the Gibbs family. Inside are Mr. and Mrs. Gibbs.", [webbHouse, mainStreet], [])

webbHouse = b.Location("Webb House", ["Move", "Talk", "Check"], "The home of the Webb family. Inside are Mr. and Mrs. Webb.", [gibbHouse, mainStreet], [])

wallyRoom = b.Location("Wally's room", ["Move", "Talk", "Check"], "Wally Webb's room. Inside is wally webb", [webbHouse], [])
mainStreet = b.Location("Main Street", ["Move", "Talk", "Check"], "To the north are the Gibb and Webb houses. To the east is the soda shop. To the south is the school and ball field.", [gibbHouse, webbHouse, school, ballField], [])

# Declaring some [pretty epic] variables 
turns = 15
eventsCompleted = []
currentLocation = mainStreet

# Starting text
b.print2("Welcome! Travel about the town by using the menus. Try to experience all you can before the turn limit is up. \n \n Type the number of the action you want to do. [Note: 'Check' doesn't use a turn] \n")
b.print2(f"You are standing on Main Street. {mainStreet.description} \n")

while turns > 0:
  option = b.drawMenu(len(currentLocation.menuOptions), currentLocation.menuOptions, turns)
  if option == 1:
    currentLocation = b.move(currentLocation)
    print(currentLocation)
    turns -=1
  if option == 2:
    pass
  if option == 3:
    pass