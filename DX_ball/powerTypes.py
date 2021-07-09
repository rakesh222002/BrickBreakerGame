from paddle import paddleCode
from layout import gameLayout
import time
class initPower():
    def __init__(self):
        self.power = '?'
        self.startTime = 0
        self.counter = 3
    def addPower(self):
        self.power = '?'
        return self.power
class decreasePad(initPower):
    def addPower(self):
        if paddleCode.padlength>5:
            paddleCode.padlength-=3
            for i in range(0,gameLayout.width):
                gameLayout.pixels[gameLayout.length-4][i] = ' '
        self.power = 'D'

class increasePad(initPower):
    def addPower(self):
        if paddleCode.padlength<25:
            paddleCode.padlength+=3
            for i in range(0,gameLayout.width):
                gameLayout.pixels[gameLayout.length-4][i] = ' '
            if paddleCode.x+paddleCode.padlength >= gameLayout.width-1:
                paddleCode.x = gameLayout.width - paddleCode.padlength
        self.power = 'I'

class increaseSpeed(initPower):
    def addPower(self):
        if self.counter > 1:
            self.counter -= 1
            self.power = 'S'

class thruBall(initPower):
    def addPower(self):
        gameLayout.thruBall = 1

'''class paddleGrab(initPower):
    def addPower(self):
        gameLayout.startFlag = 1'''

powerType = initPower()