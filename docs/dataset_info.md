# 📊 Dataset Information

## 🧠 Dataset Name
**Berkeley Segmentation Dataset (BSDS500)**  
[Official Website](https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/resources.html)

---

## 🧾 Description
The **Berkeley Segmentation Dataset (BSDS500)** is a collection of natural images designed for benchmarking image segmentation algorithms.  
It provides both the raw images and multiple **human-labeled ground truth segmentations**, making it ideal for evaluating algorithmic performance against human perception.

The dataset is widely used in research on:
- Image segmentation  
- Boundary detection  
- Region merging and clustering  
- Perceptual grouping

---

## 📂 Dataset Structure
Each image in BSDS500 includes:
- **Original Image** (`.jpg`)  
- **Ground Truth Segmentations** (`.mat` or `.png` formats)  
- **Human boundary annotations**

The dataset is divided into three subsets:
- **Training Set:** 200 images  
- **Validation Set:** 100 images  
- **Test Set:** 200 images  



## 🧪 Usage in This Project
In this project, BSDS500 images were used to:
- Perform segmentation using **Canny**, **K-Means**, and **Watershed** methods.  
- Evaluate the segmentation performance using the **Intersection over Union (IoU)** metric.  
- Compare region-based and edge-based segmentation approaches.  

The dataset enables a fair comparison by providing consistent ground truth references for each test image.

---