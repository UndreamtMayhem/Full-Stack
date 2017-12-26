""" Character utilties """

from create_character_database import Character

from models.model_logic import update_winner


def setup_matches(CACHE):
    """ Facade pattern explain it"""
    for character_index in range(0, len(CACHE), 2):

        player_1_attack_points = generate_character_attack(
            CACHE[character_index])

        player_2_attack_points = generate_character_attack(
            CACHE[character_index + 1])

        player_id_of_who_won = who_wins(
            player_1_attack_points, player_2_attack_points)

        if player_id_of_who_won == "player 1":
            update_winner(CACHE[character_index])
            # update_loser()
        else:
            update_winner(CACHE[character_index + 1])
            # update_loser()


def generate_character_attack(character):
    """ Algorithm for generating the players attack damage """
    character_attack_score = character.strength + character.inteligence +\
        character.energy_projection + character.mental_power +\
        character.fightning_ability + character.speed
    return character_attack_score


def who_wins(character_score_1, character_score_2):
    """ Determines who wins """
    if character_score_1 > character_score_2:
        return "player 1"
    else:
        return "player 2"

"""
def update_loser(CACHE):
     Update loser SQL ALchemy 
    # session.query(Character).filter(Character.id == CACHE['id']).update(
    # {Character.wins: Character.wins + 1}, synchronize_session=False)

    return "not implemented future implementation"
"""
