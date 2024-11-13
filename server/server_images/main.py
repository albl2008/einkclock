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

# Palette colors for the 7 colors supported by the panel#

PALETTE = [
    (0, 0, 0),         # Black
    (255, 255, 255),   # White
    (0, 255, 0),       # Green
    (0, 0, 255),       # Blue
    (255, 0, 0),       # Red
    (255, 255, 0),     # Yellow
    (255, 128, 0),     # Orange
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
    
    return palette_image


async def generate_image(prompt):
    mandatory = "The image generated will be printed in 7 colour ACeP display, so please generate an image considering this. Think on styles like pop art, or single line drawings or something in bold colours and well defined. One image about: "
    response = await client.images.generate(prompt=mandatory + ' ' + prompt,
    n=1,
    model="dall-e-3",
    size="1024x1024")
    image_url = response.data[0].url

    # Download image
    image_data = requests.get(image_url).content
    img = Image.open(BytesIO(image_data))

    
    img.save(f"server_images/images/imagegen.png")
    

    

    resize_and_convert(img)

    return

def resize_and_convert(image, width=600, height=448):
    # Resize the image to the display size
    image_resized = image.resize((width, height))

    # Convert the image to the 7-color palette
    image_converted = convert_image_to_palette(image_resized, PALETTE)

    # Save the image
    image_converted.save(f"server_images/images/image-converted.png")

    return


