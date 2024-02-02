# this file will contain all the URL end points (i.e, the frontend functionning of the website)
# the login page would go in auth.py file but anything else that the user can interact with is created in the views.py file

from flask import Blueprint
# a Blueprint means all the URLs / routes one can find on a website, it helps to keep the website organised, we wouldn't have to keep all the views in one place
views = Blueprint('views', __name__)
# we don't have to name this variable & argument with the same name as our file

@views.route('/') # this would be the home page, # / means home page of the website (decorator, / means home page, this is the route or end point to the home page)
def home(): # now whenever we go to the home page of our website this function would run, # this function under the decorator for home page route would run whenever we go to the home page
    return "<h1>Test</h1>"