from flask import Blueprint
# a Blueprint means all the URLs / routes one can find on a website, it helps to keep the website organised, we wouldn't have to keep all the views in one place
auth = Blueprint('auth', __name__)

# this file would have the login, logout & signup page
# if we have any errors in the routes, the server would crash

@auth.route('/login')
def login():
    return "<p>Login</p>"
# even though we can put our HTML code for a webpage as a string here, but we would create & put all our html files / templates inside the templates folder

@auth.route("/logout")
def logout():
    return "<p>Logout</p>"

@auth.route("/signup")
def sign_up():
    return "<p>Sign Up</p>"