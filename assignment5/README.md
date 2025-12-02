# Assignment 5 — Circle Hough Transform

This assignment focuses on detecting circular shapes using the **Hough Transform**, both through a **manual implementation** of the 3D Hough space and through a **real-world application** using OpenCV’s `cv2.HoughCircles`.  
The goal is to understand how circle detection works mathematically and how it behaves in practical scenarios with noisy, real images.

---

## Objective

Develop two circle-detection systems:

1. **EX4b.a — Manual Circle Hough Transform**  
   Implement the full pipeline from scratch:
   - Edge detection  
   - Accumulator construction  
   - Radius voting  
   - Thresholding  
   - Minimum-distance filtering  
   - Final circle reconstruction  

2. **EX4b.b — Coin Detection with HoughCircles**  
   Use OpenCV’s built-in circle detector to locate and classify real U.S. coins based on pixel radius.

---

## How It Works

### 🔵 Manual Hough Transform (EX5.a)

A circle in an image is described by three parameters:

- **a** — center x coordinate  
- **b** — center y coordinate  
- **r** — radius  

Each edge pixel potentially belongs to infinitely many circles.  
The Hough Transform discretizes this 3D parameter space and uses a **voting mechanism**:

- For each edge point → vote for all possible (a, b, r) that form a circle through it  
- True circles create **peaks in the accumulator**  

After thresholding and suppressing duplicates, the peaks correspond to detected circles.

This part demonstrates:
- Why Hough is robust even when arcs are missing  
- How geometric voting reconstructs full shapes  
- How accumulator resolution affects detection quality  

---

### 🟢 HoughCircles for Real Coins (EX5.b)

Here we use OpenCV’s optimized implementation.  
Unlike the synthetic image in EX4b.a, the coins image includes:

- Illumination changes  
- Weak edges  
- Shadows  
- Small coins (dimes) that are harder to detect  

To get accurate results, **parameter tuning** is essential.

The final working configuration:

```python
acc_ratio = 1.0
min_dist = 60
canny_upper_th = 60
acc_th = 45
minR = 40
maxR = 74
