def displayBoard(board):
    for i in range(9):
        ele = board[i]
        if ele==1:
            ele = "O"
        if ele==-1:
            ele = "X"
        if ele==0:
            ele = " "
        print(f" {ele} ", end="")
        if (i+1)%3 != 0:
            print("|", end="")
        elif ((i+1)%3 == 0 and (i+1)<9) :
            print("\n---+---+---")
 
 
def displayBoardPositions(board):
    print("\nThese are the positions on board. Use these numbers to fill in your moves. \n")
    for i in range(9):
        print(f" {i+1} ", end="")
        if (i+1)%3 != 0:
            print("|", end="")
        elif ((i+1)%3 == 0 and (i+1)<9) :
            print("\n---+---+---")
    print()
 
 
 
def huTurn(board):
    pos = input("\n\nEnter your move (X): ")
    if pos=="[exit]":
        print("\n\n~ EXITING GAME ~\n\n")
        exit(0)
    pos = int(pos)
 
    if pos>0 and pos<=9:
        if(board[pos-1] != 0):
            print("This position is already filled.")
            huTurn(board)
        board[pos-1] = -1
    else:
        huTurn(board)
    
 
def minimax(board, player):
    x = checkForWin(board)
    if(x != 0):
        return (x*player)
    pos = -1
    value = -2
    for i in range(0, 9):
        if(board[i] == 0):
            board[i] = player
            score = -minimax(board, (player*-1))
            if(score > value):
                value = score
                pos = i
            board[i] = 0
 
    if(pos == -1):
        return 0
    return value



def aiTurn(board):
    pos = -1
    value = -2
    for i in range(0, 9):
        if(board[i] == 0):
            board[i] = 1
            score = -minimax(board, -1)
            board[i] = 0
            if(score > value):
                value = score
                pos = i
 
    board[pos] = 1
 
 
def checkForWin(board):
    rule1 = [0, 1, 2]
    rule2 = [3, 4, 5]
    rule3 = [6, 7, 8]
    rule4 = [0, 3, 6]
    rule5 = [1, 4, 7]
    rule6 = [2, 5, 8]
    rule7 = [0, 4, 8]
    rule8 = [2, 4, 6]
    winMoves = [rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8]
 
    for i in range(0, 8):
        if(board[winMoves[i][0]] != 0):
            if (board[winMoves[i][0]] == board[winMoves[i][1]] and 
                board[winMoves[i][0]] == board[winMoves[i][2]]):
                return board[winMoves[i][2]]
    return 0



print("""
-------------------------------------
            Tic-Tac-Toe
-------------------------------------
""")
 
board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
 
print("""Play with the computer -
Computer : O
You      : X
""")
 
player = input("""Enter 
1: to play 1st
2: to play 2nd
Choice? """)
 
player = int(player)
 
print("\nTo leave the game at any moment, enter [exit].")
displayBoardPositions(board)
 
for i in range(0, 9):
    if(checkForWin(board) != 0):
        break
    if((i+player) % 2 == 0):
        aiTurn(board)
        print("\n\n>> After computer's move")
        displayBoard(board)
 
    else:
        huTurn(board)
        print("\n>> After your move")
        displayBoard(board)
 
        
x = checkForWin(board)
 
print(f"\n\n{'_'*30}\n")
if(x == 0):
    res = "RESULT : Draw"
    print(res.center(30))
if(x == -1):
    res = "RESULT : You win (X)"
    print(res.center(30))
if(x == 1):
    res = "RESULT : Computer(O) wins"
    print(res.center(30))
print(f"{'_'*30}")
print()
