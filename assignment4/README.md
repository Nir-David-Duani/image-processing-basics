# Assignment 4 — Vignetting Correction

This assignment focuses on detecting and correcting **vignetting**, a common optical issue where brightness decreases toward the edges of an image.  
The goal is to simulate how a camera system can automatically correct for this artifact using a lightweight mathematical model.

---

## Objective
Develop an algorithm that:
1. Learns the vignetting pattern from a **single calibration image** (white wall).
2. Stores compact calibration parameters (β vector).
3. Uses them to correct any new image taken with the same lens.

---

## Mathematical Background

Vignetting can be modeled as a **spatially varying intensity function**:  
\[
I(x, y) = I_0(x, y) \cdot V(x, y)
\]
where \(I(x, y)\) is the observed pixel intensity, \(I_0(x, y)\) is the true (ideal) image, and \(V(x, y)\) is the vignetting function (values ≤ 1) describing the light falloff.

Since \(V(x, y)\) tends to vary smoothly across the frame, it can be approximated using a **polynomial model**:
\[
V(x, y) = \beta_0 + \beta_1 x + \beta_2 y + \beta_3 x^2 + \beta_4 y^2 + \beta_5 xy
\]

Given a **calibration image** of a uniform surface (white wall), we can estimate β by solving a **least-squares regression** problem:
\[
X\beta = y
\]
where:
- \(X\) is a matrix built from pixel coordinates and polynomial terms  
- \(y\) is the flattened grayscale calibration image  
- \(\beta = (X^T X)^{-1} X^T y\)

Once β is estimated, we can reconstruct \(V(x, y)\) for any image and correct it using:
\[
I_{\text{corrected}}(x, y) = \frac{I(x, y)}{V(x, y)}
\]

---

## Implementation Overview

### Core Functions
- **`get_index_matrix()`** — builds the feature matrix `X` based on pixel coordinates and polynomial terms (`x`, `y`, `x²`, `y²`, `xy`).
- **`get_calib_coeffs(calib_map)`** — computes calibration coefficients using **least squares regression**.
- **`fix_raw_im(b, vig_im)`** — reconstructs the calibration map and applies correction by dividing the raw image by the model’s prediction.
- **`calib_testing()`** — evaluates reconstruction accuracy with RMSE and an L1 error map.

---

## Example Results

| Original | Fixed |
|:---------:|:------:|
| ![original1](original_image1.png) | ![fixed1](fixed_image1.png) |
| ![original2](original_image2.png) | ![fixed2](fixed_image2.png) |
| ![original3](original_image3.png) | ![fixed3](fixed_image3.png) |

---

## Key Concepts
- Vignetting correction via **parametric polynomial modeling**  
- **Least squares estimation** of calibration coefficients (`X @ β = y`)  
- **Radial brightness modeling** using low-order polynomial terms  
- Image normalization and correction using **OpenCV** and **NumPy**

---

## Tools Used
Python 3 • NumPy • OpenCV • Matplotlib

---

## What I Learned
- How to model and correct optical distortions mathematically  
- Implementing regression-based calibration in image processing  
- Understanding how cameras store lens-specific calibration data  
- Evaluating correction accuracy both visually and numerically
