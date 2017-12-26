#!/usr/bin/python

from flask import Flask, flash, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import exc
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

#from database_setup import Base, Users, Blog
from blogsetup import Base, Users, Blog
import flask_login
from password import make_salt, create_password, validate_password
import os
from datetime import datetime
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound
from werkzeug.utils import secure_filename


from registering.register import RegistrationLogic
from bloglogic.create_blog import BlogLogic


app = Flask(__name__)

engine = create_engine('sqlite:///userblogs.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


'''
    IMAGE UPLOADING
'''

UPLOAD_FOLDER = os.getcwd() + '/static/blog/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    ''' FILES ALLOWED for upload '''
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


'''
    Login SYSTEM
'''
app.secret_key = 'super secret string'

login_manager = flask_login.LoginManager()

login_manager.init_app(app)

# MAKE ALL THE CACHED MODELS

CACHE = {}

''' LOGIN ROUTES '''


class User(flask_login.UserMixin):
    pass


@login_manager.user_loader
def user_loader(username):
    try:
        curruser = session.query(Users).filter_by(username=username).one()
        if username not in curruser.username:
            return

        user = User()
        user.id = username
        
        CACHE['current_user'] = curruser
        return user
    except MultipleResultsFound:
        print("failed")
        # Deal with it
    except NoResultFound:
        # Deal with it
        print(" failed")


@login_manager.request_loader
def request_loader(request):

    username = request.form.get('username')
    try:
        curruser = session.query(Users).filter_by(username=username).one()

        if username not in curruser.username:
            return

        user = User()
        user.id = username

        user.is_authenticated = request.form['pw'] == curruser.password
        return user
    except MultipleResultsFound:
        print("")
        # Deal with it
    except NoResultFound:
        print("")


# login system
@app.route('/login/', methods=['GET', 'POST'])
def login():
    ''' USER LOGIN ROUTE AND LOGIC
    '''
    if request.method == 'GET':
        return render_template('login.html')

    else:
        username = request.form['username']
        validated_password = request.form['pw']

        try:
            curruser = session.query(Users).filter_by(username=username).one()

            if validate_password(validated_password + curruser.salt, curruser.password) is True:

                user = User()
                user.id = curruser.username

                flask_login.login_user(user)

                flash('You were successfully logged in')
                return redirect(url_for('recent'))

            else:
                flash('Incorrect Password')
                return redirect(url_for('login'))

        except NoResultFound as e:
            flash('Username doesnt exist')
            return render_template('login.html')


# TODO look for username and email see if they already exist
# if password doesnt match send old values back down to the form
@app.route('/register/', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':
        # TODO validate form
        password = request.form['pw']
        password1 = request.form['pw1']
        username = request.form['username']
        email = request.form['email']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        about = request.form['about']

        if password == password1:

            '''
                Passwords match 
                1. create the new user with the form values -
                2. make salt
                3. hash password
                4. create cleaned user
                5. create example blog 
                6. save and commit

            '''

            # 1. create the new user with the form values -
            new_user = RegistrationLogic(
                about, email, first_name, last_name, password, username)
            # 2. Make salt
            new_user.set_salt()
            # 3. Hash password
            new_user.set_salted_password()
            # 4. Create cleaned user
            cleaned_user = new_user.create_sql_user()
            # 5. create example blog
            users_first_blog = new_user.create_users_first_blog(cleaned_user)


            try:
                session.add(cleaned_user)
                session.add(users_first_blog)
                session.commit()
                flash('Account Created Successfully')
                # redirect('/login')
                return redirect(url_for('login'))
            except exc.IntegrityError as e:
                flash('username exists')
                session.rollback()
                return render_template("register.html")

        else:
            flash('Passwords did not match')
            # TODO use old values and pass to view
            # populate the views with old values
            return render_template("register.html")
    else:
        return render_template("register.html")




@app.route('/logout/')
def logout():
    ''' LOGOUT '''
    flask_login.logout_user()
    CACHE.pop('current_user', None)
    return redirect(url_for('index'))


@login_manager.unauthorized_handler
def unauthorized_handler():
    ''' deal with unauthorised users '''
    flash('You must login to access this route')
    return redirect(url_for('recent'))


@app.route('/')
def index():
    ''' HOME PAGE '''
    return render_template('landing_page.html')


@app.route('/recent/')
def recent():
    ''' GET RECENT BLOGS AND DISPLAY THEM '''
    if bool(CACHE):
        blogs = session.query(Blog).order_by(
            Blog.date_uploaded.desc()).limit(30)
        return render_template('top_blogs.html', blogs=blogs, curruser=CACHE['current_user'])
    else:
        blogs = session.query(Blog).order_by(
            Blog.date_uploaded.desc()).limit(30)
        return render_template('top_blogs.html', blogs=blogs, curruser={})


# CRUD ability  next

@app.route('/public/createblog/', methods=['GET', 'POST'])
@flask_login.login_required
def createblog():
    ''' Create a blog for the user'''
    if request.method == 'POST':

        # check file form first
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']

        # TODO validate other fields

        # if user does not select file, browser also submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        # check it has valid extension
        # if file is correct collect all the other fields
        if file and allowed_file(file.filename):

            filename = secure_filename(file.filename)

            # TODO then validate somemore

            body = request.form['body']
            caption = request.form['caption']
            description = request.form['description']
            name = request.form['name']
            is_public = request.form['public']
            title = request.form['title']
            image_url = filename
            # Create blog from the form fields
            new_blog = BlogLogic(body, caption, description,
                                 name, image_url, is_public, title)
            # Create and SQL formatted blog
            sql_blog = new_blog.create_blog(CACHE['current_user'])

            try:
                session.add(sql_blog)
                session.commit()
                # save image
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                flash('Succeedded')
                return redirect(url_for('createblog', filename=filename))
            except exc.IntegrityError as e:
                flash('couldnt save blog')
                session.rollback()
                return render_template('createblog.html')

        return render_template('createblog.html')
    else:
        #flash('Invalid file format')
        return render_template('createblog.html')


@app.route('/public/blogs/<domain>/')
@app.errorhandler(404)
@flask_login.login_required
def users_blogs(domain):
    try:

        allow_edit = False
        if(domain == flask_login.current_user.id):
            allow_edit = True

        single_blog = session.query(Blog, Users).join(
            Users).filter_by(username=domain).limit(30)
        return render_template('users_blogs.html', single_blog=single_blog, curruser=CACHE['current_user'], allow_edit=allow_edit)
    except MultipleResultsFound:
        return render_template('404.html'), 404
    except NoResultFound:
        return render_template('404.html'), 404


@app.route('/public/blogs/<domain>/<int:blog_id>/')
@app.errorhandler(404)
@flask_login.login_required
def domain_blog_read(domain, blog_id):
    try:
        allow_edit = False
        if(domain == flask_login.current_user.id):
            allow_edit = True
        single_blog = session.query(Blog, Users).join(Users).filter(
            Users.username == domain).filter(Blog.id == blog_id).one()
        return render_template('indivdual_blog.html', single_blog=single_blog, curruser=CACHE['current_user'], allow_edit=allow_edit)
    except MultipleResultsFound:
        return render_template('404.html'), 404
        # Deal with it
    except NoResultFound:
        return render_template('404.html'), 404


@app.route('/public/blogs/<string:domain>/<int:blog_id>/update', methods=['GET', 'POST'])
@flask_login.login_required
def domain_blog_update(domain, blog_id):
    if request.method == 'POST':
        try:
            # get the blog to edit
            editedBlog = session.query(Blog).filter_by(id=blog_id).one()

            # check this is users blog
            if domain == flask_login.current_user.id:

                # Validate fields
                if request.form['body']:
                    editedBlog.body = request.form['body']
                if request.form['caption']:
                    editedBlog.caption = request.form['caption']
                if request.form['description']:
                    editedBlog.description = request.form['description']
                if request.form['name']:
                    editedBlog.name = request.form['name']
                if request.form['public']:
                    editedBlog.is_public = request.form['public']
                if request.form['title']:
                    editedBlog.title = request.form['title']



                file = request.files['file']

                # if user does not select file use the old one
                if file.filename == '':
                    
                    session.add(editedBlog)
                    session.commit()

                    flash('Successfully edited blog')

                    return redirect('/public/blogs/'+domain+'/'+str(blog_id) +'/')
                # check it has valid extension
                # if file is correct delete old file and add a new one
                if file and allowed_file(file.filename):
                    
                    filename = secure_filename(file.filename)

                    path = app.config['UPLOAD_FOLDER']+"/"+editedBlog.image_url
           
                    # remove old photo
                    if os.path.isfile(path):
                        os.remove(path) 

                    

                    editedBlog.image_url = filename
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

                    session.add(editedBlog)
                    session.commit()
                    return redirect('/public/blogs/'+domain+'/'+str(blog_id) +'/')


        except MultipleResultsFound:
            return render_template('404.html'), 404
        # Deal with it
        except NoResultFound:
            return render_template('404.html'), 404
        else:
            return 'Unauthorized'
    else:
        
        if domain == flask_login.current_user.id:
            


            single_blog = session.query(Blog, Users).join(Users).filter(
                Users.username == domain).filter(Blog.id == blog_id).one()
            return render_template('indivdual_blog_update.html', single_blog=single_blog, curruser=CACHE['current_user'])


@app.route('/public/blogs/<string:domain>/<int:blog_id>/delete', methods=['GET', 'POST'])
@flask_login.login_required
def domain_blog_delete(domain, blog_id):
 # similar logic
    if request.method == 'POST':
        deleteBlog = session.query(Blog).filter_by(id=blog_id).one()
        try:
            #if username == stored value
            #username has to be whose logged in
            if domain == flask_login.current_user.id:
                
                
                path = app.config['UPLOAD_FOLDER']+"/"+deleteBlog.image_url
           
                # remove old photo
                if os.path.isfile(path):
                    os.remove(path) 

                session.delete(deleteBlog)
                session.commit()
                return redirect('/public/blogs/'+domain+'/')
            else:
                return 'Unauthorized'
        except MultipleResultsFound:
            return render_template('404.html'), 404
            # Deal with it
        except NoResultFound:
            return render_template('404.html'), 404


   
    else:
        allow_edit = False
        # try to deal with zero rows returned
        if domain == flask_login.current_user.id:
            allow_edit = True
            try:
                single_blog = session.query(Blog, Users).join(Users).filter(
                    Users.username == domain).filter(Blog.id == blog_id).one()
                return render_template('indivdual_blog_delete.html', single_blog=single_blog, curruser=CACHE['current_user'], allow_edit=allow_edit)
            except MultipleResultsFound:
                return render_template('404.html'), 404
            # Deal with it
            except NoResultFound:
                return render_template('404.html'), 404


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
