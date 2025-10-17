# 🖼️ Comparative Analysis of Edge-Based, Clustering-Based & Watershed Segmentation


<div style="display: flex; justify-content: center; gap: 10px; margin-bottom: 20px;">
    <img src="data/raw/example4.png" alt="Segmentation 1" width="250">
    <img src="data/ground_truth/gt4.png" alt="Segmentation 2" width="250">
</div>


<div style="display: flex; justify-content: center; gap: 10px; margin-top: 20px;">
    <a href="https://www.python.org/">
        <img src="https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white" alt="Python Badge">
    </a>
    <a href="LICENSE">
        <img src="https://img.shields.io/badge/License-MIT-green" alt="License Badge">
    </a>
    <a href="https://jupyter.org/">
        <img src="https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter&logoColor=white" alt="Jupyter Badge">
    </a>
</div>


> **Exploring classical image segmentation methods with morphological post-processing, evaluated using the IoU metric on BSDS500 dataset.**  

---

## 🧩 Abstract

Image segmentation is a core task in computer vision with applications ranging from **object recognition** to **medical imaging**.  
This study presents a comparative analysis of **edge-based** and **region-based** segmentation methods on the **Berkeley Segmentation Dataset (BSDS500)**.  

We implemented:

- 🔹 **Canny Edge Detection** – gradient-based edge extraction  
- 🔹 **K-Means Clustering** – color-based region segmentation  
- 🔹 **Watershed Segmentation** – intensity-topography-based region labeling  
- 🔹 **Morphological Closing** – post-processing to improve object continuity  

All methods were fine-tuned, and results were **quantitatively evaluated using the Intersection over Union (IoU) metric**.  
The analysis shows that **region-based approaches outperform edge-based methods in accuracy**.

---

## 🧠 Keywords

`Image Segmentation` • `Edge Detection` • `K-Means` • `Watershed` • `Morphological Processing` • `IoU Metric`  

---

## 🧬 Methodology

| Method | Description | Tuned Parameters |
|--------|-------------|-----------------|
| **Canny Edge Detection** | Extracts edges based on gradients; morphological closing ensures continuity. | σ = 0.2, 0.33, 0.5 • Closing radius = 0, 3, 5 |
| **K-Means Clustering** | Groups pixels by color similarity; the largest cluster defines main object region. | k = 2, 3, 4 • Closing radius = 0, 3, 5 |
| **Watershed Segmentation** | Treats pixel intensities as topography; basins correspond to object regions. | Footprint = 3, 5, 7 • Closing radius = 0, 3, 5 |
| **Morphological Closing** | Smooths object edges and fills small holes. | Applied to all methods |

> ⚡ Morphological post-processing significantly improved object continuity and IoU scores for all methods.

---

## ⚙️ Installation & Usage

```bash
# Clone the repository
git clone https://github.com/ozgratahan/Image-Segmentation-Analysis.git
cd Image-Segmentation-Analysis

# Install dependencies
pip install -r requirements.txt
```

## Run Segmentation Methods
```bash
# Edge-based segmentation
python src/canny_segmentation.py

# Region-based segmentation
python src/kmeans_segmentation.py
python src/watershed_segmentation.py

# Evaluate IoU
python src/evaluate_iou.py

# Interactive parameter tuning & visualization
jupyter notebook notebooks/parameter_tuning_and_segmentation_examples.ipynb
```
## 🧪 Example Results

### Canny Edge Detection
<div align="center">
    <img src="data\processed\canny_before_closing1.png" alt="Canny Kenar Tespiti Sonucu" width="400">
</div>

### K-Means Segmentation
<div align="center">
    <img src="data\processed\k-means_before_closing1.png" alt="K-Means Kümeleme Sonucu" width="400">
</div>

### Watershed Segmentation
<div align="center">
    <img src="data\processed\Watershed_before_closing1.png" alt="Watershed Segmentasyon Sonucu" width="400">
</div>



## 📊 Quantitative Results
Method |Optimal Parameters|	IoU Score

Canny σ = 0.5 | closing = 5	| 0.527

K-Means	k = 2| closing = 5	| 0.776

Watershed fp = 3| closing = 5	| 0.532

## 🔍 Discussion

All methods benefited from morphological post-processing, which improved object continuity and overall IoU performance.
K-Means achieved the highest accuracy, showing that color-based clustering effectively captures region similarity.
Watershed performed competitively but exhibited sensitivity to noise and over-segmentation.
Canny segmentation was the fastest but yielded fragmented edges due to lack of regional context.


## 🧭 Conclusion and Future Work

This study presents a structured comparison of classical segmentation methods under equal evaluation conditions.
Results highlight the superiority of region-based segmentation, particularly K-Means, in handling natural images.
Future research will focus on integrating deep learning-based models (e.g., U-Net, Mask R-CNN) to further improve segmentation accuracy on complex datasets.

## 📚 References

Martin, D., Fowlkes, C., Tal, D., & Malik, J. (2001). A database of human segmented natural images and its application to evaluating segmentation algorithms and measuring ecological statistics. ICCV 2001, Vancouver, Canada.

Yogamangalam, R., & Karthikeyan, B. (2013). Segmentation Techniques Comparison in Image Processing. IJET, 5(1), 307.

Kaur, D., & Kaur, Y. (2014). Various Image Segmentation Techniques: A Review. IJCSMC, 3(5), 809.
