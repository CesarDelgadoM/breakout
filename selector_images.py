import random

images = {
    1:"sprites/brick_red.png",
    2:"sprites/brick_blue.png",
    3:"sprites/brick_green.png",
    4:"sprites/brick_yellow.png",
    8:"sprites/brick_red.png",
    7:"sprites/brick_blue.png",
    6:"sprites/brick_green.png",
    5:"sprites/brick_yellow.png",
    9:"sprites/brick_pink.png",
}

def select_image():
    i = random.randint(1, 9)
    return images[i]
