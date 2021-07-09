class Brick(object):
    def __init__(self, type):
        if type == ' ':
            self.brick = '   '
        else:
            self.brick = '[' + type + ']'
    def getBrick(self):
        return self.brick

class BrickTypes(Brick):
    def addBrick(self):
        return self.brick