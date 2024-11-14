from io import BytesIO

from flask import Flask, Response, redirect, send_file, request, url_for

from composer_2 import ImageComposer2
from PIL import Image
from composer_7 import ImageComposer7
from server_images.main import generate_image
import time
from dotenv import load_dotenv
import os

load_dotenv()

weahter_api_key = os.getenv("OPENWEATHER_API_KEY")

app = Flask(__name__)
IMAGE_PATH = "server_images/images/output.png"

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


@app.route("/image")
def image():
    path = "server_images/images/image-converted.png"
    return send_file(path, mimetype="image/png")


@app.route("/weather_image")
def weather_image():
    path = "server_images/images/weather.png"
    return send_file(path, mimetype="image/png")

@app.route("/random_image/")
def random_image():
    prompt = request.args.get("prompt", "a random image")
    generate_image(prompt)
    
    path = "server_images/images/imagegen.png"
    return 'Image saved' + path



@app.route("/render_weather/")
def render_weather():
    api_key = os.getenv("OPENWEATHER_API_KEY")
    composer = ImageComposer7(
        api_key,
        lat="-32.89084",
        long="-68.82717",
        timezone="America/Argentina/Mendoza",
    )
    
    # Call the render method to get the image as a byte stream
    output = composer.render()
    
    # Reset the pointer of the BytesIO stream to the beginning
    output.seek(0)

    with open("server_images/images/weather.png", "wb") as f:
        f.write(output.getvalue())

    return "Image saved as weather.png"
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)


    