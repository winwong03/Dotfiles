# MAKING THE GARDEN

"""garden = garden[row][column]"""

alphabet = [' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

width = 10;
height = 10;
delimiter= ' '

garden = [['-' for x in range(width+1)] for x in range(height+1)]

garden[0][0] = ' '

garden[0][1] = '{:>2}'.format(alphabet[1])

for x in range(2, width + 1):
    garden[0][x] = '{:>1}'.format(alphabet[x])

for x in range(1, height+1):
    garden[x][0] = '{:>2}'.format(str(x))


# MAIN

import random

# DEFINING FUNCTIONS
def randomCol():
    """This function randomizes the worm into a certain column"""
    col = random.randint(1, width)
    return col

def randomRow():
    """This function randomizes the worm into a certain row"""
    row = random.randint(1, height)
    return row

def randomOrientation():
    """This function randomizes the worm into lying horizontally or vertically"""
    orien = random.randint(0,1)
    return orien

def displayGarden():
    for int in range(len(garden)):
        b = delimiter.join(garden[int])
        print b;

# INFORMATION ABOUT THE WORMS

length = 3

""""randomOrientation == 1 if lying vertically and 0 if lying horizontally"""

wormList = [[1, randomCol(), randomRow(), length, randomOrientation()],
            [2, randomCol(), randomRow(), length, randomOrientation()],
            [3, randomCol(), randomRow(), length, randomOrientation()],
            [4, randomCol(), randomRow(), length, randomOrientation()],
            [5, randomCol(), randomRow(), length, randomOrientation()],
            [6, randomCol(), randomRow(), length, randomOrientation()]]

# INSERTING WORMS
def insertWorm(worm):
    if worm[4] == 0:
        for i in range(worm[3]):
            if (worm[1]+i > width):
                garden[worm[2]][((worm[1]+i) % (width+1)) +1] = 'W';
            else:
                garden[worm[2]][worm[1]+i] = 'W'
    elif worm[4] == 1:
        for i in range(worm[3]):
            if (worm[2]+i > height):
                garden[((worm[2]+i)%(height+1))+1][worm[1]] = 'W';
            else:
                garden[worm[2]+i][worm[1]] = 'W'

# Welcoming the player statement
print ("Welcome! In this game, we hunt for worms in a garden!")
print ("Here is the garden:")
displayGarden()

#CHOICES

def nextMove():

    choice = int(input("Please, enter 1 to 6 to display each of the worms or 7 to display them\n all (someworms may overlap), and 8 to quit: "))
    
    if choice == 8:
        print("Wasn't it fun! Bye!")
    if choice == 7:
        insertWorm(wormList[0])
        insertWorm(wormList[1])
        insertWorm(wormList[2])
        insertWorm(wormList[3])
        insertWorm(wormList[4])
        insertWorm(wormList[5])
        displayGarden()
        nextMove()
    if choice == 1:
        insertWorm(wormList[0])
        displayGarden()
        nextMove()
    if choice == 2:
        insertWorm(wormList[1])
        displayGarden()
        nextMove()
    if choice == 3:
        insertWorm(wormList[2])
        displayGarden()
        nextMove()
    if choice == 4:
        insertWorm(wormList[3])
        displayGarden()
        nextMove()
    if choice == 5:
        insertWorm(wormList[4])
        displayGarden()
        nextMove()
    if choice == 6:
        insertWorm(wormList[5])
        displayGarden()
        nextMove()

nextMove()

# HuntingWorms
