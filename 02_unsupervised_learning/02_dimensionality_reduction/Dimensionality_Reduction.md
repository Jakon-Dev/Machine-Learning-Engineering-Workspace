Return to [[Unsupervised_Learning]]

# Dimensionality Reduction

Dimensionality reduction is the process of reducing the number of random variables under consideration by obtaining a set of principal variables.

## Core Concept
High-dimensional data can be difficult to visualize and analyze (the "curse of dimensionality"). Dimensionality reduction helps by:
- **Feature Selection**: Choosing a subset of original features.
- **Feature Extraction**: Projecting data into a lower-dimensional space (e.g., PCA, t-SNE).

## Mathematical Intuition
**Principal Component Analysis (PCA):**
Finds the directions (Principal Components) that maximize the variance of the data. This involves calculating the **eigenvectors** and **eigenvalues** of the covariance matrix.
The first principal component $w_1$ satisfies:
$$w_1 = \arg \max_{\|w\|=1} \{ \|Xw\|^2 \}$$

**t-SNE (t-distributed Stochastic Neighbor Embedding):**
A non-linear technique specifically designed for visualization. It minimizes the divergence between probability distributions that represent similarities in high-dimensional and low-dimensional spaces.

## Use Cases
- Data visualization (2D/3D).
- Noise reduction.
- Speeding up training of downstream models.

## Advantages & Disadvantages
- **Advantages**: Solves multicollinearity, improves visualization, reduces storage and compute.
- **Disadvantages**: Loss of information, reduced interpretability (transformed features aren't easily related to physical variables).

# Quick Challenge
**Objective:** Reduce the 784 dimensions of the MNIST dataset to 2 dimensions for visualization.
**Dataset:** `sklearn.datasets.fetch_openml('mnist_784')`
**Evaluation Metric:** Create a scatter plot where the different digits are clearly separated into distinct clusters. Use **PCA** first, then try **t-SNE** to see the difference.
