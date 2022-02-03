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

    # Vectorized
    # new_im.array = image.array * factor + mid

    return new_im

def blur(image, kernel_size):
    # kernel size is the nu,ber of pixels to tske into account when app
    # (ie kerel_size -3 would be neighbors to the left/right, top/bottom)
    # kernel size should always be an *odd* number
    x_pixels, y_pixels, num_channels = image.array.shape
    new_im = Image(x_pixels = x_pixels, y_pixels = y_pixels, num_channels = num_channels)

    neighbor_range = kernel_size // 2 # how many neighbors to one side we need to look at
    
    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                # we are going to use a naive implementation of iterating through each neighbor
                # and summing
                # there is a faster way but this is more strightfoward to understand
                total = 0
                for x_i in range(max(0,x-neighbor_range), min(x_pixels-1, x+neighbor_range) +1):
                    for y_i in range(max(0, y-neighbor_range), min(y_pixels-1, y+neighbor_range) +1):
                        total += image.array[x_i, y_i, c]
                new_im.array[x, y, c] = total / (kernel_size **2) # Average

    return new_im
                     
# note:
# this blur inplemented above is a kernel of size n, where each value is 1/n!
# for example, k=3 would be thid kernel:
# [1/3   1/3 1/3]
# [1/3   1/3 1/3]
# [1/3   1/3 1/3]

def aplpy_kernel(image, kernel):
    # the kernel should be a numpy 2D array  that represents the kernel we'll use!
    # for the sake of simplicity of this implemnentatino, let us assume the Kenel is square
    # for example the sobel x kernel (detecting horizontal edges) is as follows:
    # [1 0 -1]
    # [2 0 -2]
    # [1 0 -1]
    x_pixels, y_pixels, num_channels = image.array.shape
    new_im = Image(x_pixels = x_pixels, y_pixels = y_pixels, num_channels = num_channels)

    kernel_size = kernel.shape[0]
    neighbor_range = kernel_size // 2 # how many neighbors to one side we need to look at
    
    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                total = 0
                for x_i in range(max(0,x-neighbor_range), min(x_pixels-1, x+neighbor_range) +1):
                    for y_i in range(max(0, y-neighbor_range), min(y_pixels-1, y+neighbor_range) +1):
                        #  we need to find which value of the kernel this corresponds to
                        x_k = x_i + neighbor_range - x
                        y_k = y_i + neighbor_range - y
                        kernel_val = kernel[x_k, y_k]
                        total += image.array[x_i, y_i, c] * kernel_val
                new_im.array[x, y, c] = total
    
    return new_im


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

    # darken
    # darkened_im = adjust_brightness(lake, 0.3)
    # darkened_im.write_image('darkened2.png')

    # adjust the contrast for the lake
    # incr_contrast = adjust_contrast(lake, 2, 0.5)
    # incr_contrast.write_image('increased_contrast.png')

    # decreasing the contrast of the lake
    # decr_contrast = adjust_contrast(lake, 0.5   , 0.5)
    # decr_contrast.write.image('decreased_contrast.png')

    # blur with Kernel 3
    # blur_3 = blur(city, 3)
    # blur_3.write_image('blur_k3.png')

    # # blur with Kernel 15
    # blur_15 = blur(city, 15)
    # blur_15.write_image('blur_k15.png')

    # let's apply a sobel edge detection kernel on the x and y axis
    sobel_x_kernel = np.array([
        [1, 2, 1],
        [0, 0, 0]
        [-1, -2, -1], 
    ])
    sobel_y_kernel = np.array([
        [1, 0, -1],
        [2, 0, -2],
        [1, 0, -1]
    ])

sobel_x = aplpy_kernel(city, sobel_x_kernel)
sobel_x.write_image('edge_x.png')
sobel_y = aplpy_kernel(city, sobel_y_kernel)
sobel_y.write_image('edge_y.png')