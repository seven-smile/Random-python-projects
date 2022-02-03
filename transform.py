from image import Image
import numpy as np

def adjust_brightness(image, factor):
    # when we adjust the brightnes, we just to scale each value by theh same amount
    # factor is a value > 8, how much you want to brighten the image by
    # ( < 1 = darken, > 1 = brighten)
    x_pixels, y_pixels, num_channels = image.array.shape # get x, y pixels of images,  # channels
    # make an empty image so we don't actually modify the original one
    new_im = Image(x_pixels = x_pixels, y_pixels=y_pixels, num_channels = num_channels)

    # This is the most initiative way to do this(non-vectorized)
    # for x in range(x_pixels):
    #     for y in range(y_pixels):
    #         for c in range(num_channels):
    #             new_im.array[x, y, c] = image.array[x, y, c] * factor

    # Vectorized Version
    new_im.array = image.array * factor 

    return new_im

def adjust_contrast(image, factor, mid = 0.5):
    # adjust the contrast by increasing the diffrence from the user-defined.
    # Midpoint by some amount, factor
    x_pixels, y_pixels, num_channels = image.array.shape
    new_im = Image(x_pixels = x_pixels, y_pixels = y_pixels, num_channels = num_channels)

    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                new_im.array[x, y, c] = (image.array[x, y, c] - mid) * factor + mid

# 
def blur(image, kernel_size):
    # kernel size is the nu,ber of pixels to tske into account when app
    # (ie kerel_size -3 would be neighbors to the left/right, top/bottom)
    # kernel size should always be an *odd* number
    pass

def aplpy_kernel(image, kernel):
    # the kernel should be a 2D array  that represents the kernel we'll use!
    # for the sake of simplicity of this implemnentatino, let us assume the Kenel is square
    # for example the sobel x kernel (detecting horizontal edges) is as follows:
    # [1 0 -1]
    # [2 0 -2]
    # [1 0 -1]
    pass

def combine_images(image1, image2):
    # let's combine two images using the squared sum of squares: value = sqrt(value_1+=2, value)
    # size of image1, and image2 Must be the Same
    pass

if __name__ == ' __main__':
    lake = Image(filename = 'lake.png')
    city = Image(filename = 'city.png')

    # let's lighten the lake
    # Brightened_im = adjsut_brightness(lake, 1.7)
    # brightened_im.write_image('brightened.png)

    #darken
    darkened_im = adjust_brightness(lake, 0.3)
    darkened_im.write_image('darkened2.png')