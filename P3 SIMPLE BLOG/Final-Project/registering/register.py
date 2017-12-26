from datetime import datetime
from password import make_salt, create_password, validate_password
from blogsetup import Users, Blog


# TODO add form validation

class RegistrationLogic(object):
    def __init__(self, about, email, first_name, last_name, password, username):
        
        # default_fields
        default_link = '/'
        default_profile_picture = 'userprofile.png'

        self.about = about
        self.email = email
        self.facebook_link = default_link
        self.first_name = first_name
        self.gender = 'male'
        self.last_name = last_name
        self.linkedin_link = default_link
        self.password = password
        self.pininterest_link = default_link
        self.profile_pic = default_profile_picture
        self.salt = ''
        self.snapchat_link = default_link
        self.twitter_link = default_link
        self.username = username

    def __repr__(self):
        return(
            self.about +
            self.email +
            self.facebook_link +
            self.first_name +
            self.gender +
            self.last_name +
            self.linkedin_link +
            self.password +
            self.pininterest_link +
            self.profile_pic +
            self.salt +
            self.snapchat_link +
            self.twitter_link)

    def set_salt(self):
        """SETS salt."""
        # create salt
        new_salt = make_salt()
        self.salt = new_salt
        print(self.salt)

    def set_salted_password(self):
        """SETS salt password."""
        # create salted password
        self.password= create_password(self.password, self.salt)
        print(self.password)

    def create_users_first_blog(self, blog_user):
        """Create user an example blog."""
        default_body = '''
        Tumeric austin adaptogen edison bulb irony cornhole put a bird on it, four dollar toast kinfolk cardigan affogato hell of chartreuse raw denim. Normcore etsy la croix tattooed meggings edison bulb hammock hella. Skateboard hexagon salvia taiyaki prism, letterpress godard blog gluten-free twee. Occupy skateboard YOLO, intelligentsia forage pinterest kombucha snackwave vexillologist glossier readymade. Raw denim etsy health goth hammock coloring book everyday carry humblebrag pickled try-hard unicorn. Blue bottle disrupt mumblecore viral meggings before they sold out snackwave knausgaard put a bird on it. Venmo tbh semiotics readymade, butcher leggings blog listicle activated charcoal farm-to-table hoodie. Roof party whatever celiac art party, quinoa tbh you probably haven't heard of them wayfarers blue bottle tacos. Kogi snackwave letterpress truffaut, vegan ramps ugh copper mug freegan retro yuccie small batch flannel fingerstache. Keffiyeh af biodiesel wayfarers semiotics godard. Man braid skateboard gluten-free four loko enamel pin tumeric.
        '''

        first_blog = Blog(
            body=default_body,
            caption="dgfdgfdgdgfd",
            date_uploaded=datetime.now(),
            description="fdshjfgdshjfgsd",
            is_public=True,
            image_url='mainimage.jpg',
            likes=0,
            name="blog",
            title="YOUR first blog",
            user=blog_user,
        )
        return first_blog

    def create_sql_user(self):
        """create_sql_user object and returns it to allow user to save it."""
        new_user = Users(
            about=self.about,
            email=self.email,
            facebook_link=self.facebook_link,
            first_name=self.first_name,
            gender=self.gender,
            last_name=self.last_name,
            linkedin_link=self.linkedin_link,
            password=self.password,
            pininterest_link=self.pininterest_link,
            profile_pic=self.profile_pic,
            salt=self.salt,
            snapchat_link=self.snapchat_link,
            twitter_link=self.twitter_link,
            username=self.username)
        return new_user
