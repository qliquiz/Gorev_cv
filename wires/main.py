from skimage.measure import label
from skimage.morphology import binary_closing, binary_dilation, binary_opening, binary_erosion
import matplotlib.pyplot as plt
import numpy as np


struct = np.ones((3, 3))

def erosion(arr, struct = struct):
    result = np.zeros_like(arr)
    for i in range(1, arr.shape[0] - 1):
        for j in range(1, arr.shape[1] - 1):
            sub = arr[i-1:i+2, j-1:j+2]
            if np.all(sub == struct):
                result[i, j] = 1
    return result

# Задача 1
""" data = np.load('wires/wires1.npy.txt')
plt.figure()
plt.imshow(data)
labeled = label(erosion(data))
count = 0
for label in range(1, labeled.max() + 1):
    plt.figure()
    plt.imshow(labeled == label)
    count += 1
print('Всего проводов', count)
plt.show() """

# Задача 2
""" data = np.load('wires/wires2.npy.txt')
plt.figure()
plt.imshow(data)
labeled = label(erosion(data))
count = 0
for label in range(1, labeled.max() + 1):
    plt.figure()
    plt.imshow(labeled == label)
    count += 1
print('Всего проводов', count)
plt.show() """

# Задача 3
""" data = np.load('wires/wires3.npy.txt')
plt.figure()
plt.imshow(data)
labeled = label(erosion(data))
count = 0
for label in range(1, labeled.max() + 1):
    plt.figure()
    plt.imshow(labeled == label)
    count += 1
print('Всего проводов:', count)
plt.show() """

# Задача 4
""" data = np.load('wires/wires4.npy.txt')
plt.figure()
plt.imshow(data)
labeled = label(erosion(data))
count = 0
for label in range(1, labeled.max() + 1):
    plt.figure()
    plt.imshow(labeled == label)
    count += 1
print('Всего проводов:', count)
plt.show() """

# Задача 5
""" data = np.load('wires/wires5.npy.txt')
plt.figure()
plt.imshow(data)
labeled = label(erosion(data))
count = 0
for label in range(1, labeled.max() + 1):
    plt.figure()
    plt.imshow(labeled == label)
    count += 1
print('Всего проводов:', count)
plt.show() """

# Задача 6
""" data = np.load('wires/wires6.npy.txt')
plt.figure()
plt.imshow(data)
labeled = label(erosion(data))
count = 0
for label in range(1, labeled.max() + 1):
    plt.figure()
    plt.imshow(labeled == label)
    count += 1
print('Всего проводов:', count)
plt.show() """