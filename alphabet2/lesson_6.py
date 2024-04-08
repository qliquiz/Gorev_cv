import matplotlib.pyplot as plt 
import numpy as np 
from skimage.measure import label, regionprops
from pathlib import Path 
from collections import defaultdict 


def has_vline(arr, width = 1): 
    return width <= np.sum(arr.mean(0) == 1) 

def extractor(region):
    area = region.area / region.image.size
    cx, cy = region.centroid_local
    cy /= region.image.shape[0]
    cx /= region.image.shape[1]
    eccentricity = region.eccentricity < 0.4 and -1 or region.eccentricity
    perimeter = region.perimeter / region.image.size
    euler = region.euler_number
    vlines = has_vline(region.image, 3)
    return np.array([area, cy, cx, eccentricity, perimeter, euler, vlines])

def distance(p1, p2):
    return ((p1 - p2) ** 2).sum() ** 0.5

def classificator(props, classes):
    klass = None
    min_d = 10 ** 16

    for cls in classes:
        d = distance(props, classes[cls])
        
        if d < min_d:
            min_d = d
            klass = cls

    return klass


image = plt.imread(Path(__file__).parent / "alphabet_small.png").mean(2)
image[image == 1] = 0
image[image > 0] = 1

labeled = label(image)
regions = regionprops(labeled)

classes = {
    "A": extractor(regions[2]),
    "B": extractor(regions[3]),
    "8": extractor(regions[0]),
    "0": extractor(regions[1]),
    "1": extractor(regions[4]),
    "W": extractor(regions[5]),
    "X": extractor(regions[6]),
    "*": extractor(regions[7]),
    "-": extractor(regions[9]),
    "/": extractor(regions[8]),
}

image = plt.imread(Path(__file__).parent / "alphabet.png").mean(2)
image[image > 0] = 1

labeled = label(image)
regions = regionprops(labeled)
result = defaultdict(lambda: 0)

for region in regions:
    result[classificator(extractor(region), classes)] += 1

print(result)

print(np.max(labeled))

plt.imshow(regions[0].image)
plt.show()