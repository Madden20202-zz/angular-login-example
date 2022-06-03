from flask import Flask
from flask_sqlachemy import SQLAlchemy

app = flask(__name__)

# Set up db so that it goes to the users.db file
app.config['SQLALCHEMY_DATABASE_URl'] = 'sqlite:/src/backend/users.db'
db = SQLAlchemy(app)

# create the Users model
class Users(db.model):
    id = db.Column(db.Integer, primary_key=true)
    username = db.Column(db.String)
    password = db.Column(db.String)

db.create.all()

