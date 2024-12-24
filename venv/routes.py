from flask import render_template, redirect, url_for, flash, request
from app import app, db, bcrypt
from models import User, DeveloperProfile, EmployerProfile
from forms import RegistrationForm, LoginForm, DeveloperProfileForm, EmployerProfileForm
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password, role=form.role.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=True)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/developer/profile", methods=['GET', 'POST'])
@login_required
def developer_profile():
    if current_user.role != 'developer':
        return redirect(url_for('home'))
    form = DeveloperProfileForm()
    if form.validate_on_submit():
        profile = DeveloperProfile(user_id=current_user.id, github_link=form.github_link.data,
                                   portfolio_description=form.portfolio_description.data, skills=form.skills.data)
        db.session.add(profile)
        db.session.commit()
        flash('Profile Updated', 'success')
    return render_template('developer_profile.html', form=form)

@app.route("/employer/profile", methods=['GET', 'POST'])
@login_required
def employer_profile():
    if current_user.role != 'employer':
        return redirect(url_for('home'))
    form = EmployerProfileForm()
    if form.validate_on_submit():
        profile = EmployerProfile(user_id=current_user.id, company_name=form.company_name.data,
                                  industry=form.industry.data)
        db.session.add(profile)
        db.session.commit()
        flash('Profile Updated', 'success')
    return render_template('employer_profile.html', form=form)
