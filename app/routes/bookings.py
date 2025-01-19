from flask import Blueprint, render_template, current_app, request, redirect, url_for,flash

booking_bp = Blueprint('bookings', __name__)
@booking_bp.route('/', methods=['GET', 'POST'])
def booking():
    cars =  current_app.mongo.db.cars.find()
    cars = list(cars)
    return render_template('booking.html', cars=cars)
@booking_bp.route('/book_car', methods=['GET', 'POST'])
def bookings():
    if request.method == 'POST':
        car_id = request.form.get('car_id')
        name = request.form.get('name')
        email = request.form.get('email')
        card_number = request.form.get('card_number')
        expiration = request.form.get('expiration')
        cvv = request.form.get('cvv')
        current_app.mongo.db.bookings.insert_one({
            "car_id": car_id,
            "name": name,
            "email": email,
            "card_number": card_number,
            "expiration": expiration,
            "cvv": cvv
        })
        flash("Booking received successfully!", "success")
        return redirect(url_for('bookings.booking'))
    return render_template('booking.html')
@booking_bp.route('/make-unavailable', methods=['POST'])
def make_unavailable():
    data = request.get_json()
    car_id = data.get('car_id')

    if not car_id:
        flash("Car ID not provided!", "error")

    car = current_app.mongo.db.find_one({"car_id": car_id})
    if car:
        current_app.mongo.db.update_one({"car_id": car_id}, {"$set": {"available": False}})
        flash("Car has been booked!", "success")
    else:
        flash("Car not available!", "error")
    return redirect(url_for('cars.list_cars'))