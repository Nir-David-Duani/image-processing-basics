import cv2
import matplotlib.pyplot as plt
import numpy as np

figsize = (10, 10)


def bilateral_one_pixel(source, x, y, d, sigma_r, sigma_s):
    # === init vars
    filtered_pix = 0
    Wp = 0

    # TODO:
    # 1. run on all neighboors (~3 lines)
    k = d // 2
    center_val = source[y, x]
    for dy in range(-k, k + 1):
        for dx in range(-k, k + 1):
            nx = x + dx
            ny = y + dy
            # 2. if neighboor out of matrix indices - don't count him in your computation (~2 lines)
            if nx < 0 or nx >= source.shape[1]:
                continue
            if ny < 0 or ny >= source.shape[0]:
                continue
            # 3. find filtered_pix (~6 lines)
            neighbor_val = source[ny, nx]

            dist2 = dx*dx + dy*dy
            w_s = np.exp(-dist2 / (2 * (sigma_s**2)))

            diff = center_val - neighbor_val
            w_r = np.exp(-(diff*diff) / (2 * (sigma_r**2)))

            w = w_s * w_r

            filtered_pix += neighbor_val * w
            Wp += w
    
    if Wp == 0:
            return center_val
    filtered_pix = filtered_pix / Wp

    # make result uint8
    filtered_pix = np.clip(filtered_pix, 0, 255).astype(np.uint8)
    return filtered_pix


def bilateral_filter(source, d, sigma_r, sigma_s):
    # build empty filtered_image
    filtered_image = np.zeros(source.shape, np.uint8)
    # make input float
    source = source.astype(float)
    # d must be odd!
    assert d % 2 == 1, "d input must be odd"

    # TODO: run on all pixels with bilateral_one_pixel(...) (~4 lines)
    for y in range(source.shape[0]):
        for x in range(source.shape[1]):

            new_val = bilateral_one_pixel(source, x, y, d, sigma_r, sigma_s)
            filtered_image[y, x] = new_val

    return filtered_image


# upload noisy image
src = cv2.imread("butterfly_noisy.jpg")
src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

plt.figure(figsize=(10, 10))
plt.imshow(src, cmap="gray", vmin=0, vmax=255)
plt.colorbar()
plt.title("original noisy image in grey scale")
plt.show()

# ======== run
d = 5  # edge size of neighborhood perimeter
sigma_r = 12  # sigma range
sigma_s = 16  # sigma spatial

my_bilateral_filtered_image = bilateral_filter(src, d, sigma_r, sigma_s)

plt.figure(figsize=(10, 10))
plt.imshow(my_bilateral_filtered_image)
plt.colorbar()
plt.title("my_bilateral_filtered_image")
plt.show()

# compare to opencv
cv2_bilateral_filtered_image = cv2.bilateralFilter(src, d, sigma_r, sigma_s)

plt.figure(figsize=(10, 10))
plt.imshow(cv2_bilateral_filtered_image)
plt.colorbar()
plt.title("cv2_bilateral_filtered_image")
plt.show()

# compare to regular gaussian blur
gaussian_filtered_image = cv2.GaussianBlur(src, (d, d), sigma_s)
plt.figure(figsize=(10, 10))
plt.imshow(gaussian_filtered_image)
plt.colorbar()
plt.title("regular gaussian blur")
plt.show()

# copare canny results between regular two images
th_low = 100
th_high = 200
res = cv2.Canny(my_bilateral_filtered_image, th_low, th_high)
plt.figure(figsize=(10, 10))
plt.imshow(res)
plt.colorbar()
plt.title("Canny on my_bilateral_filtered_image")
plt.show()

res = cv2.Canny(gaussian_filtered_image, th_low, th_high)
plt.figure(figsize=(10, 10))
plt.imshow(res)
plt.colorbar()
plt.title("Canny on regular gaussian blur")
plt.show()
