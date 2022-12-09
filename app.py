#import the application factory function(create_app) from __init__.py in petfax directory/folder
from petfax import create_app

#Now that we have access to the factory function by the code above, 
# we can create an app instance by invoking the function and saving it to a variable called app.
app = create_app()
