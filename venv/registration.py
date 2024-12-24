import cx_Oracle
from flask import render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash
from app import app, cursor, connection
from forms import RegistrationForm


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password_hash = generate_password_hash(form.password.data)
        role = form.role.data

        try:
            query = """
                INSERT INTO Users (username, email, password_hash, role)
                VALUES (:username, :email, :password_hash, :role)
            """
            cursor.execute(query, {'username': username, 'email': email, 'password_hash': password_hash, 'role': role})
            connection.commit()
            flash("Registration successful!", "success")
            return redirect(url_for('login'))
        except cx_Oracle.DatabaseError as e:
            flash(f"An error occurred: {str(e)}", "danger")

    return render_template('register.html', form=form)
