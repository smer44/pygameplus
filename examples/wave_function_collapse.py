import random

import pygame
import numpy as np
import ctypes
ctypes.windll.user32.SetProcessDPIAware()
# activate the pygame library .
pygame.init()
X = 2752
Y = 1152

# create the display surface object
# of specific dimension..e(X, Y).
scrn = pygame.display.set_mode((X, Y))

# set the pygame window name
pygame.display.set_caption('image')

# create a surface object, image is drawn on it.
raw = pygame.image.load(r"samples\Cat.png").convert()
imp = pygame.transform.scale2x(raw)
imp = pygame.transform.scale2x(imp)
imp = pygame.transform.scale2x(imp)
imp = pygame.transform.scale2x(imp)
arr = pygame.surfarray.array3d(raw)


def to_tiles(arr):
    pad = (1, 1), (1, 1), (0, 0)
    arr = np.pad(arr, pad, mode='constant', constant_values=0)
    res_dim = lambda x, d: ((x - d + 1) * d)
    res_shape = res_dim(arr.shape[0], 3), res_dim(arr.shape[1], 3), 3
    res_array = np.zeros(res_shape, dtype=arr.dtype)
    res_array[-1,:,:] = (255,0,0)
    res_array[:,-1,:] = (255,0,0)

    for x in range(0,len(arr)-2):
        rx = x * 3
        for y in range(0,len(arr[x])-2):
            ry = y*3
            #print(f"{rx=} , {ry=} ,{x=}, {y=}")
            res_array[rx:rx+3,ry:ry+3] = arr[x:x+3,y:y+3]
    return res_array


def tiles_to_map(arr):
    ret = dict()
    for x in range(0,len(arr)-2-3,3):
        for y in range(0,len(arr[x])-2-3,3):
            tile = arr[x:x+3,y+1:y+3].reshape(-1)
            tile = tuple(tile)
            right_tile = arr[x+3:x+6,y+5:y+6].reshape(-1)
            right_tile = tuple(right_tile)
            row = ret.setdefault(tile, dict())
            counts = row.get(right_tile, 0)
            row[right_tile] = counts + 1
    return ret
#print(__name__)
from random import choice
def random_fill(tiles,array):
    misses = 0
    for x in range(0,len(array)-2,3):
        tile, row = random.choice(list(tiles.items()))

        array[x:x + 3, 1:3] = np.array(tile).reshape(3,2,3)
        for y in range(3,len(array[x])-1):
            last_key = array[x:x+3,y-2:y]
            last_key = tuple(last_key.reshape(-1))
            row = tiles.get(last_key,None)
            if row:
            #select random item from row is it actually:
                next_key, count = random.choice(list(row.items()))

                next_key = np.array(next_key).reshape(3,1,3)
                array[x:x+3, y:y+1]  = next_key
            else:
                misses += 1


    print(f"{misses=}")


tile_array = to_tiles(arr)
tiles = tiles_to_map(tile_array)

#print(list(tiles.items())[0])

res_shape = arr.shape[0]*10, arr.shape[1]*10,3
result_array = np.zeros(res_shape, dtype = arr.dtype)

random_fill(tiles,result_array)


res_surf = pygame.surfarray.make_surface(result_array)
res_surf = pygame.transform.scale2x(res_surf)
res_surf = pygame.transform.scale2x(res_surf)
#res_surf = pygame.transform.scale2x(res_surf)
#.time.delay(1)

scrn.blit(res_surf, (0, 0))
#scrn.blit(imp, (300, 0))

pygame.display.flip()
status = True
while (status):

    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for i in pygame.event.get():

        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if i.type == pygame.QUIT:
            status = False

# deactivates the pygame library
pygame.quit()