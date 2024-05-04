import cv2
from skimage.draw import disk
import numpy as np
import matplotlib.pyplot as plt
import time
from itertools import chain


def euclidean(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def find_local_max(arr, neighborhood_size=3):
    maxima = []
    h, w = arr.shape
    offset = neighborhood_size // 2

    for y in range(offset, h - offset):
        for x in range(offset, w - offset):
            neighborhood = arr[y-offset:y+offset+1, x-offset:x+offset+1]
            if np.all(arr[y, x] >= neighborhood):
                maxima.append((y, x))
    return maxima


image = np.zeros((100, 100))
# image[30:50, 30:50] = 1

rr, cc = disk((35, 35), 20)
image[rr, cc] = 1
rr, cc = disk((65, 65), 25)
image[rr, cc] = 1

t = time.perf_counter()
pos = np.where(image == 1)
distance_map = np.zeros_like(image)


for y, x in zip(*pos):
    step = 1
    min_d = 10 ** 19
    while True:
        size = 2 * step + 1
        top = [y - step] * size, list(range(x - step, x + step + 1))
        bottom = [y + step] * size, list(range(x - step, x + step + 1))
        left = list(range(y - step + 1, y + step)), [x - step] * size
        right = list(range(y - step + 1, y + step)), [x + step] * size
        for ny, nx in zip(chain(top[0], bottom[0], left[0], right[0]),
                        chain(top[1], bottom[1], left[1], right[1])):
            if image[ny, nx] == 0:
                d = euclidean(y, x, ny, nx)
                if d < min_d:
                    min_d = d
        if min_d != 10 ** 19:
            distance_map[y, x] = min_d
            break
        step += 1


maxima = find_local_max(distance_map, neighborhood_size=6)

# Отобразить результаты
for y, x in maxima:
    cv2.circle(distance_map, (x, y), 3, (255, 0, 0), -1)


print(f'Elpased {time.perf_counter() - t}')


plt.imshow(maxima)
plt.imshow(distance_map)
plt.show()