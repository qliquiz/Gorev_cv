import numpy as np
from skimage.measure import label


def area(LB, label = 1):
    return (LB == label).sum()

data = np.load('./coins.npy.txt')

labeled = label(data)

sum = 0
dictionary = {}

for label in range(1, labeled.max() + 1):
    if area(labeled, label) == 609:
        sum += 10
    elif area(labeled, label) == 69:
        sum += 1
    elif area(labeled, label) == 145:
        sum += 2
    else:
        sum += 5

print(sum)