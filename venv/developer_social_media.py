import app
import cx_Oracle
from flask import flash, render_template
from flask_login import current_user

from venv.app import cursor, connection, app


class DeveloperSocialMedia:
    pass


@app.route('/developer-social-media', methods=['GET', 'POST'])
def developer_social_media():
    form = DeveloperSocialMedia()
    if form.validate_on_submit():
        linkedin = form.linkedin.data
        instagram = form.instagram.data
        facebook = form.facebook.data
        user_id = current_user.id  # Assuming user authentication system

        try:
            query = """
                INSERT INTO DeveloperSocialMedia (id, linkedin, instagram, facebook)
                VALUES (:id, :linkedin, :instagram, :facebook)
            """
            cursor.execute(query, {
                'id': user_id,
                'linkedin': linkedin,
                'instagram': instagram,
                'facebook': facebook
            })
            connection.commit()
            flash("Social media saved successfully!", "success")
        except cx_Oracle.DatabaseError as e:
            flash(f"An error occurred: {str(e)}", "danger")

    return render_template('developer_social_media.html', form=form)
