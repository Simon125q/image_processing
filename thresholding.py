from PIL import Image

image = Image.open("yoda.jpeg")
grayscale_image = image.convert("L")
grayscale_image.show()

single_threshold_copy = grayscale_image.copy()
double_threshold_copy = grayscale_image.copy()

def single_thresholding(image):
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            pixel_value = image.getpixel((x, y))
            if pixel_value > 127:
                image.putpixel((x, y), 255)
            else:
                image.putpixel((x, y), 0)
    return image

single_threshold_image = single_thresholding(single_threshold_copy)
single_threshold_image.show()
single_threshold_image.save("single_thresholding.jpeg")

def double_thresholding(image):
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            pixel_value = image.getpixel((x, y))
            if pixel_value > 160:
                image.putpixel((x, y), 255)
            elif pixel_value > 80:
                image.putpixel((x, y), 0)
            else:
                image.putpixel((x, y), 255)
    return image

double_threshold_image = double_thresholding(double_threshold_copy)
double_threshold_image.show()
double_threshold_image.save("double_thresholding.jpeg")
