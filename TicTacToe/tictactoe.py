def setupBoard() -> list():
    newList = [
                '',
                '',
                '',
                '',
                '',
                '',
                '',
                '',
                '',]
    return newList

def setupPlayers() -> list():
    newList = ['O', 'X']
    return newList

def playerMoved(board, possition, value) -> list():
    if board[possition] == '':
        board[possition] = value
    return board

def checkIfEnd(board) -> bool:
    for i in range(9):
        if board[i] == '':
            return False
    return True

def checkIfWin(board) -> bool:
    if (
            board[0]!='' and board[0] == board[1] == board[2] or
            board[3]!='' and board[3] == board[4] == board[5] or
            board[6]!='' and board[6] == board[7] == board[8] or
            board[0]!='' and board[0] == board[3] == board[6] or
            board[1]!='' and board[1] == board[4] == board[7] or
            board[2]!='' and board[2] == board[5] == board[8] or
            board[0]!='' and board[0] == board[4] == board[8] or
            board[2]!='' and board[2] == board[4] == board[6]
    ):
        return True
    return False

    
