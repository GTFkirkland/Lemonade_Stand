#X = floor/collision
#_ = empty
#C = kill spot/enemy
#8 = player
#E = win spot
import random
def minigame():
    level = random.randint(1,2)
    if level == 1:
        level1 = [
            ['X','X','X','X','X','X','X','E','E','X','X','X','X','X','X','X'],
            ['X','_','_','_','_','_','_','_','_','_','_','_','_','_','_','X'],
            ['X','_','_','_','_','_','_','_','_','_','_','_','_','_','_','X'],
            ['X','_','_','_','_','_','_','_','_','_','_','_','_','_','_','X'],
            ['X','_','_','_','_','_','_','_','_','_','_','_','_','_','_','X'],
            ['X','_','_','_','_','_','_','_','_','_','_','_','_','_','_','X'],
            ['X','_','_','_','_','_','_','_','_','_','_','_','_','_','_','X'],
            ['X','_','_','_','_','_','_','_','_','_','_','_','_','_','_','X'],
            ['X','_','_','_','_','_','_','_','_','_','_','_','_','_','_','X'],
            ['X','_','_','_','_','_','_','_','_','_','_','_','_','_','_','X'],
            ['X','_','_','_','_','_','_','_','_','_','_','_','_','_','_','X'],
            ['X','_','_','_','_','_','_','_','_','_','_','_','_','_','_','X'],
            ['X','_','_','_','_','_','_','_','_','_','_','_','_','_','_','X'],
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
            ['X','_','_','_','_','_','_','_','_','_','_','_','_','_','_','X'],
            ['X','_','_','_','_','_','_','_','_','_','_','_','_','_','_','X'],
            ['X','_','_','_','_','_','_','_','_','_','_','_','_','_','_','X'],
            ['X','_','_','_','_','_','_','_','_','_','_','_','_','_','_','E'],
            ['X','_','_','_','_','_','_','_','_','_','_','_','_','_','_','E'],
            ['X','_','_','_','_','_','_','_','_','_','_','_','_','_','_','X'],
            ['X','_','_','_','_','_','_','_','_','_','_','_','_','_','_','X'],
            ['X','_','_','_','_','_','_','_','_','_','_','_','_','_','_','X'],
            ['X','_','_','_','_','_','_','_','_','_','_','_','_','_','_','X'],
            ['X','_','_','_','_','_','_','_','_','_','_','_','_','_','_','X'],
            ['X','8','_','_','_','_','_','_','_','_','_','_','_','_','_','X'],
            ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
        ]

    playerLocation = [1,-2]           #bot1                       /                     bot2                      /                   bot3
    botLocations = [[random.randint(-15,-9), random.randint(9,14)],[random.randint(9,14), random.randint(-15,-9)],[random.randint(9,14), random.randint(-15,-9)]]
    level1[botLocations[0][0]][botLocations[1][1]] = 'C'
    row = 0
    answer = 'N/A'

    while True:
        for i in range(100):
            print("")
        print("You: 8")
        print("Police: C")
        print("AVOID THE POLICE, FIND THE EXIT(E)")
        for row in range(0,16):
            print(level1[row])
        print(playerLocation)
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

        
        if level1[playerLocation[1]][playerLocation[0]] == 'C':
            health = 0
            break

        if (level1[playerLocation[1]+1][playerLocation[0]] == 'E') or (level1[playerLocation[1]-1][playerLocation[0]] == 'E') or (level1[playerLocation[1]][playerLocation[0]+1] == 'E') or (level1[playerLocation[0]][playerLocation[0]-1] == 'E'):
            health = 1
            break
    return health
minigame()