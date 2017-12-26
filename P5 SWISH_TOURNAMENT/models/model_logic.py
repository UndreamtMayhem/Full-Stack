""" Model logic remove session when db is able to move here completely """
# TODO make this isnt a class
# Database Dependencies
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Custom Dependencies
from create_character_database import base, Character

ENGINE = create_engine('sqlite:///characters.db')
base.metadata.bind = ENGINE

DBSESSION = sessionmaker(bind=ENGINE)
SESSION = DBSESSION()


def fetch_all_characters():
    """ SELECT ALL CHARACTERS """
    characters = SESSION.query(Character).all()
    list_of_characters = [char for char in characters]
    return list_of_characters


def highest_winner():
    """ SELECT CHARACTERS WITH MOST WINS """
    cur = SESSION.query(Character).order_by(Character.wins.desc()).first()
    return cur.wins


def query_wins(amount_of_wins):
    """ SELECT CHARACTERS WITH SPECIFIED WINS """
    winners = SESSION.query(Character).filter_by(wins=amount_of_wins)
    return winners


def one_win():
    """ SELECT CHARACTERS WITH ONE WIN """
    winners = SESSION.query(Character).filter_by(wins=1)
    return winners


def two_wins():
    """ SELECT CHARACTERS WITH TWO WINS """
    winners = SESSION.query(Character).filter_by(wins=2)
    return winners


def three_wins():
    """ SELECT CHARACTERS WITH THREE WINS """
    winners = SESSION.query(Character).filter_by(wins=3)
    return winners


def tournament_winner():
    """ UPDATE TOURNAMENT WINNER """
    winners = SESSION.query(Character).filter_by(wins=4).one()
    SESSION.query(Character).filter(Character.id == winners.id).update(
        {Character.overall_wins: Character.overall_wins + 1}, synchronize_session=False)
    SESSION.commit()


def reset_wins():
    """ UPDATE WINS TO ZERO """
    SESSION.query(Character).filter(Character.wins > 0).update(
        {Character.wins: Character.wins == 0}, synchronize_session=False)
    SESSION.commit()


def display_leaderboard():
    """ SELECT WINNERS IN ORDER """
    overall_winner = SESSION.query(Character).order_by(
        Character.overall_wins.desc()).all()
    return overall_winner


def update_winner(cache):
    """ Update winner SQL ALchemy """
    SESSION.query(Character).filter(Character.id == cache.id).update(
        {Character.wins:Character.wins + 1}, synchronize_session=False)
    SESSION.commit()

def update_loser(cache):
    """ Update loser SQL ALchemy """
    cache = cache
    # session.query(Character).filter(Character.id == CACHE['id']).update(
    # {Character.wins: Character.wins + 1}, synchronize_session=False)

    return "not implemented future implementation"
