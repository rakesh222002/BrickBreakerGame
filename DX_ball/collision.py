from layout import gameLayout
from manager import gameManager
from paddle import paddleCode
from powers import powerManager
from disBricks import allBricks
from powerTypes import powerType
from boss import boss
import os
import time

def powerReset():
    paddleCode.padlength = 15
    for i in range(0,gameLayout.width):
        gameLayout.pixels[gameLayout.length-4][i] = ' '
    powerType.counter = 3
    gameLayout.thruBall = 0

def brickCollision(x,y,type, sx):
    if type == 1:
        gameLayout.pixels[y][x] = ' '
        gameLayout.pixels[y][x-1] = ' '
        gameLayout.pixels[y][x+1] = ' '
        allBricks.bricks[y-allBricks.y][int((x - (allBricks.x+1))/3)] = "   "
        if x%5 == 0:
            powerManager.powers.append([x,y,'I',sx])
        elif x%5 ==1:
            powerManager.powers.append([x,y,'D',sx])
        elif x%5 ==2:
            powerManager.powers.append([x,y,'S',sx])
        elif x%5 ==3:
            powerManager.powers.append([x,y,'T',sx])
        elif x%5 ==4:
            powerManager.powers.append([x,y,'G',sx])
        for i in range(len(allBricks.special)):
            if allBricks.special[i][0] == (y-allBricks.y) and allBricks.special[i][1] == int((x - (allBricks.x+1))/3):
                allBricks.special.pop(i)
                break
    elif type == 2:
        gameLayout.pixels[y][x] = '1'
        gameLayout.pixels[y][x-1] = '['
        gameLayout.pixels[y][x+1] = ']'
        allBricks.bricks[y-allBricks.y][int((x - (allBricks.x+1))/3)] = "[1]"
        for i in range(len(allBricks.special)):
            if allBricks.special[i][0] == (y-allBricks.y) and allBricks.special[i][1] == int((x - (allBricks.x+1))/3):
                allBricks.special.pop(i)
                break
    elif type == 3:
        gameLayout.pixels[y][x] = '2'
        gameLayout.pixels[y][x-1] = '['
        gameLayout.pixels[y][x+1] = ']'
        allBricks.bricks[y-allBricks.y][int((x - (allBricks.x+1))/3)] = "[2]"
        for i in range(len(allBricks.special)):
            if allBricks.special[i][0] == (y-allBricks.y) and allBricks.special[i][1] == int((x - (allBricks.x+1))/3):
                allBricks.special.pop(i)
                break
