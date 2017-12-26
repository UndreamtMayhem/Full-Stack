""" FLASK APP Swiss Tournament"""
# Python Modules
from random import shuffle

# Dependencies
from flask import Flask, render_template, request, redirect, url_for

# Custom modules
from character_resources import setup_matches

# Model logic
from models.model_logic import fetch_all_characters, highest_winner, one_win, two_wins, three_wins,\
                                query_wins, tournament_winner, reset_wins, display_leaderboard

APP = Flask(__name__)

CACHE = {}
CACHE['winners'] = {}
CACHE['losers'] = {}
CACHE['round1'] = {}
CACHE['round2'] = {}
CACHE['round3'] = {}
CACHE['round4'] = {}
CACHE['final_round'] = {}


@APP.route('/', methods=['GET', 'POST'])
def show_tournament():
    """ Shows the tournament and sets up matches"""
    # todo possible name  change
    wins = highest_winner()

    # When we post decide winners and losers
    if request.method == 'POST':
        # if the win of the tournament is 0 Run matches
        if wins == 0:
            setup_matches(CACHE['round1'])
            return redirect(url_for('show_round1'))
    else:
        if wins == 0:
            # retrieve all characters
            characters = fetch_all_characters()
            # shuffle the characters
            shuffle(characters)
            # CACHE the characters
            CACHE['round1'] = characters

            return render_template('round0.html', characters=CACHE['round1'])
        # if player navigate to old rounds they are put to the correct one
        elif wins == 1:
            return redirect(url_for('show_round1'))
        elif wins == 2:
            return redirect(url_for('show_round2'))
        elif wins == 3:
            return redirect(url_for('show_round3'))
        elif wins == 4:
            return redirect(url_for('show_round4'))


@APP.route('/round1/', methods=['GET', 'POST'])
def show_round1():
    """ Run round 1"""
    # Retrieve highest win
    wins = highest_winner()
    if request.method == 'POST':
        if wins == 1:
            # Run matches for winners and losers
            setup_matches(CACHE['round2']['winners'])
            setup_matches(CACHE['round2']['losers'])
            return redirect(url_for('show_round2'))
    else:
        if wins == 1:
            # randomly pick all teams with 1 win
            winners = one_win()
            # randomly pick all teams with 0 win
            losers = query_wins(0)

            # set up the cache
            CACHE['round2']['winners'] = list(winners)
            CACHE['round2']['losers'] = list(losers)
            # pass the cache to the view
            return render_template('round1.html', round2=CACHE['round2'])
        elif wins == 0:
            return redirect(url_for('show_tournament'))
        elif wins == 2:
            return redirect(url_for('show_round2'))
        elif wins == 3:
            return redirect(url_for('show_round3'))
        elif wins == 4:
            return redirect(url_for('show_round4'))


@APP.route('/round2/', methods=['GET', 'POST'])
def show_round2():
    """ round 2"""
    wins = highest_winner()

    if request.method == 'POST':
        # Select winners send to the next round
        if wins == 2:
            setup_matches(CACHE['round3']['winners2'])
            setup_matches(CACHE['round3']['winners'])
            setup_matches(CACHE['round3']['losers'])
            return redirect('/round3/')
    else:
        if wins == 2:
            # randomly pick all teams with 2 win
            winners2 = two_wins()
            # randomly pick all teams with 1 win
            winners = one_win()
            # randomly pick all teams with 0 win
            losers = query_wins(0)

            CACHE['round3']['winners2'] = list(winners2)
            CACHE['round3']['winners'] = list(winners)
            CACHE['round3']['losers'] = list(losers)

            return render_template('round2.html', round3=CACHE['round3'])
        elif wins == 0:
            return redirect(url_for('show_tournament'))
        elif wins == 1:
            return redirect(url_for('show_round1'))
        elif wins == 3:
            return redirect(url_for('show_round3'))
        elif wins == 4:
            return redirect(url_for('show_round4'))


@APP.route('/round3/', methods=['GET', 'POST'])
def show_round3():
    """ Display round 3 """
    wins = highest_winner()

    if request.method == 'POST':
        if wins == 3:
            setup_matches(CACHE['round4']['winners3'])
            setup_matches(CACHE['round4']['winners2'])
            setup_matches(CACHE['round4']['winners'])
            setup_matches(CACHE['round4']['losers'])
            return redirect('/round4/')
    else:
        if wins == 3:
            # randomly pick all teams with 3 win
            winners3 = three_wins()
            # randomly pick all teams with 2 win
            winners2 = two_wins()
            # randomly pick all teams with 1 win
            winners = one_win()
            # randomly pick all teams with 0 win
            losers = query_wins(0)

            CACHE['round4']['winners3'] = list(winners3)
            CACHE['round4']['winners2'] = list(winners2)
            CACHE['round4']['winners'] = list(winners)
            CACHE['round4']['losers'] = list(losers)

            return render_template('round3.html', round4=CACHE['round4'])
        elif wins == 0:
            return redirect(url_for('show_tournament'))
        elif wins == 1:
            return redirect(url_for('show_round1'))
        elif wins == 2:
            return redirect(url_for('show_round2'))
        elif wins == 4:
            return redirect(url_for('show_round4'))


@APP.route('/round4/', methods=['GET', 'POST'])
def show_round4():
    """ ROUND 4"""
    wins = highest_winner()

    if request.method == 'POST':
        if wins == 4:
            # possible rename
            tournament_winner()
            reset_wins()
            return redirect(url_for('show_tournament'))
    else:
        if wins == 4:
            # randomly pick all teams with 4 win
            winners4 = query_wins(4)
            # randomly pick all teams with 3 win
            winners3 = three_wins()
            # randomly pick all teams with 2 win
            winners2 = two_wins()
            # randomly pick all teams with 1 win
            winners = one_win()
            # randomly pick all teams with 0 win
            losers = query_wins(0)

            CACHE['final_round']['winners4'] = list(winners4)
            CACHE['final_round']['winners3'] = list(winners3)
            CACHE['final_round']['winners2'] = list(winners2)
            CACHE['final_round']['winners'] = list(winners)
            CACHE['final_round']['losers'] = list(losers)

            return render_template('round4.html', final_round=CACHE['final_round'])

        elif wins == 0:
            return redirect(url_for('show_tournament'))
        elif wins == 1:
            return redirect(url_for('show_round1'))
        elif wins == 2:
            return redirect(url_for('show_round2'))
        elif wins == 3:
            return redirect(url_for('show_round3'))


@APP.route('/leaderboard/', methods=['GET', 'POST'])
def leaderboard():
    """ Display LeaderBoard"""
    return render_template('leaderboard.html', leaderboard=display_leaderboard())


if __name__ == '__main__':
    APP.debug = True
    APP.run(host='127.0.0.1', port=5000)
