# Add functions from bookshelf.py
import bookshelf as b

score = 0
turns = 10
eventsCompleted = []

''' List of endings:
        Bucket, Marriage, Wally, 
'''
# Starting text
b.print2("Welcome! Travel about the town by using the menus. ")

print(b.drawMenu(4, ["Hunt", "Move", "Travel to Texas", "Yes"], turns))
turns -= 1
