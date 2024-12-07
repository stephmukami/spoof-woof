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

import sys
import hashlib

def hashfile(file):
    BUFFER_SIZE = 65536 # confirm the average file size 
    sha256 = hashlib.sha256()

    with open(file,"rb") as f: #what does rb mean,must the file be hardcoded
        while True:
            data = f.read(BUFFER_SIZE)

            if not data:
                break

            sha256.update(data)

    return sha256.hexdigest()

file_hash = hashfile(sys.argv[1])
print(f"Hashed file is {file_hash}")