from openai import OpenAI


import requests
from io import BytesIO
from PIL import Image
from dotenv import load_dotenv
import os
import numpy as np


load_dotenv()


print("API KEY: " + os.getenv("OPENAI_API_KEY"))


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

PALETTE = [
    (0, 0, 0),        # BLACK
    (255, 255, 255),  # WHITE
    (0, 255, 0),      # GREEN
    (0, 0, 255),      # BLUE
    (255, 0, 0),      # RED
    (255, 255, 0),    # YELLOW
    (128, 0, 255),    # PURPLE
    (255, 140, 0),    # ORANGE
    (102, 102, 102)   # GREY
]

def find_closest_color(pixel, palette):
    # Calculate the Euclidean distance between a pixel and each color in the palette
    distances = [np.sqrt(np.sum((np.array(pixel) - np.array(color)) ** 2)) for color in palette]
    return palette[np.argmin(distances)]  # Return the closest color from the palette

def convert_image_to_palette(image, palette):
    # Resize and convert the image to RGB mode if not already
    image = image.convert("RGB")
    
    # Create a new image to store the palette-converted pixels
    palette_image = Image.new("RGB", image.size)
    pixels = palette_image.load()
    
    # Process each pixel in the original image
    for y in range(image.height):
        for x in range(image.width):
            original_pixel = image.getpixel((x, y))
            closest_color = find_closest_color(original_pixel, palette)
            pixels[x, y] = closest_color
    
    palette_image.show()

    return palette_image


def generate_image(prompt):
    response = client.images.generate(prompt=prompt,
    n=1,
    model="dall-e-3",
    size="1024x1024")
    image_url = response.data[0].url

    # Download image
    image_data = requests.get(image_url).content
    img = Image.open(BytesIO(image_data))

    #img.show()

    #random_number = np.random.randint(1000, 2000)
    img.save(f"server_images/images/imagegen.png")
    #img.save(f"images/imagegen-{random_number}.jpg")

    

    resize_and_convert(img)

    return

def resize_and_convert(image, width=600, height=448):
    # Resize the image to the display size
    image_resized = image.resize((width, height))

    # Convert to a limited palette (7 colors)
    image_reduced = image_resized.convert('P', palette=PALETTE, colors=7)

    

    #random_number = np.random.randint(1000, 2000)
    # Save the image
    image_reduced.save(f"server_images/images/image-converted.png")

    return 



