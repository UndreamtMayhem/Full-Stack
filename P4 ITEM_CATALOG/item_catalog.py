""" Flask item catalog """
from flask import Flask, render_template, request, redirect, jsonify, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import BASE, Restaurant, MenuItem

APP = Flask(__name__)

ENGINE = create_engine('sqlite:///restaurantmenu.db')
BASE.metadata.bind = ENGINE

DBSESSION = sessionmaker(bind=ENGINE)
SESSION = DBSESSION()

""" JSON routes """
@APP.route('/restaurant/<int:restaurant_id>/menu/JSON')
def restaurant_menu_json(restaurant_id):
    """returns a restaurants Menu items in JSON format"""
    restaurants = SESSION.query(MenuItem).join(Restaurant).\
         filter(Restaurant.id == restaurant_id).\
         all()
    return jsonify(menu_item=[r.serialize for r in restaurants])

@APP.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/JSON')
def menu_item_json(restaurant_id, menu_id):
    """returns a restaurant Menus indivdual item in JSON format"""
    restaurants = SESSION.query(MenuItem).join(Restaurant).\
         filter(Restaurant.id == restaurant_id).\
         all()
    matched_menu_item = []
    for r in restaurants:
        if r.id == menu_id:
            matched_menu_item.append(r)
    return jsonify(menu_item=[r.serialize for r in matched_menu_item])

@APP.route('/restaurant/JSON')
def restaurants_json():
    """returns all restaurants in JSON format"""
    restaurants = SESSION.query(Restaurant).all()
    return jsonify(restaurants=[r.serialize for r in restaurants])

@APP.route('/menus/JSON')
def menu_items_json():
    """returns all menu items in JSON format"""
    items = SESSION.query(MenuItem).all()
    return jsonify(menu_items=[r.serialize for r in items])

@APP.route('/menu/<int:menu_id>/JSON')
def single_menu_item_json(menu_id):
    """returns individual menu item in JSON format"""
    menu_item = SESSION.query(MenuItem).filter_by(id=menu_id).all()
    return jsonify(menu_items=[m.serialize for m in menu_item])

""" APP routes"""

@APP.route('/')
def show_restaurants():
    """returns homepage"""
    restaurants = SESSION.query(Restaurant).all()
    return render_template('index.html', restaurants=restaurants)

@APP.route('/about')
def about_restaurants():
    """returns about page"""
    return render_template('about.html')

@APP.route('/latest')
def latest_restaurants():
    """returns latest page"""
    return render_template('latest.html')

@APP.route('/restaurants')
def menu_restaurants():
    """returns restaurants and displays to page"""
    restaurants = SESSION.query(Restaurant).all()
    return render_template('restaurants.html', restaurants=restaurants)

@APP.route('/reservations')
def reservations_restaurants():
    """returns latest reservations page"""
    return render_template('reservations.html')

@APP.route('/photos')
def photos_restaurants():
    """returns photos"""
    return render_template('photos.html')


@APP.route('/restaurant/new/', methods=['GET', 'POST'])
def new_restaurant():
    """POST  Create a new restaurant: GET  render Create a new restaurant form"""
    if request.method == 'POST':
        created_restaurant = Restaurant(
            name=request.form['name'],
            description=request.form['description'],
            image=request.form['image'])
        SESSION.add(created_restaurant)
        SESSION.commit()
        return redirect(url_for('show_restaurants'))
    else:
        return render_template('newRestaurant.html')


@APP.route('/restaurant/<int:restaurant_id>/edit/', methods=['GET', 'POST'])
def edit_restaurant(restaurant_id):
    """V 0.0.2 POST  Edit a restaurant: GET  render Edit a restaurant form"""
    edited_restaurant = SESSION.query(
        Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        if request.form['name'] and  request.form['description'] and request.form['image']:
            edited_restaurant.name = request.form['name']
            edited_restaurant.description = request.form['description']
            edited_restaurant.image = request.form['image']
            return redirect(url_for('menu_restaurants'))
    else:
        return render_template(
            'editRestaurant.html', restaurant=edited_restaurant)

@APP.route('/restaurant/<int:restaurant_id>/delete/', methods=['GET', 'POST'])
def delete_restaurant(restaurant_id):
    """V 0.0.0 POST Delete a restaurant: GET  render  Delete a restaurant form"""
    restaurant_to_delete = SESSION.query(
        Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        SESSION.delete(restaurant_to_delete)
        SESSION.commit()
        return redirect(
            url_for('menu_restaurants', restaurant_id=restaurant_id))
    else:
        return render_template(
            'deleteRestaurant.html', restaurant=restaurant_to_delete)


@APP.route('/restaurant/<int:restaurant_id>/')
@APP.route('/restaurant/<int:restaurant_id>/menu/')
def show_menu(restaurant_id):
    """V 0.0.0 POST Show a restaurant menu: GET  render Show a restaurant menu form"""
    restaurant = SESSION.query(Restaurant).filter_by(id=restaurant_id).one()
    items = SESSION.query(MenuItem).filter_by(
        restaurant_id=restaurant_id).all()
    return render_template('menus.html', items=items, restaurant=restaurant)

@APP.route('/restaurant/<int:restaurant_id>/menu/new/', methods=['GET', 'POST'])
def new_menu_item(restaurant_id):
    """V 0.0.0 POST Create a new menu item: GET  render Create a new menu item form"""
    if request.method == 'POST':
        # TODO validation and if else branch
        new_item = MenuItem(name=request.form['name'],
                            description=request.form['description'],
                            price=request.form['price'],
                            course=request.form['course'],
                            restaurant_id=restaurant_id)
        SESSION.add(new_item)
        SESSION.commit()
        return redirect(url_for('show_menu', restaurant_id=restaurant_id))
    else:
        return render_template('newmenuitem.html', restaurant_id=restaurant_id)

# showMenu
@APP.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit', methods=['GET', 'POST'])
def edit_menu_item(restaurant_id, menu_id):
    """V 0.0.2 POST Edit a menu item: GET  render Edit a menu item form"""
    edited_item = SESSION.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        # TODO needs an else
        if request.form['name']:
            edited_item.name = request.form['name']
        if request.form['description']:
            edited_item.description = request.form['description']
        if request.form['price']:
            edited_item.price = request.form['price']
        if request.form['course']:
            edited_item.course = request.form['course']
        SESSION.add(edited_item)
        SESSION.commit()
        return redirect(url_for('show_menu', restaurant_id=restaurant_id))
    else:
        return render_template(
            'editmenuitem.html', restaurant_id=restaurant_id, menu_id=menu_id, item=edited_item)

@APP.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete', methods=['GET', 'POST'])
def delete_menu_item(restaurant_id, menu_id):
    """V 0.0.0 POST Delete a menu item: GET  render Delete a menu item form"""
    item_to_delete = SESSION.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        SESSION.delete(item_to_delete)
        SESSION.commit()
        return redirect(url_for('show_menu', restaurant_id=restaurant_id))
    else:
        return render_template('deletemenuitem.html', item=item_to_delete)


if __name__ == '__main__':
    APP.debug = True
    APP.run(host='0.0.0.0', port=5000)
