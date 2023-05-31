from PIL import Image

RED_WEIGHT = 0.2126
GREEN_WEIGHT = 0.7152
BLUE_WEIGHT = 0.0722

# open image and convert it to TGB mode
original_image  = Image.open('yoda.jpeg')
grayscale_image = original_image.convert('RGB')

# get data about pixels to pixel_table and get image dimensions
pixel_table = grayscale_image.load()
width, height = grayscale_image.size

# iterate through each pixel and convert it to grayscale
for y in range(height):
    for x in range(width):
        red, green, blue = pixel_table[x, y]
        grayscale_value = int(0.2126*red + 0.7152*green + 0.0722*blue)
        pixel_table[x, y] = (grayscale_value, grayscale_value, grayscale_value)

grayscale_image.save("grayscale_yoda.jpeg")
grayscale_image.show()