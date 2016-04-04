import ImageUtils as util
import GrayScale as grayScale
import Smoothening as smoothening
from datetime import datetime
import math

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
                    if diff <= minimum and diff >= 0:
                        minimum = diff
            output[index] = (minimum, minimum, minimum)
    return output

def dilate(input, w, h):
    return

def main():
    print 'executing...'
    im = util.open('in/captcha.jpg')
    fileName = "out/e-" + datetime.now().strftime('%Y%m%d%H%M%S') + ".jpg"
    arr = util.toBytes(im)
    arr = grayScale.luminousity(arr)
    arr = smoothening.median(arr, im.width, im.height, 2)
    arr = util.uniformedThresholding(arr, im.width, im.height, (100, 100, 100))
    window = [(0, 0, 0)] * 3 * 3
    arr = erode(arr, im.width, im.height, window, 3, 3)
    util.save(fileName, arr, im.mode, im.size)
    print 'done executing...'

if __name__ == "__main__":
    main()
