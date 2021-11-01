from flask import render_template, request
import requests
from .forms import PokeForm
from flask_login import login_user, current_user, logout_user, login_required
from app.models import User

from .import bp as main

@main.route('/', methods = ['GET'])
def index():
    return render_template('index.html.j2')


@main.route('/poke', methods=['GET', 'POST'])
def poke():
    form= PokeForm()
    if request.method == 'POST' and form.validate_on_submit():
        
        name = request.form.get('name')
        url = f'https://pokeapi.co/api/v2/pokemon/{name}'
        print(url)
        response = requests.get(url)
        if response.ok:
            if not response.json():
                error_string="ERROR loading"
                return render_template('poke.html.j2' , error = error_string, form=form) 
            data = response.json()
            new_data=[]
            pokemon_name = data['name']
            pokemon_dict={}
            pokemon_dict= {
                'name': data['name'],
                'ability_name': data['ability_name'],
                'base_experience': data['base_experience'],
                'sprite_front_shiny': data['sprite_front_shiny']
                }
            new_data.append(pokemon_dict)
            return render_template('poke.html.j2', names=new_data)     
        else:
            error_string="ERROR loading"
            return render_template('poke.html.j2' , error = error_string)

    return render_template('poke.html.j2')

