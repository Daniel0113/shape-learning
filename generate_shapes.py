from PIL import Image, ImageDraw, ImageFilter
import random
import os

def create_black_and_white_shape(shape, training_or_testing, shape_id): 
    img = Image.new('L', (24, 24), color = 255)
    draw = ImageDraw.Draw(img)
    folder = '0' 
    if shape == 'rectangle':
        draw.rectangle(xy = [random.randint(2, 12), random.randint(2, 12), random.randint(14, 22), random.randint(16, 22)], fill=128, outline=0, width=1)
    if shape == 'ellipse':
        draw.ellipse(xy = [random.randint(2, 12), random.randint(2, 12), random.randint(14, 22), random.randint(16, 22)], fill=128, outline=0, width=1)
        folder = '1'
    if shape == 'triangle':
        x = random.randint(10, 15)
        y = random.randint(10, 15)
        radius = random.randint(4, 8)
        draw.regular_polygon([x, y, radius], n_sides=3, rotation=0, fill=128, outline=1)
        folder = '2'

    current_directory = os.path.dirname(os.path.realpath(__file__))
    directory = os.path.join(current_directory, 'shapes', training_or_testing, folder, '{0}_{1}.png'.format(shape, shape_id))
    img.save(directory)

def create_shapes(shape, num_shapes, training_or_testing):
    shapes = ['rectangle', 'ellipse', 'triangle']
    for i in range(num_shapes):
        create_black_and_white_shape(shape, training_or_testing, i)

# create_shapes('rectangle', 1000, 'training')
# create_shapes('ellipse', 1000, 'training')
# create_shapes('triangle', 1000, 'training')