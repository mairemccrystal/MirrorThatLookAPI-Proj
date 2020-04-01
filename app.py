import os
from flask import Flask, render_template, request, jsonify, make_response
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId, json_util
import http.client, urllib.request, urllib.parse, urllib.error, base64
import requests
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
    #return make_response(jsonify({data_to_return}))
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

#use the mirrorLookAPI

@app.route("/sim", methods=['POST', 'GET'])
def mirrorLook():
    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': 'ba10a036532d4c438ded719c0f797a4e',
        'Ocp-Apim-Subscription-Key': 'ba10a036532d4c438ded719c0f797a4e',
    }

    params = urllib.parse.urlencode({
        # Request parameters
        'image': 'https://contestimg.wish.com/api/webimage/5c394bfbe3e6604287a573da-large.jpg?cache_buster=276746c000af54b686498893ade2baea',
        # 'gender': '{string}',
         #'limit': '2',
    })

    conn = http.client.HTTPSConnection('api.mirrorthatlook.com')
    conn.request("GET", "/v2/mirrorthatlook?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    # print(data)

    my_json = data.decode('utf8')
    python_obj = json.loads(my_json)

    loaded_json = json.dumps(my_json)
    loaded_json = json.loads(my_json)

    #print(loaded_json)
    linksData = []
    links = ((loaded_json["result"][0]["products"][0]["affiliates"][0]["link"]))
    for x in range(10):
        y = ((loaded_json["result"][0]["products"][x]["affiliates"][0]["link"]))
        linksData.append(y)

    # new_json = str(new_json).strip('[]')

    #return links
    return make_response(jsonify(linksData))


@app.route("/classification", methods=['POST', 'GET'])
def classifyImage():
    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': 'ba10a036532d4c438ded719c0f797a4e',
        'Ocp-Apim-Subscription-Key': 'ba10a036532d4c438ded719c0f797a4e',
    }

    params = urllib.parse.urlencode({
        # Request parameters
        'image': 'https://contestimg.wish.com/api/webimage/5c394bfbe3e6604287a573da-large.jpg?cache_buster=276746c000af54b686498893ade2baea',
        # 'gender': '{string}',
         #'limit': '2',
    })

    conn = http.client.HTTPSConnection('api.mirrorthatlook.com')
    conn.request("GET", "/v2/mirrorthatlook?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    # print(data)

    my_json = data.decode('utf8')
    python_obj = json.loads(my_json)

    loaded_json = json.dumps(my_json)
    loaded_json = json.loads(my_json)

    # this works to classify the group that the item is in from the image
    classification = ((loaded_json["result"][0]["group"]))

    #return links
    return make_response(jsonify(classification))


if __name__ == "__main__":
    app.run(port=4555, debug=True)