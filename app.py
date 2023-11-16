from flask import Flask, Response, request
from simple_lama_inpainting import SimpleLama
import numpy as np
import cv2
from flask_cors import CORS

# The server
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# The model
simple_lama = SimpleLama()

img_path = "test_im.png"
mask_path = "test_mask.png"

@app.route("/greet")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/")
def inpaint():
    print("Starting...")
    image = request.files.get('image').read()
    mask = request.files.get('mask').read()
    print(type(image))  # <class 'bytes'>

    print("\nConverting to memory buffers...")
    image = np.fromstring(image, np.uint8)
    mask = np.fromstring(mask, np.uint8)
    print(type(image))  # <class 'numpy.ndarray'>

    print("\nConverting to PIL images...")
    # TODO: why is this needed?
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    mask = cv2.imdecode(mask, cv2.IMREAD_GRAYSCALE)
    print(type(image))  # <class 'numpy.ndarray'>

    print("\nInpainting...")
    image_inpainted = simple_lama(image, mask)
    print(type(image_inpainted)) # <class 'PIL.Image.Image'>

    print("\nCreating reponse...")
    image_inpainted = np.array(image_inpainted)
    print(type(image_inpainted))    # <class 'numpy.ndarray'>

    image_inpainted = cv2.imencode('.png', image_inpainted)[1].tobytes()
    print(type(image_inpainted))    # <class 'bytes'>

    response = Response(image_inpainted, mimetype='image/png')
    print(type(response))   # <class 'flask.wrappers.Response'>

    print("\nDone!")
    return response
