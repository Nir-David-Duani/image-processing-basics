# Assignment 3 – Bilateral Filtering and Edge Detection

This assignment focuses on implementing a **Bilateral Filter** from scratch and comparing it to OpenCV’s built-in version and a regular Gaussian blur.  
The goal is to understand how different filtering methods affect noise reduction and edge preservation.

## Original Image

![Original](butterfly_noisy.jpg)

## Bilateral Filter Implementation

A bilateral filter smooths images while keeping edges sharp by combining:
- **Spatial weight** – pixels closer to the center have higher influence  
- **Range weight** – pixels with similar intensity have higher influence  

Parameters used:
- `d = 5`  
- `sigma_s = 16`  
- `sigma_r = 12`

## Results Comparison

| Original Noisy Image | Custom Bilateral Filter | OpenCV Bilateral Filter | Gaussian Blur |
|:--------------------:|:-----------------------:|:-----------------------:|:--------------:|
| ![original](original_noisy_image_grey_scale.png) | ![my](my_bilateral_filtered_image.png) | ![cv2](cv2_filtered_image.png) | ![gaussian](regular_gaussian_blur.png) |

## Edge Detection (Canny)

| On Custom Bilateral Filter | On Gaussian Blur |
|:---------------------------:|:----------------:|
| ![canny_bilateral](Canny_my_bileteral_filtered_image.png) | ![canny_gaussian](Canny_regular_gaussian_blur_filtered_image.png) |

## Conclusions

- **Noise reduction:** The bilateral filter effectively removes noise while keeping edges visible and defined.  
- **Edge preservation:** Compared to Gaussian blur, bilateral filtering maintains object boundaries better.  
- **Canny results:** Edge maps from the bilateral version are cleaner and more accurate.  
- **Performance:** The custom implementation is slower but helps understand how the spatial and range components interact.  
- **Validation:** The custom and OpenCV results look nearly identical, confirming the correctness of the implementation.

## Tools Used
Python 3 • NumPy • OpenCV • Matplotlib

## What I Learned
- How bilateral filtering works at the pixel level  
- How Gaussian blur and bilateral differ in edge behavior  
- How filtering influences the quality of edge detection  
- The value of implementing algorithms manually before using built-in functions
