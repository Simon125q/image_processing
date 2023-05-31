from PIL import Image
import operator
import time

def calculate_summed_table(image):
    width, height = image.size
    summed_table = [[(0, 0, 0)] * width for _ in range(height)]
    summed_table[0][0] = image.getpixel((0, 0))
    
    for x in range(1, width):
        summed_table[0][x] = tuple(map(operator.add, image.getpixel((x, 0)), summed_table[0][x - 1]))
    
    for y in range(1, height):
        summed_table[y][0] = tuple(map(operator.add, image.getpixel((0, y)), summed_table[y - 1][0]))
    
    for x in range(1, width - 1):
        for y in range(1, height - 1):
            summed_table[y][x] = tuple(map(operator.sub, 
                                           tuple(map(operator.add, 
                                                     tuple(map(operator.add, image.getpixel((x, y)), summed_table[y - 1][x])), 
                                                     summed_table[y][x - 1])), 
                                           summed_table[y - 1][x - 1]))
    return summed_table

def apply_box_blur():
    radius = 35
    image = Image.open("road.jpg").convert('RGB')
    new_image = image.copy()
    width, height = image.size
    area = (2 * radius + 1) ** 2
    summed_table = calculate_summed_table(image)
    
    for x in range(radius + 1, width - radius - 1):
        print(x)
        for y in range(radius + 1, height - radius - 1):
            sum_pixels = tuple(map(operator.add,
                                   tuple(map(operator.sub, 
                                             tuple(map(operator.sub, summed_table[y + radius][x + radius], summed_table[y + radius][x - radius - 1])), 
                                             summed_table[y - radius - 1][x + radius])), 
                                   summed_table[y - radius - 1][x - radius - 1]))
            new_image.putpixel((x, y), tuple(map(operator.floordiv, sum_pixels, (area, area, area))))
    
    return new_image

start_time = time.time()
output_image = apply_box_blur()
output_image.save("blurred_road.jpg")
output_image.show()
end_time = time.time()
execution_time = end_time - start_time
print("Execution Time:", execution_time)
