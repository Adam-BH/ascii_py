import cv2
import argparse
import os

# brightest to lowest
CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

portion = int(255 / len(CHARS))
ranges = [range(i, i + portion) for i in range(0, 255 - portion, portion)]


def pixel2ascii(value):
    for i in range(len(ranges)):
        if value in ranges[i]:
            return CHARS[i]
    return CHARS[len(CHARS) - 1]


def main(path, width, output):
    try:
        img = cv2.imread(path, 0)
        img = cv2.resize(img, (width, int((img.shape[0] / img.shape[1]) * width)))
    except:
        print("input is not a valid image")
        quit()

    file = open(output, "w")
    for row in img:
        for pixel in row:
            char = pixel2ascii(pixel)
            file.write(char)

            print(char, end="")
        file.write("\n")
        print()
    file.close()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("input", help="path to input image")
    ap.add_argument("-o", "--output", help="path to output text")
    ap.add_argument("-w", "--width", help="new image width", type=int)

    args = ap.parse_args()

    w = args.width
    o = args.output
    i = args.input

    if w == None:
        w = 150
    if o == None:
        o = "output.txt"

    if w == 0:
        print("width cannot be zero")
        quit()
    if os.path.isfile(i) == False:
        print("input path must be valid")
        quit()

    main(
        path=i,
        width=w,
        output=o,
    )
