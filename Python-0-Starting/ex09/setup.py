from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()
with open ("LICENSE", "r") as fh:
    license = fh.read()

setup(
    name="ft_package",
    version="0.0.1",
    author="alaajili",
    author_email="alaajili@student.1337.ma",
    description="A sample test package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license=license,
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)