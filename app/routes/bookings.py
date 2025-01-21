from flask import Blueprint, render_template, flash, current_app

booking_bp = Blueprint('bookings', __name__)
@booking_bp.route('/book/<int:car_id>', methods=['GET', 'POST'])
def bookings(car_id):
    cars = current_app.mongo.db.cars.find()
    cars = list(cars)
    car = current_app.mongo.db.cars.find_one({'car_id': car_id})
    if car:
        new_availability = not car.get('available', False)
        current_app.mongo.db.cars.update_one(
            {'car_id': car['car_id']},
            {'$set': {'available': new_availability}},
        )
    flash(f'Booking successfully for car ID {car_id}','success')
    return render_template('car_list.html',cars=cars)
