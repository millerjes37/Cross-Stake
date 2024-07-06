from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
import requests
from .models import User

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.validate_login(email, password)
        if user:
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Invalid credentials. Please try again.', 'error')

    return render_template('login.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        phone_number = request.form['phone_number']
        billing_address = request.form['billing_address']
        user = User.register(email, password, name, phone_number, billing_address)
        if user:
            login_user(user)
            flash('Registration successful!', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Registration failed. Please try again.', 'error')

    return render_template('register.html')

@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.index'))

@main.route('/owners', methods=['GET', 'POST'])
@login_required
def owners():
    if request.method == 'POST':
        owner_data = {
            'name': request.form['name'],
            'email': request.form['email'],
            'phone_number': request.form['phone_number'],
            'billing_address': request.form['billing_address']
        }
        try:
            response = requests.post('http://127.0.0.1:8000/api/owners/', json=owner_data)
            response.raise_for_status()
            if response.status_code == 201:
                flash('Owner added successfully!', 'success')
                return redirect(url_for('main.index'))
        except requests.RequestException as e:
            print(f"Error creating owner: {e}")
            flash('Error adding owner. Please try again.', 'error')

    return render_template('owners.html')

@main.route('/add_horse', methods=['GET', 'POST'])
@login_required
def add_horse():
    if request.method == 'POST':
        horse_data = {
            'name': request.form['name'],
            'owner': current_user.id,
            'trainer': request.form['trainer'],
            'year_born': request.form['year_born'],
            'gender': request.form['gender'],
            'gait': request.form['gait'],
            'selected_stakes': request.form['selected_stakes']
        }
        try:
            response = requests.post('http://127.0.0.1:8000/api/horses/', json=horse_data)
            response.raise_for_status()
            if response.status_code == 201:
                flash('Horse added successfully!', 'success')
                return redirect(url_for('main.index'))
        except requests.RequestException as e:
            print(f"Error creating horse: {e}")
            flash('Error adding horse. Please try again.', 'error')

    return render_template('add_horse.html')
