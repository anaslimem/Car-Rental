from flask import Blueprint, render_template, current_app, request, redirect, url_for,flash

cars_bp= Blueprint('cars', __name__)
@cars_bp.route('/', methods=['GET', 'POST'])
def cars():
    return redirect(url_for('cars.list_cars'))

@cars_bp.route('/list_cars', methods=['GET'])
def list_cars():
    cars = current_app.mongo.db.cars.find()
    cars = list(cars)
    return render_template("car_list.html", cars=cars)
