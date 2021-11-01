from flask import render_template, request, redirect, url_for, flash
from .forms import LoginForm, RegisterForm, EditProfile
from app.models import User
from flask_login import login_user, current_user, logout_user, login_required
from .import bp as auth

@auth.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
   
        email = request.form.get("email").lower()
        password = request.form.get("password")
                               
        u= User.query.filter_by(email=email).first()

        if u and u.check_hashed_password(password):
            login_user(u)
            flash('You have sucessfully logged in!, success')
            return redirect(url_for('main.index'))
        error_string = "Invalid email password combo"
        return render_template('login.html.j2', error = error_string, form=form)
    return render_template('login.html.j2', form=form)

@auth.route('/logout')
@login_required
def logout():
    if current_user:
        logout_user()
        flash('You have successfully logged out!, danger')
        return redirect(url_for('auth.login'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():
        try:
            new_user_data = {
                "first_name":form.first_name.data.title(),
                "last_name":form.last_name.data.title(),
                "email":form.email.data.lower(),
                "password": form.password.data
            }
            new_user_object = User
            new_user_object.from_dict(new_user_data)
            new_user_object.save()
        except:
            error_string = "There was an unexpected error creating your account. Please enter again."
            return render_template('register.html.j2',form=form, error = error_string)
        return redirect(url_for('auth.login')) 
    return render_template('register.html.j2', form = form) 


@auth.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    form= EditProfile()
    if request.method == "POST" and form.validate_on_submit():
        new_user_data={
                "first_name":form.first_name.data.title(),
                "last_name":form.last_name.data.title(),
                "email":form.email.data.lower(),
                "password": form.password.data
        }
    user=User.query.filter_by(email=form.email.data.lower())
    if user and current_user.email !=user.email:
        flash('email already in use', 'danger')
        return redirect(url_for('auth.edit_profile'))
    try:
        current_user.from_dict(new_user_data)
        current_user.save()
        flash ("profile updated, sucess")
    except:
        flash('there was an unexpected error', 'danger')
        return redirect(url_for('auth.edit_profile'))
    return render_template('auth/register.html.j2', form= form)
