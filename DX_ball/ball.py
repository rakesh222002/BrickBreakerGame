from layout import gameLayout
from paddle import paddleCode
from collision import collision
from boss import boss
from manager import gameManager
import random
import time
class Ball:

    def __init__(self,x,y):
        self.speedX = 1
        self.speedY = 1
        self.x = float(x)
        self.y = float(y)
        self.rand = random.randint(0,paddleCode.padlength-1)
        gameLayout.pixels[int(self.x)][int(self.y)] = 'O'
    def moveBall(self):
        if gameLayout.startFlag != 1:
            for i in range(0,gameLayout.width):
                gameLayout.pixels[gameLayout.length-5][i] = ' '
            gameLayout.pixels[gameLayout.length-5][int(paddleCode.x + self.rand)] = 'O'
            self.y = float(gameLayout.length-5)
            self.x = float(int(paddleCode.x + self.rand))
            gameManager.iTime = time.time()
        else:
            decider = collision(self.x, self.y, self.speedX, self.speedY)
            if decider == "INV-X":
                self.speedX = -self.speedX
            elif decider == "INV-Y":
                self.speedY = -self.speedY
            elif decider == "INV-X+INV-Y":
                self.speedX = -self.speedX
                self.speedY = -self.speedY
            if gameLayout.pixels[int(self.y-self.speedY)][int(self.x+self.speedX)] == ' ':
                self.x += self.speedX
                self.y -= self.speedY
            if gameLayout.startFlag == 1:
                boss.ballx = int(self.x)
                boss.bally = int(self.y)
                gameLayout.pixels[int(self.y)][int(self.x)] = 'O'