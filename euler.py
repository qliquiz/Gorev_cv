import numpy as np
from skimage.measure import label


image = np.load("./holes.npy")

labeled = label(image)

crooss_masks = np.array([
    [[0,0], [0,1]],
    [[0,1], [1,1]],])

def match(a, mask):
    if np.all(a == mask):
        return True
    return False

def euler(B, masks):
    X = 0
    V = 0
    for y in range(0, B.shape[0]-1):
        for x in range(0, B.shape[1]-1):
            sub= B[y:y+2, x:x+2]
            
            if match(sub, masks[0]):
                X+=1
            if match(sub, masks[1]):
                V+=1

    return X-V

m = []

for i in range(1, np.max(labeled)):
    B = labeled == i
    k = euler(B, crooss_masks)
    m.append(k)

one = 0
two = 0
null = 0

for i in m:
    if i == 0:
        one += 1
    elif i == -1:
        two += 1
    elif i == 1:
        null += 1

print(f'Одно отверстие: {one}, два: {two}, нет: {null}')