from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db_datalake = None
db_roots = None

def init_db_datalake(app: Flask):
    global db_datalake
    db_datalake = SQLAlchemy(app)

def init_db_raices(app: Flask):
    global db_roots
    db_roots = SQLAlchemy(app)