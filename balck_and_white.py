from PIL import Image
import numpy as np
import math

def find_minimum(current_value, new_value):
    if new_value < current_value:
        return new_value
    else:
        return current_value

def histogram_equalization(image):
    image_array = np.asarray(image)
    image_width = image.size[0]
    image_height = image.size[1]
    total_pixels = image_width * image_height
    histogram = np.zeros(256)
    new_pixel_values = np.zeros(256)
    output_image = np.zeros((image_height, image_width, 3))
    sum_of_pixels = 0
    flattened_image_array = np.ndarray.flatten(image_array)
    pixel_occurrences = np.bincount(flattened_image_array) / 3

    smallest_occurrence = pixel_occurrences[0]
    for i in range(255):
        smallest_occurrence = find_minimum(smallest_occurrence, pixel_occurrences[i])

    for intensity in range(255):
        histogram[intensity] = pixel_occurrences[intensity] + sum_of_pixels
        sum_of_pixels += pixel_occurrences[intensity]
        new_pixel_values[intensity] = math.ceil((histogram[intensity] - smallest_occurrence) / (
                total_pixels - smallest_occurrence) * 255)

    for x in range(image_height):
        for y in range(image_width):
            pixel_intensity = image_array[x][y][0]
            for z in range(3):
                output_image[x][y][z] = new_pixel_values[pixel_intensity]

    image_after_equalization = Image.fromarray(output_image.astype(np.uint8))
    image_after_equalization.save("image_after_equalization.png")
    image_after_equalization.show()

image = Image.open('grayscale_yoda.jpeg')
histogram_equalization(image)
