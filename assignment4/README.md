# Assignment 4 — Vignetting Correction

This assignment focuses on detecting and correcting **vignetting**, a common optical issue where brightness decreases toward the edges of an image.  
The goal is to simulate how a camera system can automatically correct for this artifact using a **regression-based mathematical model**.

---

## Objective
Develop an algorithm that:
1. Learns the vignetting pattern from a **single calibration image** (white wall).  
2. Uses **Least Squares Regression** to estimate the parameters that describe the light falloff.  
3. Applies the learned model to correct new images taken with the same lens.

---

## How It Works

Vignetting causes the corners of an image to appear darker than the center.  
To fix this, we capture a calibration photo of a **uniform white wall** and analyze how the brightness changes across the frame.  

We assume that brightness varies smoothly with position, and therefore can be approximated with a **polynomial regression model** that depends on pixel coordinates (x, y).  
Using **Least Squares Regression**, we find the model parameters (β) that best fit the brightness distribution.  
These parameters are then used to reconstruct a calibration map that compensates for uneven illumination.  

When applied to a new image, the algorithm divides each pixel by its corresponding calibration value, resulting in a corrected, evenly illuminated image.

In short:
- Measure the light falloff using a calibration image.  
- Model the brightness variation with **regression**.  
- Apply the model to correct new images efficiently and automatically.

---

## Implementation Overview

### Core Functions
- **`get_index_matrix()`** — builds a coordinate-based data matrix for the regression model.  
- **`get_calib_coeffs(calib_map)`** — performs **Least Squares Regression** to calculate model coefficients (β).  
- **`fix_raw_im(b, vig_im)`** — reconstructs the calibration map using the regression output and corrects the image.  
- **`calib_testing()`** — evaluates reconstruction accuracy for verification and debugging.

---

## Example Results

| Original | Fixed |
|:---------:|:------:|
| ![original1](original_image1.png) | ![fixed1](fixed_image1.png) |
| ![original2](original_image2.png) | ![fixed2](fixed_image2.png) |
| ![original3](original_image3.png) | ![fixed3](fixed_image3.png) |

---

## Key Concepts
- Regression-based modeling for optical distortions  
- Polynomial approximation of brightness variation  
- Least Squares estimation (`X @ β = y`)  
- Efficient calibration for camera systems using compact parameter storage  

---

## Tools Used
Python 3 • NumPy • OpenCV • Matplotlib  

---

## What I Learned
- How to use **regression techniques** to model and correct real-world optical artifacts  
- How to implement and apply **Least Squares Regression** in an image-processing context  
- How calibration models can replace full-size images and save memory  
- How to visualize and verify the effect of regression-based correction