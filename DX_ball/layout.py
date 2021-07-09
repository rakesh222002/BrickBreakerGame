from colorama import init, Fore, Style
class Layout:
    def __init__(self):
        self.width = 100
        self.length = 35
        self.startFlag = 0
        self.thruBall = 0
        self.pixels = [[] for i in range(0,self.length)]
        for i in range(0, self.length):
            for j in range(0,self.width):
                self.pixels[i].append(' ')

    def printData(self):
        for i in range(0, self.length):
            temp = ''
            for j in range(0,self.width):
                if i == 0 or j == 0 or i==self.length-1 or j==self.width-1 or i==4:   
                    self.pixels[i][j] = 'X'
                temp = temp + self.pixels[i][j]
            for k in range(0,self.width):
                if temp[k] == 'X':
                    print (Fore.YELLOW + temp[k],end="")
                    print (Style.RESET_ALL,end="")
                elif temp[k] == 'Z':
                    print (Fore.BLUE + temp[k],end="")
                    print (Style.RESET_ALL,end="")
                elif temp[k] == '1' or temp[k] == '2' or temp[k] == '3':
                    print (Fore.RED + temp[k],end="")
                    print (Style.RESET_ALL,end="")
                elif temp[k] == '[':
                    print (Fore.GREEN + temp[k],end="")
                    print (Style.RESET_ALL,end="")
                elif temp[k] == ']':
                    print (Fore.GREEN + temp[k],end="")
                    print (Style.RESET_ALL,end="")
                else: 
                    print (temp[k],end="")
            print()
gameLayout = Layout()            
