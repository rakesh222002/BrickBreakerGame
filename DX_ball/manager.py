from layout import gameLayout
import time
class Manager:
    def __init__(self):
            self.time = 0
            self.score = 0
            self.lives = 3
            self.boss = 3
            self.level = 1
            self.iTime = time.time()
            self.sttime = time.time()
    def printData(self):
        gameLayout.pixels[2][1] = 'L'
        gameLayout.pixels[2][2] = 'I'
        gameLayout.pixels[2][3] = 'V'
        gameLayout.pixels[2][4] = 'E'
        gameLayout.pixels[2][5] = 'S'
        gameLayout.pixels[2][7] = '='
        gameLayout.pixels[2][9] = str(self.lives)
        gameLayout.pixels[2][25] = 'B'
        gameLayout.pixels[2][26] = 'O'
        gameLayout.pixels[2][27] = 'S'
        gameLayout.pixels[2][28] = 'S'
        gameLayout.pixels[2][29] = '='
        gameLayout.pixels[2][30] = str(self.boss)
        gameLayout.pixels[2][35] = 'L'
        gameLayout.pixels[2][36] = 'E'
        gameLayout.pixels[2][37] = 'V'
        gameLayout.pixels[2][38] = 'E'
        gameLayout.pixels[2][39] = 'L'
        gameLayout.pixels[2][40] = '='
        gameLayout.pixels[2][41] = str(self.level)
        gameLayout.pixels[2][80] = 'S'
        gameLayout.pixels[2][81] = 'C'
        gameLayout.pixels[2][82] = 'O'
        gameLayout.pixels[2][83] = 'R'
        gameLayout.pixels[2][84] = 'E'
        gameLayout.pixels[2][85] = '='
        gameLayout.pixels[2][86] = str(self.score)
        gameLayout.pixels[2][50] = 'T'
        gameLayout.pixels[2][51] = 'I'
        gameLayout.pixels[2][52] = 'M'
        gameLayout.pixels[2][53] = 'E'
        gameLayout.pixels[2][54] = '='
        gameLayout.pixels[2][55] = str(int(time.time() - self.sttime))
        gameLayout.pixels[2][99] = 'X'
gameManager = Manager()