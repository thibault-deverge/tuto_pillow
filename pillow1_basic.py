from PIL import Image

# create new image by import
image = Image.open('animal.jpeg')

# alternative way to import a image
# with Image.open('animal.jpeg'):
#     image.show()

# creating image from scratch
image_blank = Image.new('RGBA', (1000, 600))

# show the picture
# image.show()

# saving the picture
# image.save('test_save.png')

# image information
print(image.size)
print(image.filename)
print(image.format)
print(image.format_description)
