Return to [[Unsupervised_Learning]]

# Clustering Algorithms

Clustering is an unsupervised learning task that involves grouping a set of objects such that objects in the same group (cluster) are more similar to each other than to those in other groups.

## Core Concept
Unlike classification, clustering does not use labeled data. It relies on finding inherent patterns and structures based on similarity measures.

Common types:
- **Partitioning**: Dividing data into non-overlapping groups (e.g., K-Means).
- **Hierarchical**: Building a tree of clusters (e.g., Agglomerative Clustering).
- **Density-based**: Grouping points based on their concentration (e.g., DBSCAN).

## Mathematical Intuition
**K-Means Objective Function (Inertia):**
Minimize the sum of squared distances between each point and its assigned cluster centroid:
$$J = \sum_{j=1}^{k} \sum_{i \in C_j} \|x_i - \mu_j\|^2$$
Where $\mu_j$ is the centroid of cluster $C_j$.

**DBSCAN**: Uses density reachability. A point is a **Core Point** if it has at least `MinPts` neighbors within a radius $\epsilon$.

## Use Cases
- Customer segmentation for marketing.
- Document grouping.
- Image compression (color quantization).

## Advantages & Disadvantages
- **Advantages**: Discovers hidden structures, requires no labels.
- **Disadvantages**: Hard to evaluate "correctness," sensitive to initial parameters (K in K-Means, $\epsilon$ in DBSCAN).

# Quick Challenge
**Objective:** Segment mall customers based on their annual income and spending score.
**Dataset:** `Mall Customer Segmentation Data` (Kaggle).
**Evaluation Metric:** Use the **Elbow Method** and **Silhouette Score** to find the optimal number of clusters. Aim for a Silhouette Score above **0.45**.
