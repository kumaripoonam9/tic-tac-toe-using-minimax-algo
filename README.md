# Tic-Tac-Toe using minimax algorithm
Python code for Tic-Tac-Toe game between computer and user using minimax algorithm.


### Algorithm

Algorithm for minimax for the game

```
function minimax(board, player):

if current board state is a terminal state i.e. has any winning moves :
    return board value
end if
if player is max player :
    bestval = -INFINITY 
    for each move in board :
        if position is empty :
            value = minimax(board, depth+1, false)
            bestval = max( bestval, value) 
        end if
    end for loop
    return best value
else :
    bestVal = +INFINITY 
    for each move in board :
        if position is empty :
            value = minimax(board, min player)
            bestval = min( bestval, value)
        end if
    end for loop 
    return best value
end if
end function
```

