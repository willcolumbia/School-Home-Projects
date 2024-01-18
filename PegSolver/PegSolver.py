boardlst = []
inp = 0
moves = []
legalMoves = []
hole = "_"
peg = "X"
boards = []
jumps = []
n = 0

def initalizeGame(n):
    k = n-1 
    valid = True
    for i in range (0,n):
        for j in range(0,k):
            print(" ",end="  ")
        k = k -1
        for j in range(0,i+1):
            print("(",i,",",j,")",end="")
        print("\r")
        print("\r")
    while valid:
        temp = tuple(input("hello user, please enter the empty space on the board in the format '  _ , _ ' \n").split(","))
        empty = tuple(map(int,temp))
        if(len(empty) == 2):
            if (empty[0] < n) and (empty[1] <= empty[0]) and empty[0] >= 0 and empty[1] >=0:
                valid = False
            else:
                print("invalid input please try again")
        else:
                print("invalid input please try again")
    temp = []
    for i in range(0,n):
        temp = tuple((x,y) for x in range(n) for y in range(x+1))
    lst = list(temp)
    k = len(lst)
    return lst,empty
    

def legal_moves(target,lst):
    testPrint =[]
    for peg in lst:
        x , y = peg
        for middle_pos, start_pos in (
            ((x, y-1), (x, y-2)),   # UP
            ((x-1, y), (x-2, y)),   # LEFT
            ((x, y+1), (x, y+2)),   # DOWN
            ((x+1, y), (x+2, y)),    # RIGHT
            ((x-1,y-1),  (x-2, y-2)), #UP LEFT
            ((x+1, y+1), (x+2, y+2)),   # DOWN RIGHT
            ):
            for neighbor in (
            ((x, y-1)),   # UP
            ((x-1, y)),   # LEFT
            ((x, y+1)),   # DOWN
            ((x+1, y)),   # RIGHT
            ((x-1,y-1)),  # LEFT UP
            ((x+1,y+1)),  #RIGHT DOWN
            ((x-1,y+1))   #LEFT DOWN
            ):
                if(middle_pos in lst) and (start_pos in lst) and middle_pos == neighbor and ((x,y) == target):
                    testPrint.append([start_pos,middle_pos])
    legalMoves.append(testPrint)
    

def printboard(board):
    curr = 0
    stop = 2
    rows = n
    k = n-1
    for i in range(rows):
        for j in range(0,k):
            print(end=" ")
        k = k -1
        for j in range(1,stop):
            print(board[curr],end=" ")
            curr += 1
        print("")
        stop += 1
            
            
            
    
def solve(n,empty):
    board = []
    for i in range(n):
        if(empty == i):
            board.insert(i,hole)
        else:
            board.insert(i,peg)
    original = board.copy()
    if(solveInternal(board)):
        jumps.reverse()
        print("\nInital Board")
        printboard(original)
        print("\n -------MOVES TO SOLVE-------\n")
        for i in range (len(boards)):
            print("\n","##",jumps[i],"##","\n")
            printboard(boards[i])
        return True
    else:
        print("NO SOLUTION FOUND")
        return False


def solveInternal(board):
    for move in moves:
        if((board[move[0]]==peg) and (board[move[1]] == peg) and (board[move[2]] == hole)):
            board[move[0]] = hole
            board[move[1]] = hole
            board[move[2]] = peg
            clone = board.copy()
            boards.append(clone)
            
            if(solveInternal(board)):
                output = "MOVE PEG AT "+str(boardlst[move[0]])+" OVER PEG AT "+str(boardlst[move[1]])+" TO OPEN POSITION "+str(boardlst[move[2]])
                jumps.append(output)
                return True
                
            
            boards.pop()
            board[move[0]] = peg
            board[move[1]] = peg
            board[move[2]] = hole
    pegCount = board.count(peg)
    if((pegCount == 1)):
        return True
    else:
        return False
 
    





if __name__ == "__main__":   
    n = int(input("Please enter the size of the board\nEXAMPLE: input 5 will result in a board with 15 pegs\n"))
    if(type(n) == int) and (n>4):
        boardlst, inp = initalizeGame(n)
        empty = boardlst.index(inp)
        for pos in boardlst:
            legal_moves(pos,boardlst)
        for i in range(len(legalMoves)):
            for j in range(len(legalMoves[i])):
                moves.append([boardlst.index(boardlst[i]),boardlst.index(legalMoves[i][j][1]),boardlst.index(legalMoves[i][j][0])])
        solve(len(boardlst),empty)
    else:
        print("INVALID BOARD SIZE TRY AGAIN")
        