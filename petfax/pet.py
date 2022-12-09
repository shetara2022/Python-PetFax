#import Bluepriint and render_template
from flask import (Blueprint, render_template)
import json

pets = json.load(open('pets.json'))
# print(pets)

#create a new instance of Blueprint and save it to a variable called bp
bp = Blueprint(
    'pet',
    __name__, 
    url_prefix='/pets'
    )

#blueprint index route 
@bp.route('/')
def index():
    return render_template('pets/index.html', pets=pets)

@bp.route('/<int:id>')
def show(id): 
    pet = pets[id - 1]
    return render_template('pets/show.html', pet=pet)