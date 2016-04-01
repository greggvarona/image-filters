import operator
from operator import itemgetter
import ImageUtils as util
from datetime import datetime

def median2(input, w, h, ww, wh):
    output = []
    window = [util.downSignal() for el in range(ww * wh)]
    for row in range(h):
        for col in range(w):
            origin = row * w + col
            for windowY in range(wh):
                for windowX in range(ww):
                    y = row + windowY - (wh/2)
                    x = col + windowX - (ww/2)
                    # The following nested conditions makes sure that the
                    # kernel's origin doesn't go out of the image's boundaries.
                    if(x >= 0 and y >= 0):
                        if(x < w and y < h):
                            index = y * w + x
                            wIndex = windowY * ww + windowX
                            window[wIndex] = input[index]
            window = sorted(window, key=itemgetter(0, 1, 2))
            if (util.isEdge(origin, w, h)):
                window = handleEdge(window)
            output.append(window[len(window) / 2])
    return output

def median(input, w, h, radius):
    output = []
    ww = (radius * 2) + 1
    wh = ww
    return median2(input, w, h, ww, wh)

def handleEdge(window):
    output = []
    output = sorted(window, key=itemgetter(0, 1, 2))
    idx = 0
    #print output
    while output[idx] == util.downSignal():
        output[idx] = output[len(output) - 1 - idx]
        idx = idx + 1
    output = sorted(output, key=itemgetter(0, 1, 2))
    return output

def main():
    im = util.open('in/captcha.png')
    arr = util.toBytes(im)
    out = []
    fileMedian = "out/m-" + datetime.now().strftime('%Y%m%d%H%M%S') + ".png"
    print("Executing... ")
    out = median(arr, im.width, im.height, 1)
    util.save(fileMedian, out, im.mode, im.size)
    print("done saving ")

if __name__ == "__main__":
    main()