def collision(x, y, speedX, speedY):
    collisionVal = "-1"
    if y.is_integer() and x.is_integer():
        gameLayout.pixels[int(y)][int(x)] = ' '
    nextX = x + speedX
    nextY = y - speedY
    if nextX.is_integer() and nextY.is_integer():
        px = int(x)
        py = int(y)
        nextX = int(nextX)
        nextY = int(nextY)
        if nextY < 5:
            collisionVal = "INV-Y"
            os.system("aplay sound/paddle.wav -q &")
        elif nextX > gameLayout.width - 2 or nextX < 1:
            collisionVal = "INV-X"
            os.system("aplay sound/paddle.wav -q &")
        elif nextY > gameLayout.length - 2:
            gameManager.lives -= 1
            for i in range(0,gameLayout.width):
                gameLayout.pixels[gameLayout.length-2][i] = ' ' 
            gameLayout.startFlag = 0
            powerReset()
            if gameManager.lives == 0:
                print("Score : ",end="")
                print(gameManager.score)
                quit()
        elif gameLayout.pixels[nextY][px] == 'Z' or gameLayout.pixels[nextY][nextX] == 'Z':
            collisionVal = 'INV-Y'
            os.system("aplay sound/paddle.wav -q &")
            if (time.time() - gameManager.iTime)>30:
                allBricks.brickMotion()

        elif gameLayout.thruBall == 1:
            if gameLayout.pixels[nextY][nextX] == '[':
                brickCollision(nextX+1,nextY,1, speedX)
                gameManager.score+=5
                os.system("aplay sound/paddle.wav -q &")
            elif gameLayout.pixels[nextY][nextX] == '1' or gameLayout.pixels[nextY][nextX] == '2' or gameLayout.pixels[nextY][nextX] == '3' or gameLayout.pixels[nextY][nextX] == 'U':
                brickCollision(nextX,nextY,1, speedX)
                gameManager.score+=5
                os.system("aplay sound/paddle.wav -q &")
            elif gameLayout.pixels[nextY][nextX] == ']':
                brickCollision(nextX-1,nextY,1, speedX)
                gameManager.score+=5
                os.system("aplay sound/paddle.wav -q &")
        elif gameLayout.pixels[nextY][px] == '[' and gameLayout.pixels[py][nextX] == ']':
            if gameLayout.pixels[nextY][px+1] != 'U':
                brickCollision(px+1,nextY,int(gameLayout.pixels[nextY][px+1]), speedX)
            elif gameLayout.pixels[py][nextX-1] != 'U':
                brickCollision(nextX-1,py,int(gameLayout.pixels[py][nextX-1]), speedX)
                gameManager.score+=5
            collisionVal = "INV-X+INV-Y"
            os.system("aplay sound/paddle.wav -q &")
        elif gameLayout.pixels[nextY][px] == ']' and gameLayout.pixels[py][nextX] == '[':
            if gameLayout.pixels[nextY][px-1] != 'U':
                brickCollision(px-1,nextY,int(gameLayout.pixels[nextY][px-1]), speedX)
            elif gameLayout.pixels[py][nextX+1] != 'U':
                brickCollision(nextX+1,py,int(gameLayout.pixels[py][nextX+1]), speedX)
                gameManager.score+=5
            collisionVal = "INV-X+INV-Y"
            os.system("aplay sound/paddle.wav -q &")
        elif gameLayout.pixels[nextY][px] == '1' or gameLayout.pixels[nextY][px] == '2' or gameLayout.pixels[nextY][px] == '3' or gameLayout.pixels[nextY][px] == 'U':
            if gameLayout.pixels[nextY][px] != 'U':
                brickCollision(px,nextY,int(gameLayout.pixels[nextY][px]), speedX)
                gameManager.score+=5
            collisionVal = "INV-Y"
            os.system("aplay sound/paddle.wav -q &")
        elif gameLayout.pixels[py][nextX] == '[' or gameLayout.pixels[py][nextX] == ']':
            if gameLayout.pixels[py][nextX] == '[':
                if gameLayout.pixels[py][nextX+1] != 'U':
                    brickCollision(nextX+1,py,int(gameLayout.pixels[py][nextX+1]), speedX)
                    gameManager.score+=5
            elif gameLayout.pixels[py][nextX] == ']':
                if gameLayout.pixels[py][nextX-1] != 'U':
                    brickCollision(nextX-1,py,int(gameLayout.pixels[py][nextX-1]), speedX)
                    gameManager.score+=5
            collisionVal = "INV-X"
            os.system("aplay sound/paddle.wav -q &")
        elif gameLayout.pixels[nextY][px] == '[' or gameLayout.pixels[nextY][px] == ']':
            if gameLayout.pixels[nextY][px] == '[':
                if gameLayout.pixels[nextY][px+1] != 'U':
                    brickCollision(px+1,nextY,int(gameLayout.pixels[nextY][px+1]), speedX)
                    gameManager.score+=5
            elif gameLayout.pixels[nextY][px] == ']':
                if gameLayout.pixels[nextY][px-1] != 'U':
                    brickCollision(px-1,nextY,int(gameLayout.pixels[nextY][px-1]), speedX)
                    gameManager.score+=5
            collisionVal = "INV-Y"
            os.system("aplay sound/paddle.wav -q &")
        elif gameLayout.pixels[nextY][nextX] == '[' or gameLayout.pixels[nextY][nextX] == ']':
            if gameLayout.pixels[nextY][nextX] == '[':
                if gameLayout.pixels[nextY][nextX+1] != 'U':
                    brickCollision(nextX+1,nextY,int(gameLayout.pixels[nextY][nextX+1]), speedX)
                    gameManager.score+=5
            elif gameLayout.pixels[nextY][nextX] == ']':
                if gameLayout.pixels[nextY][nextX-1] != 'U':
                    brickCollision(nextX-1,nextY,int(gameLayout.pixels[nextY][nextX-1]), speedX)
                    gameManager.score+=5
            collisionVal = "INV-Y"
            os.system("aplay sound/paddle.wav -q &")
        elif gameLayout.pixels[nextY][nextX] == '1' or gameLayout.pixels[nextY][nextX] == '2' or gameLayout.pixels[nextY][nextX] == '3' or gameLayout.pixels[nextY][nextX] == 'U':
            if gameLayout.pixels[nextY][nextX-1] != 'U':
                brickCollision(nextX,nextY,int(gameLayout.pixels[nextY][nextX]), speedX)
                gameManager.score+=5
            collisionVal = 'INV-Y'
            os.system("aplay sound/paddle.wav -q &")
        elif gameLayout.pixels[nextY][nextX] == '-':
            collisionVal = 'INV-Y'
            gameManager.boss-=1
        elif gameLayout.pixels[nextY][nextX] == '/' or gameLayout.pixels[nextY][nextX] == '\\' or gameLayout.pixels[nextY][nextX] == '|':
            collisionVal = 'INV-X'
            gameManager.boss-=1
        if gameManager.boss == 0:
            print("congragulations and celebrations")
            gameManager.score+=50
            print(gameManager.score)
            quit()
    return collisionVal