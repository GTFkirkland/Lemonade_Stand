#X = floor/collision
#_ = empty
#C = kill spot/enemy
#8 = player
#E = win spot
from time import sleep
import random
#bot func
def getBot(level1):
    run = False
    while run == False:
        try:
            run = True
            global botLocations
            botLocations = [['N/A', random.randint(-15,-2)],['N/A', random.randint(-15,-2)],['N/A', random.randint(-15,-2)]]
            for i in range(0,3):
                if botLocations[i][1] < -8:
                    botLocations[i][0] = random.randint(1,14)
                else:
                    botLocations[i][0] = random.randint(9,14)
    
            if (level1[botLocations[0][1]][botLocations[0][0]] == 'X' or level1[botLocations[0][1]][botLocations[0][0]] == 'C') or (level1[botLocations[1][1]][botLocations[1][0]] == 'X' or level1[botLocations[1][1]][botLocations[1][0]] == 'C') or (level1[botLocations[2][1]][botLocations[2][0]] == 'X' or level1[botLocations[2][1]][botLocations[2][0]] == 'C'):
                while level1[botLocations[0][1]][botLocations[0][0]] == 'X' or level1[botLocations[1][1]][botLocations[1][0]] == 'X' or level1[botLocations[2][1]][botLocations[2][0]] == 'X':
                    botLocations = [['N/A', random.randint(-15,-2)],['N/A', random.randint(-15,-2)],['N/A', random.randint(-15,-2)]]
                    for i in range(0,2):
                        if botLocations[i][1] < -8:
                            botLocations[i][0] = random.randint(1,14)
                        else:
                            botLocations[i][0] = random.randint(9,14)
        except:
            run = False

def moveBot(level1, playerLocation, botNumber):
    global botLocations
    move = 'N/A'
    if botLocations[botNumber][0] == playerLocation[0]:
        move = 'vert'
    
    elif botLocations[botNumber][1] == playerLocation[1]:
        move = 'horo'
    
    else:
        if random.randint(1,2) == 1: #horo move
            move = 'horo'
        else: #vert move
            move = 'vert'
    
    while True:
        if move == 'horo':
            copy = botLocations[botNumber][0]
            if playerLocation[0] < botLocations[botNumber][0]:
                level1[botLocations[botNumber][1]][botLocations[botNumber][0]] = '_'
                botLocations[botNumber][0] = botLocations[botNumber][0]-1
            else:
                level1[botLocations[botNumber][1]][botLocations[botNumber][0]] = '_'
                botLocations[botNumber][0] = botLocations[botNumber][0]+1
            if level1[botLocations[botNumber][1]][botLocations[botNumber][0]] == 'X':
                level1[botLocations[botNumber][1]][botLocations[botNumber][0]] = 'X'
                botLocations[botNumber][0] = copy
                move = 'vert'
            else:
                break
        else:
            copy = botLocations[botNumber][1]
            if playerLocation[1] < botLocations[botNumber][1]:
                level1[botLocations[botNumber][1]][botLocations[botNumber][0]] = '_'
                botLocations[botNumber][1] = botLocations[botNumber][1]-1
            else:
                level1[botLocations[botNumber][1]][botLocations[botNumber][0]] = '_'
                botLocations[botNumber][1] = botLocations[botNumber][1]+1
            if level1[botLocations[botNumber][1]][botLocations[botNumber][0]] == 'X':
                level1[botLocations[botNumber][1]][botLocations[botNumber][0]] = 'X'
                botLocations[botNumber][1] = copy
                move = 'horo'
            else:
                break
    level1[botLocations[botNumber][1]][botLocations[botNumber][0]] = 'C'
    return level1
        






