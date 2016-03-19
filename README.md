##Image Filters##

Practicing basic image processing. Although, the project uses Pillow it does
not rely on the operators that are already included, instead this is an attempt
to implement them.

Pillow is only used to convert a stream of image data to a list of tuples that
contain the RGB bytes (depending on the mode).

###Pre-conditions###
So far, the supported image type is PNG, because different modes/types have
different tuples in Pillow.
