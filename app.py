from flask import Flask , render_template, request, url_for, redirect, jsonify
from pymongo import MongoClient
from datetime import datetime
import socket

app = Flask(__name__)

client = MongoClient("mongodb://mongodb_container:27017")
db = client["posts"]
post = db.posts


@app.route('/', methods=('GET', 'POST'))
def index():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    server_hostname = socket.gethostname()
    
    return render_template('index.html', current_date=current_date, server_hostname=server_hostname)

@app.route('/posts', methods=('GET',))
def getPosts():
    # Fetch last 10 records
    records = list(db.test_collection.find().sort("_id", -1).limit(10))
    
    
    for record in records:
        record['_id'] = str(record['_id'])
    
    return render_template('app_show_posts.html', posts=records)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)