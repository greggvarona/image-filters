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
                            rgb = list(input[index])
                            k = kernel[kIndex]
                            a += k * rgb[3]
                            r += k * rgb[0]
                            g += k * rgb[1]
                            b += k * rgb[2]
            output.append(tuple([clampRGBValue(r), clampRGBValue(g), clampRGBValue(b), clampRGBValue(a)]))
    return output

def clampRGBValue(theByte):
    return int(max(min(theByte, 255), 0))

def toByte(rgbTuple):
    rgba = list(rgbTuple)
    return (rgba[0] << 16) | (rgba[1] << 8) | (rgba[2])

def uniformedThresholding(input, w, h, level):
    output = []
    for row in range(h):
        for col in range(w):
            replacement = tuple([255, 255, 255, 255])
            index = row * w + col
            levelRgbByte = toByte(level)
            rgbByte = toByte(input[index])
            if (rgbByte < levelRgbByte):
                replacement = tuple([0, 0, 0, 255])
            output.append(replacement)
    return output

def downSignal():
    return (0, 0, 0)

def isEdge(index, w, h):
    return (index / w == 0 or index == (w-1))
