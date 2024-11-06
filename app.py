from flask import Flask, send_from_directory
import webbrowser
import threading
import os

# Define the directory where your project files are located
project_directory = r"C:\Project1\Responsive-Ecommerce-Website"

app = Flask(__name__, static_folder=project_directory)

@app.route('/')
def serve_homepage():
    # Serve the main HTML file (e.g., index.html or login-ecommerce.html)
    return send_from_directory(project_directory, "login-ecommerce.html")

@app.route('/<path:path>')
def serve_file(path):
    # Serve any file requested within the project directory
    return send_from_directory(project_directory, path)

def open_browser():
    # Open the default page in the browser
    webbrowser.open("http://127.0.0.1:5000/")

if __name__ == '__main__':
    # Open the browser in a separate thread
    threading.Timer(1, open_browser).start()
    # Start the Flask server on localhost
    app.run(port=5000, debug=True)
