import sys
import time

import requests
from PIL import Image

from flask import send_file


IMAGE_SIZE = (600, 448)



def log_message(message):
    with open("/var/log/cron.log", "a") as log_file:
        log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")


def show_image(image):
    log_message(f"--------------- RELOAD CLIMA! -------------------")
    image.save("server_images/images/weather.png")


    




filename = sys.argv[1]


if "://" in filename:
    # URL
    response = requests.get(filename, stream=True)
    if response.status_code == 200 and 'image' in response.headers['Content-Type']:
        response.raw.decode_content = True
        image = Image.open(response.raw)
    else:
        print("Error: URL did not return a valid image")
        sys.exit(1)
else:
    # Filename
    image = Image.open(filename)
show_image(image)