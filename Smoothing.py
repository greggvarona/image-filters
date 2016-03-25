import operator
from operator import itemgetter
import ImageUtils as util
from datetime import datetime

def median(input, w, h, window, ww, wh):
    output = []
    for row in range(h):
        for col in range(w):
            #origin = row * w + col
            window = [(0,0,0), (0,0,0), (0,0,0)] * 3
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
            #print "window: " + str(row) + " " + str(col) + str(window[len(sorted(window, key=itemgetter(0, 1, 2))) / 2])
            #print sorted(window, key=itemgetter(0, 1, 2))
            output.append(window[len(sorted(window, key=itemgetter(0, 1, 2))) / 2])
            #output.append(tuple([clampRGBValue(r), clampRGBValue(g), clampRGBValue(b), clampRGBValue(a)]))
    return output

def main():
    im = util.open('in/very-small.png')
    arr = util.toBytes(im)
    window = [(0,0,0), (0,0,0), (0,0,0)] * 3
    out = []
    fileMedian = "out/m-" + datetime.now().strftime('%Y%m%d%H%M%S') + ".png"
    print("Executing... ")
    print("input ")
    #print arr
    out = median(arr, im.width, im.height, window, 3, 3)
    util.save(fileMedian, out, im.mode, im.size)
    print("out ")
    #print out
    print("done saving ")

if __name__ == "__main__":
    main()
