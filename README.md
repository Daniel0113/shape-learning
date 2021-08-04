# shape-learning
This small project is a essentially a "Hello World!" of image-based machine learning, except I went out of my way to generate my own images in bulk for fun. I used `python3.9` for this exercise.

## Quick Setup
### Setting up the environment
In the root directory, create a virtualenv called `.venv` with the following:

`$ python3.9 -m venv .venv`

From there, activate the virtual environment using:

`$ source .venv/bin/activate`

After the environment is activated, the following will install the dependencies needed

`$ pip install -r requirements.txt`

### Generating the images
Let's say we want to create 1000 images to train with, and 200 to test against. We can do the following in IDLE (or however else you might want to do it)

```
>>> from generate_shapes import create_all_shapes
>>> create_all_shapes(1000, 'training')
>>> create_all_shapes(200, 'testing')
```

The code above will 
1. place 1000 rectangle images in `shapes/training/0`,
2. place 1000 ellipse images in `shapes/training/1`,
3. place 1000 triangle images in `shapes/training/2`
4. place 200 rectangle images in `shapes/testing/0`,
5. place 200 ellipse images in `shapes/testing/1`,
6. place 200 triangle images in `shapes/testing/2`

Now that the data is populated, shapes are classified in the program as 
```
rectangle: 0
ellipse: 1
triangle: 2
```

From there, you can run the notebook (`shapes_ml.ipynb`) file using the `jupyter notebook` command at the root directory. You may notice that the accuracy isn't the best. How might this be improved? How much more accurate is the model if using 2000, 3000, or more training images per shape?


## Some notes about the image generation
Currently, the images have the following attributes
1. 24x24 using 8-bit pixels, black and white
2. 1 shape per image, in a random location with random height and width 
3. The shape stays fully inside the image
