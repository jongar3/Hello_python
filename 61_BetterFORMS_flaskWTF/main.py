from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email


app = Flask(__name__)
app.secret_key = "co1-qd2m-231-a"  # Needed for CSRF protection in Flask-WTF forms

class LoginForm(FlaskForm):
    email = StringField(label= 'Email', validators=[DataRequired(), Email(message="The field must be an email", granular_message=False, check_deliverability=True, allow_smtputf8=True, allow_empty_local=False)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit= SubmitField('Log In')



@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        login_email = login_form.email.data
        login_password = login_form.password.data
        if login_email== "admin@email.com" and login_password== "123456": 
            return render_template('success.html')
        else:
            return render_template('denied.html')
    else:
        return render_template('login.html', form=login_form)

if __name__ == '__main__':
    app.run(debug=True)