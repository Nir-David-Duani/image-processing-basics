# EX2_1
# build dilate and erode functions
import matplotlib.pyplot as plt
import numpy as np

figsize = (10, 10)


img = np.zeros((50, 50))
img[20:30, 20:30] = 1

plt.figure(figsize=figsize)
plt.imshow(img, cmap="gray")
plt.title("original image")
plt.show()

kernel = np.zeros((5, 5), dtype=np.uint8)
kernel[2, :] = 1
kernel[:, 2] = 1


plt.figure(figsize=figsize)
plt.imshow(kernel, cmap="gray")
plt.title("kernel")
plt.show()


def my_dilate(img, kernel):
    # original sizes
    h, w = img.shape 
    kH, kW = kernel.shape

    # padding
    pad_y = kH//2
    pad_x = kW//2

    padded = np.zeros((h + 2*pad_y, w + 2*pad_x))
    padded[pad_y:pad_y+h, pad_x:pad_x+w] = img

    output = np.zeros_like(img)
    
    # cross coralation
    for y in range(h):
        for x in range(w):
            window = padded[y:y+kH ,x:x+kW]
            value = np.sum(window*kernel)
            if value >= 1:
                output[y, x] = 1
            else:
                output[y, x] = 0

    return output


plt.figure(figsize=figsize)
plt.imshow(my_dilate(img, kernel), cmap="gray")
plt.title("my_dilate")
plt.show()

# show that cv2.dilate and my_dilate are the same using absolute difference
import cv2

cv_result_dilate = cv2.dilate(img, kernel, iterations=1)
my_result_dilate = my_dilate(img, kernel)

diff_dilate = np.abs(cv_result_dilate - my_result_dilate)

if np.all(diff_dilate == 0):
    print("cv2.dilate & my_dilate are the same!")
else:
    print("try again...")


def my_erode(img, kernel):
    # original sizes
    h, w = img.shape 
    kH, kW = kernel.shape

    # padding
    pad_y = kH//2
    pad_x = kW//2

    padded = np.zeros((h + 2*pad_y, w + 2*pad_x))
    padded[pad_y:pad_y+h, pad_x:pad_x+w] = img

    output = np.zeros_like(img)
    
    # cross coralation
    for y in range(h):
        for x in range(w):
            window = padded[y:y+kH ,x:x+kW]
            value = np.sum(window*kernel)
            if value == np.sum(kernel):
                output[y, x] = 1
            else:
                output[y, x] = 0

    return output



plt.figure(figsize=figsize)
plt.imshow(my_erode(img, kernel), cmap="gray")
plt.title("my_erode")
plt.show()

# show that cv2.erode and my_erode are the same using absolute difference
cv_result_erode = cv2.erode(img, kernel, iterations=1)
my_result_erode = my_erode(img, kernel)

diff_erode = np.abs(cv_result_erode - my_result_erode)

if np.all(diff_erode == 0):
    print("cv2.erode & my_erode are the same!")
else:
    print("try again...")
