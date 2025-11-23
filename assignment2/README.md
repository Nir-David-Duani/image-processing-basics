# Assignment 2 — Morphological Operations & Connected Components

This assignment explores **basic morphology in image processing** using NumPy and OpenCV.  
It includes two exercises: manually implementing dilation and erosion, and using morphological operations to detect words in a newspaper image.

---

## 🧩 Exercises

### 1. Implement Dilation and Erosion (NumPy)
Created custom `my_dilate()` and `my_erode()` functions that simulate morphological operations by sliding a kernel over a binary image.

**Key Concepts:**
- Cross-correlation and neighborhood operations  
- Image padding and kernel design  
- Binary image manipulation  

**Example Output:**  
A dilated square shape demonstrating the kernel effect.

---

### 2. Find Words in a Newspaper (OpenCV)
Used thresholding, dilation, and connected components to group text and detect separate words in a newspaper article.

**Key Steps:**
1. Convert the image to grayscale and apply a threshold.  
2. Use a rectangular kernel for dilation to merge characters of each word.  
3. Apply `cv2.connectedComponents()` to identify and draw bounding boxes.  

**Key Concepts:**
- Morphological operators (`cv2.dilate`, `cv2.erode`)  
- Binary masks and thresholding  
- Connected component analysis  

---

## 🖼️ Results

| Original | After Threshold | After Dilation |
|:---------:|:----------------:|:----------------:|
| ![original](news.jpg) | ![threshold](threshold_example.png) | ![dilated](dilated_example.png) |

---

## 🧠 What I Learned
- How morphological filters affect binary images  
- How to detect connected regions using OpenCV  
- The relationship between image structure and kernel design

---

## 🧰 Technologies
- Python 3  
- NumPy  
- OpenCV  
- Matplotlib