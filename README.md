# 🧠 Image Processing Projects

A collection of Python-based projects exploring the **mathematical and algorithmic foundations** of image processing and computer vision.  
Each assignment implements core techniques *from scratch* using **NumPy**, **OpenCV**, and **Matplotlib** — emphasizing **understanding the math behind the algorithms** rather than relying on built-in functions.

---

## 📚 Overview

This repository includes several assignments demonstrating different aspects of digital image analysis:

| Assignment | Topic | Main Concepts |
|-------------|--------|----------------|
| [Assignment 1 – Pyramids Everywhere](./assignment1/README.md) | Intro to Python, NumPy, and OpenCV basics | String manipulation, array operations, image masking and overlay |
| [Assignment 2 – Morphological Operations & Connected Components](./assignment2/README.md) | Implementing dilation and erosion manually; detecting words in an image | Morphological filters, binary masks, connected components |
| [Assignment 3 – Bilateral Filtering & Edge Detection](./assignment3/README.md) | Building a bilateral filter from scratch and comparing to OpenCV | Non-linear filtering, noise reduction, Canny edge detection |
| [Assignment 4 – Vignetting Correction via Regression](./assignment4/README.md) | Correcting brightness falloff (vignetting) using a mathematical model | Polynomial modeling, **Least Squares Regression**, camera calibration |

📌 *More projects will be added soon.*

---

## 🧮 Topics Covered
- Image representation and pixel-level operations  
- Convolution and kernel-based filtering  
- Morphological operators (dilate, erode)  
- Binary thresholding and connected components  
- Bilateral filtering and noise reduction  
- Regression-based image correction (vignetting)  
- Visualization and debugging with Matplotlib  

---

## 🧰 Technologies Used
- Python 3  
- NumPy  
- OpenCV  
- Matplotlib  
- Jupyter Notebook  

---

## 🎯 Learning Objectives
These projects aim to:
- Understand the **mathematics and regression models** behind image processing  
- Implement algorithms manually before using OpenCV’s built-in methods  
- Strengthen algorithmic thinking and visualization skills  
- Explore how computer vision systems process and enhance real-world images  

---

## 📸 Example Results

| Task | Before | After |
|:-----|:--------|:-------|
| **Morphological Dilation** | ![Before](assignment2/original_image.png) | ![After](assignment2/dilated_image_kernel(2,5).png) |
| **Bilateral Filtering** | ![Before](assignment3/original_noisy_image_grey_scale.png) | ![After](assignment3/my_bilateral_filtered_image.png) |
| **Vignetting Correction** | ![Before](assignment4/original_image1.png) | ![After](assignment4/fixed_image1.png) |

---

## 👩‍💻 Author
Created by **Nir David Duani**  
Developed as part of the **Honors Program in Computer Science at Reichman University**,  
focusing on hands-on algorithmic understanding and mathematical modeling in image processing.

