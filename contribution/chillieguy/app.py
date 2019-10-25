# Flask imports

from flask import Flask, render_template, request, redirect, jsonify
from flask import url_for, flash

# Database imports

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Catagory, Item

# Login, Authorization and Anti-forgery imports

from flask import session as login_session
import random
import string

# Google OAuth

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
import requests
from flask import make_response
from functools import wraps

# Create the app

app = Flask(__name__)

CLIENT_ID = json.loads(open('client_secrets.json', 'r').read())['web']['client_id']  # noqa
APPLICATION_NAME = "Chillie's Sports Catalog"

# Connect to Database and create database session
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# DECORATOR - Require login to access specified pages
def login_required(f):
    '''
    Force login to access routes or send to login page
    '''
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in login_session:
            flash('Login to continue!', 'info')
            return redirect(url_for('showLogin'))
        return f(*args, **kwargs)
    return decorated_function


# Routes

@app.route('/')
@app.route('/catalog/')
def index():
    '''
    Display home page of website
    '''
    catagories = session.query(Catagory).all()
    items = session.query(Item).order_by(Item.updated_at).limit(10).all()
    return render_template('index.html', catagories=catagories, items=items)


# @app.route('/catalog/<int:catagory_id>/')
@app.route('/catalog/<string:catagory_name>/')
def show_catagory(catagory_name):
    '''
    Show page that lists all items in catagory
    '''
    catagory = session.query(Catagory).filter_by(name=catagory_name).first()
    items = session.query(Item).filter_by(catagory_id=catagory.id)

    return render_template('showcatagory.html', catagory=catagory, items=items)


@app.route('/catalog/<string:catagory_name>/<int:item_id>/')
def show_item(catagory_name, item_id):
    '''
    Show page that list details on specified item
    '''
    catagory = session.query(Catagory).filter_by(name=catagory_name).first()
    item = session.query(Item).filter_by(id=item_id).one()

    return render_template('showitem.html', catagory=catagory, item=item)


@app.route('/catalog/additem/', methods=['GET', 'POST'])
@login_required
def add_item():
    '''
    GET - Display page to add item
    POST - Submit page form and save to database
    '''
    catagories = session.query(Catagory).all()

    if request.method == "POST":
        if request.form['item'] and request.form['description'] and request.form['catagory']:  # noqa
            name = request.form['item']
            description = request.form['description']
            catagory_id = int(request.form['catagory'])
            user_id = login_session['user_id']

            new_item = Item(name=name,
                            description=description,
                            catagory_id=catagory_id,
                            user_id=user_id)
            session.add(new_item)
            session.commit()
        else:
            flash("Please complete all fields in form.", "warning")
            return render_template('additem.html', catagories=catagories)

        flash("Item created!", 'success')
        return redirect(url_for('index'))

    return render_template('additem.html', catagories=catagories)


@app.route('/catalog/edititem/<int:item_id>/', methods=['GET', 'POST'])
@login_required
def edit_item(item_id):
    '''
    GET - Display page with item info to be modified
    POST - Submit page form and save to database
    '''
    item = session.query(Item).filter_by(id=item_id).one()
    catagories = session.query(Catagory).all()
    catagory = session.query(Catagory).filter_by(id=item.catagory_id).one()

    if item.user_id != login_session['user_id']:
        flash('Current user is not allowed to modify current item!', 'danger')
        return render_template('showitem.html', item=item, catagory=catagory)

    if request.method == "POST":
        if request.form['item'] and request.form['description'] and request.form['catagory']:  # noqa
            name = request.form['item']
            description = request.form['description']
            catagory_id = int(request.form['catagory'])

            edit_item = session.query(Item).filter_by(id=item_id).one()
            edit_item.name = name
            edit_item.description = description
            edit_item.catagory_id = catagory_id
            session.commit()
        else:
            flash("Please complete all fields in form.", "warning")
            return render_template('additem.html', catagories=catagories)

        flash("Item updated!", 'success')
        return redirect(url_for('index'))

    return render_template('edititem.html', item=item, catagories=catagories)


