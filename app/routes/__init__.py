from flask import Blueprint

# Create a blueprint for the routes
auth_bp = Blueprint('auth', __name__)
cars_bp = Blueprint('cars', __name__)
admin_bp = Blueprint('admin', __name__)
booking_bp = Blueprint('booking', __name__)

# Import the routes
from .auth import auth_bp
from .cars import cars_bp
from .admin import admin_bp
from .bookings import booking_bp
