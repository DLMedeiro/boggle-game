from flask import Flask, render_template, session, request, redirect, flash


app = Flask(__name__)

app.config['SECRET_KEY'] = 'BoggleFun'

from boggle import Boggle

boggle_game = Boggle()
responses = [];
score = 0;


# Landing page, button to redirect to game, initializes game board on click
@app.route('/')
def home():
    return render_template('index.html')


# @app.route('/test')
# def test():
#     return render_template('game_play.html')

# Game Play Page
@app.route('/play_game')
def play():
    responses.clear();
    score = 0;
    board = boggle_game.make_board()
    session['board'] = board


    return render_template('game_play.html', board = board, responses = responses, score = score)


@app.route('/play_game', methods = ['POST'])
def game_play():
    word = request.form['word']
    board = session['board']
    score = 0;

    if word in responses:
        flash("Word already added to list")
    elif boggle_game.check_valid_word(board, word) == "not-on-board":
        flash("Word not listed on board!")
    elif boggle_game.check_valid_word(board, word) == "not-word":
        flash("Not a valid word!")
    elif boggle_game.check_valid_word(board, word) == "ok":
        flash("Word added to list!")
        responses.append(word)
    # page refresh removes flash message
    
    for response in responses:
        score = score + len(response)

    return render_template('game_play.html', responses = responses, board = board, score = score)
