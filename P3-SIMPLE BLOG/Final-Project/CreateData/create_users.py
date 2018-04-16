# Python dependencies
from datetime import datetime

# SQL ALCHEMY DEPENDENCIES
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Local dependencies
from blogsetup import Base, Users
from password import create_password, make_salt, validate_password


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




def create_users():
    abouts = [
        'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Sed nisi. Nulla quis sem at nibh elementum imperdiet. Duis sagittis ipsum. Praesent mauris. Fusce nec tellus sed augue semper porta. Mauris massa. Vestibulum lacinia arcu eget nulla. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Curabitur sodales ligula in libero. Sed dignissim lacinia nunc. Curabitur tortor. Pellentesque nibh. Aenean quam. In scelerisque sem at dolor. Maecenas mattis. Sed convallis tristique sem. Proin ut ligula vel nunc egestas porttitor. Morbi lectus risus, iaculis vel, suscipit quis, luctus non, massa. Fusce ac turpis quis ligula lacinia aliquet. Mauris ipsum. Nulla metus metus, ullamcorper vel, tincidunt sed, euismod in, nibh. Quisque volutpat condimentum velit. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nam nec ante. Sed lacinia, urna non tincidunt mattis, tortor neque adipiscin.',
        'I love jujubes cotton candy sweet liquorice jujubes. Donut candy jelly gingerbread muffin carrot cake pastry marshmallow topping. Sweet roll jelly beans lemon drops jelly beans icing tiramisu cake pie. Jujubes cookie croissant gingerbread. Wafer apple pie jelly beans candy canes gingerbread tiramisu donut lollipop apple pie. Pudding cake gummies I love chupa chups tart cotton candy jujubes lollipop. Cake chocolate wafer brownie. Halvah pudding chocolate tootsie roll I love cake icing croissant candy canes. Biscuit sesame snaps lemon drops sweet pudding. Donut chocolate cake toffee topping ice cream. Biscuit pastry candy icing tootsie roll. Croissant chupa chups carrot cake carrot cake. Lollipop caramels tiramisu jelly beans.',
        'Zombies reversus ab inferno, nam malum cerebro. De carne animata corpora quaeritis. Summus sit​​, morbo vel maleficia? De Apocalypsi undead dictum mauris. Hi mortuis soulless creaturas, imo monstra adventus vultus comedat cerebella viventium. Qui offenderit rapto, terribilem incessu. The voodoo sacerdos suscitat mortuos comedere carnem. Search for solum oculi eorum defunctis cerebro. Nescio an Undead zombies. Sicut malus movie horror.',
        'Don\'t be too proud of this technological terror you\'ve constructed. The ability to destroy a planet is insignificant next to the power of the Force. As you wish. Look, I can take you as far as Anchorhead. You can get a transport there to Mos Eisley or wherever you\'re going.'
    ]

    emails = [
        'a@a.com',
        'b@b.com',
        'c@c.com',
        'd@d.com',
    ]

    first_names = [
        'Roman',
        'Andrew',
        'Chay',
        'Spencer',
        'Jaydan',
    ]

    last_names = [
        'Carter',
        'Hunt',
        'Williams',
        'Parker',
        'Hamilton'
    ]
    usernames = [
        'a',
        'b',
        'c',
        'd'
    ]

    users = []
    for i in range(0, 4):
        print("Created user: " + usernames[i])
        # make password salt
        new_salt = make_salt()

        # create salted password
        salted_password = create_password('a', new_salt)


        user = Users(
            about=abouts[i],
            #blogs_following = ["b", "c"]
            email=emails[i],
            facebook_link='/',
            first_name=first_names[i],
            gender='male',
            last_name=last_names[i],
            linkedin_link='/',
            password=salted_password,
            pininterest_link='/',
            profile_pic='userprofile.png',
            salt=new_salt,
            snapchat_link='/',
            twitter_link='/',
            #tags = ['a', 'ghfgh', 'ghfhgfh']
            username=usernames[i],
        )

        

        session.add(user)
        session.commit()


    print("Finished making users")