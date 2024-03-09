import numpy as np
import matplotlib.pyplot as plt
from scipy.datasets import face


""" def translate(B, vector):
    translated = np.zeros_like(image)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            ni = i - vector[0]
            nj = j - vector[1]
            if ni < 0 or nj < 0:
                continue
            if ni >= image.shape[0] or nj >= image.shape[1]:
                continue
            translated[ni, nj] = image[i, j]
    return translated

image = face(False)

result = translate(image, (-100, -200))

plt.imshow(result)
plt.show() """


arr = np.array([[0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,1,1,1,1,1,1,1,0,0],
                [0,0,0,0,1,1,1,1,0,0],
                [0,0,0,0,1,1,1,1,0,0],
                [0,0,0,1,1,1,1,1,0,0],
                [0,0,0,0,1,1,1,1,0,0],
                [0,0,0,1,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0]])

struct = np.ones((3, 3))

def dilation(arr, struct = struct):
    result = np.zeros_like(arr)
    for i in range(1, arr.shape[0] - 1):
        for j in range(1, arr.shape[1] - 1):
            rsub = np.logical_and(arr[i, j], struct)
            result[i-1:i+2, j-1:j+2] = np.logical_or(result[i-1:i+2, j-1:j+2], rsub)
    return result

def erosion(arr, struct = struct):
    result = np.zeros_like(arr)
    for i in range(1, arr.shape[0] - 1):
        for j in range(1, arr.shape[1] - 1):
            sub = arr[i-1:i+2, j-1:j+2]
            if np.all(sub == struct):
                result[i, j] = 1
    return result

def closing(arr, struct = struct):
    return dilation(erosion(arr, struct), struct)

def opening(arr, struct = struct):
    return erosion(dilation(arr, struct), struct)

plt.imshow(erosion(arr))
plt.show()