from load_image import ft_load 

if __name__ == "__main__":
    try:
        arr = ft_load("../landscape.jpg")
        print(arr)
    except AssertionError as e:
        print(e)