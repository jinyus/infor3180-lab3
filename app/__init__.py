from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'randomkey'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '2525'
app.config['MAIL_USERNAME'] = 'enter your username here'
app.config['MAIL_PASSWORD'] = 'enter your password here'
mail = Mail(app)

from app import views