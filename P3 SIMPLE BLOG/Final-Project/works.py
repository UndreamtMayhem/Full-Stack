
from flask import Flask, render_template, request, redirect, jsonify, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Users, Blog
import flask_login
from password import make_salt, create_password, validate_password
from datetime import datetime
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound

app = Flask(__name__)

engine = create_engine('sqlite:///blogs.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


app.secret_key = 'super secret string'  # Change this!

login_manager = flask_login.LoginManager()

login_manager.init_app(app)




users = {'foo@bar.tld': {'pw': 'secret'}}
curuser = {}

class User(flask_login.UserMixin):
    pass


@login_manager.user_loader
def user_loader(email):
    try:
        curruser = session.query(Users).filter_by(email = email).one()
        if email not in curruser.email:
            return

        user = User()
        user.id = email
        return user
    except MultipleResultsFound:
        print("")
        # Deal with it
    except NoResultFound:
        print("")

@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    
    try:
        curruser = session.query(Users).filter_by(email = email).one()
        if email not in curruser.email:
            return

        user = User()
        user.id = email


        user.is_authenticated = request.form['pw'] == users[email]['pw']
        print(user.is_authenticated)
        return user
    except MultipleResultsFound:
        print("")
        # Deal with it
    except NoResultFound:
        print("")


#make into a glorified view
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
       # {% if current_user.is_authenticated %}
       #     Hi {{ current_user.name }}!
       #     {% endif %}
        return render_template('login.html')
    else:
        email = request.form['email']
        validated_password = request.form['pw']
        curruser = session.query(Users).filter_by(email = email).one()

        #salted_password = create_password(validated_password, new_salt)        
        #if validate_password('password', 'retrivedsalt') == True:
        if validate_password(validated_password + curruser.salt, curruser.password) == True:
                print("validated password XD")
                user = User()
                user.id = curruser.email
                flask_login.login_user(user)
                return redirect('/public/domain')
                #return redirect(url_for('protected'))

        return 'Bad login'



    
        
        # get user from database 
        # mock it i need encryption
        # get from laptop


### login system

@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # validate form
        username = request.form['username']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password1 = request.form['pw']
        password2 = request.form['pw1']

        if password1 == password2:
            print("Passwords Match")
        
            # create salt
            new_salt = make_salt()
            print(new_salt)
        
            # create salted password
            salted_password = create_password(password1, new_salt)
            print(salted_password)
            start_up_blog = Blog(title="My first blog", body="Your blog is a little lonely", date_uploaded=datetime.now(), is_public= False)

            new_user = Users(username=username, first_name=first_name, last_name=last_name, email=email, password=salted_password, salt=new_salt, gender='male', blog=start_up_blog)
            # create a sample blog
            #blog=blog1

            session.add(new_user)
            session.commit()
            redirect('/')

        return render_template("register.html")

    else:
       # {% if current_user.is_authenticated %}
       #     Hi {{ current_user.name }}!
       #     {% endif %}
        return render_template("register.html")
     


















@app.route('/protected')
@flask_login.login_required
def protected():
    return 'Logged in as: ' + flask_login.current_user.id


@app.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'

@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'


@app.route('/')
@app.route('/public/')
def index():

    return render_template('landing_page.html')


@app.route('/public/domain/')
@flask_login.login_required
def domain():
    blogs = session.query(Blog).order_by(Blog.date_uploaded.asc()).limit(30)
    return render_template('top_blogs.html', blogs=blogs)

### CRUD ability 
@app.route('/public/createblog/', methods=['GET', 'POST'])
@flask_login.login_required
def createblog():
    if request.method == 'POST':
        print("add a form")
        blogtitle = request.form['blogtitle']
        blogcontent = request.form['blogcontent']
        public = request.form['public']
        new_blog = Blog(title=blogtitle, body=blogcontent, is_public=public, date_uploaded=datetime.now())
        session.add(new_blog)
        session.commit()
        return render_template('createblog.html')
    else:
        print(flask_login.current_user.id)
        return render_template('createblog.html')

#@app.route('/public/domain/<int:blogid>/')
@app.route('/public/<string:domain>/<int:blog_id>/')
@app.errorhandler(404)
@flask_login.login_required
def domain_blog_read(domain, blog_id):
    # similar logic
    if request.method == 'POST':
        print("add a form")
    else:
        try:
            #Users.username == "a",
            single_blog = session.query(Users).filter(Users.username == domain, Blog.id == blog_id).one()
            #filter(Blog.id == blogid).one()
            #x = g.filter(Blog.id == blogid)
            print(single_blog.blog.body)
            #print(g[1].blog.body)
            #filter(Blog.id == blogid).one()
            #single_blog = session.query(Blog).filter_by(id=blog_id).one()
            #single_blog = session.query(Users, Blog).join(Blog).filter_by(id=blogid).one()
            return render_template('indivdual_blog.html', blog=single_blog)
        except MultipleResultsFound:
            return render_template('404.html'), 404
            # Deal with it
        except NoResultFound:
            return render_template('404.html'), 404
        
    




@app.route('/public/<string:domain>/<int:blog_id>/update/')
@flask_login.login_required
def domain_blog_update(domain, blog_id):
# similar logic
    try:
        #Users.username == "a",
        single_blog = session.query(Users).filter(Users.username == domain, Blog.id == blog_id).one()
        #filter(Blog.id == blogid).one()
        #x = g.filter(Blog.id == blogid)
        print(single_blog.blog.body)
        #print(g[1].blog.body)
        #filter(Blog.id == blogid).one()
        #single_blog = session.query(Blog).filter_by(id=blog_id).one()
        #single_blog = session.query(Users, Blog).join(Blog).filter_by(id=blogid).one()
        return render_template('indivdual_blog_update.html', blog=single_blog)
    except MultipleResultsFound:
        return render_template('404.html'), 404
        # Deal with it
    except NoResultFound:
        return render_template('404.html'), 404



@app.route('/public/<string:domain>/<int:blog_id>/delete/')
@flask_login.login_required
def domain_blog_delete(domain, blog_id):
 # similar logic
    try:
        #username
        single_blog = session.query(Users).filter(Users.username == domain, Blog.id == blog_id).one()
        #filter(Blog.id == blogid).one()
        #x = g.filter(Blog.id == blogid)
        print(single_blog.blog.body)
        #print(g[1].blog.body)
        #filter(Blog.id == blogid).one()
        #single_blog = session.query(Blog).filter_by(id=blog_id).one()
        #single_blog = session.query(Users, Blog).join(Blog).filter_by(id=blogid).one()
        return render_template('indivdual_blog_delete.html', blog=single_blog)
    except MultipleResultsFound:
        return render_template('404.html'), 404
        # Deal with it
    except NoResultFound:
        return render_template('404.html'), 404





""""
# Show all restaurants
@app.route('/b')
@app.route('/blogs/')
def showBlogs():
    blogs = session.query(Blog).all()
    # return "This page will show all my restaurants"
    return render_template('index.html', blogs=blogs)


# Create a new restaurant
@app.route('/restaurant/new/', methods=['GET', 'POST'])
def newRestaurant():
    if request.method == 'POST':
        newRestaurant = Restaurant(name=request.form['name'])
        session.add(newRestaurant)
        session.commit()
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('newRestaurant.html')
    # return "This page will be for making a new restaurant"

# Edit a restaurant


@app.route('/restaurant/<int:restaurant_id>/edit/', methods=['GET', 'POST'])
def editRestaurant(restaurant_id):
    editedRestaurant = session.query(
        Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedRestaurant.name = request.form['name']
            return redirect(url_for('showRestaurants'))
    else:
        return render_template(
            'editRestaurant.html', restaurant=editedRestaurant)

    # return 'This page will be for editing restaurant %s' % restaurant_id

# Delete a restaurant


@app.route('/restaurant/<int:restaurant_id>/delete/', methods=['GET', 'POST'])
def deleteRestaurant(restaurant_id):
    restaurantToDelete = session.query(
        Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        session.delete(restaurantToDelete)
        session.commit()
        return redirect(
            url_for('showRestaurants', restaurant_id=restaurant_id))
    else:
        return render_template(
            'deleteRestaurant.html', restaurant=restaurantToDelete)
    # return 'This page will be for deleting restaurant %s' % restaurant_id


# Show a restaurant menu
@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu/')
def showMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(
        restaurant_id=restaurant_id).all()
    return render_template('menu.html', items=items, restaurant=restaurant)
    # return 'This page is the menu for restaurant %s' % restaurant_id

# Create a new menu item


@app.route(
    '/restaurant/<int:restaurant_id>/menu/new/', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    if request.method == 'POST':
        newItem = MenuItem(name=request.form['name'], description=request.form[
                           'description'], price=request.form['price'], course=request.form['course'], restaurant_id=restaurant_id)
        session.add(newItem)
        session.commit()

        return redirect(url_for('showMenu', restaurant_id=restaurant_id))
    else:
        return render_template('newmenuitem.html', restaurant_id=restaurant_id)

    return render_template('newMenuItem.html', restaurant=restaurant)
    # return 'This page is for making a new menu item for restaurant %s'
    # %restaurant_id

# Edit a menu item


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit',
           methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
    editedItem = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['description']:
            editedItem.description = request.form['name']
        if request.form['price']:
            editedItem.price = request.form['price']
        if request.form['course']:
            editedItem.course = request.form['course']
        session.add(editedItem)
        session.commit()
        return redirect(url_for('showMenu', restaurant_id=restaurant_id))
    else:

        return render_template(
            'editmenuitem.html', restaurant_id=restaurant_id, menu_id=menu_id, item=editedItem)

    # return 'This page is for editing menu item %s' % menu_id

# Delete a menu item


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete',
           methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    itemToDelete = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        return redirect(url_for('showMenu', restaurant_id=restaurant_id))
    else:
        return render_template('deleteMenuItem.html', item=itemToDelete)
    # return "This page is for deleting menu item %s" % menu_id
"""

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
