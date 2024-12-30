from PIL import Image
import numpy as np
import random
import json


def save_key(key, key_file):
    with open(key_file, "w") as f:
        json.dump({"key": key}, f)
    print(f"Key saved to {key_file}")


def load_key(key_file):
    with open(key_file, "r") as f:
        data = json.load(f)
    return data["key"]


def generate_noise(shape, key):
    np.random.seed(key)  
    return np.random.randint(0, 256, shape, dtype=np.uint8)


def encrypt_image(input_path, output_path, key_file):
  
    key = random.randint(10, 10000)
    save_key(key, key_file)

  
    img = Image.open(input_path).convert("RGB")
    img_array = np.array(img, dtype=np.uint8)

  
    noise = generate_noise(img_array.shape, key)

  
    noisy_image_array = np.bitwise_xor(img_array, noise)

  
    noisy_image = Image.fromarray(noisy_image_array)
    noisy_image.save(output_path)
    print(f"Encrypted image saved to {output_path}")

    return noise  


def decrypt_image(input_path, output_path, key_file):

    key = load_key(key_file)


    img = Image.open(input_path).convert("RGB")
    noisy_image_array = np.array(img, dtype=np.uint8)


    noise = generate_noise(noisy_image_array.shape, key)


    decrypted_image_array = np.bitwise_xor(noisy_image_array, noise)


    decrypted_image = Image.fromarray(decrypted_image_array)
    decrypted_image.save(output_path)
    print(f"Decrypted image saved to {output_path}")


input_image = r"input_image.jpg"  
encrypted_image = r"encrypted_image.jpg"  
decrypted_image = r"decrypted_image.jpg"  
key_file = r"encryption_key.json"  


noise = encrypt_image(input_image, encrypted_image, key_file)


decrypt_image(encrypted_image, decrypted_image, key_file)
