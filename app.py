from flask import Flask , render_template, request, url_for, redirect
from pymongo import MongoClient
from datetime import datetime
import socket

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.flask_db
post = db.posts


@app.route('/', methods=('GET', 'POST'))
def index():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    server_hostname = socket.gethostname()
    
    return render_template('index.html', current_date=current_date, server_hostname=server_hostname)

"""
def home():
    # Fetching the current date
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Fetching the server hostname
    server_hostname = socket.gethostname()
    
    # HTML content for the page
    html_content = f"""
"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>One Page Flask App</title>
    </head>
    <body>
        <h3>Sorry for having forked this I'm just looking to learn on a project :)</h3>
        <h1>Welcome to My Flask Application</h1>
        <p><strong>Your Name:</strong> Louay Belkhamsa</p>
        <p><strong>Project Name:</strong> Lou's Studies Blog</p>
        <p><strong>Website Version:</strong> V1</p>
        <p><strong>Server Hostname:</strong> {server_hostname}</p>
        <p><strong>Current Date:</strong> {current_date}</p>
    </body>
    </html>
"""
"""
    
    return html_content
"""
if __name__ == "__main__":
    app.run(debug=True)