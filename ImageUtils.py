import operator
from operator import itemgetter
from PIL import Image

def open(fileName):
    im = Image.open(fileName) #Can be many different formats.
    return im

def toBytes(im):
    return list(im.getdata())

def save(fileName, imgData, mode, size):
    newImage = Image.new(mode, size)
    newImage.putdata(imgData)
    newImage.save(fileName)

def convolve(input, w, h, kernel, kw, kh):
    output = []
    for row in range(h):
        for col in range(w):
            #origin = row * w + col
            for kernelY in range(kh):
                for kernelX in range(kw):
                    y = row + kernelY - (kh/2)
                    x = col + kernelX - (kw/2)
                    # The following nested conditions makes sure that the
                    # kernel's origin doesn't go out of the image's boundaries.
                    if(x >= 0 and y >= 0):
                        if(x < w and y < h):
                            index = y * w + x
                            kIndex = kernelY * kw + kernelX
                            rgba = list(input[index])
                            k = kernel[kIndex]
                            r += k * rgba[0]
                            g += k * rgba[1]
                            b += k * rgba[2]
            output.append(tuple([clampRGBValue(r), clampRGBValue(g), clampRGBValue(b), rgba[3]]))
    return output

def clampRGBValue(theByte):
    return int(max(min(theByte, 255), 0))

def toByte(rgbTuple):
    rgb = list(rgbTuple)
    return (rgb[0] << 16) | (rgb[1] << 8) | (rgb[2])

def uniformedThresholding(input, w, h, level):
    output = []
    levelRgbByte = toByte(level)
    for row in range(h):
        for col in range(w):
            index = row * w + col
            replacement = (0, 0, 0, 255)
            rgbByte = toByte(input[index])
            if (rgbByte < levelRgbByte):
                replacement = (255, 255, 255, 255)
            output.append(replacement)
    return output

def downSignal():
    return (0, 0, 0)

def isEdge(index, w, h):
    return (index / w == 0 or index == (w-1))