def minigame():
    global botLocations
    level = random.randint(1,2)
    if level == 1:
        level1 = [
            ['X','X','X','X','X','X','X','E','E','X','X','X','X','X','X','X'],
            ['X','_','_','_','_','_','_','_','_','_','_','_','_','_','_','X'],
            ['X','_','_','_','X','_','_','_','_','_','_','_','_','_','_','X'],
            ['X','_','_','_','X','_','_','_','_','_','_','_','_','_','_','X'],
            ['X','_','_','_','X','X','X','X','X','X','_','_','_','_','_','X'],
            ['X','_','_','_','_','_','_','_','_','_','_','_','_','_','_','X'],
            ['X','_','_','_','_','_','_','_','_','_','_','_','_','_','_','X'],
            ['X','_','_','_','_','_','_','_','_','_','_','X','_','_','_','X'],
            ['X','_','_','_','_','_','_','_','_','_','_','X','_','_','_','X'],
            ['X','_','_','_','_','_','_','X','_','_','_','X','_','_','_','X'],
            ['X','_','_','_','_','_','_','_','_','_','_','X','_','_','_','X'],
            ['X','_','_','_','_','_','_','_','_','_','_','X','_','_','_','X'],
            ['X','_','_','_','_','_','_','_','_','_','_','X','_','_','_','X'],
            ['X','_','_','_','_','_','_','_','_','_','_','_','_','_','_','X'],
            ['X','8','_','_','_','_','_','_','_','_','_','_','_','_','_','X'],
            ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
        ]
    else:
        level1 = [
            ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
            ['X','_','_','_','_','_','_','_','_','_','_','_','_','_','_','X'],
            ['X','_','_','_','_','_','_','_','_','_','_','_','_','_','_','X'],
            ['X','_','_','_','_','_','_','_','_','_','_','_','_','_','_','X'],
            ['X','_','_','_','_','_','_','_','_','_','_','_','_','_','X','X'],
            ['X','_','_','_','_','_','_','_','_','_','_','_','X','_','_','X'],
            ['X','_','_','X','X','X','X','X','_','_','_','_','X','_','_','X'],
            ['X','_','_','_','_','_','_','_','_','_','_','_','X','_','_','E'],
            ['X','_','_','_','_','_','_','_','_','_','_','_','_','_','_','E'],
            ['X','_','_','_','_','_','_','_','_','_','_','_','_','_','_','X'],
            ['X','_','_','_','_','_','_','_','X','_','_','_','_','_','_','X'],
            ['X','_','_','_','_','_','_','_','X','_','_','_','_','_','_','X'],
            ['X','_','_','_','_','_','_','_','X','_','_','_','_','_','_','X'],
            ['X','_','_','_','_','_','_','_','_','_','_','_','_','_','_','X'],
            ['X','8','_','_','_','_','_','_','_','_','_','_','X','_','_','X'],
            ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
        ]
    #board = x: 1 -> 14 /y: -2 -> -15
    playerLocation = [1,-2]
    # botLocations = [[random.randint(-15,-2), random.randint(9,14)],[random.randint(-15,-9), random.randint(9,14)],[random.randint(-15,9), random.randint(9,14)]]
    #getting bots
    getBot(level1)
    level1[botLocations[0][1]][botLocations[0][0]] = 'C'
    level1[botLocations[1][1]][botLocations[1][0]] = 'C'
    level1[botLocations[2][1]][botLocations[2][0]] = 'C'
    
    row = 0
    answer = 'N/A'

    while True:
        for i in range(100):
            print("")
        print("You/Player: 8")
        print("Police: C")
        print("Wall: X")
        print("Exit (North or East)")
        print("AVOID THE POLICE, FIND THE EXIT(E) WITH wasd")
        for row in range(0,16):
            print(level1[row])
        print(playerLocation)
        print(botLocations)
        answer = input('Move: ')

        if (answer == 'w') or (answer == 'W'):
            if level1[playerLocation[1]-1][playerLocation[0]] == '_':
                level1[playerLocation[1]][playerLocation[0]] = '_'
                playerLocation[1] = playerLocation[1]-1
                level1[playerLocation[1]][playerLocation[0]] = '8'

        if (answer == 's') or (answer == 'S'):
            if level1[playerLocation[1]+1][playerLocation[0]] == '_':
                level1[playerLocation[1]][playerLocation[0]] = '_'
                playerLocation[1] = playerLocation[1]+1
                level1[playerLocation[1]][playerLocation[0]] = '8'

        if (answer == 'd') or (answer == 'D'):
            if level1[playerLocation[1]][playerLocation[0]+1] == '_':
                level1[playerLocation[1]][playerLocation[0]] = '_'
                playerLocation[0] = playerLocation[0]+1
                level1[playerLocation[1]][playerLocation[0]] = '8'

        if (answer == 'a') or (answer == 'A'):
            if level1[playerLocation[1]][playerLocation[0]-1] == '_':
                level1[playerLocation[1]][playerLocation[0]] = '_'
                playerLocation[0] = playerLocation[0]-1
                level1[playerLocation[1]][playerLocation[0]] = '8'

        #bot movement
        level1 = moveBot(level1, playerLocation, 0)
        level1 = moveBot(level1, playerLocation, 1)
        level1 = moveBot(level1, playerLocation, 2)
        
        if (level1[playerLocation[1]+1][playerLocation[0]] == 'C') or (level1[playerLocation[1]-1][playerLocation[0]] == 'C') or (level1[playerLocation[1]][playerLocation[0]+1] == 'C') or (level1[playerLocation[1]][playerLocation[0]-1] == 'C') or (level1[playerLocation[1]][playerLocation[0]] in botLocations):
            health = 0
            for i in range(100):
                print("")
            print("You died...")
            for row in range(0,16):
                print(level1[row])
            break

        if (level1[playerLocation[1]+1][playerLocation[0]] == 'E') or (level1[playerLocation[1]-1][playerLocation[0]] == 'E') or (level1[playerLocation[1]][playerLocation[0]+1] == 'E') or (level1[playerLocation[1]][playerLocation[0]-1] == 'E'):
            for i in range(100):
                print("")
            print("YOU FOUND THE EXIT")
            for row in range(0,16):
                print(level1[row])
            print("exiting...")
            sleep(0.1)
            health = 1
            break
    return health
minigame()