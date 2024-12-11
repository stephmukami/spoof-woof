import hashlib
import PIL.Image
import random
import numpy as np
import io
import piexif


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
    modified_array = (img_array & 0xFE) | noise  
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


def modify_exif_metadata(original_image):
    """
    Modifies EXIF metadata to include random comments.
    """
    error_logged = False
    try:
        # Extract EXIF data from the image object directly or initialize an object for EXIF with some common fields
        exif_data = original_image.info.get('exif', b'')
        
        if not exif_data:
            exif_dict = {"0th": {}, "Exif": {}, "GPS": {}, "Interop": {}, "1st": {}, "thumbnail": None}
        else:
            exif_dict = piexif.load(exif_data)

        # Modifications to be made to the EXIF data
        modifications = [
            ('0th', piexif.ImageIFD.XPComment, str(random.random()).encode('utf-16')),
            ('Exif', piexif.ExifIFD.UserComment, f"Modification {random.randint(0, 1000)}".encode('utf-16'))
        ]

        # Apply the modifications
        for ifd, tag, value in modifications:
            if ifd in exif_dict:
                exif_dict[ifd][tag] = value

        exif_bytes = piexif.dump(exif_dict)
        return exif_bytes

    except Exception as e:
        if not error_logged:
            print(f"Error modifying EXIF: {e}")
            error_logged = True
        return None


def modify_input_image(image, temperature):
    """
    Modifies the image using the multiple strategies.
    """
    quality = max(10, int(85 - (temperature * 5)))
    compressed_image = exploit_compression_artifacts(image, quality)
    lsb_modified_image = modify_lsb(compressed_image)
    noise_modified_image = add_noise(lsb_modified_image)
    exif_data = modify_exif_metadata(noise_modified_image)
    return noise_modified_image, exif_data


def simulated_annealing(image, desired_prefix, temperature=1.0, cooling_rate=0.99, max_iterations=2):
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
        modified_image, exif_data = modify_input_image(current_image, current_temperature)

        modified_image_bytes = image_to_bytes(modified_image, exif_data=exif_data)
        modified_hash = calculate_hash(modified_image_bytes)

        if modified_hash.startswith(target_prefix):
            print(f"Match found after {iteration} iterations!")
            print(f"Original hash: {original_hash}")
            print(f"Target prefix: {target_prefix}")
            print(f"Final hash: {modified_hash}")
            return modified_image

        current_temperature *= cooling_rate

    print(f"No match found after {max_iterations} iterations.")
    print(f"Original hash: {original_hash}")
    print(f"Target prefix: {target_prefix}")
    print(f"Final hash: {modified_hash}")
    return current_image


if __name__ == "__main__":
    original_image = PIL.Image.open("./original.jpg")
    desired_prefix = "0x24"
    result_image = simulated_annealing(original_image, desired_prefix)
    result_image.save("modified_output_image.jpg")
