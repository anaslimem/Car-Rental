from flask import Blueprint, render_template,redirect, url_for,current_app


auth_bp = Blueprint('auth', __name__,template_folder='../templates')
@auth_bp.route('/')
def main():
    return redirect(url_for('auth.login'))
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    user = current_app.mongo.db.users
    user.insert_one({"username": "Anas", "email": "limemanas0@gmail.com", "password": "ot21rj2357"})
    users = current_app.mongo.db.users.find()
    users = list(users)
    return render_template("register.html",users=users)
