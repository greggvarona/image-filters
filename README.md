## Image Filters ##

This project showcases basic implementations of filters/operators used in image processing.

The project uses Pillow, only to convert a stream of image data to a list of tuples that
contain the RGB bytes (depending on the mode). To install pillow using pip run:
```
  python -m pip install pillow
```

### Supported File Types ###
The supported image type is PNG, because it doesn't use lossy compression like JPEG does. This means that the quality of the image is unaffected when saving. Other formats have not yet been explored.
