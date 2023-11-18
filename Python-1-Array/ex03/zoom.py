from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def zoom():
    try:
        path = "../animal.jpeg"
        img = ft_load(path)
        print(np.array(img))
        zoomed_img = img.crop((100, 100, 500, 500))
        print("New shape after slicing:", zoomed_img.size)
        print(np.array(zoomed_img))

        plt.imshow(zoomed_img)
        plt.title("Zoomed Image")
        plt.axis('on')
        plt.show()
    except Exception as e:
        print(e)


    


if __name__ == "__main__":
    zoom()