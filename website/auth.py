from flask import render_template, request, Blueprint, flash, get_flashed_messages
from flask import *

views = Blueprint('views')

import sqlite3
conn = sqlite3.connect('database.db')
cursor = conn.cursor()




@views.route('/register', methods=['POST'])

def register():


    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        

        # Check if the email is already registered
        cursor.execute('SELECT * FROM Register WHERE email=?', (email,))
        existing_user = cursor.fetchone()

        if existing_user:
            flash('Email already registered. Please use a different email.', category='error')
            return render_template('home.html', message='Email already registered')

        # Insert the new user into the Register table
        cursor.execute('INSERT INTO Register (username, email, password) VALUES (?, ?, ?)', (username, email, password))
        conn.commit()
        flash('Registration successful! Now Login!', category='success')


    return render_template('home.html', messages=get_flashed_messages(with_categories=True))


@views.route('/register', methods=['POST'])

def register():

    if request.method == 'POST':

        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if the email is already registered
        cursor.execute('SELECT * FROM Register WHERE email=?', (email,))
        existing_user = cursor.fetchone()

        if existing_user:

            flash('Email already registered. Please use a different email.', category='error')
            return render_template('home.html', message='Email already registered')

        # Insert the new user into the Register table
        cursor.execute('INSERT INTO Register (username, email, password) VALUES (?, ?, ?)', (username, email, password))
        conn.commit()
        flash('Registration successful! Now Login!', category='success')
        

    return render_template('home.html', messages=get_flashed_messages(with_categories=True))