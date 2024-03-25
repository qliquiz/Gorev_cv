import matplotlib.pyplot as plt
from skimage.measure import label, regionprops
import numpy as np
from collections import defaultdict
from pathlib import Path


def filling_factor(arr):
    return np.sum(arr) / arr.size

def count_holes(arr):
    labeled = label(np.logical_not(arr))
    regions = regionprops(labeled)
    holes = 0
    for region in regions:
        coords = np.where(labeled == region.label)
        bound = 1
        for y, x in zip(*coords):
            if y == 0 or x == 0 or y == arr.shape[0] - 1 or x == arr.shape[1] - 1:
                bound = 0
        holes += bound
    return holes


def have_vline(arr, width=1):
    return width <= np.sum(arr.mean(0) == 1)


def recognize(region):
    if filling_factor(region.image) == 1.0:
        return '-'
    else:
        holes = count_holes(region.image)
        if holes == 2:
            if have_vline(region.image, 3):
                return "B"
            else:
                return "8"
        elif holes == 1:
            ny, nx = (region.centroid_local[0]/region.image.shape[0],region.centroid_local[1]/region.image.shape[1])
            eccentricity = region.eccentricity    
            if have_vline(region.image, 3): 
                if np.isclose(ny, nx, 0.089): 
                    return "P" 
                else: 
                    return "D" 
            if np.isclose(ny, nx, 0.05): 
                return "0" 
            else: 
                return "A"
        else:
            if have_vline(region.image):
                return '1'
            else:
                eccentricity = region.eccentricity

                framed = region.image.copy()
                framed[0, :] = 1
                framed[-1, :] = 1
                framed[:, 0] = 1
                framed[:, -1] = 1
                holes = count_holes(framed)
                if eccentricity < 0.4:
                    return '*'
                else:
                    match holes:
                        case 2: return '/'
                        case 4: return 'X'
                        case 5: return 'W'
                        case _: return '+'
    return '_'


image = plt.imread('symbols.png').mean(2)
image[image > 0] = 1
regions = regionprops(label(image))

result = defaultdict(lambda:0)

path = Path('.') / 'result'
path.mkdir(exist_ok=True)

plt.figure()
for i, region in enumerate(regions):
    symbol = recognize(region)
    if symbol == 'P' or symbol == 'D' or symbol == 'A' or symbol == '0':
        plt.clf()
        plt.title(f'{symbol=}')
        plt.imshow(region.image)
        plt.tight_layout()
        plt.savefig(path / f'{i}.png')
    result[symbol] += 1

for region in regions:
    symbol = recognize(region)
    result[symbol] += 1

print(result)
# plt.title(len(regions))
# plt.imshow(regions[198].image)
# plt.show()