#import Flask 
from flask import Flask

#define a function that will be the application factory
def create_app():
    app = Flask(__name__)        #<--inside the function create a new app instance of Flask 

#create a basic index route 
    @app.route('/')              
    def hello():
        return 'Hello, PetFax!'

#import blueprint
    from . import pet

#register blueprint
    app.register_blueprint(pet.bp)

 # register fact blueprint 
    from . import fact
    app.register_blueprint(fact.bp)

    
#return the app instance at the end of the factory
    return app

