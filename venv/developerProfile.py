import cx_Oracle
from flask import flash, render_template
from flask_login import current_user
from portfolio_app.venv.app import app, cursor, connection
from portfolio_app.venv.forms import DeveloperProfileForm


@app.route('/developer-profile', methods=['GET', 'POST'])
def developer_profile():
    form = DeveloperProfileForm()
    if form.validate_on_submit():
        github_link = form.github_link.data
        portfolio_description = form.portfolio_description.data
        skills = form.skills.data
        user_id = current_user.id

        try:
            query = """
                INSERT INTO DeveloperProfiles (id, github_link, portfolio_description, skills)
                VALUES (:id, :github_link, :portfolio_description, :skills)
            """
            cursor.execute(query, {
                'id': user_id,
                'github_link': github_link,
                'portfolio_description': portfolio_description,
                'skills': skills
            })
            connection.commit()
            flash("Profile saved successfully!", "success")
        except cx_Oracle.DatabaseError as e:
            flash(f"An error occurred: {str(e)}", "danger")

    return render_template('developer_profile.html', form=form)
