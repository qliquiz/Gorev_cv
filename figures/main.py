import numpy as np
from skimage.measure import label
import matplotlib.pyplot as plt


data = np.load('figures/ps.npy.txt')

labeled = label(data)

count_of_struct1 = count_of_struct2 = count_of_struct3 = count_of_struct4 = 0

struct1 = np.array([[1, 1, 1],
                    [1, 0, 1]])

struct2 = np.array([[1, 0, 1],
                    [1, 1, 1]])

struct3 = np.array([[1, 1],
                    [1, 0],
                    [1, 1]])

struct4 = np.array([[1, 1],
                    [0, 1],
                    [1, 1]])

# for label in range(1, labeled.max() + 1):
#     if label == struct1:
#         count_of_struct1 += 1
#     elif label == struct2:
#         count_of_struct2 += 1
#     elif label == struct3:
#         count_of_struct3 += 1
#     elif label == struct4:
#         count_of_struct4 += 1

# print(labeled.max())
# print(count_of_struct1)
# print(count_of_struct2)
# print(count_of_struct3)
# print(count_of_struct4)

print(struct1 in labeled)
plt.imshow(labeled)
plt.show()