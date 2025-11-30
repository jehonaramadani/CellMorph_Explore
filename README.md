# CellMorph Explore
 A modular pipeline for simulating and analyzing grayscale cell images — built for clarity, reproducibility, and real-world relevance.

# Overview
 This project simulates a full bioimage analysis workflow using synthetic microscopy-like images. It includes:
  Synthetic image generation (100 noisy grayscale cells)
  Preprocessing (Gaussian blur + binary thresholding)
  Morphological feature extraction (area, perimeter, circularity)
  Dimensionality reduction (PCA)
  Clustering (KMeans)
  CSV export for downstream analysis 

# Goals
  Preprocess cell images (denoising, segmentation)
  Extract morphological features
  Cluster cells based on shape
  Visualize clusters and explore biological patterns

# Tools
 Core: scikit-image, OpenCV, NumPy, Pandas, scikit-learn, matplotlib
 Optional: napari for interactive image inspection

# Structure
 notebooks/     → step-by-step analysis (Jupyter)
 src/           → reusable functions (e.g., synthetic generator)
 data/          → generated grayscale cell images
 results/       → binary masks, feature tables, cluster assignments

# Future Work
 Integrate transcriptomic data via AnnData
 Explore deep feature learning with PyTorch
 Compare synthetic vs real microscopy datasets

# Cell Morphology Clusters
 This scatter plot shows how synthetic cells group based on shape features — area, perimeter, and circularity — after dimensionality reduction via PCA. 
 Each point represents a cell, colored by its cluster assignment from KMeans.

 The PCA axes (PC1 and PC2) capture the most variance in the data, allowing us to visualize structural differences between cells. 
 Cluster separation suggests distinct morphological patterns, with one outlier indicating a potentially unique shape profile.

 ![Cell Morphology Clusters](results/plots/cell_morphology_clusters.png)