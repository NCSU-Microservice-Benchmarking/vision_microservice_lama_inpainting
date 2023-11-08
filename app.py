# Source https://flask.palletsprojects.com/en/3.0.x/quickstart
from flask import Flask
from simple_lama_inpainting import SimpleLama
from PIL import Image

# The server
app = Flask(__name__)

# The model
simple_lama = SimpleLama()

img_path = "test_im.png"
mask_path = "test_mask.png"

@app.route("/greet")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/")
def inpaint():
    image = Image.open(img_path)
    mask = Image.open(mask_path).convert('L')
    result = simple_lama(image, mask)
    result.save("inpainted.png")
    return "<p>Done!</p>"
