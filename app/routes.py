# from flask import render_template, request, redirect, url_for, flash
# import requests
# from .forms import LoginForm, PokeForm, RegisterForm
# from models import User
# from flask_login import login_user, current_user, logout_user, login_required

# @app.route('/', methods = ['GET'])
# def index():
#    return render_template('index.html.j2')


# @app.route('/poke', methods=['GET', 'POST'])
# def poke():
#     form= PokeForm()
#     if request.method == 'POST' and form.validate_on_submit():
        
#         name = request.form.get('name')
#         url = f'https://pokeapi.co/api/v2/pokemon/{name}'
#         print(url)
#         response = requests.get(url)
#         if response.ok:
#             if not response.json():
#                 error_string="ERROR loading"
#                 return render_template('poke.html.j2' , error = error_string, form=form) 
#             data = response.json()
#             new_data=[]
#             pokemon_name = data['name']
#             pokemon_dict={}
#             pokemon_dict= {
#                 'name': data['name'],
#                 'ability_name': data['ability_name'],
#                 'base experience': data['base experience'],
#                 'sprite front shiny': data['sprite front shiny']
#                 }
#             new_data.append(pokemon_dict)
#             return render_template('poke.html.j2', names=new_data)     
#         else:
#             error_string="ERROR loading"
#             return render_template('poke.html.j2' , error = error_string)


#     return render_template('poke.html.j2')


# @app.route('/login', methods=['GET','POST'])
# def login():
#     form = LoginForm()
#     if request.method == 'POST' and form.validate_on_submit():
   
#         email = request.form.get("email").lower()
#         password = request.form.get("password")
                               
#         u= User.query.filter_by(email=email).first()

#         if u and u.check_hashed_password(password):
#             login_user(u)
#             flash('You have sucessfully logged in!, sucess')
#             return redirect(url_for("index"))
#         error_string = "Invalid Email password combo"
#         return render_template('login.html.j2', error = error_string, form=form)
#     return render_template('login.html.j2', form=form)

# @app.route('/logout')
# @login_required
# def logout():
#     if current_user:
#         logout_user()
#         flash('You have sucessfully logged out!, danger')
#         return redirect(url_for('login'))


# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     form = RegisterForm()
#     if request.method == 'POST' and form.validate_on_submit():
#         try:
#             new_user_data = {
#                 "first_name":form.first_name.data.title(),
#                 "last_name":form.last_name.data.title(),
#                 "email":form.email.data.lower(),
#                 "password": form.password.data
#             }
     
#             new_user_object = User
         
#             new_user_object.from_dict(new_user_data)
        
#             new_user_object.save()
#         except:
#             error_string = "There was an unexpected Error creating your account. Please Try again."
#             return render_template('register.html.j2',form=form, error = error_string) #when we had an error creating a user
#         return redirect(url_for('login')) # on a post request that successfully creates a new user
#     return render_template('register.html.j2', form = form) #the render template on the Get request
