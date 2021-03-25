from flask import Flask, request
from flask_cors import CORS
app = Flask(__name__, static_url_path='/static')
UPLOAD_FOLDER ='static/uploads/'
DOWNLOAD_FOLDER = 'static/downloads/'
ALLOWED_EXTENSIONS = {'jpg', 'png', '.jpeg'}
# APP CONFIGURATIONS
app.config['SECRET_KEY'] = 'YourSecretKey'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

CORS(app)

import numpy as np
import cv2

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()