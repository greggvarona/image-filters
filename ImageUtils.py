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
                    if(x >= 0 && y >= 0):
                        if(x < w && y < h):
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
