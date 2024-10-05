import hashlib
import os
import time

from PIL import Image

#from display.waveshare_epd import epd5in83bc
#from display.show import show_image

HASH_FILE = "last_hash_weather.txt"

def log_message(message):
    with open("/var/log/cron.log", "a") as log_file:
        log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")
        

def calculate_file_hash(file_path):
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        log_message(f"File not found: {file_path}")
        return None

def get_last_hash():
    try:
        with open(HASH_FILE, "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return None

def store_current_hash(current_hash):
    with open(HASH_FILE, "w") as file:
        file.write(current_hash)

def check_file_change(file_path):
    last_hash = get_last_hash()
    current_hash = calculate_file_hash(file_path)
    
    if current_hash is None:
        return
    
    if current_hash != last_hash:
        log_message(f"------------------- {file_path} CAMBIO CLIMA! -------------------")
        send_to_epd()
        store_current_hash(current_hash)  # Update the stored hash
    else:
        log_message(f"Sin cambios CLIMA! {file_path}.")

def send_to_epd():
    fiepath = "server_images/images/image-converted.png"
    image = Image.open(fiepath)
    log_message("Sending to EPD")
    #show_image(image)

    


# Example usage
image_path = "server_images/images/weather.png"
log_message("Chequeando Clima")
check_file_change(image_path)
