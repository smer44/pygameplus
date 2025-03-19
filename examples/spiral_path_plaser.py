def foldl(func, start, iterable):
    for item in iterable:
        yield start
        start = func(start, item)
    yield start

def arange(a,b,s):
    while a < b:
        yield a
        a += s


add = lambda a, b: a + b


def foldl_sum(iterable):
    return [x for x in foldl(add, 0, iterable)]


def binary_search(value, arr):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= value:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return result

class PolygonPathWeightedPlaser:

    def __init__(self, xx, yy):
        self.xx = xx
        self.yy = yy
        self.calculate_all()

    def calculate_all(self):
        dists = self.calculate_distances(self.xx, self.yy)
        ndists = self.normalize_discantes(dists)
        self.ndists = ndists
        self.sums = foldl_sum(ndists)

    def calculate_distances(self, xx, yy):
        assert xx, f"PolygonPathWeightedPlaser : path is empty"
        assert len(xx) == len(yy), f"PolygonPathWeightedPlaser : path length do not match"
        ret = []
        for n in range(len(xx) - 1):
            x0 = xx[n]
            x1 = xx[n + 1]
            y0 = yy[n]
            y1 = yy[n + 1]
            d = ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5
            ret.append(d)
        return ret

    def normalize_discantes(self, dists):
        s = sum(dists)
        return [d / s for d in dists]

    def get_coord(self, value):
        xx = self.xx
        yy = self.yy
        pos = binary_search(value, self.sums)
        value_base = self.sums[pos]
        value_base_next = self.sums[pos + 1]
        x0 = xx[pos]
        y0 = yy[pos]
        x1 = xx[pos + 1]
        y1 = yy[pos + 1]
        value -= value_base
        # normalize by setp size:
        value /= (value_base_next - value_base)
        # interpolate between:
        x = x0 * (1 - value) + x1 * value
        y = y0 * (1 - value) + y1 * value
        return x, y

xx = [0, 300,500,100]
yy = [100, 200, 300, 400]

pop = PolygonPathWeightedPlaser(xx,yy)

coords = [pop.get_coord(value) for value in arange(0,1,0.01)]

for value in arange(0,1,0.01):
    print(pop.get_coord(value))


import pygame
import sys


def visualize_movement(points, width=800, height=600, speed=5):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Point Movement Visualization")

    clock = pygame.time.Clock()
    point_radius = 5  # Small circle radius
    index = 0  # Track current point

    while True:
        screen.fill((0, 0, 0))  # Clear screen with black background

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.draw.lines(screen,(0, 0, 255),False, points)
        if index < len(points):
            px,py = points[index]
            #px *=width
            #py *=height
            pygame.draw.circle(screen, (255, 0, 0), (px, py), point_radius)
            index += 1  # Move to the next point

        pygame.display.flip()
        clock.tick(speed)  # Control speed of movement


visualize_movement(coords)
