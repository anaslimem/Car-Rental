from flask import Blueprint, render_template, jsonify,current_app


cars_bp= Blueprint('cars', __name__)
@cars_bp.route('/', methods=['GET'])
def list_cars():
    cars = current_app.mongo.db.cars
    cars.insert_one({"name": "Toyota","Model":"Corolla","Year":"2021"})
    cars = current_app.mongo.db.cars.find()
    cars_list = list(cars)
    return render_template("car_list.html", cars=cars_list)

