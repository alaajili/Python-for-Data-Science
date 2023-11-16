from os import system

def run():
    system("python3 setup.py sdist bdist_wheel")
    system("pip3 install ./dist/ft_package-0.0.1.tar.gz")

if __name__ == "__main__":
    run()