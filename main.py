# Add functions from bookshelf.py
import bookshelf as b

turns = 15
eventsCompleted = []

# Locations

# Declaring locations so the program doesn't flip out
school = ballField = gibbHouse = webbHouse = wallyRoom = mainStreet = "temp"

school = b.Location(["Move", "Talk", "Check"], "The town school. Kids are walking out as the school day ends. Standing nearby is Rebbecca Gibbs.", [ballField, mainStreet])

ballField = b.Location(["Move", "Talk", "Check"], "The baseball field. Nearby, George Gibbs is practicing his swing.", [school, mainStreet])

gibbHouse = b.Location(["Move", "Talk", "Check"], "The home of the Gibb family. Inside are Mr. and Mrs. Gibb.", [webbHouse, mainStreet])

wallyRoom = b.Location(["Move", "Talk", "Check", "Kill"], "Wally Webb's room. Wally is busy having appendicitis.", [webbHouse])

webbHouse = b.Location(["Move", "Talk", "Check"], "The home of the Webb family. Inside are Mr. and Mrs. Webb.", [wallyRoom, gibbHouse, mainStreet])

mainStreet = b.Location(["Move", "Talk", "Check"], "Main street. To the north are the Gibb and Webb houses. To the east is the soda shop. To the south is the school and ball field.", [gibbHouse, webbHouse, school, ballField])

# Starting text
b.print2("Welcome! Travel about the town by using the menus. Try to experience all you can before the turn limit is up. \n \n Type the number of the action you want to do. [Note: 'Check' doesn't use a turn] \n")

b.print2(f"You are standing on main street. {mainStreet.description} \n")
b.drawMenu(len(mainStreet.menuOptions), mainStreet.menuOptions, turns)