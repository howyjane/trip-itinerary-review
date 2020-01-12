import os
from flask import Flask, render_template, redirect, request, url_for, send_from_directory
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from werkzeug.utils import secure_filename
from datetime import datetime
import re


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
    tripInfo = conn[DATABASE_NAME][COLLECTION_NAME].find().sort("_id", pymongo.DESCENDING)
    return render_template("index.html", tripInfo=tripInfo)

@app.route('/search_trip', methods=['POST','GET'])
def search_trip():
    
    tripInfo = conn[DATABASE_NAME][COLLECTION_NAME].find().sort("country",1)
    tripInfo2 = conn[DATABASE_NAME][COLLECTION_NAME].find().sort("city",1)
    tripInfo3 = conn[DATABASE_NAME][COLLECTION_NAME].find().sort("city",1)
    return render_template("search.html", tripInfo=tripInfo, tripInfo2=tripInfo2,tripInfo3=tripInfo3) 
    
@app.route('/search_results', methods=['POST','GET'])
def search_results():
    
    tripInfo = conn[DATABASE_NAME][COLLECTION_NAME].find()
    return render_template("searchresults.html", tripInfo=tripInfo) 

@app.route("/search_trip", methods=['POST','GET'])  
def search():  
    #Searching a Task with various references  
  
    tripId=request.values.get("_id") 
    country = request.form['country']
   
    if(tripId=="_id",country=="country"):  
         tripInfo = conn[DATABASE_NAME][COLLECTION_NAME].find()({'_id': ObjectId(tripId)})
    else:  
        return 'no records found'
    return render_template('search.html',tripInfo=tripInfo)

@app.route('/searchlandingpagesummarytrip/<tripId>')
def searchlandingpagesummary_trip(tripId):
    tripInfo = conn[DATABASE_NAME][COLLECTION_NAME].find_one({'_id': ObjectId(tripId)})
    return render_template("searchlandingpagesummary.html", tripInfo=tripInfo)
    
@app.route('/add_trip')
def add_trip():
    return render_template("add.html")
    

@app.route('/add_trip', methods=['POST'])
def getvalue():
    name = request.form['name']
    country = request.form['country']
    city = request.form['city']
    startdate = request.form['sd']
    enddate = request.form['ed']
    triptitle = request.form['triptitle']
    tripreview = request.form['tripreview']
    tripattraction = request.form['tripattraction']
    ratings = request.form['ratings']
    totalestimatedcost = request.form['totalestimatedcost']
    file = request.files['photo']
    
    imageUrl = ''
    if file.filename != '':
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        imageUrl = url_for('uploaded_file', filename=filename)
    
    newTrip = {
        "name": request.form['name'],
        "country": request.form['country'],
        "city": request.form['city'],
        "startdate": request.form['sd'],
        "enddate": request.form['ed'],
        "triptitle": request.form['triptitle'],
        "tripreview": request.form['tripreview'],
        "tripattraction": request.form['tripattraction'],
        "totalestimatedcost": request.form['totalestimatedcost'],
        "ratings": request.form['ratings'],
        "imageURL":imageUrl,
        
    }
    
    tripInfo=conn[DATABASE_NAME][COLLECTION_NAME].insert_one(newTrip)
    return render_template("summary.html", n=name, c=country, cc=city, sd=startdate, ed=enddate, tt=triptitle, rv=tripreview, a=tripattraction, ct=totalestimatedcost, r=ratings, filename=filename)
    
    
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/summary_trip')
def summary_trip():
    return render_template("summary.html")

@app.route('/landingpagesummarytrip/<tripId>')
def landingpagesummary_trip(tripId):
    tripInfo = conn[DATABASE_NAME][COLLECTION_NAME].find_one({'_id': ObjectId(tripId)})
    return render_template("landingpagesummary.html", tripInfo=tripInfo)
    
@app.route('/edit/<tripId>')
def edit_trip(tripId):
    tripInfo = conn[DATABASE_NAME][COLLECTION_NAME].find_one({'_id': ObjectId(tripId)})
    return render_template("edit.html", tripInfo=tripInfo)  
    

@app.route('/edit_trip', methods=['POST'])
def update_trip():
    tripId=request.values.get("_id") 
    name = request.form['name']
    country = request.form['country']
    city = request.form['city']
    startdate = request.form['sd']
    enddate = request.form['ed']
    triptitle = request.form['triptitle']
    tripreview = request.form['tripreview']
    tripattraction = request.form['tripattraction']
    ratings = request.form['ratings']
    totalestimatedcost = request.form['totalestimatedcost']
    file = request.files['photo']
    
   
    
    imageUrl = ''
    if file.filename != '':
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        imageUrl = url_for('uploaded_file', filename=filename)

 
        tripInfo=conn[DATABASE_NAME][COLLECTION_NAME].update({'_id': ObjectId(tripId)},

        { "$set": {
        "name": request.form['name'],
        "country": request.form['country'],
        "city": request.form['city'],
        "startdate": request.form['sd'],
        "enddate": request.form['ed'],
        "triptitle": request.form['triptitle'],
        "tripreview": request.form['tripreview'],
        "tripattraction": request.form['tripattraction'],
        "totalestimatedcost": request.form['totalestimatedcost'],
        "ratings": request.form['ratings'],
        "imageURL":imageUrl,
                             }
                 })

        return render_template("summary.html", n=name, c=country, cc=city, sd=startdate, ed=enddate, tt=triptitle, rv=tripreview, a=tripattraction, ct=totalestimatedcost, r=ratings, filename=filename)


@app.route('/delete_trip/<tripId>')
def delete_trip(tripId):
    tripInfo = conn[DATABASE_NAME][COLLECTION_NAME].find_one_and_delete({'_id': ObjectId(tripId)})
    return render_template("delete.html", tripInfo=tripInfo) 


if __name__ == '__main__': 
    app.run(host=os.environ.get('IP'),port=int(os.environ.get('PORT')),debug=True)
    

