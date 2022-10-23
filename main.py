# Add functions from bookshelf.py
import bookshelf as b

# Declaring locations and people so the program doesn't flip out
school = ballField = gibbHouse = webbHouse = wallyRoom = mainStreet = wallyWebb = howieNewsome = mzGibbs = mrGibbs = mzWebb = mrWebb = georgeGibbs = rebeccaGibbs = emilyWebb = None
listOLocations = [school, ballField, gibbHouse, webbHouse, wallyRoom, mainStreet]
options = ["Move", "Talk", "Check"]

# Locations
school = b.Location("School", options, "The town school. Kids are walking out as the school day ends. Standing nearby is Rebecca Gibbs.")
ballField = b.Location("Baseball Field", options, "The baseball field. Nearby, George Gibbs is practicing his swing.")
gibbHouse = b.Location("Gibbs House", options, "The home of the Gibbs family. Inside are Dr. and Mrs. Gibbs.")
webbHouse = b.Location("Webb House", options, "The home of the Webb family. Inside are Mr. and Mrs. Webb.")
wallyRoom = b.Location("Wally's room", options, "Wally Webb's room. Inside is Wally Webb.")
drugStore = b.Location("Drugstore", options, "Town drugstore. Behind the counter is That Guy, standing nearby is Emily Webb.")
mainStreet = b.Location("Main Street", options, "To the north are the Gibb and Webb houses. To the east is the drugstore. To the south is the school and ball field. Standing nearby is Howie Newsome.")

# People
rebecca = b.Person("Rebecca","Phosphate","Baseball")
george = b.Person("George","Baseball","Note")
drGibbs = b.Person("Dr. Gibbs","Coffee",None)
msGibbs = b.Person("Ms. Gibbs","Newspaper","Coffee")
mrWebb = b.Person("Mr. Webb","Milk Bottle","Quarter")
msWebb = b.Person("Ms. Webb","Other Note","Newspaper")
wally = b.Person("Wally",None,None)
guy = b.Person("That Guy","Quarter","Phosphate")
emily = b.Person("Emily","Note","Other Note")
howie = b.Person("Howie",None,"Milk Bottle")

# People 2: Revenge of the Dialogue
howie.dialogue = "Hello, traveler! Welcome to our town!"
wally.dialogue = "Hey! What are you doing in my room?!"
guy.dialogue = "You want a soda? Only 25 cents!"


# Adding adjacent locations because this program hates me
school.adjacentLocations = [ballField, mainStreet]
ballField.adjacentLocations = [school, mainStreet]
gibbHouse.adjacentLocations = [webbHouse, mainStreet]
webbHouse.adjacentLocations = [wallyRoom, gibbHouse, mainStreet]
wallyRoom.adjacentLocations = [webbHouse]
drugStore.adjacentLocations = [mainStreet]
mainStreet.adjacentLocations = [gibbHouse, webbHouse, school, ballField, drugStore]

# Adding people to locations because this program hates me
school.adjacentLocations = [ballField, mainStreet]
ballField.adjacentLocations = [school, mainStreet]
gibbHouse.adjacentLocations = [webbHouse, mainStreet]
webbHouse.adjacentLocations = [wallyRoom, gibbHouse, mainStreet]
wallyRoom.adjacentLocations = [webbHouse]
drugStore.adjacentLocations = [mainStreet]
mainStreet.adjacentLocations = [gibbHouse, webbHouse, school, ballField, drugStore]

# Declaring some [pretty epic] variables 
turns = 15
eventsCompleted = []
currentLocation = mainStreet
item = None
gameWinnable = True
# Starting text
b.print2("Welcome! Travel about the town by using the menus. Try to experience all you can before the Moon crashes into the earth. \n \n Type the number of the action you want to do. [Note: 'Check' doesn't use a turn] \n")
b.print2(f"You are standing on Main Street. {mainStreet.description} \n")

while turns > 0:
  if turns != 15:
    print(currentLocation.description)
  option = b.drawMenu(len(currentLocation.menuOptions), currentLocation.menuOptions, turns)
  if option == 1:
    currentLocation = b.move(currentLocation)
    turns -=1
  if option == 2:
    item = b.talk(currentLocation, item)
    turns -= 1
  if option == 3:
    print(f"People nearby: {currentLocation.people} Item: {item}")