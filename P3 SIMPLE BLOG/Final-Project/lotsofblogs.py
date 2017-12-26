from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from blogsetup import Base, Users, Blog

from password import make_salt, create_password, validate_password

# create salt


import random
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

# TEST 1 ADD MULTIPLE BLOGS TO A USER

default_body = '''
Tumeric austin adaptogen edison bulb irony cornhole put a bird on it, four dollar toast kinfolk cardigan affogato hell of chartreuse raw denim. Normcore etsy la croix tattooed meggings edison bulb hammock hella. Skateboard hexagon salvia taiyaki prism, letterpress godard blog gluten-free twee. Occupy skateboard YOLO, intelligentsia forage pinterest kombucha snackwave vexillologist glossier readymade. Raw denim etsy health goth hammock coloring book everyday carry humblebrag pickled try-hard unicorn. Blue bottle disrupt mumblecore viral meggings before they sold out snackwave knausgaard put a bird on it. Venmo tbh semiotics readymade, butcher leggings blog listicle activated charcoal farm-to-table hoodie. Roof party whatever celiac art party, quinoa tbh you probably haven't heard of them wayfarers blue bottle tacos. Kogi snackwave letterpress truffaut, vegan ramps ugh copper mug freegan retro yuccie small batch flannel fingerstache. Keffiyeh af biodiesel wayfarers semiotics godard. Man braid skateboard gluten-free four loko enamel pin tumeric.
'''


i = 0
# CREATE USERS FIRST THEN DD BLOGS TO THEM


new_salt = make_salt()


# create salted password
salted_password = create_password('a', new_salt)


user1 = Users(
    about="ghjhjghjghjgjhg hj ghjgjhgjhgjhgjhgjhg",
    #blogs_following = ["b", "c"]
    email="a@a.com",
    facebook_link='/',
    first_name='hgjhghjgjhg',
    gender='male',
    last_name='hgujgfhfhg',
    linkedin_link='/',
    password=salted_password,
    pininterest_link='/',
    profile_pic='userprofile.png',
    salt=new_salt,
    snapchat_link='/',
    twitter_link='/',
    #tags = ['a', 'ghfgh', 'ghfhgfh']
    username='a',
)
session.add(user1)
session.commit()

# add a blog
blog1 = Blog(
    body=default_body,
    caption="dgfdgfdgdgfd",
    date_uploaded=datetime.now(),
    description="fdshjfgdshjfgsd",
    is_public=True,
    image_url='mainimage.jpg',
    likes=random.randint(5, 1000),
    name="blog",
    title="Urban Burger",
    user=user1,
)


session.add(blog1)
session.commit()


new_salt = make_salt()
print(new_salt)

# create salted password
salted_password = create_password('b', new_salt)
print(salted_password)

user2 = Users(
    about="jhyut hj ghjgjhgjhgjhgjhgjhg",
    #blogs_following = ["b", "c"]
    email="b@b.com",
    facebook_link='/',
    first_name='111 hgjhghjgjhg',
    gender='male',
    last_name='33 44 hgujgfhfhg',
    linkedin_link='/',
    password=salted_password,
    pininterest_link='/',
    profile_pic='userprofile.png',
    salt=new_salt,
    snapchat_link='/',
    twitter_link='/',
    #tags = ['a', 'ghfgh', 'ghfhgfh']
    username='b',
)
session.add(user2)
session.commit()


new_salt = make_salt()
print(new_salt)

# create salted password
salted_password = create_password('c', new_salt)
print(salted_password)


user3 = Users(
    about=" 121212jhyut hj ghjgjhgjhgjhgjhgjhg",
    #blogs_following = ["b", "c"]
    email="c@c.com",
    facebook_link='/',
    first_name='111 hgjhghjgjhg',
    gender='male',
    last_name='33 44 hgujgfhfhg',
    linkedin_link='/',
    password=salted_password,
    pininterest_link='/',
    profile_pic='userprofile.png',
    salt=new_salt,
    snapchat_link='/',
    twitter_link='/',
    #tags = ['a', 'ghfgh', 'ghfhgfh']
    username='c',
)
session.add(user3)
session.commit()


i += 1

blog2 = Blog(
    body=default_body,
    caption="dgfdgfdgdgfd",
    date_uploaded=datetime.now(),
    description="fdshjfgdshjfgsd",
    is_public=False,
    image_url='mainimage.jpg',
    likes=random.randint(0, 1000),
    name="blog" + str(i),
    title="Urban Burger",
    user=user1,
)

session.add(blog2)
session.commit()


i += 1
blog3 = Blog(
    body=default_body,
    caption="dgfdgfdgdgfd",
    date_uploaded=datetime.now(),
    description="fdshjfgdshjfgsd",
    is_public=False,
    image_url='mainimage.jpg',
    likes=random.randint(0, 1000),
    name="blog" + str(i),
    title="Urban Burger",
    user=user2,
)

session.add(blog3)
session.commit()

i += 1
blog4 = Blog(
    body=default_body,
    caption="dgfdgfdgdgfd",
    date_uploaded=datetime.now(),
    description="fdshjfgdshjfgsd",
    is_public=False,
    image_url='mainimage.jpg',
    likes=random.randint(0, 1000),
    name="blog" + str(i),
    title="Urban Burger",
    user=user3,
)


session.add(blog4)

session.commit()


print("added more blogs!")
