# this file will make the website folder (the folder in which it is present) a python package, that means we can import the website folder as a package & whatever is inside the __init__.py file will run automatically whenever we import the website folder as a package.

from flask import Flask 

def create_app():
    app = Flask(__name__)
    app.config['SECRET KEY'] = 'rc2rTcueQa3cerGdtyAh9b' # this encrypts the session data (cookies, etc)
    # the key could be anything here as per our choice but we shouldn't reveal the key like this for an app in production
    # registering the blueprints that were created like views & auth
    from .views import views # . just means the root directory of the package or the package itself, we can even write the package name like this from webapp.views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix = '/') # home page (views)
    app.register_blueprint(auth, url_prefix = '/') # login page , url_prefix means where can a specific file within the blueprint be accessed, we can even put a prefix here like '/auth/'
    return app



