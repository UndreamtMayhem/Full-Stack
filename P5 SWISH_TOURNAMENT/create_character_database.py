"""   Character database schema """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

base = declarative_base()


class Character(base):
    """ Character database schema """
    __tablename__ = 'character'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    strength = Column(Integer)
    inteligence = Column(Integer)
    energy_projection = Column(Integer)
    mental_power = Column(Integer)
    fightning_ability = Column(Integer)
    speed = Column(Integer)
    wins = Column(Integer)
    loses = Column(Integer)
    overall_wins = Column(Integer)
    overall_losses = Column(Integer)
    image = Column(String(500))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'strength': self.strength,
            'inteligence': self.inteligence,
            'energy_projection': self.energy_projection,
            'mental_power': self.mental_power,
            'fightning_ability': self.fightning_ability,
            'speed': self.speed,
            'wins': self.wins,
            'loses': self.loses,
            'overall_wins': self.overall_wins,
            'overall_losses': self.overall_losses,
            'image': self.image,
        }

ENGINE = create_engine('sqlite:///characters.db')

base.metadata.create_all(ENGINE)
