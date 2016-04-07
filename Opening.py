import ImageUtils as util
import GrayScale as grayScale
import Smoothening as smoothening
from datetime import datetime
import math
import time

def erode(input, w, h, window, ww, wh):
    wwHalf = int(math.floor(ww / 2))
    whHalf = int(math.floor(wh / 2))
    output = [(0 , 0, 0)] * w * h
    for row in range(whHalf, h - whHalf): # rows in the image except the border
        for col in range(wwHalf, w - wwHalf): # columns in the image except the border
            minimum = 255
            index = row * w + col
            for wRow in range(wh):
                for wCol in range(ww):
                    xi = col - wwHalf - 1 + wCol
                    yi = row - whHalf - 1 + wRow
                    indexi = yi * w + xi
                    wIndex = wRow * ww + wCol
                    iPixel = list(input[indexi])[0]
                    wPixel = list(window[wIndex])[0]
                    diff = iPixel - wPixel
                    if diff < minimum and diff >= 0:
                        minimum = diff
            output[index] = (minimum, minimum, minimum)
    return output

def dilate(input, w, h, window, ww, wh):
    wwHalf = int(math.floor(ww / 2))
    whHalf = int(math.floor(wh / 2))
    output = [(0 , 0, 0)] * w * h
    for row in range(whHalf, h - whHalf): # rows in the image except the border
        for col in range(wwHalf, w - wwHalf): # columns in the image except the border
            maximum = 0
            index = row * w + col
            for wRow in range(wh):
                for wCol in range(ww):
                    xi = col - wwHalf - 1 + wCol
                    yi = row - whHalf - 1 + wRow
                    indexi = yi * w + xi
                    wIndex = wRow * ww + wCol
                    iPixel = list(input[indexi])[0]
                    wPixel = list(window[wIndex])[0]
                    diff = iPixel + wPixel
                    if diff >= maximum and diff > 0:
                        maximum = diff
            output[index] = (maximum, maximum, maximum)
    return output

def opening(input, w, h, ewindow, eww, ewh, dwindow, dww, dwh):
    output = erode(input, w, h, ewindow, eww, ewh)
    output = dilate(output, w, h, dwindow, dww, dwh)
    return output

def main():
    print 'executing...'
    im = util.open('in/image1.png')
    openingFile = "out/opening-" + datetime.now().strftime('%Y%m%d%H%M%S') + ".png"
    arr = util.toBytes(im)

    start = time.time()
    arr = grayScale.averaging(arr)
    print 'grayscale : ' + str(time.time() - start)

    start = time.time()
    arr = smoothening.median(arr, im.width, im.height, 2)
    print 'median : ' + str(time.time() - start)

    start = time.time()
    arr = util.uniformedThresholding(arr, im.width, im.height, (125, 125, 125))
    print 'uniformedThresholding : ' + str(time.time() - start)

    start = time.time()
    window = [(0, 0, 0)] * 3 * 3
    opened = opening(arr, im.width, im.height, window, 3, 3, window, 3, 3)
    print 'opening : ' + str(time.time() - start)

    util.save(openingFile, opened, im.mode, im.size)
    print 'done executing...'

if __name__ == "__main__":
    main()
