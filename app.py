from flask import Flask, request
from flask_cors import CORS
app = Flask (__name__)
CORS(app)

import numpy as np
import cv2
from PIL import Image
from model import *

def image_convert(img):
    img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
    img = cv2.resize(np.array(img), (28, 28), interpolation=cv2.INTER_AREA)
    img = 255 - (img)
    img = img / 255
    img.reshape((28, 28, 1))
    return img

@app.route('/')
def hello():
    return 'Hello!'

@app.route('/number', methods=['POST'])
def number():
    img = image_convert(Image.open(request.files['file'].stream))
    if(np.sum(img)<1.0): return "?, ?"
    return "99, 99"
    result = pred(img)
    answer = np.argmax(result)
    prob = result[0][answer] * 100.0
    return str(answer) + ", " + str(round(prob, 2))

if __name__ == "__main__":
    app.run()