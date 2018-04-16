# Full-Stack Udacity Project 3

## Simple Blog
I wanted to focus more on Database functionality like SQL alchemy and password libraries

Homepage

![logo](https://github.com/UndreamtMayhem/Udacity-Full-Stack-Unfinished/blob/master/P3%20SIMPLE%20BLOG%20done/Project%20Images/blogindex.PNG "didnt read")


### Installation
1. run blog_setup.py to create the database
` $ python blog_setup.py

2. run populateblogs.py to populate the database
` $ python populateblogs.py

3. run python3 simpleblog.py and navigate to http://127.0.0.1:5000/ in your browser


User Accounts: are very basic. When you add your own the password requires more security

username: a
password: a

username: b
password: b

username: c
password: c

username: d
password: d


### Whats used 
- Python v3
- Flask
- SQL alchemy
- Styling
    - CSS
    - W3 school css
    
- JS
    - custom js inlined on landing page
- python 
    - password.py: uses pbkdf2_sha256
        - random salt
        - create password
        - validate password
        - make salt
    - create data and populate database
    - /CreateData
### Database models
- Gender
- Users
- Tag
- Blog


### Routes
- /
- login
- register
- logout
- recent
- popular
- tags
- /blogs/tags/<tag>
- /public/blogs/<domain:username>
- /public/blogs/<domain:username>/<int:blog_id>
- /public/createblog
- /public/blogs/<domain:username>/<int:blog_id>/update
- /public/blogs/<domain:username>/<int:blog_id>/delete