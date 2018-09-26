import random
from os import system
from time import sleep

game = []
mask = []

def aesthetic(listNumbers):
    for a in range(0, len(listNumbers)):
        print(listNumbers[a], '->', a)

def table(w,h):
    global game
    global mask

    if (w*h)%2 == 1:
        print('The table needs an even value')
        table(int(input("table size: ")))
    numbers = random.sample(range(0, 100), int((w*h)/2))*2
    for a in range(h):
        game.append([ ])
        mask.append([ ])
        for b in range(w):
            game[a].append([])
            mask[a].append([])
    for c in range(0,h):
        for d in range(0,w):
            numb = random.choice(numbers)
            game[c][d] = numb
            mask[c][d] = 'xx'
            numbers.remove(numb)
    system('clear')
    aesthetic(mask)

def unmask(y,z):
    global game
    global mask
    mask[y][z] = game[y][z]
    system('clear')
    aesthetic(mask)

def masking(y,z, y1,z1):
    global game
    global mask
    mask[y][z] = 'xx'
    mask[y1][z1]= 'xx'
    system('clear')
    aesthetic(mask)

def check(y,z):
    global mask
    global game
    if mask[y][z] == 'xx':
        return False
    return True

def match(r,c,r1,c1):
    global game
    if game[r][c] == game[r1][c1]:
        return True
    return False

def checkTable(tableHeight, tableWidth):
    while isinstance(tableHeight, int) == False or isinstance(tableWidth, int) == False or tableSize%2 == 1 or tableHeight <= 0 or tableWidth <= 0:
        while tableHeight.isnumeric() == False or tableWidth.isnumeric() == False:
            print("You need to choose a number")
            tableHeight = input("Table number of rows: ")
            tableWidth = input("Table number of columns: ")
            system('clear')
        tableHeight = int(tableHeight)
        tableWidth = int(tableWidth)
        tableSize = (tableWidth*tableHeight)
        if (tableSize%2 == 1 or tableHeight == 0 or tableWidth == 0):
            if tableHeight <= 0 or tableWidth <= 0:
                print("Please select a number greater than 0")
                tableHeight = input("Table number of rows: ")
                tableWidth = input("Table number of columns: ")
                system('clear')
            elif tableSize%2 == 1:
                print("The multiplication of rows and columns need to be an even number, please choose a different input")
                tableHeight = input("Table number of rows: ")
                tableWidth = input("Table number of columns: ")
                system('clear')
    table(tableWidth, tableHeight)
    return tableSize, tableWidth, tableHeight

def checkNumber(a,b, tableWidth, tableHeight):
    while isinstance(a, int) == False or isinstance(b, int) == False or a >= tableHeight or b >= tableWidth or check(a,b) == True:
        while a.isnumeric() == False or b.isnumeric() == False:
            print("You need to choose a number")
            a = input("Row -> ")
            b = input("Column -> ")
        a = int(a)
        b = int(b)
        if a >= tableHeight or b >= tableWidth:
            if a >= tableHeight and b >= tableWidth:
                print("Your column and row are outside the range of the table, please play again")
                a = input("Row -> ")
                b = input("Column -> ")
            elif a >= tableHeight:
                print("Your row is outside the range of the table, please play again")
                a = input("Row -> ")
                b = input("Column -> ")
            elif b >= tableWidth:
                print("Your column is outside the range of the table, please play again")
                a = input("Row -> ")
                b = input("Column -> ")
        elif check(a, b):
            print("This card was already revealed, please select a different one")
            a = input("Row -> ")
            b = input("Column -> ")
    return a, b

def Game():
    global p1
    global p2
    system('clear')
    print("Welcome to a memory game!")
    print("Please send a value for rows and columns, their multiplication can not be an odd number (memory games needs an even value of cards)")
    tableHeight = input("Table number of rows: ")
    tableWidth = input("Table number of columns: ")
    system('clear')
    tableSize, tableWidth, tableHeight = checkTable(tableHeight, tableWidth)

    p1 = 0
    p2 = 0
    points = int((tableSize)/2)
    turn = True
    print("Each player choose 2 cards on their turn, and if they match that player score a point")
    print("Cards keep revealed for 2.5 seconds after each player turn in case they do not match")
    print("You can go to https://github.com/luccab/python_memory to read more about the rules, to see this code or to contact me!")

    while points != 0:
        if turn:
            print("Player one it's your turn")
            print('First card:')
            row = input("Row -> ")
            column = input("Column -> ")
            row, column = checkNumber(row, column, tableWidth, tableHeight)
            unmask(row, column)

            print('Second card:')
            row1 = input("Row -> ")
            column1 = input("Column -> ")
            row1, column1 = checkNumber(row1, column1, tableWidth, tableHeight)
            unmask(row1, column1)

            if match(row, column, row1, column1):
                p1 += 1
                points -= 1
                turn = False
            else:
                sleep(2.5)
                masking(row,column,row1, column1)
                turn = False
            print("Scoreboard: ")
            print("Player 1 = ", p1)
            print("Player 2 = ", p2)
        else:
            print("Player two it's your turn")
            print('First card:')
            row = input("Row -> ")
            column = input("Column -> ")
            row, column = checkNumber(row, column, tableWidth, tableHeight)
            unmask(row,column)

            print('Second card:')
            row1 = input("Row -> ")
            column1 = input("Column -> ")
            row1, column1 = checkNumber(row1, column1, tableWidth, tableHeight)
            unmask(row1, column1)

            if match(row, column, row1, column1):
                p2 += 1
                points -= 1
                turn = True
            else:
                sleep(2.5)
                masking(row,column,row1, column1)
                turn = True
            print("Scoreboard: ")
            print("Player 1 = ", p1)
            print("Player 2 = ", p2)

    if p1 > p2:
        print("Congratulations Player 1 you won the game!")
        print( "Results:")
        print("Player 1: ", p1)
        print("Player 2: ", p2)
    elif p2 > p1:
        print("Congratulations Player 2 you won the game!")
        print( "Results:")
        print("Player 1: ", p1)
        print("Player 2: ", p2)
    elif p2 == p1:
        print("It was a tie")
        print( "Results:")
        print("Player 1: ", p1)
        print("Player 2: ", p2)

Game()
another = str(input("Do you want to play another Game ?[y/n]"))
while another == 'y':
    Game()
    another = str(input("Do you want to play another Game ?[y/n]"))
print("Thanks for playing!")
