import random as ran

class Board:
    def __init__(self):
        self.board = [[0,0,0],
                      [0,0,0],
                      [0,0,0]]
        self.turn = 0

    def displayBoard(self):
        symbols = {0:" ",
                   1:"X",
                   2:"O"}
        def sym(boardPos):
            return symbols[self.board[boardPos[0]][boardPos[1]]]
            
        print(f"{sym((0,0))}|{sym((0,1))}|{sym((0,2))}")
        print( "-┼-┼-")
        print(f"{sym((1,0))}|{sym((1,1))}|{sym((1,2))}")
        print( "-┼-┼-")
        print(f"{sym((2,0))}|{sym((2,1))}|{sym((2,2))}")

    def placeTile(self,tile):
        self.board[tile[0]][tile[1]] = (1,2)[self.turn%2]
        self.turn+=1

    def threeInRow(self):
        vert = list("000.000.000.")
        horz = list("000.000.000.")
        diag = list("000.000.0")
        
        for y in range(3):
            for x in range(3):
                index = x+(y*3)
                horz[(0,1,2,4,5,6,8,9,10)[index]] = str(self.board[y][x])
                vert[(0,4,8,1,5,9,2,6,10)[index]] = str(self.board[y][x])
                diag[(0,8,8,8,1,8,8,8,2)[index]] = str(self.board[y][x])
                diag[(8,8,4,8,5,8,6,8,8)[index]] = str(self.board[y][x])
        lines = "".join((vert+horz+diag))
        
        if '111' in lines:
            return("X")

        elif '222' in lines:
            return("O")

        elif not "0" in  lines:
            return("TIE")

        else:
            return False

    def endCheck(self):
        end = self.threeInRow()
        endBool = False
        if end == "X":
            print("X wins!")
            endBool = True
        elif end == "O":
            print("O wins!")
            endBool = True
        elif end == "TIE":
            print("Tie game!")
            endBool = True
        if endBool:
            self.turn = -1
        
def run(players):
    again = True
    while again:
        board = Board()
        board.displayBoard()
        
        while board.turn != -1:
            if players[board.turn%2] == "bot":
                board.placeTile(ranInput(board))
            elif players[board.turn%2] == "live":
                board.placeTile(getInput(board))
            board.displayBoard()
                
            board.endCheck()
        print("Again? (y,n)")
        if input() != "y":
            again = False
        players.reverse()
            
def getInput(board):
    fin = False
    turn = board.turn
    print(f"You are {('X','O')[board.turn%2]}")
    while not fin:
        print("Input coords X:0-2,Y:0-2 ex. '1,2'")
        pos = str(input())
        if len(pos) == 3:
            if pos[0] in "012" and pos[2] in "012":
                x = list("012").index(pos[0])
                y = list("012").index(pos[2])
                if board.board[y][x] == 0:
                    fin = True
                else:
                    print("Choose a blank Square")
            else:
                print("Invalid Coords")
        else:
            print("Invalid Input")
    return (y,x)

def ranInput(board):
    print("")
    fin = False
    while not fin:
        x = ran.randint(0,2)
        y = ran.randint(0,2)
        if board.board[y][x] == 0:
            fin = True
    return (y,x)
    
run(["live","bot"])
    