@app.route('/catalog/deleteitem/<int:item_id>/', methods=['GET', 'POST'])
@login_required
def delete_item(item_id):
    '''
    GET - Display confirmation page for item deletion
    POST - Submit page and remove item from database
    '''
    item = session.query(Item).filter_by(id=item_id).one()
    catagory = session.query(Catagory).filter_by(id=item.catagory_id).one()

    if item.user_id != login_session['user_id']:
        flash('Current user is not allowed to delete current item!', 'danger')
        return render_template('showitem.html', item=item, catagory=catagory)

    if request.method == "POST":
        item = session.query(Item).filter_by(id=item_id).one()
        session.delete(item)
        session.commit()
        flash("Item deleted!", 'danger')
        return redirect(url_for('index'))

    return render_template('deleteitem.html', item=item, catagory=catagory)


# JSON endpoints

@app.route('/catalog/JSON')
@app.route('/catalog/json')
@app.route('/catalog/catalog.json')
def catalogJSON():
    '''
    Return all items in json format
    '''
    items = session.query(Item).all()

    return jsonify(Item=[item.serialize for item in items])


@app.route('/catalog/catagory/JSON')
@app.route('/catalog/catagory/json')
def catagoriesJSON():
    '''
    Return all catagories in json format
    '''
    catagories = session.query(Catagory)

    return jsonify(Catagory=[catagory.serialize for catagory in catagories])


@app.route('/catalog/catagory/<int:catagory_id>/JSON')
@app.route('/catalog/catagory/<int:catagory_id>/json')
def catagoryJSONid(catagory_id):
    '''
    Return all items in catagory from provided catagory id
    '''
    items = session.query(Item).filter_by(catagory_id=catagory_id)

    return jsonify(Item=[item.serialize for item in items])


@app.route('/catalog/catagory/<string:catagory_name>/JSON')
@app.route('/catalog/catagory/<string:catagory_name>/json')
def catagoryJSONstring(catagory_name):
    '''
    Return all items in catagory from provided catagory name
    '''
    catagory = session.query(Catagory).filter_by(name=catagory_name).first()
    items = session.query(Item).filter_by(catagory_id=catagory.id)

    return jsonify(Item=[item.serialize for item in items])


@app.route('/catalog/item/<int:item_id>/JSON')
@app.route('/catalog/item/<int:item_id>/json')
def itemJSON(item_id):
    '''
    Return item details from provided item id
    '''
    item = session.query(Item).filter_by(id=item_id).one()

    return jsonify(Item=item.serialize)


# Anti-forgery state token
@app.route('/login/')
def showLogin():
    '''
    Display login page
    '''
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    return render_template("login.html", STATE=state)


@app.route('/gconnect', methods=['POST'])
def gconnect():
    '''
    Connect to Google OAUTH
    '''
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print("Token's client ID does not match app's.")
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'), 200)  # noqa
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += ' Logging In!</h1>'
    flash("Logged in as %s" % login_session['username'], 'success')
    print("done!")
    return output


@app.route('/gdisconnect')
def gdisconnect():
    '''
    Disconnect from Google OAUTH
    '''
    access_token = login_session.get('access_token')
    if access_token is None:
        print('Access Token is None')
        response = make_response(json.dumps('Current user not connected'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    print('In gdisconnect access token is %s', access_token)
    print('User name is: ')
    print(login_session['username'])
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % login_session['access_token']  # noqa
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print('result is ')
    print(result)
    if result['status'] == '200':
        del login_session['user_id']
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        flash("Successfully logged out!", 'success')
        return redirect(url_for('index'))
    else:
        flash("Failed to logout!", 'danger')
        return redirect(url_for('index'))


# User helper functions

def createUser(login_session):
    '''
    Add new user to database
    '''
    newUser = User(name=login_session['username'],
                   email=login_session['email'],
                   picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    '''
    Return user info from provided user id
    '''
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    '''
    Return user id from provided email
    '''
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)