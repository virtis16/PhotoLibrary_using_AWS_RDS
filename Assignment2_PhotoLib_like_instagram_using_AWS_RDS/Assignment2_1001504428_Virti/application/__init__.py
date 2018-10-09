#Name : Virti Bipin Sanghavi
#Student Id : 1001504428
#Assignment 2 - CSE 6331 Cloud Computing
#Reference to the code used from some online blogs, websites and repositories
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

application=Flask(__name__)
application.config.from_object('config')
db=SQLAlchemy(application)