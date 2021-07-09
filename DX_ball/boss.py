from layout import gameLayout
from paddle import paddleCode
from manager import gameManager
from powerTypes import powerType
import time
def powerReset():
    paddleCode.padlength = 15
    for i in range(0,gameLayout.width):
        gameLayout.pixels[gameLayout.length-4][i] = ' '
    powerType.counter = 3
    gameLayout.thruBall = 0

class Boss:
    def __init__(self):
        self.boss = [[] for i in range(0,4)]
        self.time = time.time()
        self.bullets = []
        self.lives = 3
        self.ballx = 0
        self.bally = 0
        for i in range(4):
            for j in range(8):
                self.boss[i].append(' ')
        for i in range(4):
            if i%2==0:
                self.boss[0][3+i] = '/'
            else:
                self.boss[0][3+i] = '\\'
        self.boss[1][3] = '|'
        self.boss[1][4] = '|'
        self.boss[1][5] = '|'
        self.boss[1][6] = '|'
        self.boss[2][2] = '/'
        for i in range(3,7):
            self.boss[2][i] = '-'
        self.boss[2][7] = '\\'
        for i in range(2,8):
            self.boss[3][i] = '-'
    def displayBoss(self):
        if paddleCode.x+8+int(paddleCode.padlength/4) < gameLayout.width:
            for i in range(4):
                for j in range(gameLayout.width):
                    gameLayout.pixels[5+i][j] = ' '
            for i in range(4):
                for j in range(8):
                    gameLayout.pixels[5+i][paddleCode.x+int(paddleCode.padlength/4)+j] = self.boss[i][j]
    def dropBullet(self):
        if (time.time()-self.time) % 5 < 0.2:
            self.bullets.append([paddleCode.x+int(paddleCode.padlength/4)+4, 8])
        for i in range(len(self.bullets)):
            gameLayout.pixels[self.bullets[i][1]][self.bullets[i][0]] = ' '
            self.bullets[i][1] += 1
            if gameLayout.pixels[self.bullets[i][1]][self.bullets[i][0]] == 'Z':
                gameManager.lives -= 1
                gameLayout.startFlag = 0
                gameLayout.pixels[self.bally][self.ballx] = ' '
                powerReset()
                if gameManager.lives == 0:
                    print("Score : ",end="")
                    print(gameManager.score)
                    quit()
            elif self.bullets[i][1] > gameLayout.length-4:
                self.bullets.pop(i)
                break
            else: 
                gameLayout.pixels[self.bullets[i][1]][self.bullets[i][0]] = 'B'
boss = Boss()
                