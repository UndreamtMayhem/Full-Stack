# Full-Stack Udacity Project 4

## Item Catalog: Restaurant menu items


Homepage
add codepen link


## description of project
You will develop an application that provides a list of items within a variety of categories as well as provide a user 
registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

## About this project
* Using relational database through an ORM
* Using Template engine
* Using CRUD
* Using python3
* Using OOP language

To run this final project

Install flask : sudo pip install Flask

Dependencies:
* SQL Alchemy
* Template engine: http://jinja.pocoo.org/docs/2.10/templates/

### Getting Started
1. run `python3 database_setup.py to create the database
2. run `python3 lotsofmenus.py to populate the database
3. run `python3 ./item-catalog.py and navigate to localhost:5000 in your browser

### Whats used 
- Python v3
- Flask v1.11
- SQL Alchemy
- Styling
    - CSS
    - Bulma css
    - fontawesome
- JS
    - Jquery
 
### Database
- Restaurant
- MenuItem

### Routes
- /
- /about
- /latest
- /restaurants
- /reservations
- /photos
- /restaurant/new/
- /restaurant/<int:restaurant_id>/edit/
- /restaurant/<int:restaurant_id>/delete/
- /restaurant/<int:restaurant_id>/
- /restaurant/<int:restaurant_id>/menu/new/
- /restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit
- /restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete

### Future requirements
* Tidy up design
* Add more json routes
* Potentially rename Menu to recipe
* Validate forms 
* Error Handle SQL ALCHEMY 
* Move model and queries into a module