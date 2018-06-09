def getIsWin(board, mark):
    for x in range(3):
        win = True
        for y in range(3):
            if board[x][y] != mark:
                win = False
                break

        if win:
            return True

    for y in range(3):
        win = True
        for x in range(3):
            if board[x][y] != mark:
                win = False
                break

        if win:
            return True

    if board[0][0] == mark and board[1][1] == mark and board[2][2] == mark:
        return True

    if board[2][0] == mark and board[1][1] == mark and board[0][2] == mark:
        return True

    return False

def getCopy(board):
    l = initBoard()
    for x in range(3):
        for y in range(3):
            l[x][y] = board[x][y]

    return l

def getMoveList(board):
    move_list = []
    for x in range(3):
        for y in range(3):
            if board[x][y] == '0':
                move_list.append((x, y))

    return move_list

def makeMove(board, move, mark):
    x, y = move
    board[x][y] = mark

def initBoard():
    board = [['0']*3 for x in range(3)]
    return board

def printBoard(board):
    print("\n", end="")
    for x in range(3):
        for y in range(3):
            print(board[x][y] + " ", end="")
        print("\n", end="")

def flip(mark):
    if mark == 'X':
        return 'O'
    else:
        return 'X'

def boardIsFull(board):
    for x in range(3):
        for y in range(3):
            if board[x][y] == '0':
                return False

    return True

def getMinMove(board, mark):
    move_list = getMoveList(board)

    move_score = 1
    for move in move_list:
        copy_board = getCopy(board)
        makeMove(copy_board, move, mark)

        if getIsWin(copy_board, mark):
            move_score = -1
            win_move = move
            break

        if boardIsFull(copy_board):
            score = 0
        else:
            score, move_temp = getMaxMove(copy_board, flip(mark))

        if score < move_score:
            move_score = score
            
    return move_score

def getMaxMove(board, mark):
    move_list = getMoveList(board)
    
    win_move = None
    move_score = -1
    for move in move_list:
        copy_board = getCopy(board)
        makeMove(copy_board, move, mark)

        if getIsWin(copy_board, mark):
            move_score = 1
            win_move = move
            break

        if boardIsFull(copy_board):
            score = 0
        else:
            score = getMinMove(copy_board, flip(mark))
            
        if score > move_score:
            move_score = score
            win_move = move
            
    return (move_score, win_move)

def getPlayerMove(board):
    line = input("Enter Move : ")
    l = line.strip().split(' ')
    x, y = int(l[0]), int(l[1])

    if board[x][y] != '0':
        return getPlayerMove(board)
    else:
        return x, y

def main():
    board = initBoard()

    winner = None
    for x in range(9):
        if x%2 == 1:
            score, move_t = getMaxMove(board, 'X')
            makeMove(board, move_t, 'X')
            printBoard(board)
            if getIsWin(board, 'X'):
                winner = 'X'
                break
        else:
            move_t = getPlayerMove(board)
            makeMove(board, move_t, 'O')
            printBoard(board)
            if getIsWin(board, 'O'):
                winner = 'O'
                break

    if winner == 'X':
        print("Player 1")
    elif winner == 'O':
        print("Player 2")
    else:
        print("Draw")

if __name__ == '__main__':
    main()
