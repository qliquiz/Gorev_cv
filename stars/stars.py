from skimage.measure import label
from skimage.morphology import binary_closing, binary_dilation, binary_opening, binary_erosion
import matplotlib.pyplot as plt
import numpy as np

data = np.load('stars/stars.npy')

labeled = label(data)
start_struct = np.array([[1, 0, 0, 0, 1],
                        [0, 1, 0, 1, 0],
                        [0, 0, 1, 0, 0],
                        [0, 1, 0, 1, 0],
                        [1, 0, 0, 0, 1]])

start_struct2 = np.array([[0, 0, 1, 0, 0],
                        [0, 0, 1, 0, 0],
                        [1, 1, 1, 1, 1],
                        [0, 0, 1, 0, 0],
                        [0, 0, 1, 0, 0]])

erosed = binary_erosion(data, start_struct)

labeled_erosed = label(erosed)

print(labeled_erosed.max())

erosed = binary_erosion(data, start_struct2)

labeled_erosed = label(erosed)

print(labeled_erosed.max())