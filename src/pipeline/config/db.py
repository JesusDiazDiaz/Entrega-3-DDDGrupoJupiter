from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db_dataleak = None
db_roots = None

def init_db_dataleak(app: Flask):
    global db_dataleak
    db_dataleak = SQLAlchemy(app)

def init_db_raices(app: Flask):
    global db_roots
    db_roots = SQLAlchemy(app)