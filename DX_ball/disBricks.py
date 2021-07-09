from brick import BrickTypes
from layout import gameLayout
import random
import time
class AllBricks:
    def __init__(self):
        self.y = 10
        self.rows = 8
        self.cols = 16
        self.x = 10
        self.special = []
        self.bricks = [[] for i in range(0,self.rows)]
    def addBricks(self):
        for i in range(self.y,self.y + self.rows):
            for j in range(self.x, self.x+(3*self.cols)):
                if j%3 == 2:
                    if j%9 == 2:
                        if random.uniform(0,1)<0.2:
                            self.special.append([i-self.y, int((j-self.x)/3)])
                        rnum = random.randint(1,3)    
                        brick = BrickTypes(str(rnum))
                    if j%9 == 5:
                        brick = BrickTypes(' ')
                    if j%9 == 8:
                        brick = BrickTypes(' ')
                    if i%3 == 0 and (j%9 == 8 or j%9==5 and j!=(self.x+(3*self.cols)-1)):
                        brick = BrickTypes('U')
                    #if j == 23 or j == 65:
                    #    brick = BrickTypes('B')
                    self.bricks[i-self.y].append(brick.addBrick())
    def addBricks2(self):
        self.bricks = [[] for i in range(0,self.rows)]
        self.special = []
        for i in range(self.y,self.y + self.rows):
            for j in range(self.x, self.x+(3*self.cols)):
                if j%3 == 2:
                    if j%9 == 2:
                        if random.uniform(0,1)<0.2:
                            self.special.append([i-self.y, int((j-self.x)/3)])
                        rnum = random.randint(1,3)    
                        brick = BrickTypes(str(rnum))
                    if j%9 == 5:
                        brick = BrickTypes(' ')
                    if j%9 == 8:
                        if random.uniform(0,1)<0.2:
                            self.special.append([i-self.y, int((j-self.x)/3)])
                        rnum = random.randint(1,3)    
                        brick = BrickTypes(str(rnum))
                    if i%3 == 0 and (j%9 == 8 or j%9==5 and j!=(self.x+(3*self.cols)-1)):
                        brick = BrickTypes('U')
                    #if j == 23 or j == 65:
                    #    brick = BrickTypes('B')
                    self.bricks[i-self.y].append(brick.addBrick())
    def addBricks3(self):
        self.special = []
        self.bricks = [[] for i in range(0,self.rows)]
        for i in range(self.y,self.y + self.rows):
            for j in range(self.x, self.x+(3*self.cols)):
                if j%3 == 2:
                    if random.uniform(0,1)<0.2:
                        brick = BrickTypes('U')
                        self.bricks[i-self.y].append(brick.addBrick())
                    else:
                        brick = BrickTypes(' ')
                        self.bricks[i-self.y].append(brick.addBrick()) 
    def displayBricks(self):
        for i in range(self.y, self.rows+self.y):
            for j in range(self.x, self.x+(3*self.cols)):
                if j%3 == 2:
                    gameLayout.pixels[i][j] = self.bricks[i-self.y][int((j-self.x)/3)][0]
                    gameLayout.pixels[i][j+1] = self.bricks[i-self.y][int((j-self.x)/3)][1]
                    gameLayout.pixels[i][j+2] = self.bricks[i-self.y][int((j-self.x)/3)][2]
    def brickMotion(self):
        for j in range(0, gameLayout.width):
            gameLayout.pixels[self.y][j] = ' '
            if gameLayout.pixels[gameLayout.length - 6][j] == '[':
                print("GAME OVER YOU FOOL")
                quit()
        self.y+=1
    def endCond(self):
        for i in range(self.y,self.y + self.rows):
            for j in range(self.x, self.x+(3*self.cols)):
                if j%3 == 2:
                    if self.bricks[i-self.y][int((j-self.x)/3)][1] == '1' or  self.bricks[i-self.y][int((j-self.x)/3)][1] == '2' or self.bricks[i-self.y][int((j-self.x)/3)][1] == '3':
                        return 0
        return 1
    def cleanBricks(self):
        self.bricks = [[] for i in range(0,self.rows)]
        self.special = []
        for i in range(self.y,self.y + self.rows):
            for j in range(self.x, self.x+(3*self.cols)):
                if j%3 == 2:
                    self.bricks[i-self.y].append('   ')

        for i in range(0, gameLayout.length-5):
            for j in range(0,gameLayout.width):
                gameLayout.pixels[i][j] = ' '

    def rainbowBricks(self):
        for i in range(len(self.special)):
            rnum = random.randint(1,3)    
            brick = BrickTypes(str(rnum))
            self.bricks[self.special[i][0]][self.special[i][1]] = brick.addBrick()

allBricks = AllBricks()