import os
from flask import Flask, render_template, redirect, request, url_for, send_from_directory
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/home/ubuntu/environment/uploads'
app.config["MONGO_DBNAME"] = 'Project3'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
conn = pymongo.MongoClient('mongodb+srv://root:rOOtUser@clusterjane-dczgp.mongodb.net/test?retryWrites=true&w=majority')
DATABASE_NAME = 'Project3'
COLLECTION_NAME = 'addtrip'

mongo = PyMongo(app)

@app.route('/')
@app.route('/index')
def index():
    tripInfo = conn[DATABASE_NAME][COLLECTION_NAME].find().sort("_id", pymongo.DESCENDING).limit(8)
    return render_template("index.html", tripInfo=tripInfo)

@app.route('/search_trip')
def search_trip():
    return render_template("search.html") 

@app.route('/summary_trip')
def summary_trip():
    return render_template("summary.html")  

@app.route('/landingpagesummary_trip/<tripId>')
def landingpagesummary_trip(tripId):
    tripInfo = conn[DATABASE_NAME][COLLECTION_NAME].find_one(tripId)
    return render_template("landingpagesummary.html", tripInfo = tripInfo)  

@app.route('/add_trip')
def add_trip():
    return render_template("add.html")

@app.route('/add_trip', methods=['POST'])
def getvalue():
    name = request.form['name']
    file = request.files['photo']
    imageUrl = ''
    if file.filename != '':
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        imageUrl = url_for('uploaded_file', filename=filename)
    newTrip = {
        "name": request.form['name'],
        "country": 'test country',
        "city": 'test city',
        "startdate": '01/12/2019',
        "enddate": '01/12/2019',
        "triptitle": 'test trip title',
        "tripreview": 'review',
        "totalestimatedcost": 123,
        "imageURL": imageUrl,
    }
    conn[DATABASE_NAME][COLLECTION_NAME].insert_one(newTrip)
    return render_template("summary.html", n=name)
    
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),port=int(os.environ.get('PORT')),debug=True)