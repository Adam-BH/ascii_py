import cv2


class asciiImage:
    def __init__(self, chars=["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]):
        self.CHARS = chars
        portion = int(255 / len(self.CHARS))
        self.RANGES = [range(i, i + portion) for i in range(0, 255 - portion, portion)]

    def __pixel2ascii(self, value):
        for i in range(len(self.RANGES)):
            if value in self.RANGES[i]:
                return self.CHARS[i]
        return self.CHARS[len(self.CHARS) - 1]

    def __checkInputs(self, p, w):
        if w == 0:
            print("[Error]: Image width cannot be zero")
            quit()

        try:
            img = cv2.imread(p)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        except Exception as e:
            print(f"{p} is not a valid image", e)
            quit()

    def img2ascii(self, path, width=100):
        self.__checkInputs(path, width)

        img = cv2.imread(path, 0)
        img = cv2.resize(img, (width, int((img.shape[0] / img.shape[1]) * width)))

        asciiText = ""

        for row in img:
            for pixel in row:
                char = self.__pixel2ascii(pixel)
                asciiText += char
            asciiText += "\n"

        return asciiText
