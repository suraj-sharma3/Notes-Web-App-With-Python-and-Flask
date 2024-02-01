# this file will make the website folder (the folder in which it is present) a python package, that means we can import the website folder as a package & whatever is inside the __init__.py file will run automatically whenever we import the website folder as a package.

from flask import Flask 

def create_app():
    app = Flask(__name__)
    app.config['SECRET KEY'] = 'rc2rTcueQa3cerGdtyAh9b' # this encrypts the session data (cookies, etc)
    # the key could be anything here as per our choice but we shouldn't reveal the key like this for an app in production
    return app



