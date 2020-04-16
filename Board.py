class Player:
    def __init__(self,color,name):
        self.color = color
        self.name = name
class Board:
    def __init__(self,row = 6,col = 10,gameSize = 4,players = [Player("red","red 1"),Player("yellow","Player 2")]): # Default values 
        self.row = row
        self.column = col
        self.board = [[False for x in range(col)] for y in range(row)]
        self.counts = [0 for x in range(col)]
        self.gameSize = gameSize# How many points to connect, Default value is 4
        self.player = len(players)# How many players are playing. Default value is 2.
        self.playerList = players
        self.currentPlayer = 1 # Player 1 is starting
        self.isFinished = False
        



    def checker(self):
        player = self.playerList[self.currentPlayer-1]
        # Horizontal
        for row in self.board:
            for columnIndex in range(self.column - self.gameSize +1):
                control = True
                for point in range(self.gameSize):
                    control = control and (row[columnIndex + point] == player.color)
                if control:
                    return True
        
        # Vertical
        for columnIndex in range(self.column):
            for rowIndex in range(self.row - self.gameSize +1):
                control = True
                for point in range(self.gameSize):
                    control = control and (self.board[rowIndex + point][columnIndex] == player.color)
                if(control):
                    return True

         #Diagonal \
        for rowIndex in range(self.row - self.gameSize +1):
            for columnIndex in range(self.column - self.gameSize +1):
                control = True 
                for point in range(self.gameSize):
                    control = control and (self.board[rowIndex+point][columnIndex+point] == player.color)
                if control:
                    return True
        
        #Diagonal /
        for rowIndex in range(self.row - self.gameSize + 1):
            for columnIndex in range(self.column -1, self.gameSize-2,-1):
                control = True
                for point in range(self.gameSize):
                    control = control and (self.board[rowIndex+point][columnIndex-point] == player.color)
                if control:
                    return True                

    def play(self,column):
        player = self.playerList[self.currentPlayer-1]
        # = int(input("{}'s turn ".format(player.name)))-1
        print("{}'s turn ".format(player.name))
        if self.isFinished:
            print("Game has already finished.")
            return
        if(self.counts[column] == self.row):
            print("Invalid Column! Please choose a different column")
            return
        emptyRow= self.row -1 - self.counts[column]
        print(emptyRow,column)
        count = emptyRow*self.column + column 
        from Main import filler
        filler(count,player.color)
        self.board[emptyRow][column] = player.color
        
        self.counts[column] +=1
        if self.checker():
            self.print()
            print("{} has won!".format(player.name))
            self.isFinished = True
        else:
            self.currentPlayer = self.currentPlayer % self.player +1

            self.print()
            print("{}'s turn ".format(self.playerList[self.currentPlayer-1].name))
        
    
    def print(self):
        for row in self.board:
            print(row)
        print("---------")