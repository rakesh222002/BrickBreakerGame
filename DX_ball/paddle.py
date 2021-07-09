from input import Get, input_to
from layout import gameLayout
import signal
class Paddle:
    def __init__(self):
        self.x = 28
        self.y = gameLayout.length - 4
        self.padlength = 15    
    def createPaddle(self):
        for i in range(0,self.padlength):
            gameLayout.pixels[self.y][self.x + i] = 'Z'
    def paddleMovement(self):
        input = input_to(Get())
        if input == 'a' and gameLayout.pixels[self.y][self.x - 1] != 'X':
            gameLayout.pixels[self.y][self.x + self.padlength -1] = ' '
            self.x -= 1
            self.createPaddle()
        if input == 'd' and gameLayout.pixels[self.y][self.x + self.padlength] != 'X':
            gameLayout.pixels[self.y][self.x] = ' '
            self.x += 1
            self.createPaddle()
        if input == ' ':
            gameLayout.startFlag = 1
        if input == 'l':
            return 1
        return 0
paddleCode = Paddle()