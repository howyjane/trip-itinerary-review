import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId


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
    tripInfo = conn[DATABASE_NAME][COLLECTION_NAME].find().limit(8)
    return render_template("index.html", tripInfo=tripInfo)

@app.route('/search_trip')
def search_trip():
    return render_template("search.html") 

@app.route('/summary_trip')
def summary_trip():
    return render_template("summary.html")  

@app.route('/landingpagesummary_trip')
def landingpagesummary_trip():
    return render_template("landingpagesummary.html")  

@app.route('/add_trip')
def add_trip():
    return render_template("add.html")

@app.route('/add_trip', methods=['POST'])
def getvalue():
    name = request.form['name']
    return render_template("summary.html", n=name)
    
@app.route('/uploads/<path:filename>', methods=['POST'])
def save_upload(filename):
    mongo.save_file(filename, request.files['file'])
    return redirect(url_for('get_upload', filename=filename))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),port=int(os.environ.get('PORT')),debug=True)