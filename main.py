# this is the file to run to start the web app

from webapp import create_app # we can import anything which is within the webapp as the webapp folder is now a package because it has the __init__.py file & to access the functions within the __init__.py file, we can directly use the name of the package which is 'webapp' here

app = create_app()

if __name__ == '__main__': # this means only if we run the main.py file directly, then the code should be executed. The code shouldn't be executed if we import this main.py file
    app.run(debug = True) # our web server would run basically this line would only execute if we run the main.py file directly

# app.run() would launch our website
# for app in production, we'll keep debug = False 
# debug = True means that anytime we make any change to our website code, Flask would re run the web server

# if we don't add the code to be executed within the clock of this if statement "if __name__ == '__main__':", the code would run everytime we import the main.py file in some other file even if we don't execute the main.py file

