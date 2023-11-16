from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    try:
        with Image.open(path) as img:
            print(f"The format of the image is: {img.format}")
            img_arr = np.array(img)
            print(f"The shape of the image is: {img_arr.shape}")
            return img_arr
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
    except Exception as e:
        print(f"An error occurred: {e}. Please check the file and try again.")
