"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.model):
    """User for application"""



def connect_db(app):
    """Connecting database to flask app"""

    db.app = app
    db.init_app(app)