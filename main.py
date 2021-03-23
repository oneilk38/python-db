from flask import Flask, jsonify, request
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DECIMAL
from flask_sqlalchemy import SQLAlchemy

import pymysql
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost:3306/imdb'
db = SQLAlchemy(app)

