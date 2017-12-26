""" Adds character to the database """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from create_character_database import Character, base

ENGINE = create_engine('sqlite:///characters.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
base.metadata.bind = ENGINE

DBSession = sessionmaker(bind=ENGINE)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()

SESSION = DBSession()

""" CHARACTERS """
character1 = Character(name="Eyeless Jack",
                       strength=4, inteligence=5,
                       energy_projection=1, mental_power=1,
                       fightning_ability=4, speed=3,
                       wins=0, loses=0, overall_wins=0,
                       overall_losses=0, image="eyelessjack.png")

SESSION.add(character1)
SESSION.commit()


character2 = Character(name="Jeff the Killer",
                       strength=5,
                       inteligence=4,
                       energy_projection=1,
                       mental_power=3,
                       fightning_ability=3,
                       speed=5,
                       wins=0, loses=0, overall_wins=0,
                       overall_losses=0, image="jeff_the_killer.jpg")
SESSION.add(character2)
SESSION.commit()


character3 = Character(name="The Girl",
                       strength=3, inteligence=4,
                       energy_projection=1, mental_power=5,
                       fightning_ability=4, speed=2,
                       wins=0, loses=0, overall_wins=0,
                       overall_losses=0, image="thegirl.jpg")
SESSION.add(character3)
SESSION.commit()

character4 = Character(name="Uboa",
                       strength=2, inteligence=3,
                       energy_projection=1, mental_power=2,
                       fightning_ability=2, speed=2,
                       wins=0, loses=0, overall_wins=0,
                       overall_losses=0, image="uboa.jpeg")
SESSION.add(character4)
SESSION.commit()

character5 = Character(name="SlenderMan",
                       strength=3, inteligence=5,
                       energy_projection=5, mental_power=5,
                       fightning_ability=4, speed=2,
                       wins=0, loses=0, overall_wins=0,
                       overall_losses=0, image="slender_man.jpg")
SESSION.add(character5)
SESSION.commit()

character6 = Character(name="Weeping girl",
                       strength=2, inteligence=1,
                       energy_projection=4, mental_power=5,
                       fightning_ability=1, speed=2,
                       wins=0, loses=0, overall_wins=0,
                       overall_losses=0, image="weeping_girl.jpg")
SESSION.add(character6)
SESSION.commit()


character7 = Character(name="Melanie (penpal)",
                       strength=2, inteligence=2,
                       energy_projection=2, mental_power=2,
                       fightning_ability=2, speed=2,
                       wins=0, loses=0, overall_wins=0,
                       overall_losses=0, image="melanie.jpg")
SESSION.add(character7)
SESSION.commit()

character8 = Character(name="The rake",
                       strength=2, inteligence=2,
                       energy_projection=2, mental_power=2,
                       fightning_ability=2, speed=2,
                       wins=0, loses=0, overall_wins=0,
                       overall_losses=0, image="the_rake.jpg")
SESSION.add(character8)
SESSION.commit()


character9 = Character(name="Ticci Toby",
                       strength=3, inteligence=3,
                       energy_projection=1, mental_power=2,
                       fightning_ability=5, speed=5,
                       wins=0, loses=0, overall_wins=0,
                       overall_losses=0, image="ticci_toby.jpg")
SESSION.add(character9)
SESSION.commit()

character10 = Character(name="Ben Drowned",
                        strength=2, inteligence=3,
                        energy_projection=1, mental_power=3,
                        fightning_ability=3, speed=3,
                        wins=0, loses=0, overall_wins=0,
                        overall_losses=0, image="ben_drowned.jpg")
SESSION.add(character10)
SESSION.commit()

character11 = Character(name="Bloody Painter (Helen)",
                        strength=1, inteligence=4,
                        energy_projection=2, mental_power=2,
                        fightning_ability=4, speed=2,
                        wins=0, loses=0, overall_wins=0,
                        overall_losses=0, image="bloody_painter.jpg")
SESSION.add(character11)
SESSION.commit()


character12 = Character(name="Still Water",
                        strength=3, inteligence=5,
                        energy_projection=1, mental_power=1,
                        fightning_ability=4, speed=3,
                        wins=0, loses=0, overall_wins=0,
                        overall_losses=0, image="stillwater.jpeg")
SESSION.add(character12)
SESSION.commit()

character13 = Character(name="Sniper",
                        strength=3, inteligence=4,
                        energy_projection=1, mental_power=3,
                        fightning_ability=5, speed=5,
                        wins=0, loses=0, overall_wins=0,
                        overall_losses=0, image="sniper.jpeg")
SESSION.add(character13)
SESSION.commit()

character14 = Character(name="She Looms",
                        strength=2, inteligence=5,
                        energy_projection=4, mental_power=5,
                        fightning_ability=2, speed=3,
                        wins=0, loses=0, overall_wins=0,
                        overall_losses=0, image="she_looms.jpg")
SESSION.add(character14)
SESSION.commit()


character15 = Character(name="Laughing Jack",
                        strength=2, inteligence=3,
                        energy_projection=4, mental_power=5,
                        fightning_ability=3, speed=3,
                        wins=0, loses=0, overall_wins=0,
                        overall_losses=0, image="laughing_jack.jpg")
SESSION.add(character15)
SESSION.commit()

character16 = Character(name="Tails Doll",
                        strength=2, inteligence=3,
                        energy_projection=2, mental_power=2,
                        fightning_ability=3, speed=5,
                        wins=0, loses=0, overall_wins=0,
                        overall_losses=0, image="tails_doll.jpg")
SESSION.add(character16)
SESSION.commit()
print("added Characters!")
