import os
from flask import Flask, render_template, request, jsonify, make_response
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId, json_util
import json


app = Flask(__name__)
CORS(app)


APP_ROOT = os.path.dirname(os.path.abspath(__file__))

client = MongoClient("mongodb://admin:admin@cluster0-shard-00-00-zgcvy.mongodb.net:27017,cluster0-shard-00-01-zgcvy.mongodb.net:27017,cluster0-shard-00-02-zgcvy.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.stylesearch
#dbCollection = db.Style
dbCollection = db.test
users = db.users


#the default app route
@app.route("/")
def index():
 #   return render_template("upload.html")
    return render_template("sidebar.html")

#this is to insert into the database
@app.route("/database", methods=['POST', 'GET'])
def database():

    dbCollection.insert({'ID' : '502', 'Garment Layer' : 'Top', 'Colour' : 'black'})
    return '<h1>Added a record! </h1>'


#go and check the button when we click the button
def contact():
    if request.method == 'GET':
        if request.form['dbadd'] == 'Add DB Value':
            database()

@app.route("/showAll", methods=['POST', 'GET'])
def showAll():

    data_to_return = []
    for x in dbCollection.find():
        data_to_return.append(x)
    return json.dumps(data_to_return, indent=4, default=json_util.default)

@app.route("/showColour", methods=['POST', 'GET'])
def showColor():
    colourData = []
    for x in dbCollection.find({"Colour" : "black"}):
        colourData.append(x)
    return json.dumps(colourData, indent=4, default=json_util.default)


@app.route("/showColourID", methods=['POST', 'GET'])
def showColorIDs():
    colourData = []
    for x in dbCollection.find({"Colour" : "red"}, {'_id': 0, 'Garment Layer' : 0, 'Colour' : 0}):
        colourData.append(x)


    return json.dumps(colourData, indent=4, default=json_util.default)

@app.route("/test", methods=['POST', 'GET'])
def test():
    newarray = []
    idthing = dbCollection.distinct("ID");
    newarray.append(idthing)
    return json.dumps(newarray, indent=4, default=json_util.default)


#upload an image
@app.route("/upload", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'data/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)

    return render_template("complete.html")

if __name__ == "__main__":
    app.run(port=4555, debug=True)