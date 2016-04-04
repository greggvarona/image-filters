import ImageUtils as util
import GrayScale as grayScale
import Smoothing as smoothing
from datetime import datetime

def erode(input, w, h):
    return

def dilate(input, w, h):
    return

def main():
    print 'executing...'
    im = util.open('in/inverted-captcha.jpg')
    fileName = "out/o-" + datetime.now().strftime('%Y%m%d%H%M%S') + ".jpg"
    arr = util.toBytes(im)
    arr = grayScale.luminousity(arr)
    arr = util.uniformedThresholding(arr, im.width, im.height, tuple([100,100,100]))
    arr = smoothing.median(arr, im.width, im.height, 1)
    util.save(fileName, arr, im.mode, im.size)
    print 'done executing...'

if __name__ == "__main__":
    main()
