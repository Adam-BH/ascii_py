from setuptools import setup

with open("README.md", "r") as f:
    README = f.read()

setup(
    name="ascii-python",
    version="0.1.0",
    description="A python package for making ascii art",
    long_description=README,
    long_description_content_type="text/markdown",
    py_modules=["ascii_py"],
    package_dir={"": "src"},
    url="https://github.com/Adam-BH/ascii.py",
    author="Adam Bhouri",
    author_email="adam.bhouri@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "opencv-python",
    ],
    extras_require={"dev": ["pytest"]},
)
