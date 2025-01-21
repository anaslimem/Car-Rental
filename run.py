from flask import Flask
from flask_pymongo import PyMongo
from flask_login import LoginManager, current_user
from models import User

def create_app():
    app = Flask(__name__,static_folder='app/static')
    app.config['UPLOAD_FOLDER'] = 'app/static/images'
    app.config['SECRET_KEY'] = '12345'
    app.config['MONGO_URI'] = 'mongodb://localhost:27017/car_rental'
    mongo = PyMongo(app)
    login_manager = LoginManager(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Please log in to access this page.'
    login_manager.login_message_category = 'warning'
    @login_manager.user_loader
    def load_user(user_id):
        user_data = mongo.db.users.find_one({'_id': user_id})
        if user_data:
            return User(**user_data)
        return None
    # Import and register blueprints
    from app.routes import auth_bp, cars_bp, admin_bp, booking_bp
    app.register_blueprint(auth_bp, url_prefix='/')
    app.register_blueprint(cars_bp, url_prefix='/cars')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(booking_bp, url_prefix='/booking')
    app.mongo = mongo
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
