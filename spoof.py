# Input: original.jpg, target_prefix = "0x24"
# Output: altered.jpg with hash starting with "0x24"

# Steps:
# 1. Load "original.jpg".
# 2. Parse "0x24" as the target prefix.
# 3. Compute SHA hash of "original.jpg".
# 4. Locate editable parts of the image (metadata, padding).
# 5. Modify editable sections iteratively to match the prefix.
# 6. Save the modified image as "altered.jpg".
# 7. Verify the hash of "altered.jpg" starts with "0x24".
# 8. Output the adjusted hash and file name.
"""
remember to check usecases eg if there arent enough args
"""
from PIL import Image
import hashlib
import sys

def adjust_image_hash(hex_prefix, input_file, output_file):
    # Read the input image
    with open(input_file, "rb") as f:
        original_data = bytearray(f.read())
    
    # Parse the target prefix
    target_prefix = hex_prefix.lower()

    # Modify metadata or append padding
    padding = b""
    for i in range(1000000):  # Limit iterations to prevent infinite loops
        # Add padding to modify the hash
        modified_data = original_data + padding

        # Compute hash
        sha256 = hashlib.sha256()
        sha256.update(modified_data)
        hash_result = sha256.hexdigest()
        if i % 10000 == 0:
            print(f"Iteration {i}: Current hash {hash_result}")

        # Check if hash starts with the desired prefix
        if hash_result.startswith(target_prefix):
            # Write the modified file
            with open(output_file, "wb") as outf:
                outf.write(modified_data)
            print(f"Success! Hash: {hash_result}")
            return

        # Add more padding if prefix doesn't match
        padding = padding + b"\x00"  # Adjust padding byte as needed

    print("Failed to find a matching hash prefix within the iteration limit.")

# Command-line interface
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python spoof.py <target_prefix> <input_file> <output_file>")
        sys.exit(1)
    
    target_prefix = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]
    
    adjust_image_hash(target_prefix, input_file, output_file)
