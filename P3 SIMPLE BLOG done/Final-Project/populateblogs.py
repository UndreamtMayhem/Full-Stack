from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from blogsetup import Base, Users, Blog, Tag

from password import make_salt, create_password, validate_password


from CreateData.create_tags import create_tags
from CreateData.create_users import create_users
from CreateData.create_blogs import create_blogs



import random
import time
engine = create_engine('sqlite:///userblogs.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()



''' Create Default Tags '''
create_tags()

create_users()

create_blogs()

print("added lots of lots of blogs!")
