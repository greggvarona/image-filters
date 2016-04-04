import ImageUtils as util
from datetime import datetime

def averaging(arr):
    grayed = []
    for p in arr:
        rgb = list(p)
        avg = ((rgb[0] + rgb[1] + rgb[2]) / 3)
        grayed.append(tuple([avg, avg, avg]))
    return grayed

def luminousity(arr):
    grayed = []
    for p in arr:
        rgb = list(p)
        lum = int(rgb[0] * 0.21) + int(rgb[1] * 0.72) + int(rgb[2] * 0.07)
        grayed.append(tuple([lum, lum, lum]))
    return grayed

def lightness(arr):
    grayed = []
    for p in arr:
        rgb = list(p)
        avg = (min(rgb[0], rgb[1], rgb[2]) + max(rgb[0], rgb[1], rgb[2])) / 2
        grayed.append(tuple([avg, avg, avg]))
    return grayed

def main():
    im = util.open('in/captcha.jpg')
    arr = util.toBytes(im)
    fileAverage = "out/a-" + datetime.now().strftime('%Y%m%d%H%M%S') + ".jpg"
    fileLuminance = "out/l-" + datetime.now().strftime('%Y%m%d%H%M%S') + ".jpg"
    fileLightness = "out/li-" + datetime.now().strftime('%Y%m%d%H%M%S') + ".jpg"
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
