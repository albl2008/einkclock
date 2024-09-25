from io import BytesIO

from flask import Flask, Response, redirect, send_file, request, url_for

from composer_2 import ImageComposer2
from composer_7 import ImageComposer7
import sys
sys.path.append('../server-images') 
from main import generate_image
import time
from dotenv import load_dotenv
import os

load_dotenv()

weahter_api_key = os.getenv("OPENWEATHER_API_KEY")

app = Flask(__name__)


@app.route("/")
def index():
    # Get API key
    api_key = request.args.get("api_key")
    if not api_key:
        return '{"error": "no_api_key"}'
    # Render
    if request.args.get("style", "2") == "7":
        composer = ImageComposer7(
            api_key,
            lat=request.args.get("latitude", "-32.89084"),
            long=request.args.get("longitude", "-68.82717"),
            timezone=request.args.get("timezone", "America/Argentina/Mendoza"),
        )
        output = composer.render()
        
    else:
        composer = ImageComposer2(
            api_key,
            lat=request.args.get("latitude", "-32.89084"),
            long=request.args.get("longitude", "-68.82717"),
            timezone=request.args.get("timezone", "America/Argentina/Mendoza"),
        )
        image = composer.render()
        output = BytesIO()
        image.save(output, "PNG")
    # Send to client
    output.seek(0)
    return send_file(output, mimetype="image/png")

@app.route("/randomImage/")
def random_image():
    prompt = request.args.get("prompt", "a random image")
    final = prompt.replace("_", " ")
    generate_image(final)
    prompt = request.args.get("prompt", "a random image")
    final = prompt.replace("_", " ")
    generate_image(final)

    # Create a response with the image and set the appropriate headers
    response = send_file("../server-images/images/image-converted.png", mimetype="image/png")
    response.headers['Refresh'] = '95; url=%s' % url_for('index', api_key=weahter_api_key, style="7", latitude="-32.89084", longitude="-68.82717", timezone="America/Argentina/Mendoza")


    return response
    
    