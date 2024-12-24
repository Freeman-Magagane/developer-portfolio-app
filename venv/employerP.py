import cx_Oracle
from flask import flash, render_template
from flask_login import current_user
from app import app, cursor, connection
from forms import EmployerProfileForm


@app.route('/employer-profile', methods=['GET', 'POST'])
def employer_profile():
    form = EmployerProfileForm()
    if form.validate_on_submit():
        project_name = form.project_name.data
        industry = form.industry.data
        user_id = current_user.id  # Assuming user authentication system

        try:
            query = """
                INSERT INTO EmployerProfiles (id, project_name, industry)
                VALUES (:id, :project_name, :industry)
            """
            cursor.execute(query, {
                'id': user_id,
                'project_name': project_name,
                'industry': industry
            })
            connection.commit()
            flash("Profile saved successfully!", "success")
        except cx_Oracle.DatabaseError as e:
            flash(f"An error occurred: {str(e)}", "danger")

    return render_template('employer_profile.html', form=form)
