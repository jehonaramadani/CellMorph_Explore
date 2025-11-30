### CellMorph Explore

A modular pipeline for simulating and analyzing grayscale cell images — built for clarity, reproducibility, and real-world relevance.


### Overview

This project simulates a full bioimage analysis workflow using synthetic microscopy-like images. It includes:

- Synthetic image generation (100 noisy grayscale cells)  
- Preprocessing (Gaussian blur + binary thresholding)  
- Morphological feature extraction (area, perimeter, circularity)  
- Dimensionality reduction (PCA)  
- Clustering (KMeans)  
- CSV export for downstream analysis  


### Goals

- Preprocess cell images (denoising, segmentation)  
- Extract morphological features  
- Cluster cells based on shape  
- Visualize clusters and explore biological patterns  


### Tools

- Core: scikit-image, OpenCV, NumPy, Pandas, scikit-learn, matplotlib 
- Optional: napari for interactive image inspection  


### Installation

Clone the repo and set up the environment:
'bash
git clone https://github.com/jehonaramadani/CellMorph_Explore.git
cd CellMorph_Explore
conda env create -f environment.yml
conda activate cellmorph

