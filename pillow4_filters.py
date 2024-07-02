from PIL import Image, ImageFilter

# image import
image = Image.open('animal.jpeg')

# basic filter (and much more which work the same)
image_blur = image.filter(ImageFilter.BLUR)
image_contour = image.filter(ImageFilter.CONTOUR)
image_detail = image.filter(ImageFilter.DETAIL)

# rank filters
image_filtered_min = image.filter(ImageFilter.MinFilter(size=5))
image_filtered_median = image.filter(ImageFilter.MedianFilter(size=5))
image_filtered_max = image.filter(ImageFilter.MaxFilter(size=5))

# multiband filters
image_boxblur = image.filter(ImageFilter.BoxBlur(radius=4))
image_gaussblur = image.filter(ImageFilter.GaussianBlur(radius=4))
image_unsharp = image.filter(ImageFilter.UnsharpMask(radius=4))

# Because all these filter return an image, we can use this one
# to combine it with another filter to create differents effects
image_emboss = image.filter(ImageFilter.EMBOSS)
image_emboss_blur = image_emboss.filter(ImageFilter.GaussianBlur(radius=2))

# display
image_emboss_blur.show()
