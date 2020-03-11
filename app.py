import os
from flask import Flask, render_template, request
from pymongo import MongoClient


app = Flask(__name__)


APP_ROOT = os.path.dirname(os.path.abspath(__file__))

client = MongoClient("mongodb://admin:admin@cluster0-shard-00-00-zgcvy.mongodb.net:27017,cluster0-shard-00-01-zgcvy.mongodb.net:27017,cluster0-shard-00-02-zgcvy.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.stylesearch
#dbCollection = db.Style
dbCollection = db.test
users = db.users


@app.route("/")
def index():
 #   return render_template("upload.html")
    return render_template("sidebar.html")

@app.route("/database", methods=['POST', 'GET'])
def database():

    dbCollection.insert({'ID' : '502', 'Garment Layer' : 'Top', 'Colour' : 'black'})
    return '<h1>Added a user! </h1>'

@app.route("/test")
def contact():
    if request.method == 'GET':
        if request.form['dbadd'] == 'Add DB Value':
            database()


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