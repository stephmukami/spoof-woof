import hashlib
import PIL.Image
import random
import numpy as np
import io
import piexif
import argparse
import sys


def image_to_bytes(image, exif_data=None):
    """
    Converts an image to bytes
    """
    byte_arr = io.BytesIO()
    if exif_data:
        image.save(byte_arr, format='JPEG', quality=85, exif=exif_data)
    else:
        image.save(byte_arr, format='JPEG', quality=85)
    return byte_arr.getvalue()


def calculate_hash(image_bytes):
    """
    Calculates the SHA-256 hash of the image bytes.
    """
    return hashlib.sha256(image_bytes).hexdigest()


def exploit_compression_artifacts(image, quality):
    """
    Simulates compression artifacts by saving and reloading the image with a specified quality.
    """
    buffer = io.BytesIO()
    image.save(buffer, format='JPEG', quality=quality)
    buffer.seek(0)
    compressed_image = PIL.Image.open(buffer)
    return compressed_image.copy()


def modify_lsb(image):
    """
    Modifies the least significant bit (LSB) of image pixels.
    """
    img_array = np.array(image, dtype=np.uint8)
    noise = np.random.randint(0, 2, img_array.shape, dtype=np.uint8)
    modified_array = (img_array & 0xFE) | noise  # Clear the LSB and put the noise instead
    modified_image = PIL.Image.fromarray(modified_array, mode=image.mode)
    return modified_image


def add_noise(image):
    """
    Adds Gaussian noise to the image.
    """
    np_image = np.array(image)
    noise = np.random.normal(0, 10, np_image.shape)
    np_image = np.clip(np_image + noise, 0, 255).astype(np.uint8)
    return PIL.Image.fromarray(np_image)


def modify_exif_metadata(image):
    """
    Modifies EXIF metadata to include random comments.
    """
    error_logged = False
    try:
        # Extract EXIF data from the image object directly or initialize an object for EXIF with some common fields
        exif_data = image.info.get('exif', b'')
        exif_dict = piexif.load(exif_data) if exif_data else {"0th": {}, "Exif": {}, "GPS": {}, "Interop": {}, "1st": {}, "thumbnail": None}
        
        # Modify the EXIF data randomly
        modifications = [
            ('0th', piexif.ImageIFD.XPComment, str(random.random()).encode('utf-16')),
            ('Exif', piexif.ExifIFD.UserComment, f"Modification {random.randint(0, 1000)}".encode('utf-16'))
        ]
        
        # Apply the modifications
        for ifd, tag, value in modifications:
            if ifd in exif_dict:
                exif_dict[ifd][tag] = value

        # Dump the EXIF data and return it
        exif_bytes = piexif.dump(exif_dict)
        return exif_bytes

    except Exception as e:
        if not error_logged:
            print(f"Error modifying EXIF: {e}")
            error_logged = True
        return None
 
def apply_modification(image, temperature):
    """
    Modifies the image using multiple strategies.
    """
    quality = max(10, int(85 - (temperature * 5)))
    compressed_image = exploit_compression_artifacts(image, quality)
    lsb_modified_image = modify_lsb(compressed_image)
    noise_modified_image = add_noise(lsb_modified_image)
    exif_data = modify_exif_metadata(noise_modified_image)
    return noise_modified_image, exif_data


def simulated_annealing(image, desired_prefix, temperature=1.0, cooling_rate=0.99, max_iterations=1):
    """
    Applies simulated annealing to modify an image until its hash matches a desired prefix.
    """
    original_image = image.copy()
    original_image_bytes = image_to_bytes(original_image)
    original_hash = calculate_hash(original_image_bytes)

    target_prefix = desired_prefix
    current_image = original_image
    current_temperature = temperature
    iteration = 0

    while iteration < max_iterations:
        iteration += 1
        modified_image, exif_data = apply_modification(current_image, current_temperature)

        modified_image_bytes = image_to_bytes(modified_image, exif_data=exif_data)
        modified_hash = calculate_hash(modified_image_bytes)

        if modified_hash.startswith(target_prefix):
            print(f"Match found after {iteration} iteration(s)!")
            print(f"Original hash: {original_hash}")
            print(f"Target prefix: {target_prefix}")
            print(f"Final hash: {modified_hash}")
            return modified_image

        current_temperature *= cooling_rate

    print(f"No match found after {max_iterations} iteration(s).")
    print(f"Original hash: {original_hash}")
    print(f"Target prefix: {target_prefix}")
    print(f"Final hash: {modified_hash}")
    return modified_image

def process_image(hexstring, input_image_path, output_image_path):
    """
    Core logic for processing the image.
    """
    if not hexstring.startswith('0x'):
        raise ValueError("Hexstring must start with 0x")
    try:
        int(hexstring, 16)
    except ValueError:
        raise ValueError("Invalid hexstring, use symbols 0-9, A-F")

    try:
        original_image = PIL.Image.open(input_image_path)
        if original_image.format not in ('JPEG', 'JPG'):
            raise ValueError("Only JPG images are supported. Please provide a JPG file.")

        result_image = simulated_annealing(original_image, hexstring)
        result_image.save(output_image_path)
        return f"Modified image saved as {output_image_path}"

    except Exception as e:
        raise RuntimeError(f"Error processing image: {e}")

def main():
    parser = argparse.ArgumentParser(description="Spoof an image hash using simulated annealing")
    parser.add_argument('hexstring', type=str, help="Desired hex prefix for the image hash")
    parser.add_argument('input_image', type=str, help="Path to the input image")
    parser.add_argument('output_image', type=str, help="Path to save the modified image")
    args = parser.parse_args()

    try:
        message = process_image(args.hexstring, args.input_image, args.output_image)
        print(message)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
        
if __name__ == "__main__":
    main()