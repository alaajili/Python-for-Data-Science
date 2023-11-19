from PIL import Image
import numpy as np
import cv2


def ft_load(path: str):
    """
    Loads an image from the given file path using Pillow (PIL) library, and converts it into a NumPy array.

    Args:
    - path (str): The file path to the image.

    Returns:
    - np.array: NumPy array representing the image.
    """
    try:
        with Image.open(path) as img:
            print(f"The format of the image is: {img.format}")
            img_arr = np.array(img)
            print(f"The shape of the image is: {img_arr.shape}")
            return img
    except FileNotFoundError:
        raise AssertionError("File not found. Please provide a valid file path.")
    except Exception as e:
        raise AssertionError(f"An error occurred: {e}. Please check the file and try again.")