# Python dependencies
from datetime import datetime

# SQL ALCHEMY DEPENDENCIES
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Local dependencies
from blogsetup import Base, Blog, Tag, Users
from random import randint



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


def create_blogs():
    blog_bodies = [
        'Lorem ipsum dolor amet man bun squid 3 wolf moon yuccie, cornhole pinterest kitsch snackwave pickled. Gastropub paleo tacos, banjo single-origin coffee actually 90\'s franzen. Put a bird on it cold-pressed cloud bread, fashion axe occupy viral craft beer brunch. Wolf unicorn umami, messenger bag prism lomo hashtag health goth typewriter. Taiyaki tumeric gentrify everyday carry scenester truffaut man bun copper mug venmo tacos. Listicle williamsburg meditation pour-over. Everyday carry irony authentic cray small batch, unicorn street art schlitz hashtag.',
        '8-bit cardigan minim elit bitters mixtape four loko schlitz coloring book neutra. Godard cronut green juice beard distillery, literally snackwave kinfolk do affogato exercitation. Meh try-hard fashion axe excepteur gentrify squid cronut sunt food truck migas hell of bicycle rights. Knausgaard slow-carb pop-up tacos salvia next level locavore truffaut labore brunch poutine pickled quis skateboard. Elit dreamcatcher synth id, pug tilde whatever enim shoreditch iPhone officia meh. Kickstarter taxidermy migas YOLO put a bird on it. Kale chips hella officia, pop-up trust fund blog palo santo irure cillum tilde tofu.',
        'Lorem ipsum dolor amet stumptown cornhole chicharrones sartorial taxidermy occupy aesthetic ennui pabst blue bottle kale chips waistcoat reprehenderit jean shorts polaroid. Bicycle rights pour-over pickled tilde. 3 wolf moon exercitation single-origin coffee, helvetica copper mug freegan reprehenderit vaporware. Culpa sint laboris, ramps pug veniam stumptown freegan do roof party.',
        'Af readymade asymmetrical blog, DIY brunch taxidermy salvia id seitan pinterest. Banh mi brooklyn fixie, cronut street art adipisicing eu polaroid snackwave typewriter chambray officia occupy meh master cleanse. Before they sold out hella viral seitan williamsburg proident. Whatever bitters celiac, irony tousled pug copper mug chillwave craft beer exercitation health goth velit pickled pabst godard.',
        'Fam waistcoat tumblr, stumptown et before they sold out offal keytar yr single-origin coffee palo santo meggings. Live-edge fingerstache brunch knausgaard, bushwick ethical locavore authentic. Hell of gastropub eiusmod tofu sriracha viral chicharrones listicle chillwave microdosing consequat.',
        'Meh paleo messenger bag meggings bitters direct trade selvage letterpress raclette tote bag lorem art party pickled austin. Gentrify ut culpa unicorn etsy ex. Synth four dollar toast photo booth hella XOXO kitsch. Biodiesel iceland skateboard seitan brooklyn kombucha kickstarter.',
        'Officia literally nulla elit adaptogen. Adaptogen gochujang laborum food truck synth selfies poke PBR&B live-edge exercitation affogato. Id incididunt velit occupy disrupt voluptate deep v biodiesel before they sold out jianbing PBR&B sed sunt kombucha +1. Cloud bread viral marfa culpa. Organic XOXO bitters, tote bag blog YOLO jean shorts.',
        'Freegan culpa salvia lorem ut next level yuccie in. Scenester aliqua copper mug, in voluptate incididunt hexagon eiusmod helvetica everyday carry truffaut 90\'s. Qui normcore kogi culpa typewriter organic, pour-over ut food truck street art XOXO farm-to-table taxidermy. Scenester subway tile raw denim master cleanse af fanny pack yr. Bushwick four loko butcher roof party, vaporware seitan authentic DIY wolf cardigan. Microdosing meditation cornhole, kogi dolore health goth portland selfies artisan typewriter gochujang paleo pickled. Elit locavore excepteur umami roof party vegan enamel pin cillum affogato fashion axe mumblecore.'
    ]

    descriptions = [
        '100%. You know, here\'s your first pee test. Next one goes in your mouth.',
        'I\'m done. I\'m done. It\'s on. Bring it, as I say. I ain\'t hidin.',
        'And one of those stupid mottoes, Alex, is \'Don\'t be special. Be one of us.',
        'You know, they lay down with their ugly wives in front of their ugly children and just look at their loser lives and then they look at me '
    ]

    names = [
        'Lorem', 'ipsum', 'dolor', 'amet', 'cred', 'mumblecore', 'hoodie', 'occaecat', 'retro', 'crucifix', 'snackwave', 'dolore', 'cray', 'commodo', 'hot',
        'chicken', 'pariatur', 'proident', 'keffiyeh', 'Vice', 'laborum', 'jean', 'shorts', 'eiusmod', 'dolore', 'snackwave', 'tumblr', 'la croix', 
        'Cold-pressed', 'aliqua', 'hot', 'chicken', 'organic', 'thundercats', 'wayfarers', 'freegan', 'woke', 'irony', 'tilde', 'pork',
        'belly', 'sartorial', 'chicharrones', 'tousled', 'everyday', 'carry', 'Succulents', 'cloud', 'bread', 'prism', 'four', 'loko', 'hell'
    ]

    titles = [
        'Aliqua four loko iPhone.', 
        'XOXO mustache austin brooklyn bitters.', 
        'Shaman bushwick 8-bit incididunt.',
        'Laboris skateboard marfa ullamco',
        'portland lumbersexual af', 'adipisicing street art actually.',
        'Excepteur ullamco officia',
        'banh mi sunt iceland ut single-origin',
        'coffee godard pariatur bespoke.',
        'Fingerstache vinyl adaptogen vaporware.', 
        'sunt cred in williamsburg.',
    ]
    users = session.query(Users).order_by(
            Users.id.desc()).limit(30)

    query_tags = session.query(Tag).order_by(Tag.id.desc()).all()

    for _user in users:

        # add a blog
        for i in range(0, 10):
            print("creating blogs for : " + _user.username)
            print(query_tags[randint(0, len(query_tags) - 1)].tagname)
            blog = Blog(
                body=blog_bodies[randint(0, len(blog_bodies) - 1)],
                caption=descriptions[randint(0, len(descriptions) - 1)],
                date_uploaded=datetime.now(),
                description=descriptions[randint(0, len(descriptions) - 1)],
                is_public=True,
                image_url='mainimage.jpg',
                likes=randint(5, 1000),
                name=names[randint(0, len(names) - 1 )],
                tag=query_tags[randint(0, len(query_tags) - 1)],
                title=titles[randint(0, len(titles) - 1)],
                user=_user,
            )


            session.add(blog)
            session.commit()
    print("Finished making blogs")