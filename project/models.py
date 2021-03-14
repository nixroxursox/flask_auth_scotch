# models.py

from flask_login import UserMixin
from . import db
import logging

from sqlalchemy import create_engine

dbs = "postgresql+psycopg2://postgres:passw0rd@localhost:5432/postgres"
engine = create_engine(dbs)


class User(UserMixin, db.Model):
    id = db.Column(
        db.Integer, primary_key=True
    )  # primary keys are required by SQLAlchemy
    PIN = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
