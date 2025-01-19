from flask import Blueprint, render_template, current_app, request, redirect, url_for,flash
import os
from werkzeug.utils import secure_filename

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/')
def index():
    return redirect(url_for('admin.admin'))
#admin panel route
@admin_bp.route('/admin', methods=['GET', 'POST'])
def admin():
    cars =  current_app.mongo.db.cars.find()
    cars = list(cars)
    return render_template('admin_panel.html',cars=cars)

#route to add a new car
@admin_bp.route('/admin/add_car', methods=['GET', 'POST'])
def add_car():
        if request.method == 'POST':
            # get data from form
            car_id = request.form.get('car_id')
            car_name = request.form.get('car_name')
            car_model = request.form.get('car_model')
            car_year = request.form.get('car_year')
            car_price = request.form.get('car_price')
            # Validate if car_id, car_year, and car_price are positive numbers
            try:
                car_id = int(car_id)  # Convert to integer
                car_year = int(car_year)  # Convert to integer
                car_price = int(car_price)  # Convert to float

                # Check if they are positive
                if car_id <= 0 or car_year <= 0 or car_price <= 0:
                    flash('Car ID, Year, and Price must be positive numbers!', 'danger')
                    return redirect(url_for('admin.add_car'))

            except ValueError:
                flash('Invalid input. Please enter valid numbers for car ID, year, and price.', 'danger')
                return redirect(url_for('admin.add_car'))
            file = request.files.get('car_image')
            if file:
                filename = secure_filename(file.filename)
                file_path = os.path.join(current_app.config['UPLOAD_FOLDER'],filename)
                file.save(file_path)
                print(file_path)
                relative_path = f'{filename}'
            else:
                relative_path = None
            existing_cars =  current_app.mongo.db.cars.find_one({'car_id': car_id})
            if existing_cars:
                flash('Car with this ID already exists!', 'danger')
                return redirect(url_for('admin.add_car'))
            else:
                # insert data into mongodb
                current_app.mongo.db.cars.insert_one({
                    'car_id': car_id,
                    'car_name': car_name,
                    'car_model': car_model,
                    'car_year': car_year,
                    'car_price': car_price,
                    'car_image': relative_path,
                    'available': True
                })
                flash('Car added successfully!', 'success')
                return redirect(url_for('admin.admin'))
        return render_template('add_car.html')

#route to delete car
@admin_bp.route('/admin/delete_car', methods=['GET', 'POST'])
def delete_car():
    cars =  current_app.mongo.db.cars.find()
    cars = list(cars)
    if request.method == 'POST':
        car_id = request.form.get('car_id')
        if car_id:
            car_id = int(car_id)
            car = current_app.mongo.db.cars.find_one({'car_id': car_id})
            if car:
                current_app.mongo.db.cars.delete_one({'car_id': car_id})
                flash("Car successfully deleted", "success")
            else:
                flash("Car not found", "danger")
        else:
            flash("Car ID is required", "warning")
            return render_template('list_cars.html', cars=cars)
    return render_template("delete_car.html", cars=cars)

#route to toggle availability
@admin_bp.route('/admin/toggle_availability', methods=['GET', 'POST'])
def toggle_availability():
    car_id = request.form.get('car_id')
    try:
        car_id = int(car_id)
    except ValueError:
        flash('Invalid car ID', 'danger')
        return redirect(url_for('admin.admin'))
    car = current_app.mongo.db.cars.find_one({'car_id': car_id})
    if car:
        new_availability = not car.get('available', False)
        current_app.mongo.db.cars.update_one(
            {'car_id': car['car_id']},
            {'$set': {'available': new_availability}},
        )
        flash('Car availability updated!', 'success')
    else:
        flash(f'Car with ID {car_id} not found!', 'danger')
    return redirect(url_for('admin.admin'))


