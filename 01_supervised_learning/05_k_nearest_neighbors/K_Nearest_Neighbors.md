Return to [[Supervised_Learning]]

# K-Nearest Neighbors (KNN)

K-Nearest Neighbors is a simple, instance-based, "lazy" learning algorithm used for both classification and regression.

## Core Concept
KNN works on the principle that similar data points exist in close proximity. To classify a new point, it looks at the $K$ most similar instances (neighbors) in the training set and assigns the class most common among them.

## Mathematical Intuition
The "distance" is typically calculated using the **Euclidean Distance**:
$$d(x, y) = \sqrt{\sum_{i=1}^{n} (x_i - y_i)^2}$$

Other metrics include **Manhattan Distance** ($L_1$ norm) and **Minkowski Distance**. 

Since KNN is based on distance, **feature scaling (normalization/standardization) is mandatory** to ensure all features contribute equally.

## Use Cases
- Recommendation systems.
- Handwriting detection.
- Simple classification tasks where the decision boundary is irregular.

## Advantages & Disadvantages
- **Advantages**: No training phase, easy to understand, inherently handles multiclass.
- **Disadvantages**: Computationally expensive during prediction, requires significant memory, sensitive to irrelevant features and outliers.

# Quick Challenge
**Objective:** Use KNN to classify wine varieties based on their chemical analysis.
**Dataset:** `sklearn.datasets.load_wine`
**Evaluation Metric:** Aim for an **Accuracy** of at least **90%**. (Remember to scale your features!)
