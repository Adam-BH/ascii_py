# Ascii_py

A python package for making ascii art

## Installation

Run the following to install:

```ps
$ pip install ascii-python
```

## Usage

### Python Script

Import the ascii_py package, and you're done.

```python
import ascii_py
```

- See more in the [Docs](#-Docs) section

### Terminal

```ps
$ Coming Soon
```

# Developing Ascii_py

To install ascii_py, along with the tools you need to develop and run tests, run the following in your virtualenv:

```ps
$ pip install -e .[dev]
```

# Docs

Import the package

```python
import ascii_py
```

## asciiImage class :

The responsible class for converting ( img <-> ascii )

```python
ai = ascii_py.asciiImage(chars)
#                          ^-- Optional

'''
Chars is a list of strings used in converting images to ascii
orderd from brightest to lowest pixel values:


Default: ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
'''
```

### asciiImage.img2ascii

converts an image to ascii text

```python

asciiImg = ai.img2ascii(path, width=150)
#                               ^--Optional

'''
path  : (str)  The path to the image to be converted
width : (int)  the new width of the eimage after being converted
'''

print(asciiImg)  # <-- Returns (str)
```

## Coming Soon :

- asciiImage

  - img2asciiImg (returns an image)
  - ascii2img

- asciiVideo

- Terminal usage
