from flask import Blueprint, render_template,redirect, url_for,current_app,request,flash
from flask_login import UserMixin,login_user,logout_user,current_user
from flask_bcrypt import Bcrypt
from models import User
bcrypt = Bcrypt()
auth_bp = Blueprint('auth', __name__,template_folder='../templates')
@auth_bp.route('/')
def main():
    return redirect(url_for('auth.login'))
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = current_app.mongo.db.users.find_one({'email': email})
        if user and bcrypt.check_password_hash(user['password'],password):
            x = User(**user)
            login_user(x)
            flash('You are logged in.', 'success')
            return redirect(url_for('cars.list_cars'))
        else:
            flash('Invalid email or password.', 'danger')
    return render_template('login.html')
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
        user = current_app.mongo.db.users.find_one({'username': username})
        user1 = current_app.mongo.db.users.find_one({'email': email})
        if user is None and user1 is None:
            new_user = {
                'username': username,
                'email': email,
                'password': password
            }
            current_app.mongo.db.users.insert_one(new_user)
            flash("You are now Registered.", 'success')
            return redirect(url_for('auth.login'))
        elif user:
            flash("Username already taken!", 'danger')
        else:
            flash("You are already registered.", 'warning')
    return render_template("register.html")
