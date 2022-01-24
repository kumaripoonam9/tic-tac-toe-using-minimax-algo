# Tic-Tac-Toe using minimax algorithm
Python code for Tic-Tac-Toe game between computer and user using minimax algorithm.


### Algorithm

Minimax algorithm is a type of adversarial serach. Adversarial search is a type of search widely in competitive games like tic-tac-toe, chess etc where the final result depends upon the moves of the opponent.

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

### Snapshots of game

(AI player wins)
![snap1](https://user-images.githubusercontent.com/65129334/150751966-daa49acc-57bf-4a5a-ad68-ee7055632afa.png)
![snap2](https://user-images.githubusercontent.com/65129334/150752173-32c67ee2-7688-4588-9dcc-d972152dacbb.png)
