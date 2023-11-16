from os import system

def clear():
    system("rm -rf build")
    system("rm -rf dist")
    system("rm -rf ft_package.egg-info")
    system("pip uninstall ft_package")


if __name__ == "__main__":
    clear()