from PIL import Image, ImageEnhance

# image import
image = Image.open("animal.jpeg")

# create an enhancer
color_enhancer = ImageEnhance.Color(image)  # vibrance
contrast_enhancer = ImageEnhance.Contrast(image)
brightness_enhancer = ImageEnhance.Brightness(image)
sharpness_enhancer = ImageEnhance.Sharpness(image)

# applying the enhancer and show
enhanced_image = sharpness_enhancer.enhance(5)
enhanced_image.show()
