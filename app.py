from flask import Flask
from datetime import datetime
import socket

app = Flask(__name__)

@app.route("/")
def home():
    # Fetching the current date
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Fetching the server hostname
    server_hostname = socket.gethostname()
    
    # HTML content for the page
    html_content = f"""
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
    
    return html_content

if __name__ == "__main__":
    app.run(debug=True)