from layout import gameLayout
from powerTypes import powerType, decreasePad, increasePad, increaseSpeed, thruBall
import os
class Power:
    def __init__(self):
        self.powers = []
    def setCoods(self):
        for i in range(0,len(self.powers)):
            self.powers[i][1]+=1
            self.powers[i][0]+=self.powers[i][3]
            gameLayout.pixels[self.powers[i][1]-1][self.powers[i][0]-self.powers[i][3]] = ' '
            gameLayout.pixels[self.powers[i][1]][self.powers[i][0]] = self.powers[i][2]
            if self.powers[i][1] > gameLayout.length - 3:
                gameLayout.pixels[self.powers[i][1]][self.powers[i][0]] = ' '
                self.powers.pop(i)
                break
            elif gameLayout.pixels[self.powers[i][1]+1][self.powers[i][0]] == 'Z':
                #gameLayout.pixels[5][6] = 'Power'
                os.system("aplay sound/powerup.wav -q &")
                if self.powers[i][2] == 'I':
                    increasePad.addPower(powerType)
                elif self.powers[i][2] == 'D':
                    decreasePad.addPower(powerType)
                elif self.powers[i][2] == 'S':
                    increaseSpeed.addPower(powerType)
                elif self.powers[i][2] == 'T':
                    thruBall.addPower(powerType)
                gameLayout.pixels[self.powers[i][1]][self.powers[i][0]] = ' '
                self.powers.pop(i)
                break
            elif gameLayout.pixels[self.powers[i][1]+1][self.powers[i][0]] == 'X':
                self.powers[i][3] = -self.powers[i][3]
powerManager = Power()