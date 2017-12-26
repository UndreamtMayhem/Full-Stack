from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Character

engine = create_engine('sqlite:///characters.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


def select_winner(round,search_word):
            #CACHE['winners'] = winners
            #CACHE['losers'] = losers

            for i in range(0, len(CACHE[round][search_word]), 2):
                # Character 1 of playoff 
                ability_choosen = random.randint(1,6)
                character_score_1 = CACHE[round][search_word][2 - i][ability_choosen]

                # Character 2 of playoff 
                ability_choosen2 = random.randint(1,6)
                character_score_2 = CACHE[round][search_word][i][ability_choosen2]
                # See who the winner is 
                if character_score_1 > character_score_2:
                    #update character_score_1
                    session.query(Character).filter(Character.name == CACHE[round][search_word][2 - i][0]).\
                    update({Character.win: Character.win + 1}, synchronize_session=False)
                else:
                    #update character_score_2
                    session.query(Character).filter(Character.name == CACHE[round][search_word][i][0]).\
                    update({Character.win: Character.win + 1}, synchronize_session=False)
