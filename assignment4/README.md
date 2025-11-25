# Assignment 4 — Vignetting Correction

This project focuses on detecting and correcting **vignetting**, a common issue in photography where image brightness decreases toward the edges.  
The algorithm simulates a calibration process similar to what might happen in a real camera system.

---

## 🎯 Objective

Develop a system that automatically corrects vignetting artifacts using a single calibration image per lens configuration.

### The challenge
Due to limited hardware memory, we cannot store full calibration maps for each lens setup.  
Instead, the algorithm must compress the calibration data into a compact mathematical model.

---

## 🧠 Process Overview

1. **Calibration Phase:**  
   The user captures an image of a white wall (`calib_im.jpg`) for a given lens.  
   The system computes a set of coefficients (`β` vector) describing the vignetting model.

2. **Correction Phase:**  
   When the user takes new photos with the same lens, the algorithm reconstructs the calibration map from the coefficients  
   and divides the new image by it to fix brightness inconsistencies.

---

## ⚙️ Implementation Details

### Core Functions
- `get_index_matrix()`  
  Generates the feature matrix `X` based on image pixel coordinates (`x`, `y`, `x²`, `y²`, `xy`),  
  used to model radial intensity falloff.

- `get_calib_coeffs(calib_map)`  
  Uses **least squares regression** to estimate the calibration parameters (`β`).

- `fix_raw_im(b, vig_im)`  
  Reconstructs the calibration map and applies correction by dividing the raw image by the model output.

- `calib_testing(calib_map, rec_calib_map)`  
  Evaluates the reconstruction using **RMSE** and displays the **L1 error map**.

---

## 🖼️ Example Results

| Original Image | Fixed Image | Calibration Error Map |
|:----------------:|:-------------:|:----------------------:|
| ![original](vignette_im1.jpg) | ![fixed](fixed_image_example.png) | ![error](error_map_example.png) |

*(Images illustrate correction of peripheral darkening caused by vignetting.)*

---

## 📚 Key Concepts
- Vignetting correction using parametric modeling  
- Least Squares fitting  
- Radial intensity modeling  
- Camera calibration  
- OpenCV & NumPy matrix operations

---

## 🧰 Tools Used
Python 3 • NumPy • OpenCV • Matplotlib

---

## 🧩 What I Learned
- How to model optical artifacts mathematically  
- How calibration and correction processes are implemented in camera hardware  
- Applying linear regression to image-based problems  
- Visual evaluation of error maps and reconstruction accuracy
