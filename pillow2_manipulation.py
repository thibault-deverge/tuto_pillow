from PIL import Image, ImageColor

# image import
image = Image.open('animal.jpeg')

# rotate
red = ImageColor.getcolor('red', 'RGB')
image_rotate = image.rotate(60, expand=True, fillcolor=red)

# crop (left-top-right-bottom)
image_crop = image.crop((0, 0, 500, 400))

# flipping the image / transpose the image
image_flip_horizontal = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
image_flip_vertical = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
image_transpose = image.transpose(Image.Transpose.TRANSPOSE)
# others options: ROTATE_90/180/270, TRANSPOSE, TRANSVERSE

# resize
image_resized = image.resize((600, 1000))  # bad exemple
# better example
scale_factor = 2
new_image_size = (image.size[0] * scale_factor, image.size[1] * scale_factor)
image_resized_better = image.resize(new_image_size)

# display
image_flip_horizontal.show()
