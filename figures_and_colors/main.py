import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops
from collections import defaultdict


def get_colors(img):
    colors = []

    for cur_val in np.unique(img):
        tmp_img = np.copy(img)
        tmp_img[tmp_img != cur_val] = 0
        tmp_img[tmp_img > 0] = 1

        labeled = label(tmp_img)

        m_col = labeled.max()
        colors.append(m_col)
    
    return colors


def get_shapes(regions):
    shapes = defaultdict(lambda: 0)

    for index, region in enumerate(regions):
        key = ''
        eccent = region.eccentricity

        if eccent == 0:
            if (region.image.size == region.area):
                key = 'square'
            else:
                key = 'circle'
        else:
            key = 'rectangle'

        shapes[key] += 1

    return shapes


file = 'figures_and_colors/balls_and_rects.png'
image = plt.imread(file)
bin_image = np.mean(image,2)
bin_image[bin_image > 0] = 1
labeled = label(bin_image)
regions = regionprops(labeled)
shapes = get_shapes(regions)
colored_image = np.mean(image, 2)
colors = get_colors(colored_image)

print(f'In total: {labeled.max()}')

for cur_key in shapes:
    print(f'{cur_key}s: {shapes[cur_key]}')

for index, value in enumerate(colors):
    if index == 0:
        continue

    print(f'Shade №{index}: {value}')