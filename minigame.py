from time import sleep
import random

#make courds positivees
def convertY(y):
    return y + 16

#bot func
def getBot(level1):
    run = False
    while run == False:
        try:
            run = True
            global botLocations
            botLocations = [['N/A', convertY(random.randint(-15,-2))],
                            ['N/A', convertY(random.randint(-15,-2))],
                            ['N/A', convertY(random.randint(-15,-2))]]

            for i in range(3):
                if botLocations[i][1] < convertY(-8):
                    botLocations[i][0] = random.randint(1,14)
                else:
                    botLocations[i][0] = random.randint(9,14)

            #wall things
            if (level1[botLocations[0][1]][botLocations[0][0]] in ['X','C'] or level1[botLocations[1][1]][botLocations[1][0]] in ['X','C'] or level1[botLocations[2][1]][botLocations[2][0]] in ['X','C']):
                while (level1[botLocations[0][1]][botLocations[0][0]] == 'X' or level1[botLocations[1][1]][botLocations[1][0]] == 'X' or level1[botLocations[2][1]][botLocations[2][0]] == 'X'):
                    botLocations = [['N/A', convertY(random.randint(-15,-2))], ['N/A', convertY(random.randint(-15,-2))], ['N/A', convertY(random.randint(-15,-2))]]
                    for i in range(3):
                        if botLocations[i][1] < convertY(-8):
                            botLocations[i][0] = random.randint(1,14)
                        else:
                            botLocations[i][0] = random.randint(9,14)

        except:
            run = False


def moveBot(level1, playerLocation, botNumber):
    global botLocations
    crashTest = 0
    move = 'N/A'

    if botLocations[botNumber][0] == playerLocation[0]:
        move = 'vert'
    elif botLocations[botNumber][1] == playerLocation[1]:
        move = 'horo'
    else:
        move = 'horo' if random.randint(1,2) == 1 else 'vert'

    while True:
        if move == 'horo':
            copy = botLocations[botNumber][0]
            if playerLocation[0] < botLocations[botNumber][0]:
                level1[botLocations[botNumber][1]][botLocations[botNumber][0]] = '_'
                botLocations[botNumber][0] -= 1
            else:
                level1[botLocations[botNumber][1]][botLocations[botNumber][0]] = '_'
                botLocations[botNumber][0] += 1

            if level1[botLocations[botNumber][1]][botLocations[botNumber][0]] == 'X' or level1[botLocations[botNumber][1]][botLocations[botNumber][0]] == 'C':
                botLocations[botNumber][0] = copy
                move = 'vert'
                crashTest += 1
                if crashTest > 10:
                    break
            else:
                break

        else:
            copy = botLocations[botNumber][1]
            if playerLocation[1] < botLocations[botNumber][1]:
                level1[botLocations[botNumber][1]][botLocations[botNumber][0]] = '_'
                botLocations[botNumber][1] -= 1
            else:
                level1[botLocations[botNumber][1]][botLocations[botNumber][0]] = '_'
                botLocations[botNumber][1] += 1

            if level1[botLocations[botNumber][1]][botLocations[botNumber][0]] == 'X' or level1[botLocations[botNumber][1]][botLocations[botNumber][0]] == 'C':
                botLocations[botNumber][1] = copy
                move = 'horo'
                crashTest += 1
                if crashTest > 10:
                    break
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

    #player stuff
    playerLocation = [1, 14]

    getBot(level1)

    level1[botLocations[0][1]][botLocations[0][0]] = 'C'
    level1[botLocations[1][1]][botLocations[1][0]] = 'C'
    level1[botLocations[2][1]][botLocations[2][0]] = 'C'

    answer = 'N/A'

    while True:
        for i in range(100):
            print("")
        print("You/Player: 8 (bottom left)")
        print("Police: C")
        print("Wall: X")
        print("Exit (North or East)")
        print("AVOID THE POLICE, FIND THE EXIT(E) WITH wasd")

        for row in range(0,16):
            print(level1[row])

        print(playerLocation)
        print(botLocations)

        answer = input('Move: ')

        #movement
        if answer.lower() == 'w':
            if level1[playerLocation[1]-1][playerLocation[0]] == '_':
                level1[playerLocation[1]][playerLocation[0]] = '_'
                playerLocation[1] -= 1
                level1[playerLocation[1]][playerLocation[0]] = '8'

        elif answer.lower() == 's':
            if level1[playerLocation[1]+1][playerLocation[0]] == '_':
                level1[playerLocation[1]][playerLocation[0]] = '_'
                playerLocation[1] += 1
                level1[playerLocation[1]][playerLocation[0]] = '8'

        elif answer.lower() == 'd':
            if level1[playerLocation[1]][playerLocation[0]+1] == '_':
                level1[playerLocation[1]][playerLocation[0]] = '_'
                playerLocation[0] += 1
                level1[playerLocation[1]][playerLocation[0]] = '8'

        elif answer.lower() == 'a':
            if level1[playerLocation[1]][playerLocation[0]-1] == '_':
                level1[playerLocation[1]][playerLocation[0]] = '_'
                playerLocation[0] -= 1
                level1[playerLocation[1]][playerLocation[0]] = '8'

        #bot movement
        level1 = moveBot(level1, playerLocation, 0)
        level1 = moveBot(level1, playerLocation, 1)
        level1 = moveBot(level1, playerLocation, 2)

        #exit
        if (level1[playerLocation[1]+1][playerLocation[0]] == 'E' or level1[playerLocation[1]-1][playerLocation[0]] == 'E' or level1[playerLocation[1]][playerLocation[0]+1] == 'E' or level1[playerLocation[1]][playerLocation[0]-1] == 'E'):
            for i in range(100):
                print("")
            for row in range(0,16):
                print(level1[row])
            print("You found the EXIT and escaped the police!✅")
            print("exiting...")
            sleep(0.1)
            return 1
        #death
        elif (level1[playerLocation[1]+1][playerLocation[0]] == 'C' or level1[playerLocation[1]-1][playerLocation[0]] == 'C' or level1[playerLocation[1]][playerLocation[0]+1] == 'C' or level1[playerLocation[1]][playerLocation[0]-1] == 'C' or playerLocation in botLocations):
            for i in range(100):
                print("")
            for row in range(0,16):
                print(level1[row])
            print("You were caught and arrested!🚫")
            print("exiting...")
            sleep(0.1)
            return 0

