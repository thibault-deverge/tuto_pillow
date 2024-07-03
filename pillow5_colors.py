from PIL import Image, ImageFilter
from numpy import array

# image import
image = Image.open('animal.jpeg')

#################################
# Analysing picture information #
#################################

# numpy
# print(array(image).shape)
# print(array(image.getchannel('R')))

# colors only
# print(image.getpixel((0, 0)))
# print(image.getcolors(maxcolors= image.size[0] * image.size[1]))

# getting picture information
# print(image.mode)
# print(image.getbands())

# channels
# red_channel = (image.getchannel('R'))
# red_channel.show()

#################################
####### Color conversions #######
#################################

# 1 bit grayscale image
image_grayscale_1bit = image.convert('1')

# 8 bit grayscale image
grayscale_l = image.convert('L')

# Palette (256 colors only - 1 byte per color)
palette = image.convert('P')
palette_16 = image.convert('P', palette=Image.Palette.ADAPTIVE, colors=16)

################################
### Change Individual pixels ###
################################

image.putpixel((0, 0), (255, 0, 0))

# Replace all pixel of a certains colors
for x in range(image.size[0]):
    for y in range(image.size[1]):
        if image.getpixel((x, y))[0] > 200:
            image.putpixel((x, y), (0, 0, 0))

image.show()