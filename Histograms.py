import ImageUtils as util
import GrayScale as grayScale
from datetime import datetime
import math
from decimal import *

def frequencyDistribution(input, w, h, colorIndex):
    output = [0] * 256
    for row in range(h):
        for col in range(w):
            index = row * w + col
            rgba = list(input[index])
            output[rgba[colorIndex]] = output[rgba[colorIndex]] + 1
    return output

def normalize(input, w, h, colorIndex):
    histogram = frequencyDistribution(input, w, h, colorIndex)
    maximum = brightest(histogram)
    minimum = darkest(histogram)
    theRange = maximum - minimum
    output = []
    for row in range(h):
        for col in range(w):
            index = row * w + col
            rgba = list(input[index])
            color = rgba[colorIndex]
            normalized = int(math.floor((color - minimum) * 255 / theRange))
            output.append(tuple([normalized, normalized, normalized, rgba[3]]))
    return output

def darkest(histogram):
    minimum = 0
    ctr = 0
    while histogram[ctr] == 0 and ctr < len(histogram):
        ctr = ctr + 1
    minimum = ctr
    return minimum

def brightest(histogram):
    maximum = 255
    ctr = 255
    while histogram[ctr] == 0 and ctr >= 0:
        ctr = ctr - 1
    maximum = ctr
    return maximum

def equalize(input, w, h, colorIndex):
    theRange = 255
    area = w * h
    factor = Decimal(theRange) / Decimal(area)
    histogram = frequencyDistribution(input, w, h, colorIndex)
    output = []
    sum = 0
    for level in range(256):
        sum = sum + histogram[level]
        histogram[level] = int(math.floor(factor * sum + Decimal(0.00001)))

    for row in range(h):
        for col in range(w):
            index = row * w + col
            rgba = list(input[index])
            newRgb = histogram[rgba[colorIndex]]
            output.append(tuple([newRgb, newRgb, newRgb, rgba[3]]))
    return output

def main():
    print 'Executing Histograms.main'
    im = util.open('in/captcha.png')
    fileName = "out/normalized-" + datetime.now().strftime('%Y%m%d%H%M%S') + ".png"
    fileName2 = "out/equalized-" + datetime.now().strftime('%Y%m%d%H%M%S') + ".png"
    arr = util.toBytes(im)
    arr = grayScale.averaging(arr)
    util.save("out/tempGray.png", arr, im.mode, im.size)
    # doesn't matter which color index bec. it's gray.
    normalized = normalize(arr, im.width, im.height, 0)
    equalized = equalize(arr, im.width, im.height, 0)
    util.save(fileName, normalized, im.mode, im.size)
    util.save(fileName2, equalized, im.mode, im.size)
    print 'Done executing Histograms.main'

if __name__ == "__main__":
    main()
