import ImageUtils as util
from datetime import datetime

def averaging(arr):
    grayed = []
    for p in arr:
        rgba = list(p)
        avg = ((rgba[0] + rgba[1] + rgba[2]) / 3)
        grayed.append(tuple([avg, avg, avg, rgba[3]]))
    return grayed

def luminousity(arr):
    grayed = []
    for p in arr:
        rgba = list(p)
        lum = int(rgba[0] * 0.21) + int(rgba[1] * 0.72) + int(rgba[2] * 0.07)
        grayed.append(tuple([lum, lum, lum, rgba[3]]))
    return grayed

def lightness(arr):
    grayed = []
    for p in arr:
        rgba = list(p)
        avg = (min(rgba[0], rgba[1], rgba[2]) + max(rgba[0], rgba[1], rgba[2])) / 2
        grayed.append(tuple([avg, avg, avg, rgba[3]]))
    return grayed

def main():
    im = util.open('in/captcha.png')
    arr = util.toBytes(im)
    fileAverage = "out/a-" + datetime.now().strftime('%Y%m%d%H%M%S') + ".png"
    fileLuminance = "out/l-" + datetime.now().strftime('%Y%m%d%H%M%S') + ".png"
    fileLightness = "out/li-" + datetime.now().strftime('%Y%m%d%H%M%S') + ".png"
    print("Executing... ")
    averaged = averaging(arr)
    luminous = luminousity(arr)
    lightnessed = lightness(arr)
    util.save(fileAverage, averaged, im.mode, im.size)
    util.save(fileLuminance, luminous, im.mode, im.size)
    util.save(fileLightness, lightnessed, im.mode, im.size)
    print("done saving ")

if __name__ == "__main__":
    main()
