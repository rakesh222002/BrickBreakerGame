import os
import time
from layout import gameLayout
from paddle import paddleCode
from ball import Ball
from manager import gameManager
from disBricks import allBricks
from powers import powerManager
from powerTypes import powerType
from boss import boss
import time
from collision import powerReset
ball = Ball(30, gameLayout.length-5)
print("DX ball")
print("")
startGame = input("Press any Key to Start")
level = 0
gameManager.printData()
gameLayout.printData()
allBricks.addBricks()
paddleCode.createPaddle()
lifeCount = gameManager.lives
counter = powerType.counter
end = 0
#initial state
levelcheat = -1
while True:
    os.system("tput reset")
    if gameManager.lives == (lifeCount-1):
        #initial state
        ball = Ball(30, gameLayout.length-5)
        lifeCount = gameManager.lives
    paddleCode.createPaddle()
    allBricks.displayBricks()
    if counter == 0:
        ball.moveBall()
        allBricks.rainbowBricks()
        powerManager.setCoods()
        if gameManager.level==3:
            boss.dropBullet()
        counter = powerType.counter
    gameManager.printData()
    gameLayout.printData()
    if gameManager.level<3:
        end = allBricks.endCond()
    if end==1 or levelcheat==1:
        allBricks.cleanBricks()
        if gameManager.level == 1:
            allBricks.x = 50
            allBricks.y = 10 
            allBricks.addBricks2()
            gameManager.level +=1
            ball = Ball(30, gameLayout.length-5)
            for i in range(0,gameLayout.width):
                gameLayout.pixels[gameLayout.length-4][i] = ' '
            paddleCode.x = 28
            paddleCode.y = gameLayout.length - 4
        elif gameManager.level == 2: 
            gameManager.level +=1
            allBricks.y = 10
            allBricks.x = 25 
            allBricks.addBricks3()
            ball = Ball(30, gameLayout.length-5)
            for i in range(0,gameLayout.width):
                gameLayout.pixels[gameLayout.length-4][i] = ' '
            paddleCode.x = 28
            paddleCode.y = gameLayout.length - 4
        elif gameManager.level == 3:
            print('Game Over')
            print('score : ', end ="")
            print(gameManager.score)
            quit()
        gameManager.iTime = time.time()
        gameLayout.startFlag = 0
        powerReset()
        end = -1
        levelcheat = -1
    if gameManager.level==3:
        boss.displayBoss()
    levelcheat = paddleCode.paddleMovement()
    counter-=1