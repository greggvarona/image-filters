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
