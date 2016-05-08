"""Models and database functions for Ratings project."""

from flask_sqlalchemy import SQLAlchemy

# Here's where we create the idea of our database. We're getting this through
# the Flask-SQLAlchemy library. On db, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Part 1: Compose ORM

class Model(db.Model):
    """Car model."""

    __tablename__ = "models"

    model_id = db.Column(db.Integer,
                         autoincrement=True,
                         primary_key=True)
    year = db.Column(db.Integer,
                     nullable=False)
    brand_name = db.Column(db.String(50),
                           db.ForeignKey('brands.name'),
                           nullable=False)
    name = db.Column(db.String(50),
                     nullable=False)

    # Establish a relationship between models and brands
    # Based on foreign key above
    brand = db.relationship('Brand', backref='models')

    def __repr__(self):
        """Show info about the Model object."""
        return "<Model model_id={} year={} brand_name={} name={}>".format(self.model_id,
                                                                          self.year,
                                                                          self.brand_name,
                                                                          self.name)



class Brand(db.Model):
    """Car brand."""

    __tablename__ = "brands"

    brand_id = db.Column(db.Integer,
                         autoincrement=True,
                         primary_key=True)
    # Added unique constraint because this field is used as a Foreign Key
    name = db.Column(db.String(50),
                     nullable=False,
                     unique=True)
    founded = db.Column(db.Integer)
    headquarters = db.Column(db.String(50))
    discontinued = db.Column(db.Integer)

    def __repr__(self):
        """Show info about he Brand object"""
        return ("<Brand brand_id={} name={} founded={} " +
                "headquarters={} discontinued={}>").format(self.brand_id,
                                                           self.name,
                                                           self.founded,
                                                           self.headquarters,
                                                           self.discontinued)


# End Part 1


##############################################################################
# Helper functions

def init_app():
    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///cars'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask

    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."
