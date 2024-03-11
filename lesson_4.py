from skimage.measure import label
from skimage.morphology import binary_closing, binary_dilation, binary_opening, binary_erosion
import matplotlib.pyplot as plt
import numpy as np 


def area(LB, label=1):
    return np.sum(LB==label)

def centroid(LB, label=1):
    rows, cols = np.where(LB == label)
    cy = np.mean(rows)
    cx = np.mean(cols)
    return cy, cx

def neighbours4(y, x):
    return (y, x-1), (y-1, x), (y, x+1), (y+1,x)

def neighboursX(y, x):
    return (y-1, x-1), (y-1, x+1), (y+1, x+1), (y+1, x-1)

def neighbours8(y, x):
    return neighbours4(y, x) + neighboursX(y, x)

def get_bounds(LB, label=1, connectivity=neighbours4):
    pos = np.where(LB == label)
    bounds = []
    for y, x in zip(*pos):
        for yn, xn in connectivity(y, x):
            if yn < 0 or yn > LB.shape[0] - 1:
                bounds.append((y, x))
                break
            elif xn < 0 or xn > LB.shape[1] - 1:
                bounds.append((y, x))
                break
            elif LB[yn, xn] == 0:
                bounds.append((y, x))
                break

    return bounds

def perimeter(LB, label, connectivity=neighbours4):
    return len(get_bounds(LB, label, connectivity=neighbours4))

def draw_bounds(LB, bounds):
    result = LB.copy()
    for y, x in bounds:
        result[y, x] += 1
    return result

def distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

def circularity(LB, label = 1):
    return perimeter(LB, label) ** 2 / area(LB, label)

def radiale_distance(LB, label = 1):
    cy, cx = centroid(LB, label)
    bounds = get_bounds(LB, label)
    k = len(bounds)
    rd = 0
    for by, bx in bounds:
      rd += distance((cy, cx), (by, bx))
    return rd / k

def std_radial(LB, label = 1):
    cy, cx = centroid(LB, label)
    bounds = get_bounds(LB, label)
    k = len(bounds)
    rd = radiale_distance(LB, label)
    sr = 0
    for by, bx in bounds:
      sr += ((distance((cy, cx), (by, bx)) - rd) ** 2)
    return (sr / k) ** 0.5

def std_circularity(LB, label = 1):
    return radiale_distance(LB, label) / std_radial(LB, label)
    
LB = np.zeros((16, 16))
LB[4:, :4] = 2

LB[3:10, 8:] = 1
LB[[3, 4, 3],[8, 8, 9]] = 0
LB[[8, 9, 9],[8, 8, 9]] = 0
LB[[3, 4, 3],[-2, -1, -1]] = 0
LB[[9, 8, 9],[-2, -1, -1]] = 0

LB[12:-1, 6:9] = 3


for lbl in range(1, int(np.max(LB))+1):
    print(f'area = {area(LB, lbl)}')
    cy, cx = centroid(LB, lbl)
    print(f'circularity = {std_circularity(LB, lbl)}')
    plt.scatter([cx], [cy])
    print(f'perimeter = {perimeter(LB, lbl)}')
    # draw_perimetr(LB, lbl, get_bounds(LB, lbl))

plt.imshow(LB)
plt.show()