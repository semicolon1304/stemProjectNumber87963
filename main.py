# Add functions from bookshelf.py
import bookshelf as b

# Declaring locations and people so the program doesn't flip out
school = ballField = gibbHouse = webbHouse = wallyRoom = mainStreet = wally = howie = msGibbs = drGibbs = msWebb = mrWebb = george = rebecca = emily = None
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
drGibbs = b.Person("Dr. Gibbs","Coffee","Completion")
msGibbs = b.Person("Ms. Gibbs","Newspaper","Coffee")
mrWebb = b.Person("Mr. Webb","Milk Bottle","Quarter")
msWebb = b.Person("Ms. Webb","Other Note","Newspaper")
wally = b.Person("Wally","Appendectomy",None)
guy = b.Person("That Guy","Quarter","Phosphate")
emily = b.Person("Emily","Note","Other Note")
howie = b.Person("Howie",None,"Milk Bottle")
sign = b.Person("Ominous Sign", "literally anything", "Futility")

# People 2: Revenge of the Dialogue
howie.dialogue = "Hello, traveler! Welcome to our town!"
howie.objectDialogue = "[!] Here! Take this milk. On the house for you."
wally.dialogue = "Hey! What are you doing in my room?!"
mrWebb.dialogue = "Weather today is sunny, 65 degrees, expected to be similar for the next two days and then rain the day after that. There's a cold front coming in from the north, expected to arrive in the next two weeks. In other news, we've had three new births, a death, and apparently one new arrival to the town within the last month. Prices for commodities such as milk or sodas have gone down, but prices for bread have gone up. I know I would only pay a quarter for milk today. There are seven different church gathering events happening within the next hour. Senate elections are coming up and the Democratic candidate appears to be doing better. The next issue of the newspaper is being issued as we speak. What's new with you?"
mrWebb.objectDialogue = "[!] Oh, thank you. You the new milkman? I guess I need to pay you then. Have a quarter."
guy.dialogue = "You want a soda? Only 25 cents!"
guy.objectDialogue = "[!] Thank you! Here's your strawberry phosphate."
rebecca.dialogue = "Look at the moon! It's getting awfully close..."
rebecca.objectDialogue = "[!] *gasp* A phosphate? For me? Thanks! You're so kind! Do you think you could do me a favor and give this baseball to my brother?"
george.dialogue = "Busy. Practicing my swing."
george.objectDialogue = "[!] Oh, a baseball. Thanks, I can use this. ... Do you think you could give this note to, uh..."
emily.dialogue = "Oh, hello. I don't think we've met before."
emily.objectDialogue = "[!] A note!? From George!? Oh, wait, actually, hang on. [She takes out a slip of paper and scribbles a second note] Could you hand this to my parents?"
msWebb.dialogue = "Hi."
msWebb.objectDialogue = "[!] Oh, a note from my daughter? Thanks.                             What, do you want me to give you something in return? Here, take this newspaper, I guess."
msGibbs.dialogue = "Hello. I really like my flowers. I think I want something flower-related!"
msGibbs.objectDialogue = "[!] Oh, the front page article is about flowers! Thank you! Here, could you hand this coffee to someone? I don't remember their name."
drGibbs.dialogue = "Oh, hello, stranger. Welcome to the Gibbs house."
drGibbs.objectDialogue = "[!] Wh--Honey, do you not remember my name? And I'm right here!"


# Adding adjacent locations because this program hates me
school.adjacentLocations = [ballField, mainStreet]
ballField.adjacentLocations = [school, mainStreet]
gibbHouse.adjacentLocations = [webbHouse, mainStreet]
webbHouse.adjacentLocations = [wallyRoom, gibbHouse, mainStreet]
wallyRoom.adjacentLocations = [webbHouse]
drugStore.adjacentLocations = [mainStreet]
mainStreet.adjacentLocations = [gibbHouse, webbHouse, school, ballField, drugStore]

# Adding people to locations because this program hates me
school.people = [rebecca]
ballField.people = [george]
gibbHouse.people = [drGibbs, msGibbs]
webbHouse.people = [mrWebb, msWebb]
wallyRoom.people = [wally, sign]
drugStore.people = [guy, emily]
mainStreet.people = [howie]

# Declaring some [pretty epic] variables 
turns = 20
eventsCompleted = []
currentLocation = mainStreet
item = None
gameWinnable = True

# Starting text
b.print2("Welcome! Travel about the town by using the menus. Try to experience all you can before the Moon crashes into the earth. \n \n Type the number of the action you want to do. [Note: 'Check' doesn't use a turn] \n")
b.print2(f"You are standing on Main Street. {mainStreet.description} \n")

while turns > 0:
  if item == "Futility":
    gameWinnable = False
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
    print(f"People nearby: {' '.join([person.name for person in currentLocation.people])} Item: {item}")

if item == "Comepletion":
  b.print2("Congratulations! You managed to meet everyone and fully experience the town. Unfortunatley, The Moon seems to be seconds away from colliding with the planet. Thanks for taking the time to experience Our Tow-")
else:
  b.print2("Thanks for visiting the town. Unfortunately, you didn't manage to see everything you could've. I would tell you that you still have time but, sadly, you don't. You see, The Mo-")