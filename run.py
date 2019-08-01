from flask import Flask, render_template, request
import tictactoe

app = Flask(__name__)

class Glob:
    i = 0
    board = list()
    players = list()

@app.route('/')
@app.route('/welcome')
def welcome() -> 'html':
    return render_template('welcome.html',
                            the_title='Welcome to TicTacToe game!')

@app.route('/newgame')
def newGame() -> 'html':
    Glob.i = 0
    Glob.board = tictactoe.setupBoard()
    Glob.players = tictactoe.setupPlayers()
    return render_template('game.html',
                            the_title='Tic Tac Toe',
                            the_text='Begin the player:',
                            the_player=str(Glob.players[Glob.i]),
                            board=Glob.board)

@app.route('/game', methods=['POST'])
def game() -> 'html':
    for key in request.form:
        possition = int(key)
    player = Glob.players[Glob.i]
    if Glob.board[possition] != '':
        return  render_template('game.html',
                                the_title='Tic Tac Toe',
                                the_text='Now playing:',
                                the_player=str(player),
                                board=Glob.board)
    newI = (Glob.i+1)%2
    Glob.i = newI
    Glob.board = tictactoe.playerMoved(Glob.board, possition, player)
    print(Glob.board)
    ifWin = tictactoe.checkIfWin(Glob.board)
    if ifWin:
        return render_template('winner.html',
                                the_title='Congratulations!',
                                the_winner=str(player))
    else:
        ifEnd = tictactoe.checkIfEnd(Glob.board)
        if ifEnd:
            return render_template('deadheat.html',
                                    the_title='Strong opponent?')
    return render_template('game.html',
                            the_title='Tic Tac Toe',
                            the_text='Now playing:',
                            the_player=str(Glob.players[Glob.i]),
                            board=Glob.board)

app.run(debug=True)
