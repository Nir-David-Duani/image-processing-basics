# EX2_2
# Find different words in newspaper article
# We'll do this using morphology operators and connected components.

import cv2
import matplotlib.pyplot as plt
import numpy as np

figsize = (10, 10)

im = cv2.imread("news.jpg")
im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

plt.figure(figsize=figsize)
plt.imshow(im_gray, cmap="gray", vmin=0, vmax=255)
plt.title(f"original image", fontsize=16)
plt.show()

# let's start with turning the image to a binary one
threshold_value = 128
im_th = np.zeros_like(im_gray)
#+ we put the mask not on the right side
im_th[im_gray < threshold_value] = 255   

plt.figure(figsize=(20, 20))
#+ we changed the defult of the plt.imshow 
plt.imshow(im_th, cmap='gray', vmin=0, vmax=255)
plt.title(f"after treshold of {threshold_value}", fontsize=16)
plt.show()

# next, merge all pixels of the same word together to make one connected component using a morphologic operator
kernel_size = (2, 5)
kernel = np.ones(kernel_size, np.uint8)
dilated_im = cv2.dilate(im_th, kernel, iterations=1)

plt.figure(figsize=(20,20))
#+ we changed the defult of the plt.imshow 
plt.imshow(dilated_im, cmap='gray', vmin=0, vmax=255)
plt.title(f"Dilated Image (kernel size = {kernel_size})", fontsize=16)
plt.show()


def find_words(dilated_im, im):
    res = im.copy()

    # TODO: draw rectengles around each word:
    # 1. find all connected components
    num_labels, labels = cv2.connectedComponents(dilated_im)
    # 2. build a mask of only one connected component each time, and find it extremeties
    for label in range(1, num_labels):
        mask = np.uint8(labels == label)
        res = plot_rec(mask, res)     
    # TODO: did it came out perfect? Why? Why not?
    return res


def plot_rec(mask, res_im):
    # plot a rectangle around each word in res image using mask image of the word
    xy = np.nonzero(mask)
    y = xy[0]
    x = xy[1]
    left = x.min()
    right = x.max()
    up = y.min()
    down = y.max()

    res_im = cv2.rectangle(res_im, (left, up), (right, down), (0, 20, 200), 2)
    return res_im


plt.figure(figsize=(20, 20))
plt.title(f"find_words (kernel size = {kernel_size})", fontsize=16)
plt.imshow(find_words(dilated_im, im))
plt.show()


# now we want to mark only the big title (ONLY FIRST LINE) words, and do this ONLY using morphological operators
kernel_erode_size=(4,7)
kernel_erode = np.ones(kernel_erode_size, np.uint8)
eroded = cv2.erode(im_th, kernel_erode, iterations=1)

plt.figure(figsize=(20, 20))
plt.imshow(eroded, cmap='gray', vmin=0, vmax=255)
plt.title(f"Step 1 – Erosion: removing thin text (kernel size = {kernel_erode_size})", fontsize=18)
plt.axis('off')
plt.show()


kernel_dilate_size=(15,20)
kernel_dilate = np.ones(kernel_dilate_size, np.uint8)
binary_only_title_cc_img = cv2.dilate(eroded, kernel_dilate, iterations=2)

plt.figure(figsize=(20, 20))
plt.imshow(binary_only_title_cc_img, cmap='gray', vmin=0, vmax=255)
plt.title(f"Step 2 – Dilation: restoring and connecting title letters (kernel size = {kernel_dilate_size})", fontsize=18)
plt.axis('off')
plt.show()


plt.figure(figsize=(20, 20))
plt.imshow(find_words(binary_only_title_cc_img, im))
plt.title("Detected Title (using only Erosion and Dilation)", fontsize=20)
plt.axis('off')
plt.show()
