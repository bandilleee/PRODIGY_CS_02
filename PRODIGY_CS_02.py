from PIL import Image
import numpy as np

def encrypt_decrypt_image(input_path, output_path, key=123):
    # Load the image
    img = Image.open(input_path)
    img_array = np.array(img)

    # Apply XOR encryption
    encrypted_array = img_array ^ key

    # Convert back to image and save
    encrypted_img = Image.fromarray(encrypted_array)
    encrypted_img.save(output_path)

# Get user input for file paths
input_path = input("Enter the path of the image (e.g., image.jpg): ")
action = input("Do you want to encrypt or decrypt? (e/d): ")

# Set output file name
if action.lower() == "e":
    output_path = "encrypted.png"
    print("Encrypting the image...")
elif action.lower() == "d":
    output_path = "decrypted.jpg"
    print("Decrypting the image...")
else:
    print("Invalid choice! Exiting...")
    exit()

# Perform encryption or decryption
encrypt_decrypt_image(input_path, output_path)

print(f"Done! Saved as {output_path}")
