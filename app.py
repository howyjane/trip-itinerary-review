import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
import re

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'Project3'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
conn = pymongo.MongoClient('mongodb+srv://root:rOOtUser@clusterjane-dczgp.mongodb.net/test?retryWrites=true&w=majority')
DATABASE_NAME = 'Project3'
COLLECTION_NAME = 'addtrip'

mongo = PyMongo(app)

@app.route('/')
@app.route('/index')
def index():
    tripInfo = conn[DATABASE_NAME][COLLECTION_NAME].find()
    return render_template("index.html", tripInfo=tripInfo)
    
    
@app.route('/add_trip')
def add_trip():
    return render_template("add.html")






if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),port=int(os.environ.get('PORT')),debug=True)